# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ed\Desktop\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 71))
        self.label.setStyleSheet("QLabel {\n"
" qproperty-alignment:\'AlignVCenter | AlignRight\';\n"
" border: 1px solid gray;\n"
"}\n"
"\n"
"background-color:white;")
        self.label.setObjectName("label")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(0, 70, 61, 61))
        self.button_clear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_clear.setObjectName("button_clear")
        self.button_plusminus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plusminus.setGeometry(QtCore.QRect(60, 70, 61, 61))
        self.button_plusminus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_plusminus.setObjectName("button_plusminus")
        self.button_division = QtWidgets.QPushButton(self.centralwidget)
        self.button_division.setGeometry(QtCore.QRect(180, 70, 61, 61))
        self.button_division.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.button_division.setObjectName("button_division")
        self.button_percent = QtWidgets.QPushButton(self.centralwidget)
        self.button_percent.setGeometry(QtCore.QRect(120, 70, 61, 61))
        self.button_percent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_percent.setObjectName("button_percent")
        self.button_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiplication.setGeometry(QtCore.QRect(180, 130, 61, 61))
        self.button_multiplication.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.button_multiplication.setObjectName("button_multiplication")
        self.button_seven = QtWidgets.QPushButton(self.centralwidget)
        self.button_seven.setGeometry(QtCore.QRect(0, 130, 61, 61))
        self.button_seven.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_seven.setObjectName("button_seven")
        self.button_eight = QtWidgets.QPushButton(self.centralwidget)
        self.button_eight.setGeometry(QtCore.QRect(60, 130, 61, 61))
        self.button_eight.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_eight.setObjectName("button_eight")
        self.button_nine = QtWidgets.QPushButton(self.centralwidget)
        self.button_nine.setGeometry(QtCore.QRect(120, 130, 61, 61))
        self.button_nine.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_nine.setObjectName("button_nine")
        self.button_subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.button_subtraction.setGeometry(QtCore.QRect(180, 190, 61, 61))
        self.button_subtraction.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.button_subtraction.setObjectName("button_subtraction")
        self.button_four = QtWidgets.QPushButton(self.centralwidget)
        self.button_four.setGeometry(QtCore.QRect(0, 190, 61, 61))
        self.button_four.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_four.setObjectName("button_four")
        self.button_five = QtWidgets.QPushButton(self.centralwidget)
        self.button_five.setGeometry(QtCore.QRect(60, 190, 61, 61))
        self.button_five.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_five.setObjectName("button_five")
        self.button_six = QtWidgets.QPushButton(self.centralwidget)
        self.button_six.setGeometry(QtCore.QRect(120, 190, 61, 61))
        self.button_six.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_six.setObjectName("button_six")
        self.button_addition = QtWidgets.QPushButton(self.centralwidget)
        self.button_addition.setGeometry(QtCore.QRect(180, 250, 61, 61))
        self.button_addition.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.button_addition.setObjectName("button_addition")
        self.button_one = QtWidgets.QPushButton(self.centralwidget)
        self.button_one.setGeometry(QtCore.QRect(0, 250, 61, 61))
        self.button_one.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_one.setObjectName("button_one")
        self.button_two = QtWidgets.QPushButton(self.centralwidget)
        self.button_two.setGeometry(QtCore.QRect(60, 250, 61, 61))
        self.button_two.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_two.setObjectName("button_two")
        self.button_three = QtWidgets.QPushButton(self.centralwidget)
        self.button_three.setGeometry(QtCore.QRect(120, 250, 61, 61))
        self.button_three.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_three.setObjectName("button_three")
        self.button_point = QtWidgets.QPushButton(self.centralwidget)
        self.button_point.setGeometry(QtCore.QRect(120, 310, 61, 61))
        self.button_point.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.button_point.setObjectName("button_point")
        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.button_equals.setGeometry(QtCore.QRect(180, 310, 61, 61))
        self.button_equals.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.button_equals.setObjectName("button_equals")
        self.button_zero = QtWidgets.QPushButton(self.centralwidget)
        self.button_zero.setGeometry(QtCore.QRect(0, 310, 121, 61))
        self.button_zero.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.button_zero.setObjectName("button_zero")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.button_clear.setText(_translate("MainWindow", "C"))
        self.button_plusminus.setText(_translate("MainWindow", "+/-"))
        self.button_division.setText(_translate("MainWindow", "÷"))
        self.button_percent.setText(_translate("MainWindow", "%"))
        self.button_multiplication.setText(_translate("MainWindow", "X"))
        self.button_seven.setText(_translate("MainWindow", "7"))
        self.button_eight.setText(_translate("MainWindow", "8"))
        self.button_nine.setText(_translate("MainWindow", "9"))
        self.button_subtraction.setText(_translate("MainWindow", "-"))
        self.button_four.setText(_translate("MainWindow", "4"))
        self.button_five.setText(_translate("MainWindow", "5"))
        self.button_six.setText(_translate("MainWindow", "6"))
        self.button_addition.setText(_translate("MainWindow", "+"))
        self.button_one.setText(_translate("MainWindow", "1"))
        self.button_two.setText(_translate("MainWindow", "2"))
        self.button_three.setText(_translate("MainWindow", "3"))
        self.button_point.setText(_translate("MainWindow", "."))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.button_zero.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
