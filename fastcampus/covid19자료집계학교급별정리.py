import os
import shutil
import re

def printPATH(pathname):
        dirnames = os.listdir(pathname)

        if len(dirnames) == 0:
                print("File not exist")
        else:
            for i in range(0, len(dirnames)):
                print(pathname + dirnames[i])

def WORK():

    print("+ COVID19 자료집계 학교별 정리 +\n\n")

    test_dir = input("작업할 폴더 경로 입력(Windows탐색기 주소창에서 Ctrl+C -> Ctrl+V): ")

    test_dir += '\\'
    
    # backup_names = original_names # list
    # file_sets = set()  # set
    # file_paths = []    # list

    os.makedirs(test_dir + "유치원")
    os.makedirs(test_dir + "초등학교")
    os.makedirs(test_dir + "중학교")
    os.makedirs(test_dir + "고등학교")
    os.makedirs(test_dir + "특수학교")

    dir_names = os.listdir(test_dir) # list
    for file in dir_names:
        tmp = re.search(r'.+(유치원).+\.xls[x]',file)
        if tmp:
            shutil.move(test_dir + tmp.group(0), test_dir + "유치원")

        tmp = re.search(r'.+(중학교).+\.xls[x]',file)
        if tmp:
            shutil.move(test_dir + tmp.group(0), test_dir + "중학교")

        tmp = re.search(r'.+(고등학교).+\.xls[x]',file)
        if tmp:
            shutil.move(test_dir + tmp.group(0), test_dir + "고등학교")

    dir_names1 = os.listdir(test_dir) # list
    for file in dir_names1:
        tmp = re.search(r'.+(초등학교).+\.xls[x]',file)
        if tmp:
            shutil.move(test_dir + tmp.group(0), test_dir + "초등학교")        

    dir_names2 = os.listdir(test_dir) # list
    for file in dir_names2:
        tmp = re.search(r'.+(학교).+\.xls[x]',file)
        if tmp:
            shutil.move(test_dir + tmp.group(0), test_dir + "특수학교")


    printPATH(test_dir)

    print("\n\n파일 정리 완료!\n\n")

WORK()

print("파일 정리 끝")

exit()

# while (1):
#     t = input("다른 폴더 작업: 1\t 종료: 2 ...... ")
#     if t == '1':
#         os.system('cls')
#         WORK()
#     else:
#         print("End")
#         exit()