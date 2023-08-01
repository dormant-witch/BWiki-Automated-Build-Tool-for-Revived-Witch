import os

import utilSimple.JsonTool as jt

import utilSimple.FileGetter as fg
import wiki.wikiTool as wt

roleconfig = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "roleconfig.json"))
cwordrole_ch = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "cwordrole_ch.json"))
cnpcshape = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "cnpcshape.json"))
ccardroleconfig_handbook = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "ccardroleconfig_handbook.json"))


def getName(roleID):
    return wt.getword(roleconfig[str(roleID)]["nameTextID"], cwordrole_ch) \
        .replace("<b>·</b>", "·").replace("$heroine$", "魔女")


def isShow(roleID):
    try:
        sortID = ccardroleconfig_handbook[roleID]["sortID"]
        if sortID > 1000:
            return False
        return True
    except:
        return False





basePath = r"characters"
newPath = r"aa"

files=fg.readDir(newPath)
all=[]

for i in files:
    all.append(fg.getFileNameFromPath(i).replace("-像素小人",""))

for i in roleconfig:
    if not isShow(i):
        # print(i)
        continue
    print(getName(i))
    shapeID = str(roleconfig[i]["shapeID"])
    shapeName = cnpcshape[shapeID]["assetBundleName"].split("/")[1].split(".")[0]
    originName = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "char").replace("_v1",
                                                                                                          "") + "_bi01.png"
    originName2 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "_bi01.png"
    originName3 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "cha").replace("_v1",
                                                                                                          "") + "_bi01.png"
    originName4 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "_i01.png"
    originName5 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "char").replace("_v1",
                                                                                                           "") + "_i01.png"
    originName6 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "_001.png"
    originName7 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "char") + "bi01.png"
    originName8 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "char").replace("_v1",
                                                                                                           "") + "_act_di01.png"
    originName9 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "_01.png"
    originName10 = basePath + "\\" + shapeName + "\\sprites\\n001_i01.png"
    originName11 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "_1.png"
    originName13 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "Char") + "_i1.png"
    originName14 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "bi1.png"
    originName15 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName + "i01.png"
    originName16 = basePath + "\\" + shapeName + "\\sprites\\" + shapeName.replace("char_", "char") + "_nbi01.png"
    # print()
    # if not getName(i) in all:
    #     print(originName16, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName,newPath+"/"+getName(i)+"-像素小人.png")
    # fg.mycopyfile(originName2,newPath+"/"+getName(i)+"-像素小人.png")
    # fg.mycopyfile(originName3,newPath+"/"+getName(i)+"-像素小人.png")
    # fg.mycopyfile(originName4, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName5, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName6, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName7, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName8, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName9, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName10, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName11, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName13, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName14, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName15, newPath + "/" + getName(i) + "-像素小人.png")
    # fg.mycopyfile(originName16, newPath + "/" + getName(i) + "-像素小人.png")
