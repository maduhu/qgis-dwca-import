# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dwca_import_dialog_base.ui'
#
# Created: Fri Jul 11 15:40:48 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_DwCAImporterDialogBase(object):
    def setupUi(self, DwCAImporterDialogBase):
        DwCAImporterDialogBase.setObjectName(_fromUtf8("DwCAImporterDialogBase"))
        DwCAImporterDialogBase.resize(400, 130)
        self.button_box = QtGui.QDialogButtonBox(DwCAImporterDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 70, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(DwCAImporterDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), DwCAImporterDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), DwCAImporterDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(DwCAImporterDialogBase)

    def retranslateUi(self, DwCAImporterDialogBase):
        DwCAImporterDialogBase.setWindowTitle(_translate("DwCAImporterDialogBase", "Darwin Core Archive Importer", None))

