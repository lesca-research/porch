from PyQt5 import QtCore, QtGui, QtWidgets

def show_critical_message_box(msg, detailed_text=None):
    message_box = QtWidgets.QMessageBox()
    message_box.setIcon(QtWidgets.QMessageBox.Critical)
    message_box.setText(msg)
    if detailed_text is not None:
        message_box.setDetailedText(detailed_text)
    message_box.exec_()

def show_info_message_box(msg):
    message_box = QtWidgets.QMessageBox()
    message_box.setText(msg)
    message_box.exec_()
