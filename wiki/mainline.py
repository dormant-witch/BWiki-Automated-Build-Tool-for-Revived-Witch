import collections
import math
import json

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg
import wiki.wikiTool as wt
import wiki.upload as upload

cdungeonselectmainline = jt.readJsonFile(fg.join(wt.getDungeonselectPath(), "cdungeonselectmainline.json"))
cdungeonselectworld = jt.readJsonFile(fg.join(wt.getDungeonselectPath(), "cdungeonselectworld.json"))

cworddungeonselect_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cworddungeonselect_ch.json"))
cworditem_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cworditem_ch.json"))
cwordhandbook_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordhandbook_ch.json"))

cmonster_handbook = jt.readJsonFile(fg.join(wt.getHandbookDir(), "cmonster_handbook.json"))

citemattr = jt.readJsonFile(fg.join(wt.getItemDir(), "citemattr.json"))

cboxconfig = jt.readJsonFile(fg.join(fg.join(wt.getExcelDataDir(),"sceneinteractive"), "cboxconfig.json"))

def getBoxNumInScene(sceneId):
    num=0
    for i in cboxconfig:
        if i["SceneID"]==sceneId:
            num+=1
    return num

def getItemNames(itemList, numsList):
    itemString = ""
    if not numsList == None:
        for i in range(len(itemList)):
            itemString += "{{图标|小|" + wt.getword(citemattr[str(itemList[i])]["nameTextID"],
                                                    cworditem_ch) + "|" + str(numsList[i]) + "}}，"
    else:
        for i in range(len(itemList)):
            itemString += "{{图标|小|" + wt.getword(citemattr[str(itemList[i])]["nameTextID"],
                                                    cworditem_ch) + "|}}，"
    return itemString[:-1]


def getMonsterNames(itemList):
    itemString = ""
    for i in itemList:
        itemString += wt.getword(cmonster_handbook[str(i)]["nameTextID"], cwordhandbook_ch) + "、"
    return itemString[:-1]


def getfloorInfo(floorId, charpterName):
    charpter = cdungeonselectmainline[floorId - 1]
    # print(charpter)
    template = "{{关卡"
    template += "\n|章节=" + charpterName
    template += "\n|编号=" + charpter["floor"]
    template += "\n|名称=" + wt.getword(charpter["nameTextID"], cworddungeonselect_ch)
    template += "\n|推荐等级=" + wt.calculateRoleLvText(charpter["magic"])
    template += "\n|关卡描述=" + wt.getword(charpter["describeTextID"], cworddungeonselect_ch)
    template += "\n|怪物=" + getMonsterNames(charpter["monsterid"])
    template += "\n|探索度奖励=" + (getItemNames(charpter["chestrewardItems"], charpter["chestrewardItemNums"]) if len(
        charpter["chestrewardItems"]) > 0 else "")
    template += "\n|首通掉落=" + getItemNames(charpter["firstItems"], charpter["firstItemNums"])
    template += "\n|通关掉落=" + getItemNames(charpter["suredropItems"],None)
    template += "\n|体力消耗=" + str(charpter["spirit"])
    template += "\n|Boss战=" + ("是" if charpter["isBoss"] == 1 else "否")
    scenesList = [charpter["sceneid"]]
    if type(charpter["smallnodeid"]) == list:
        scenesList.extend(charpter["smallnodeid"])
    template += "\n|区域二=" + ("有" if len(scenesList) > 1 else "<!-- 没有区域二则不填写-->")
    template += "\n|区域三=" + ("有" if len(scenesList) > 2 else "<!-- 没有区域三则不填写-->")
    boxNums=0
    for s in scenesList:
        boxNums+=getBoxNumInScene(s)
    template += "\n|宝箱数="+str(boxNums)
    template += "\n|}}"
    return (template)


listAll = []
for charpter in cdungeonselectworld:
    template = "{{面包屑|主线地图}}\n{{章节"
    charpterName = wt.getword(charpter["chapterTextID"], cworddungeonselect_ch) + "-" + wt.getword(
        charpter["worldTextID"], cworddungeonselect_ch)
    template += "\n|章节名=" + charpterName
    template += "\n|所属世界=" + wt.getword(charpter["worldTextID"], cworddungeonselect_ch)
    template += "\n|章节描述=" + charpter["detail"]
    template += "\n|探索度奖励=" + (getItemNames(charpter["worldrewardItems"], charpter["worldrewardItemNums"]) if len(
        charpter["worldrewardItems"]) > 0 else "")
    template += "\n|关卡数=" + str(len(charpter["floorlist"]))
    template += "\n|}}\n"
    floorlist = charpter["floorlist"]
    # print(template)
    for i in floorlist:
        template += "\n" + getfloorInfo(i, charpterName)
    listAll.append(upload.createPair(charpterName, template))

upload.prepareUploadWiki(listAll)
