# utlSimple/File.Getter.py

import collections
import json
import os

__all__ = ['getAllTextInFile', 'readDir']

import shutil


def getAllTextInFileWithSeek(path, seekPos):
    with open(path, "r", encoding="utf-8") as f:
        if seekPos > 0:
            f.seek(seekPos)
        allText = f.read()
        f.close()
        return allText


def getAllTextInFile(path):
    return getAllTextInFileWithSeek(path, 0)


def getLuaWithGBKComment(path):
    startPos = 0
    with open(path, 'rb+') as f:
        for line in f:
            if "local" in str(line[:6]):
                break
            else:
                startPos += len(line)
        f.seek(startPos)
        return f.read().decode(encoding="utf-8", errors="strict")



def readDir(dirPath):
    allFiles = []
    __readDir__(dirPath, allFiles)
    return allFiles


def __readDir__(dirPath, allFiles):
    if len(dirPath) == 0:
        print(u'不能为空')
        return
    if dirPath[-1] == '/':
        print(u'文件夹路径末尾不能加/')
        return
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            __readDir__(dirPath + "\\" + f, allFiles)
            # allFiles.append(f)
        return
    else:
        allFiles.append(dirPath)


def getFileNameFromPath(path):
    return os.path.splitext(os.path.basename(path))[0]


def getFileTypeFromPath(path):
    return os.path.splitext(os.path.basename(path))[1]


def getFileParentPathFromPath(path):
    return os.path.split(path)[0]


# srcfile 需要复制、移动的文件
# dstpath 目的地址

def mycopyfile(srcfile, dstpath):  # 复制函数
    print(srcfile,dstpath)
    if not os.path.exists(srcfile):
        return "%s not exist!" % (srcfile+dstpath)
        # print ("%s not exist!"%(srcfile))
    else:
        # fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        # if not os.path.exists(dstpath):
        #     os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath)  # 复制文件
        return ""
        # print ("copy %s -> %s"%(srcfile, dstpath))


# 这个很看文件在哪
def getRoot():
    return os.getcwd()

def join(parent,child):
    return os.path.join(parent,child)

def getCacheDirPath():
    return os.path.join(getRoot(),"cache")

def getCachLuaTempDirPath():
    return os.path.join(getCacheDirPath(),"a")


def getLibDirPath():
    return os.path.join(getRoot(),"lib")

def getWikiDirPath():
    return os.path.join(getRoot(),"wiki")

def getWikiJsonDirPath():
    return os.path.join(getWikiDirPath(),"json")

def getWikiCustomDirPath():
    return os.path.join(getWikiDirPath(),"custom")

def getDriveLetter():
    return os.getcwd()[:1] + ":"

def initDir():
    if not os.path.exists(getCacheDirPath()):
        os.makedirs(getCacheDirPath())
    if not os.path.exists(getWikiJsonDirPath()):
        os.makedirs(getWikiJsonDirPath())
    if not os.path.exists(getCachLuaTempDirPath()):
        os.makedirs(getCachLuaTempDirPath())
    if not os.path.exists(getWikiDirPath()):
        os.makedirs(getWikiDirPath())
