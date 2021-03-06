# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculus_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 436)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 250, 60))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 40pt \"MS Shell Dlg 2\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_clean = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clean.setGeometry(QtCore.QRect(6, 106, 60, 60))
        self.pushButton_clean.setStyleSheet("QPushButton{\n"
"background-color: rgb(203, 203, 203);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(227, 227, 227);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(6, 172, 60, 60))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(6, 238, 60, 60))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(6, 304, 60, 60))
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(6, 370, 126, 60))
        self.pushButton_0.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_mark = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mark.setGeometry(QtCore.QRect(72, 106, 60, 60))
        self.pushButton_mark.setStyleSheet("QPushButton{\n"
"background-color: rgb(203, 203, 203);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(230, 230, 230);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_mark.setObjectName("pushButton_mark")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(72, 172, 60, 60))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(72, 238, 60, 60))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(72, 304, 60, 60))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(138, 106, 60, 60))
        self.pushButton_percent.setStyleSheet("QPushButton{\n"
"background-color: rgb(203, 203, 203);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(227, 227, 227);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(138, 238, 60, 60))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(138, 304, 60, 60))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(138, 172, 60, 60))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_dividing = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dividing.setGeometry(QtCore.QRect(204, 106, 60, 60))
        self.pushButton_dividing.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 170, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.pushButton_dividing.setObjectName("pushButton_dividing")
        self.pushButton_subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_subtraction.setGeometry(QtCore.QRect(204, 238, 60, 60))
        self.pushButton_subtraction.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 170, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.pushButton_subtraction.setObjectName("pushButton_subtraction")
        self.pushButton_collection = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_collection.setGeometry(QtCore.QRect(204, 304, 60, 60))
        self.pushButton_collection.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 170, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.pushButton_collection.setObjectName("pushButton_collection")
        self.pushButton_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiplication.setGeometry(QtCore.QRect(204, 172, 60, 60))
        self.pushButton_multiplication.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 170, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.pushButton_multiplication.setObjectName("pushButton_multiplication")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(138, 370, 60, 60))
        self.pushButton_dot.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 71);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(108, 108, 108);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(204, 370, 60, 60))
        self.pushButton_equals.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 170, 0);\n"
"    font: 75 18pt \"MS Shell Dlg 2\";\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.pushButton_equals.setObjectName("pushButton_equals")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_clean.setText(_translate("MainWindow", "C"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_mark.setText(_translate("MainWindow", "-/+"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_dividing.setText(_translate("MainWindow", "??"))
        self.pushButton_subtraction.setText(_translate("MainWindow", "-"))
        self.pushButton_collection.setText(_translate("MainWindow", "+"))
        self.pushButton_multiplication.setText(_translate("MainWindow", "??"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_equals.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
