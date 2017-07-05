# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appExterna.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
host = 'www.google.com'
port = 80
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip


#fin websocket

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(335, 352)
        self.tblPaso = QtGui.QTableWidget(Dialog)
        self.tblPaso.setGeometry(QtCore.QRect(10, 70, 301, 271))
        self.tblPaso.setObjectName(_fromUtf8("tblPaso"))
        self.tblPaso.setColumnCount(3)
        self.tblPaso.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblPaso.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblPaso.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblPaso.setHorizontalHeaderItem(2, item)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 30, 191, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        item = self.tblPaso.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID", None))
        item = self.tblPaso.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "TIPO PASO", None))
        item = self.tblPaso.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "PASO", None))
        self.label.setText(_translate("Dialog", "Modulo: PASO", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

