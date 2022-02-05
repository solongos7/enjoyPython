import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QLabel
from PyQt5 import QtCore, QtGui, uic 

Ui_Form = uic.loadUiType('./test.ui')[0]

class MyWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.Lgrid = QtWidgets.QGridLayout()
        # self.setLayout(self.Lgrid)
        self.label = QLabel('', self)
        # self.Lgrid.addWidget(self.label, 1, 1)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("폴더 선택")
        
        self.pushButton.clicked.connect(self.find_folder)

    def find_folder(self):
        global FileFolder
        FileFolder = QFileDialog.getExistingDirectory(self,'폴더를 선택', 'C:/')
        # self.label3.setText(FileFolder)
        self.label.setText(FileFolder)
        # print(FileFolder)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
