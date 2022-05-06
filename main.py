import os
import shutil
import sys


def create(contest, round):
    os.chdir("/Users/serialcoder/Projects/")
    if contest == 'AT' and round != "":
        createAtcoder(round)
    if contest == 'PE' and round != "":
        createProjectEuler(round)
    if contest == 'GC' and round != "":
        createCodeJam(round)
    if contest == 'CF' and round != "":
        createCodeForces(round)


def createProjectEuler(round):
    createFolder(os.path.join(os.getcwd(), 'ProjectEuler'))
    os.chdir(os.path.join(os.getcwd(), 'ProjectEuler'))
    createFolder(os.path.join(os.getcwd(), round))
    os.chdir(os.path.join(os.getcwd(), round))
    shutil.copyfile('/Users/serialcoder/PycharmProjects/PythonCodingUtils/Main.java',
                    os.path.join(os.getcwd(), 'Main.java'))


def createCodeJam(round):
    createFolder(os.path.join(os.getcwd(), 'GoogleCodeJam'))
    os.chdir(os.path.join(os.getcwd(), 'GoogleCodeJam'))
    createFolder(os.path.join(os.getcwd(), round))
    os.chdir(os.path.join(os.getcwd(), round))
    for i in ['A', 'B', 'C']:
        createFolder(os.path.join(os.getcwd(), i))
        shutil.copyfile('/Users/serialcoder/PycharmProjects/PythonCodingUtils/Main.java',
                        os.path.join(os.getcwd(), i, 'Main.java'))


def createCodeForces(round):
    createFolder(os.path.join(os.getcwd(), 'CodeForces-Java'))
    os.chdir(os.path.join(os.getcwd(), 'CodeForces-Java'))
    createFolder(os.path.join(os.getcwd(), 'codeforces-parser'))
    os.chdir(os.path.join(os.getcwd(), 'codeforces-parser'))
    createFolder(os.path.join(os.getcwd(), round))
    os.chdir(os.path.join(os.getcwd(), round))
    for i in ['A', 'B', 'C', 'D', 'E']:
        createFolder(os.path.join(os.getcwd(), i))
        shutil.copyfile('/Users/serialcoder/PycharmProjects/PythonCodingUtils/Main.java',
                        os.path.join(os.getcwd(), i, 'Main.java'))


def createAtcoder(round):
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
