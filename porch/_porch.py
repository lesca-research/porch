#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
usage: python3 lesca_task_helper.py CFG_JSON_FILE

Entries in CFG_JSON_FILE:
   - 'project_name'
   - 'participant_ID_prefix'
   - 'participant_ID_regexp'
   - 'visit_order_file' (path to pck file):
       The pickle file contains the mapping between blind ticket codes and
       visit order.
       Note: used in HeartBrain
   - 'trigger_tests' : list of one of ('oxysoft' | 'labchart')
   - 'default_track_info' (list of 3-element lists):
       Default entries to display in the track table. This table will be 
       saved to the user home folder for customization.
       Each entry defines a step in the track: 
                   (walk_duration_millisec, step_label, order)
       Note: used in NeuroMBAM and HeartBrain
       If not given and no custom table found in the user home folder
       then no table widget will be displayed.
   - 'task_name'
   - 'task_command'
   - 'use_rest_stand' : true | false
"""
import sys
import os
import os.path as op
from PyQt5 import QtCore, QtGui, QtWidgets
from .ui import main_ui
from .ui.widgets import (show_critical_message_box, show_info_message_box)
import subprocess
from functools import partial
from datetime import datetime

import pyautogui
from appdirs import user_data_dir
import json
import pickle

if sys.platform == 'win32':
    PYTHON_CMD = ['py', '-3']
else: # linux
    PYTHON_CMD = ['python3', '-3']

NO_PROCESS_RUNNING = 0
PROCESS_KILLED = 1
PROCESS_LEFT = 2

CMD_TRIGGER = 'lesca_trigger_test'

HBP_TRACK_INFO = [
    ("5000", "James_Ensor", "01"),
    ("5000", "Henri_Matisse", "02"),
    ("5000", "Lyonel_Feininger", "03"),
    ("5000", "Hans_Hofmann", "04"),
    ("5000", "Niki_de_Saint_Phalle", "05"),
    ("5000", "Alexander_Calder", "06"),
    ("5000", "Simon_Hantai", "07"),
    ("5000", "Mark_Tansey", "08"),
    ("5000", "James_Ensor", "09"),
    ("5000", "Henri_Matisse", "10"),
    ("5000", "Lyonel_Feininger", "11"),
    ("5000", "Hans_Hofmann", "12"),
    ("5000", "Niki_de_Saint_Phalle", "13"),
    ("5000", "Alexander_Calder", "14"),
    ("5000", "Simon_Hantai", "15"),
    ("5000", "Mark_Tansey", "16"),
]

# NeuroMBAM
NMBAM_TRACK_INFO = [
    ("5000", "Painting1", "01"),
    ("5000", "Painting2", "02"),
    ("5000", "Painting3", "03"),
    ("5000", "Painting4", "04"),
    ("5000", "Painting5", "05"),
    ("5000", "Painting6", "06"),
    ("5000", "Painting1", "07"),
    ("5000", "Painting2", "08"),
    ("5000", "Painting3", "09"),
    ("5000", "Painting4", "10"),
    ("5000", "Painting5", "11"),
    ("5000", "Painting6", "12"),
]

#
class TicketValidator(QtGui.QValidator):
    def __init__(self, tickets, parent=None):
        super(TicketValidator, self).__init__(parent=parent)
        self.tickets = tickets

    def validate(self, ticket, pos):
        if ticket not in self.tickets:
            return QtGui.QValidator.Intermediate, ticket, pos
        return QtGui.QValidator.Acceptable, ticket, pos

def check_fn_exists(fn, error_msg_prefix):
    if not op.exists(fn):
        msg = '[%s] File not found: %s' %(error_msg_prefix, fn)
        show_critical_message_box(msg)
        raise FileNotFoundError(msg)
    return fn

def check_command(cmd, error_msg_prefix):
    try:
        result = subprocess.run([cmd, '--version'])
        if result.returncode != 0:
            msg = '[%s] Error checking command %s' % (error_msg_prefix, cmd)
            show_info_message_box(msg)
            raise RuntimeError(msg)
    except FileNotFoundError as e:
        msg = '[%s] Cannot find command %s' % (error_msg_prefix, cmd)
        show_info_message_box(msg)
        raise e

class TaskHelperWidget(QtWidgets.QWidget, main_ui.Ui_Form):
    def __init__(self, cfg, parent=None):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.setupUi(self)
        self.status_bar = parent.statusBar()

        self.time_point = None
        self.radio_buttons_time_points = []
        if 'time_points' in cfg:
            for time_point in cfg['time_points']:
                radio_button = QtWidgets.QRadioButton(self.frame_time_point)
                radio_button.setText(time_point)
                self.frame_time_point_layout.addWidget(radio_button)
                radio_button.toggled.connect(partial(self.set_time_point,
                                                     time_point))
                self.radio_buttons_time_points.append(radio_button)
        else:
            self.frame_time_point.hide()
        if 'defaul_track_info' in cfg:
            for i, (walk, painting, order) in enumerate(self.load_track_info()):
                self.track_table.insertRow(self.track_table.rowCount())
                #item_walk = QtWidgets.QTableWidgetItem()
                item_walk = QtWidgets.QLineEdit(self.track_table)
                item_walk.setValidator(QtGui.QIntValidator(0,900000, item_walk))
                item_walk.setText(walk)
                item_walk.editingFinished.connect(self.on_track_table_change)
                self.track_table.setCellWidget(i, 0, item_walk)
    
                item_painting = QtWidgets.QTableWidgetItem()
                item_painting.setFlags(QtCore.Qt.ItemIsSelectable |
                                       QtCore.Qt.ItemIsEditable |
                                       QtCore.Qt.ItemIsEnabled)
                item_painting.setText(painting)
                self.track_table.setItem(i, 1, item_painting)
    
                item_order = QtWidgets.QTableWidgetItem()
                item_order.setText(order)
                self.track_table.setItem(i, 2, item_order)
    
            self.track_table.setSortingEnabled(True)
            self.track_table.sortByColumn(2, QtCore.Qt.AscendingOrder)
            self.track_table.resizeColumnsToContents();
            
            count = self.track_table.rowCount();
            scrollBarHeight = self.track_table.horizontalScrollBar().height()
            horizontalHeaderHeight = (self.track_table.horizontalHeader()
                                      .height())
            rowTotalHeight = 0
            for i in range(count):
                rowTotalHeight += (self.track_table.verticalHeader()
                                   .sectionSize(i))
            self.track_table.setMinimumHeight(horizontalHeaderHeight + 
                                              rowTotalHeight + 
                                              scrollBarHeight);
    
            self.track_table.cellChanged.connect(self.on_track_table_change)
    
        else:
            self.frame_track_table.hide()

        if not cfg.get('use_task_test_input', False):
            self.button_run_test_input.hide()

        if not cfg.get('use_task_instructions', False):
            self.button_run_instructions.hide()

        if not cfg.get('use_task_practice', False):
            self.button_run_practice.hide()

        if 'oxysoft' not in cfg.get('trigger_tests', []):
            self.button_test_trigger_oxysoft.hide()

        if 'labchart' not in cfg.get('trigger_tests', []):
            self.button_test_trigger_labchart.hide()

        if not cfg.get('use_rest_stand_task', False):
            self.frame_nirs_rest_stand.hide()

        self.visit_idx = None
        if 'visit_order_file' in cfg:
            self.check_fn_exists(cfg['visit_order_file'], 'visit_order_file')
            with open(op.join(task_folder, 'order.pck'), 'rb') as fin:
                self.ticket_to_visit_type = pickle.load(fin)
            print('Available tickets:')
            print(list(self.ticket_to_visit_type.keys()))
            ticket_validator = TicketValidator(self.ticket_to_visit_type)
            self.order_ticket_edit.setValidator(ticket_validator)
        else:
            self.visit_order_frame.hide()

        self.task_command = cfg['task_command']
        self.task_label = cfg['task_name']

        check_command(self.task_command, self.task_label + ' program')

        self.participant_field.setText(cfg['participant_ID_prefix'])
        pid_re = QtCore.QRegExp(cfg['participant_ID_regexp'])
        self.participant_field.setValidator(QtGui.QRegExpValidator(pid_re))

        (self.participant_field.editingFinished
         .connect(self.refresh_labels))

        self.radio_visit1.toggled.connect(partial(self.set_visit_idx, 0))
        self.radio_visit2.toggled.connect(partial(self.set_visit_idx, 1))

        _fpaste = partial(self.delayed_paste, self.field_nirs_calibration.text,
                          self.button_paste_calib)
        self.button_paste_calib.clicked.connect(_fpaste)

        self.process_buttons = {}

        check_command(CMD_TRIGGER, 'Trigger test command')
        (self.button_test_trigger_oxysoft.clicked.
         connect(partial(self.run_subprocess, [CMD_TRIGGER, 'oxysoft'],
                         'Test Trigger Oxysoft',
                         self.button_test_trigger_oxysoft)))
        self.process_buttons['Test Trigger Oxysoft'] = \
            self.button_test_trigger_oxysoft

        (self.button_test_trigger_labchart.clicked.
         connect(partial(self.run_subprocess, [CMD_TRIGGER, 'labchart'],
                         'Test Trigger LabChart',
                         self.button_test_trigger_labchart)))
        self.process_buttons['Test Trigger LabChart'] = \
            self.button_test_trigger_labchart

        (self.button_run_test_input.clicked.
         connect(partial(self.run_subprocess,
                         [self.task_command, 'test_input', '@PID'],
                         self.task_label,
                         self.button_run_test_input)))
        self.process_buttons[self.task_label + ' Test Input'] = \
            self.button_run_test_input

        (self.button_run_instructions.clicked.
         connect(partial(self.run_subprocess,
                         [self.task_command, 'instructions', '@PID'],
                         self.task_label,
                         self.button_run_instructions)))
        self.process_buttons[self.task_label + ' Instructions'] = \
            self.button_run_instructions

        (self.button_run_practice.clicked.
         connect(partial(self.run_subprocess,
                         [self.task_command, 'practice', '@PID'],
                         self.task_label,
                         self.button_run_practice)))
        self.process_buttons[self.task_label + ' Pratique'] = \
            self.button_run_practice

        _fpaste = partial(self.delayed_paste, self.field_nirs_task.text,
                          self.button_paste_nirs_task)
        self.button_paste_nirs_task.clicked.connect(_fpaste)

        (self.button_run_task.clicked.
         connect(partial(self.run_subprocess,
                         [self.task_command, 'main_ER', '@PID'],
                         self.task_label,
                         self.button_run_task)))
        self.process_buttons[self.task_label] = self.button_run_task

        _fpaste = partial(self.delayed_paste, self.field_nirs_rest_stand.text,
                          self.button_paste_rest_stand)
        self.button_paste_rest_stand.clicked.connect(_fpaste)

        self.current_process = None
        self.current_process_label = None

        self.refresh_labels()
        self.reset_buttons()

        self.timer = QtCore.QTimer(self)
        self.refresh_rate_ms = 1000
        self.timer.setInterval(self.refresh_rate_ms)
        self.timer.timeout.connect(self.poll_processes)
        self.timer.start()

        self.status_bar.showMessage("%s: Ready" % self.current_time())

    def set_visit_idx(self, idx, state):
        if state:
            self.visit_idx = idx
            self.refresh_labels()

    def set_time_point(self, time_point, state):
        if state:
            self.time_point = time_point
            self.refresh_labels()

    def delayed_paste(self, get_text, sender_button):
        to_paste = get_text()
        original_sender_button_text = sender_button.text()
        countdown_duration_ms = 4000
        countdown_refresh_ms = 1000
        def _countdown(count_ms):
            sender_button.setText('%d' % (count_ms // 1000))
            if count_ms <= 0:
                pyautogui.write(to_paste)
                sender_button.setText(original_sender_button_text)
            else:
                next_count_ms = count_ms - countdown_refresh_ms
                QtCore.QTimer.singleShot(countdown_refresh_ms,
                                         partial(_countdown, next_count_ms))
        _countdown(countdown_duration_ms)

    def on_track_table_change(self, *args, **kwargs):
        self.save_track_info(self.track_info())

    def track_info(self, filter_order=False):
        tt = self.track_table
        return [(tt.cellWidget(irow, 0).text(),
                 tt.item(irow, 1).text(),
                 tt.item(irow, 2).text())
                for irow in range(tt.rowCount())
                if not filter_order or tt.item(irow, 2).text().isdigit()]

    def load_track_info(self):
        store_dir = user_data_dir('HBP')
        if not op.exists(store_dir):
            os.makedirs(store_dir)
        track_fn = op.join(store_dir, 'track.json')

        if not op.exists(track_fn):
            self.save_track_info(DEFAULT_TRACK_INFO)

        with open(track_fn) as fin:
            track_info = json.load(fin)

        logger.info('Loaded track info:')
        logger.info(track_info)
        return track_info

    def save_track_info(self, track_info):
        track_fn = op.join(user_data_dir('HBP'), 'track.json')
        with open(track_fn, 'w') as fout:
            json.dump(track_info, fout)
        self.status_bar.showMessage("%s: Track information saved" %
                                    self.current_time())

    def resolve_cmd_args(self, cmd):
        resolved_cmd = []
        for arg in cmd:
            if arg == '@PID':
                if not self.participant_field.hasAcceptableInput():
                    show_critical_message_box('Invalid participant ID')
                    return None
                if self.time_point is None:
                    show_critical_message_box('Undefined time point')
                    return None
                resolved_cmd.append(self.participant_field.text())
            if arg == '@TaskVersion':
                if self.order_ticket_edit.text() == '':
                    show_critical_message_box('Missing order ticket')
                    return None
                if not self.order_ticket_edit.hasAcceptableInput():
                    show_critical_message_box('Invalid order ticket')
                    return None
                    
                ticket = self.order_ticket_edit.text()
                visit_idx = self.get_visit_idx()
                if visit_idx is None:
                    show_critical_message_box('Visit index not defined')
                    return None
                task_version = self.ticket_to_visit_type[ticket][visit_idx]

            else:
                resolved_cmd.append(arg)
        return resolved_cmd

    def run_subprocess(self, cmd, label, button_sender, button_state):
        if self.check_process() == NO_PROCESS_RUNNING:
            cmd = self.resolve_cmd_args(cmd)
            if cmd is not None:
                self.current_process = subprocess.Popen(cmd)
                self.current_process_label = label
                self.status_bar.showMessage("%s - %s starts" %
                                            (self.current_time(),
                                             self.current_process_label))

                button_sender.setText('%s en cours (press to stop)' % label)
                for other_button in self.process_buttons.values():
                    if other_button is not button_sender:
                        other_button.setEnabled(False)

    def get_visit_idx(self, zero_based=True):
        if self.visit_idx is None:
            return None
        if zero_based:
            return self.visit_idx
        else:
            return self.visit_idx + 1

    def check_process(self):
        if self.current_process is not None:
            ask = QtWidgets.QMessageBox(self)
            ask.setWindowTitle("Stop process?")
            ask.setText("%s est en cours. Stopper le programme?" %
                        self.current_process_label)
            ask.setStandardButtons(QtWidgets.QMessageBox.Yes |
                                   QtWidgets.QMessageBox.No)
            ask.setIcon(QtWidgets.QMessageBox.Question)
            answer = ask.exec()
            if (self.current_process is not None and
                answer == QtWidgets.QMessageBox.Yes):
                self.current_process.kill()
                self.current_process.wait()
                self.status_bar.showMessage("%s - %s forced to stop" %
                                            (self.current_time(),
                                             self.current_process_label))
                self.current_process = None
                self.current_process_label = None
                self.reset_buttons()
                return PROCESS_KILLED
            else:
                return PROCESS_LEFT
        else:
            return NO_PROCESS_RUNNING

    def __run_main_task(self, button_state):
        if self.check_process() == NO_PROCESS_RUNNING:
            participant_id = self.participant_field.text()
                
            if participant_id is not None and participant_id != '':
                self.button_test_trigger.setEnabled(False)
                self.button_practice_task.setEnabled(False)
                self.button_main_task.setText('Visite en cours (press to stop)')
                if self.project == 'HBP':
                    track = self.track_info(filter_order=True)
                    paintings_order = [e[1] for e in track]
                    walk_durations = [e[0] for e in track]
                    cmd = [sys.executable, self.task_script, participant_id,
                           task_version, ','.join(paintings_order),
                           ','.join(walk_durations)]
                else:
                    cmd = [sys.executable, self.task_script, participant_id]
                
                self.current_process = subprocess.Popen(cmd)
                self.current_process_label = 'Visite'
                self.status_bar.showMessage("%s - %s starts" %
                                            (self.current_time(),
                                             self.current_process_label))
            else:
                show_critical_message_box('No participant defined')

    def run_practice_task(self, button_state):
        if self.check_process() == NO_PROCESS_RUNNING:
            participant_id = self.participant_combo_box.currentText()
            if participant_id is not None and participant_id != '':
                self.button_test_trigger.setEnabled(False)
                self.button_practice_task.setText('Pratique en cours '\
                                                  '(press to stop)')
                self.button_main_task.setEnabled(False)
                if self.project == 'HBP':
                    track = self.track_info(filter_order=True)[:2]
                    cmd = [sys.executable, self.task_script, participant_id,
                           'practice', ','.join(e[1] for e in track),
                           ','.join(e[0] for e in track)]
                else:
                    cmd = [sys.executable, self.task_script, participant_id,
                           'practice']

                self.current_process_label = 'Pratique'
                self.current_process = subprocess.Popen(cmd)

                self.status_bar.showMessage("%s - %s starts" %
                                            (self.current_time(),
                                             self.current_process_label))

            else:
                show_critical_message_box('No participant defined')

    def reset_buttons(self):
        for default_label, button in self.process_buttons.items():
            button.setEnabled(True)
            button.setText('Lancer ' + default_label)

    def current_time(self):
        date_fmt = '%H:%M:%S'
        return datetime.now().strftime(date_fmt)

    def poll_processes(self):
        if self.current_process is None:
            return

        process = self.current_process
        process_label = self.current_process_label

        status = process.poll()
        if status is not None:
            # print('Status of %s: %s' % (process_label, status))
            if status == 0:
                self.status_bar.showMessage("%s - %s completed successfully" %
                                            (self.current_time(), process_label))
            else:
                self.status_bar.showMessage("%s - %s completed with error" %
                                            (self.current_time(), process_label))
            self.current_process = None
            self.current_process_label = None
            self.reset_buttons()

    def refresh_labels(self):
        pid = self.participant_field.text()
        time_point = ('_%s' % self.time_point if self.time_point is not None
                      else '')
        self.field_nirs_calibration.setPrefix('%s%s_calibration_' %
                                              (pid, time_point))
        visit_idx = self.get_visit_idx(zero_based=False)
        if visit_idx is not None:
            self.field_nirs_task.setPrefix('%s%s_main_visit%s_' %
                                           (pid, time_point, visit_idx))
        else:
            self.field_nirs_task.setPrefix('%s%s_%s_' %
                                           (pid, time_point, self.task_label))

        self.field_nirs_rest_stand.setPrefix('%s%s_rest_stand_' %
                                             (pid, time_point))

    def closeEvent(self, event):
        if self.current_process is not None:
            show_critical_message_box('Stoppez le programme en cours '\
                                      'avant de quitter.')
            event.ignore()

def show_critical_message_box(msg, detailed_text=None):
    message_box = QtWidgets.QMessageBox()
    message_box.setIcon(QtWidgets.QMessageBox.Critical)
    message_box.setText(msg)
    if detailed_text is not None:
        message_box.setDetailedText(detailed_text)
    message_box.exec_()

class TaskHelperWindow(QtWidgets.QMainWindow):
    def __init__(self, cfg):
        super(TaskHelperWindow, self).__init__()
        self.main_widget = TaskHelperWidget(cfg, self)
        self.setCentralWidget(self.main_widget)

    def flush_right(self):
        qr = self.frameGeometry()
        desktop_geometry = QtWidgets.QDesktopWidget().availableGeometry()
        rc = desktop_geometry.topRight()
        qr.moveTopRight(rc)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        self.main_widget.closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    with open(sys.argv[1]) as fin:
        configuration = json.load(fin)
    main_window = TaskHelperWindow(configuration)
    main_window.show()
    main_window.flush_right()
    sys.exit(app.exec_())
