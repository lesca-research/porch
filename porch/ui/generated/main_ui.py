# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 1472)
        Form.setMinimumSize(QtCore.QSize(430, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.participant_field = QtWidgets.QLineEdit(Form)
        self.participant_field.setInputMask("")
        self.participant_field.setText("")
        self.participant_field.setObjectName("participant_field")
        self.verticalLayout.addWidget(self.participant_field)
        self.frame_time_point = QtWidgets.QFrame(Form)
        self.frame_time_point.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_time_point.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_time_point.setObjectName("frame_time_point")
        self.frame_time_point_layout = QtWidgets.QHBoxLayout(self.frame_time_point)
        self.frame_time_point_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_time_point_layout.setObjectName("frame_time_point_layout")
        self.label_11 = QtWidgets.QLabel(self.frame_time_point)
        self.label_11.setObjectName("label_11")
        self.frame_time_point_layout.addWidget(self.label_11)
        self.verticalLayout.addWidget(self.frame_time_point)
        self.visit_order_frame = QtWidgets.QFrame(Form)
        self.visit_order_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.visit_order_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.visit_order_frame.setObjectName("visit_order_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.visit_order_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.visit_order_frame)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_4 = QtWidgets.QFrame(self.visit_order_frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.order_ticket_edit = QtWidgets.QLineEdit(self.frame_4)
        self.order_ticket_edit.setMaxLength(4)
        self.order_ticket_edit.setObjectName("order_ticket_edit")
        self.horizontalLayout_3.addWidget(self.order_ticket_edit)
        self.radio_visit1 = QtWidgets.QRadioButton(self.frame_4)
        self.radio_visit1.setObjectName("radio_visit1")
        self.horizontalLayout_3.addWidget(self.radio_visit1)
        self.radio_visit2 = QtWidgets.QRadioButton(self.frame_4)
        self.radio_visit2.setObjectName("radio_visit2")
        self.horizontalLayout_3.addWidget(self.radio_visit2)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.visit_order_frame)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.frame_track_table = QtWidgets.QFrame(Form)
        self.frame_track_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_track_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_track_table.setObjectName("frame_track_table")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_track_table)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.track_table = QtWidgets.QTableWidget(self.frame_track_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.track_table.sizePolicy().hasHeightForWidth())
        self.track_table.setSizePolicy(sizePolicy)
        self.track_table.setMinimumSize(QtCore.QSize(0, 550))
        self.track_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.track_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.track_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.track_table.setDragEnabled(False)
        self.track_table.setDragDropOverwriteMode(False)
        self.track_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.track_table.setAlternatingRowColors(True)
        self.track_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.track_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.track_table.setWordWrap(False)
        self.track_table.setColumnCount(3)
        self.track_table.setObjectName("track_table")
        self.track_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.track_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.track_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.track_table.setHorizontalHeaderItem(2, item)
        self.track_table.horizontalHeader().setDefaultSectionSize(120)
        self.track_table.horizontalHeader().setSortIndicatorShown(False)
        self.track_table.verticalHeader().setMinimumSectionSize(26)
        self.track_table.verticalHeader().setSortIndicatorShown(True)
        self.track_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.track_table)
        self.verticalLayout.addWidget(self.frame_track_table)
        self.button_run_test_input = QtWidgets.QPushButton(Form)
        self.button_run_test_input.setObjectName("button_run_test_input")
        self.verticalLayout.addWidget(self.button_run_test_input)
        self.button_run_instructions = QtWidgets.QPushButton(Form)
        self.button_run_instructions.setObjectName("button_run_instructions")
        self.verticalLayout.addWidget(self.button_run_instructions)
        self.button_run_practice = QtWidgets.QPushButton(Form)
        self.button_run_practice.setObjectName("button_run_practice")
        self.verticalLayout.addWidget(self.button_run_practice)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.frame_calibration = QtWidgets.QFrame(Form)
        self.frame_calibration.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_calibration.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calibration.setObjectName("frame_calibration")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_calibration)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_calibration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_calibration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame_calibration)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.field_nirs_calibration = QtWidgets.QSpinBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_nirs_calibration.sizePolicy().hasHeightForWidth())
        self.field_nirs_calibration.setSizePolicy(sizePolicy)
        self.field_nirs_calibration.setMinimum(1)
        self.field_nirs_calibration.setObjectName("field_nirs_calibration")
        self.horizontalLayout.addWidget(self.field_nirs_calibration)
        self.button_paste_calib = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_paste_calib.sizePolicy().hasHeightForWidth())
        self.button_paste_calib.setSizePolicy(sizePolicy)
        self.button_paste_calib.setObjectName("button_paste_calib")
        self.horizontalLayout.addWidget(self.button_paste_calib)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.button_test_trigger_oxysoft = QtWidgets.QPushButton(self.frame_calibration)
        self.button_test_trigger_oxysoft.setObjectName("button_test_trigger_oxysoft")
        self.verticalLayout_4.addWidget(self.button_test_trigger_oxysoft)
        self.button_test_trigger_labchart = QtWidgets.QPushButton(self.frame_calibration)
        self.button_test_trigger_labchart.setObjectName("button_test_trigger_labchart")
        self.verticalLayout_4.addWidget(self.button_test_trigger_labchart)
        self.verticalLayout.addWidget(self.frame_calibration)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame_nirs_task = QtWidgets.QFrame(Form)
        self.frame_nirs_task.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_nirs_task.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nirs_task.setObjectName("frame_nirs_task")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_nirs_task)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.frame_nirs_task)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.label_4 = QtWidgets.QLabel(self.frame_nirs_task)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_nirs_task)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.field_nirs_task = QtWidgets.QSpinBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_nirs_task.sizePolicy().hasHeightForWidth())
        self.field_nirs_task.setSizePolicy(sizePolicy)
        self.field_nirs_task.setMinimum(1)
        self.field_nirs_task.setObjectName("field_nirs_task")
        self.horizontalLayout_4.addWidget(self.field_nirs_task)
        self.button_paste_nirs_task = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_paste_nirs_task.sizePolicy().hasHeightForWidth())
        self.button_paste_nirs_task.setSizePolicy(sizePolicy)
        self.button_paste_nirs_task.setObjectName("button_paste_nirs_task")
        self.horizontalLayout_4.addWidget(self.button_paste_nirs_task)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.button_run_task = QtWidgets.QPushButton(self.frame_nirs_task)
        self.button_run_task.setObjectName("button_run_task")
        self.verticalLayout_5.addWidget(self.button_run_task)
        self.verticalLayout.addWidget(self.frame_nirs_task)
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.frame_nirs_rest_stand = QtWidgets.QFrame(Form)
        self.frame_nirs_rest_stand.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_nirs_rest_stand.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nirs_rest_stand.setObjectName("frame_nirs_rest_stand")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_nirs_rest_stand)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_nirs_rest_stand)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_5 = QtWidgets.QLabel(self.frame_nirs_rest_stand)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_nirs_rest_stand)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.field_nirs_rest_stand = QtWidgets.QSpinBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_nirs_rest_stand.sizePolicy().hasHeightForWidth())
        self.field_nirs_rest_stand.setSizePolicy(sizePolicy)
        self.field_nirs_rest_stand.setMinimum(1)
        self.field_nirs_rest_stand.setObjectName("field_nirs_rest_stand")
        self.horizontalLayout_5.addWidget(self.field_nirs_rest_stand)
        self.button_paste_rest_stand = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_paste_rest_stand.sizePolicy().hasHeightForWidth())
        self.button_paste_rest_stand.setSizePolicy(sizePolicy)
        self.button_paste_rest_stand.setObjectName("button_paste_rest_stand")
        self.horizontalLayout_5.addWidget(self.button_paste_rest_stand)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.button_run_trigger_sync2 = QtWidgets.QPushButton(self.frame_nirs_rest_stand)
        self.button_run_trigger_sync2.setObjectName("button_run_trigger_sync2")
        self.verticalLayout_6.addWidget(self.button_run_trigger_sync2)
        self.label_9 = QtWidgets.QLabel(self.frame_nirs_rest_stand)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.frame = QtWidgets.QFrame(self.frame_nirs_rest_stand)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.field_labchart_rest_stand = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_labchart_rest_stand.sizePolicy().hasHeightForWidth())
        self.field_labchart_rest_stand.setSizePolicy(sizePolicy)
        self.field_labchart_rest_stand.setReadOnly(True)
        self.field_labchart_rest_stand.setObjectName("field_labchart_rest_stand")
        self.horizontalLayout_2.addWidget(self.field_labchart_rest_stand)
        self.button_paste_labchart_rest_stand = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_paste_labchart_rest_stand.sizePolicy().hasHeightForWidth())
        self.button_paste_labchart_rest_stand.setSizePolicy(sizePolicy)
        self.button_paste_labchart_rest_stand.setObjectName("button_paste_labchart_rest_stand")
        self.horizontalLayout_2.addWidget(self.button_paste_labchart_rest_stand)
        self.verticalLayout_6.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_nirs_rest_stand)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Information du participant</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "Time point :"))
        self.label_3.setText(_translate("Form", "Attention de ne pas m??langer les tickets entre participants. Utiliser WBE1 pour tester bien-??tre ou CLA1 pour classique en visite 1."))
        self.order_ticket_edit.setPlaceholderText(_translate("Form", "Ticket de randomisation"))
        self.radio_visit1.setText(_translate("Form", "Visite 1"))
        self.radio_visit2.setText(_translate("Form", "Visite 2"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Pr??paration de la t??che cognitive</span></p></body></html>"))
        self.track_table.setSortingEnabled(False)
        item = self.track_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Dur??e marche ms"))
        item = self.track_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Etape"))
        item = self.track_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ordre"))
        self.button_run_test_input.setText(_translate("Form", "Lancer Test Input"))
        self.button_run_instructions.setText(_translate("Form", "Lancer Instructions"))
        self.button_run_practice.setText(_translate("Form", "Lancer Pratique"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Calibration NIRS</span></p></body></html>"))
        self.label.setText(_translate("Form", "Label NIRS calibration :"))
        self.field_nirs_calibration.setPrefix(_translate("Form", "_calibration_"))
        self.button_paste_calib.setText(_translate("Form", "->"))
        self.button_test_trigger_oxysoft.setText(_translate("Form", "Test Trigger Oxysoft"))
        self.button_test_trigger_labchart.setText(_translate("Form", "Test Trigger LabChart"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">T??che cognitive avec enregistrement (NIRS)</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "Label t??che NIRS "))
        self.button_paste_nirs_task.setText(_translate("Form", "->"))
        self.button_run_task.setText(_translate("Form", "Lancer Task"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Repos et lev?? (NIRS + Finapres)</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "Label NIRS rest/stand"))
        self.button_paste_rest_stand.setText(_translate("Form", "->"))
        self.button_run_trigger_sync2.setText(_translate("Form", "Trigger Synchro Oxysoft / LabChart"))
        self.label_9.setText(_translate("Form", "! <i> Sauvegarder les donn??es LabChart </i> !"))
        self.button_paste_labchart_rest_stand.setText(_translate("Form", "->"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
