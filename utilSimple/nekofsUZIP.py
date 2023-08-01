import os
import tkinter as tk
from tkinter import filedialog

import utilSimple.FileGetter as fg
import utilSimple.restoreLua as rsl
import utilSimple.LuaToDict as lj


def copyFileToCacheDir():
    root = tk.Tk()
    root.withdraw()
    # FolderName = filedialog.askdirectory()  #获取文件夹
    FileName = filedialog.askopenfilename(title="正在导入NEKODATA文件，注意这会覆盖旧有配置！",
                                          filetypes=[("NEKODATA文件", "*.nekodata")])  # 获取文件夹中的某文件
    if not os.path.exists(FileName):
        print("未选择文件或文件不存在")
        return False
    endFileName = fg.getCacheDirPath() + "\\" + os.path.basename(FileName)
    if fg.mycopyfile(FileName, endFileName) == "":
        return endFileName
    else:
        return False


def deZipFileInWindow():
    file = copyFileToCacheDir()
    if file == False:
        return False
    os.system('chcp 65001')
    deZipFile(file)


def deZipFile(file):
    command = fg.getLibDirPath() + "\\nekofs.exe -x \"" + file + "\" \"" + fg.getCacheDirPath() + "\""
    print(command)
    os.system(command)


# print(DriveLetter)
# 不管如何，初始化文件夹是必要的
fg.initDir()


def deZipLuaNeko():
    print("正在获取文件")
    deZipFileInWindow()
    print("已选择所有文件")
    a = fg.readDir(fg.getCacheDirPath() + "\\luacode\\data\\exceldata")

    print("准备正在进行lua文件还原，共有" + str(len(a)))
    rsl.restoreLuaFiles(a)

    a = fg.readDir(fg.getCachLuaTempDirPath())

    print("准备正在进行lua文件Json转义，共有" + str(len(a)))
    for i in a:
        lj.convertLuaToJson(i)
