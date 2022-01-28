from PyQt5.QtWidgets import QMainWindow, QApplication
from calculator import Ui_MainWindow
from PyQt5 import QtGui
import sys


class UI(QMainWindow, Ui_MainWindow):
    first_num = None
    second_num = False
    error = False
    def __init__(self):
        super(UI, self).__init__()

        self.setupUi(self)

        self.show()


        self.setWindowTitle("calculator")


        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.pushButton_0.clicked.connect(self.click_number)
        self.pushButton_1.clicked.connect(self.click_number)
        self.pushButton_2.clicked.connect(self.click_number)
        self.pushButton_3.clicked.connect(self.click_number)
        self.pushButton_4.clicked.connect(self.click_number)
        self.pushButton_5.clicked.connect(self.click_number)
        self.pushButton_6.clicked.connect(self.click_number)
        self.pushButton_7.clicked.connect(self.click_number)
        self.pushButton_8.clicked.connect(self.click_number)
        self.pushButton_9.clicked.connect(self.click_number)
        self.pushButton_dot.clicked.connect(self.float_number)
        self.pushButton_clean.clicked.connect(self.clean)
        self.pushButton_percent.clicked.connect(self.percent)
        self.pushButton_mark.clicked.connect(self.mark)
        self.pushButton_collection.clicked.connect(self.operation)
        self.pushButton_subtraction.clicked.connect(self.operation)
        self.pushButton_multiplication.clicked.connect(self.operation)
        self.pushButton_dividing.clicked.connect(self.operation)


        self.pushButton_collection.setCheckable(True)
        self.pushButton_subtraction.setCheckable(True)
        self.pushButton_multiplication.setCheckable(True)
        self.pushButton_dividing.setCheckable(True)



        self.pushButton_equals.clicked.connect(self.result) # eşittir


    def click_number(self):
        button = self.sender()

        if self.label.text() == "Error":
            self.label.setText(button.text())
        elif((self.pushButton_collection.isChecked() or self.pushButton_dividing.isChecked() or self.pushButton_subtraction.isChecked() or self.pushButton_multiplication.isChecked()) and (not self.second_num)):
            self.label.setText(str(button.text()))
            self.second_num = True

        else:
            if self.label.text()=="0":
                self.label.setText("")

            elif self.label.text()=="-0":
                self.label.setText("-")



            self.label.setText(str(self.label.text() + button.text()))
            self.pushButton_clean.setText("AC")
            print(button.text())

    def float_number(self):
        dot = False
        for i in str(self.label.text()):
            if i == ".":
                dot = True
        if dot==False:
            self.label.setText(self.label.text()+".")


    def clean(self):
        self.first_num = None
        self.second_num = False
        self.label.setText("0")
        self.pushButton_clean.setText("C")

    def percent(self):
        sayi = float(self.label.text())/100
        self.label.setText(str(sayi))

    def mark(self):
        sayi = float(self.label.text()) * -1
        self.label.setText(format(sayi,'.15g'))

    def operation(self):
        button = self.sender()
        try:
            i = int(float(self.label.text()))
            self.first_num =float(self.label.text())
        except:
            self.error = True
        button.setChecked(True)
        print(self.first_num)

    def result(self):
        snd_num = float(self.label.text())


        if self.error == True:
            pass

        elif self.pushButton_collection.isChecked():
            result_num = self.first_num + snd_num
            self.pushButton_collection.setChecked(False)
            if result_num % 1 == 0:
                if len(str(abs(int(result_num)))) > 7:
                    result_num = str(result_num)[:5] + "e" + str(result_num)[6:7]
                    print(result_num)
            else:
                if len(str(abs(int(result_num)))) > 7:
                    result_num = int(result_num)
                    result_num = str(result_num)[:5] + "e" + str(result_num)[6:7]
                    print(result_num)
                elif len(str(abs(result_num))) > 8:
                    pass
                    """
                    i = str(int(result_num))
                    ii = str(int(str(result_num)[len(i)+1:7]))
                    j = str(int(ii)+1)
                    if len(ii) == len(j):
                        result_num = i + "." + ii
                        print("a")
                    else:
                        result_num = str(int(i)+1) + str(j)[1:]
                        print("b")
                    """


            print(result_num)


        elif self.pushButton_subtraction.isChecked():
            result_num = self.first_num - snd_num
            self.pushButton_subtraction.setChecked(False)

        elif self.pushButton_multiplication.isChecked():
            result_num = self.first_num * snd_num
            self.pushButton_multiplication.setChecked(False)

        elif self.pushButton_dividing.isChecked():
            if snd_num == 0.0:
                self.error = True
            else:
                result_num = self.first_num / snd_num
                if result_num % 1 == 0:
                    if len(str(abs(int(result_num)))) > 7:
                        pass
                else:
                    if len(str(abs(int(result_num)))) > 7:
                        pass
                    elif len(str(abs(result_num))) > 8:
                        if len(str(abs(result_num))) > 7:
                            if result_num % 1 == 0:
                                result_num = int(result_num)
                                result_num = int(str(result_num)[:7])
                            else:
                                result_num = float(str(result_num)[:8])


            self.pushButton_dividing.setChecked(False)

        if self.error == False:

            try:
                i = int(result_num)

                self.label.setText(format(float(result_num),'.15g'))


            except:
                self.label.setText(result_num)



        elif self.error == True:
            self.label.setText("Error")
            self.pushButton_collection.setChecked(False)
            self.pushButton_subtraction.setChecked(False)
            self.pushButton_multiplication.setChecked(False)
            self.pushButton_dividing.setChecked(False)

        self.first_num = None
        self.second_num = False
        self.error = False



app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()