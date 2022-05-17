## Ex 4-1. 절대적 배치.
from PyQt5 import QtCore, QtGui, uic 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

Ui_Form = uic.loadUiType('./test2.ui')[0]

class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.btn_1_F)
        self.btn_2.clicked.connect(self.btn_2_F)  

        #QCalendarWidget이 자동으로 오늘 날짜가 있는 달력을 보여주게 설정
        self.calendarWidget.showToday()

    def btn_1_F(self):
        self.label.setText('버튼1 누름')
        self.textBrowser.setPlainText('Pushed Button1')

    def btn_2_F(self):
        self.label.clear()
        self.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    app.exec_()
    # sys.exit(app.exec_())