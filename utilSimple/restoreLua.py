import os
import utilSimple.FileGetter as fg

def restoreLuaFiles(allFiles):
    for file in allFiles:
        print("正在还原"+file)
        offsetCorrection(file)
        luaDecFile(file)


def offsetCorrection(file):
    with open(file,"rb") as a:
        # c=a.read()
        c=a.read()
        dd=list(c)
        # print(dd)
        dd[5]=0
        if dd[14]!=4:
            dd.insert(13,4)
        # print(dd[17])
        result = bytes(dd)
        # print(c)
        # print(result)
        with open(file, 'wb') as f:
            f.write(result)
            f.close()
        a.close()

def luaDecFile(file):
    # print(file)
    if not "lua" in file:
        return
    file2=fg.getCachLuaTempDirPath()+"\\"+os.path.basename(file)
    c=fg.getLibDirPath()+"\\luadec.exe -se UTF8 \""+file+"\">\""+file2+"\""
    # print(c)
    os.system(c)
    # print(file2)
