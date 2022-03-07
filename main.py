import os
import shutil
import sys


def create(contest, round):
    os.chdir("/Users/serialcoder/Projects/")
    if contest == 'AT' and round != "":
        createFolder(os.path.join(os.getcwd(), 'AtCoder'))
        os.chdir(os.path.join(os.getcwd(), 'AtCoder'))
        createFolder(os.path.join(os.getcwd(), round))
        os.chdir(os.path.join(os.getcwd(), round))
        for i in ['C', 'D', 'E']:
            createFolder(os.path.join(os.getcwd(), i))
            shutil.copyfile('/Users/serialcoder/PycharmProjects/PythonCodingUtils/Main.java',
                            os.path.join(os.getcwd(), i, 'Main.java'))


def createFolder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


create(sys.argv[1], sys.argv[2])
