## 업무포털 공문 파일 정리하기

import os
import sys
import shutil

from PyQt5 import QtCore, QtGui, uic 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog


Ui_Form = uic.loadUiType('./gen_neis.ui')[0]

class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.folderName = ''

        self.btn_1.clicked.connect(self.selectFolder)
        self.btn_2.clicked.connect(self.WORK)
        self.btn_3.clicked.connect(self.viewFolder)

    def selectFolder(self):
        self.folderName = QFileDialog.getExistingDirectory(self,'폴더 선택', 'C:/')
        self.TB_folderName.setPlainText(self.folderName)

    def viewFolder(self):
        QFileDialog.getOpenFileNames(self, '작업 완료', self.folderName)

    def WORK(self):
        test_dir = self.folderName + '/'

        original_names = os.listdir(test_dir)
        backup_names = original_names
        file_sets = set()  # python set
        file_paths = []    # python list

        for file in original_names:
            file_sets.add(file[:file.find(' (')])    # 파일 이름에서 공통된 부분 -> ' (' 이전 까지 == 공문번호

        original_names = list(map(lambda name: test_dir + name, original_names))

        for file in file_sets:
            file_paths.append(test_dir + file)
            os.makedirs(test_dir + file + ']')      # 공문번호별로 폴더 만들기

        for file in backup_names:
            for dir_name in file_sets:
                if file[:file.find(' (')] == dir_name:
                    shutil.move(test_dir + file, test_dir + dir_name + ']')  # 공문번호별 폴더에 파일 옮기기

        self.label_4.setText(':: 작업 완료 ::')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    app.exec_()
    # sys.exit(app.exec_())

# -------------------------------------------------------------