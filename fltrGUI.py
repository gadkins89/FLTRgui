from PyQt6 import QtCore, QtGui, QtWidgets
from fltrDict import fltrListDict, scrubDict, formatFilterDict
from addressDict import storeAddressDict, formatAddressDict
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 675)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.FLTRLabel = QtWidgets.QLabel(parent=MainWindow)
        self.FLTRLabel.setMinimumSize(QtCore.QSize(200, 100))
        self.FLTRLabel.setMaximumSize(QtCore.QSize(240, 100))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        self.FLTRLabel.setFont(font)
        self.FLTRLabel.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.FLTRLabel.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                     "font: italic 48pt \"Harlow Solid Italic\";\n"
                                     "color: white;\n"
                                     "border: 4px solid rgb(0, 85, 255);\n"
                                     "border-radius: 15px;\n"
                                     "")
        self.FLTRLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.FLTRLabel.setObjectName("FLTRLabel")
        self.horizontalLayout_2.addWidget(self.FLTRLabel)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.fullNameLabel = QtWidgets.QLabel(parent=MainWindow)
        self.fullNameLabel.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        self.fullNameLabel.setFont(font)
        self.fullNameLabel.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                         "font: italic 16pt \"Arial\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border: 4px solid rgb(0, 85, 255);\n"
                                         "border-radius: 15px;")
        self.fullNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.verticalLayout_2.addWidget(self.fullNameLabel)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 23, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.comboBox = QtWidgets.QComboBox(parent=MainWindow)
        self.comboBox.setMaximumSize(QtCore.QSize(619, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.comboBox.setToolTip("")
        self.comboBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox.setStyleSheet("font: 350 italic 18pt \"Arial\";\n"
                                    "background-color: rgb(70, 70, 70);\n"
                                    "color:  rgb(255, 255, 255);\n"
                                    "border: 4px solid rgb(0, 85, 255);\n"
                                    "border-radius: 10px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addressLabel = QtWidgets.QLabel(parent=MainWindow)
        self.addressLabel.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        self.addressLabel.setFont(font)
        self.addressLabel.setStyleSheet("font: 350 18pt \"Arial\";\n"
                                        "background-color: rgb(0, 85, 255);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 4px solid white;\n"
                                        "border-radius: 15px;")
        self.addressLabel.setText("")
        self.addressLabel.setObjectName("addressLabel")
        self.horizontalLayout.addWidget(self.addressLabel)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.listLabel = QtWidgets.QLabel(parent=MainWindow)
        self.listLabel.setStyleSheet("font: 350 18pt \"Arial\";\n"
                                     "background-color: rgb(0, 85, 255);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border: 4px solid white;\n"
                                     "border-radius: 15px;")
        self.listLabel.setText("")
        self.listLabel.setObjectName("listLabel")
        self.horizontalLayout.addWidget(self.listLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(parent=MainWindow)
        self.label.setStyleSheet("font: 700 italic 16pt \"Arial\";\n"
                                 "background-color: rgb(70, 70, 70);\n"
                                 "color: rgb(0, 85, 255);\n"
                                 "border: 4px solid rgb(0, 85, 255);\n"
                                 "border-radius: 15px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FLTRLabel.setText(_translate("MainWindow", "fltr"))
        self.fullNameLabel.setText(_translate(
            "MainWindow", "Filter | Location | Tracking | Record"))
        self.comboBox.setPlaceholderText(_translate(
            "MainWindow", ""))
        self.comboBox.setItemText(0, _translate(
            "MainWindow", "Choose A Location..."))
        self.comboBox.setItemText(1, _translate(
            "MainWindow", "ASAP General Store #101"))
        self.comboBox.setItemText(2, _translate(
            "MainWindow", "ASAP General Store #102"))
        self.comboBox.setItemText(3, _translate(
            "MainWindow", "ASAP General Store #103"))
        self.comboBox.setItemText(4, _translate(
            "MainWindow", "ASAP General Store #104"))
        self.comboBox.setItemText(5, _translate(
            "MainWindow", "ASAP General Store #300"))
        self.comboBox.setItemText(6, _translate(
            "MainWindow", "ASAP General Store #301"))
        self.comboBox.setItemText(7, _translate(
            "MainWindow", "ASAP General Store #302"))
        self.comboBox.setItemText(8, _translate(
            "MainWindow", "ASAP General Store #304"))
        self.comboBox.setItemText(9, _translate(
            "MainWindow", "ASAP General Store #307"))
        self.comboBox.setItemText(10, _translate(
            "MainWindow", "ASAP General Store #308"))
        self.comboBox.setItemText(11, _translate(
            "MainWindow", "ASAP General Store #310"))
        self.comboBox.setItemText(12, _translate(
            "MainWindow", "ASAP General Store #311"))
        self.comboBox.setItemText(13, _translate(
            "MainWindow", "ASAP General Store #313"))
        self.comboBox.setItemText(14, _translate(
            "MainWindow", "ASAP General Store #314"))
        self.comboBox.setItemText(15, _translate(
            "MainWindow", "ASAP General Store #322"))
        self.comboBox.setItemText(16, _translate(
            "MainWindow", "ASAP General Store #330"))
        self.comboBox.setItemText(17, _translate(
            "MainWindow", "ASAP General Store #332"))
        self.comboBox.setItemText(18, _translate(
            "MainWindow", "Hydro Fuel Island"))

        self.comboBox.currentTextChanged.connect(self.comboBox_select_a)

        self.comboBox.currentTextChanged.connect(self.comboBox_select_b)

        self.label.setText(_translate("MainWindow", "A.S.A.P. Energy, Inc."))

    def comboBox_select_a(self):
        value = self.comboBox.currentText()
        if value == 'Choose A Location...':
            value = 'ASAP General Store #101'
        filterList = scrubDict(fltrListDict[value])
        self.listLabel.setText(
            f'{scrubDict(formatFilterDict(value))}')
        return

    def comboBox_select_b(self):
        value = self.comboBox.currentText()
        if value == 'Choose A Location...':
            value = 'ASAP General Store #101'
        address = scrubDict(storeAddressDict[value])
        self.addressLabel.setText(
            f'{scrubDict(formatAddressDict(value))}')
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
