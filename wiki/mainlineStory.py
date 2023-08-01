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
cwordhandbook_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordhandbook_ch.json"))
word = jt.readJsonFile(fg.join(wt.getWordPath(), "cworddialogue_ch.json"))

config = jt.readJsonFile(fg.join(wt.getDialogPath(), "cdramachatconfig.json"))
chat = jt.readJsonFile(fg.join(wt.getDialogPath(), "cdramachatlist.json"))

ctimelineconfig = jt.readJsonFile(fg.join(fg.join(wt.getExcelDataDir(), "timeline"), "ctimelineconfig.json"))


# upload.prepareUploadWiki(listAll)
def getKey(id):
    for i in word:
        if i == str(id):
            return word[i]["text"]
    return ""


def getword(i):
    a = chat[str(i)]
    ids = a["nameTextID"]
    role = ""
    if ids[0] > 0 and ids[1] > 0:
        if not word[str(ids[0])]["text"] in "null":
            role = word[str(ids[0])]["text"]
        elif not word[str(ids[1])]["text"] in "null":
            role = word[str(ids[1])]["text"]
        else:
            # print(ids)
            role = "..."
    con = ""
    if a["contentTextID"] != -1:
        con = getKey(a["contentTextID"])
        return role + "：" + con
    return None


def printlog(dialogList):
    var = dialogList.split(",")
    varList = []
    for k in var:
        if "-" in k:
            realDialogList = k.split("-")
            cc = list(range(int(realDialogList[0]), int(realDialogList[1]) + 1))
            varList.extend(cc)
        else:
            varList.append(int(k))
    textSTory = ""
    for dialoglistId in varList:
        simpleDialog = getword(dialoglistId)
        if simpleDialog != None:
            textSTory +="\n"+ str(simpleDialog)
    return textSTory


# chat=dict(chat)
# print(dict(chat))


def getLog(dialogID):
    # print(dialogID, printlog(config[dialogID]["dialogList"]))
    dialogList = config[dialogID]["dialogList"]

    textStrory = printlog(dialogList)
    next = str(config[dialogID]["nextDialog"])
    while next != "0":
        print("...")
        dialogList = config[next]["dialogList"]
        textStrory +="\n"+ printlog(dialogList)
        next = str(config[next]["nextDialog"])
    return textStrory


def getChatListByScen(sceneId):
    varl=[]
    for i in ctimelineconfig:
        if ctimelineconfig[i]["Name"] == sceneId:
            return varl.append(ctimelineconfig[i]["id"])
    return varl


def getfloorInfo(floorId, charpterName):
    charpter = cdungeonselectmainline[floorId - 1]
    # print(charpter)
    template = "==" + charpter["floor"] + " " + charpterName + "=="
    template += "\n概述：" + wt.getword(charpter["describeTextID"], cworddungeonselect_ch)
    scenesList = [charpter["sceneid"]]
    if type(charpter["smallnodeid"]) == list:
        scenesList.extend(charpter["smallnodeid"])
    for i in scenesList:
        # try:
        if i >0:
            cc=getChatListByScen(i)
            if not cc ==None:
                for j in cc:
                    template += getLog(str(j))
        # except:
            # pass

    return (template)


listAll = []
for charpter in cdungeonselectworld:
    template = "{{面包屑|主线剧情}}\n[[分类:主线剧情]]\n"
    charpterName = "\n" + wt.getword(charpter["chapterTextID"], cworddungeonselect_ch) + "-" + wt.getword(
        charpter["worldTextID"], cworddungeonselect_ch)
    template += charpterName
    template += "\n剧情概括：" + charpter["detail"]

    floorlist = charpter["floorlist"]
    # print(template)
    for i in floorlist:
        template += "\n" + getfloorInfo(i, charpterName)
    listAll.append(upload.createPair("主线剧情-" + charpterName, template))

# print(listAll)
for i in listAll:
    print(i["text"])
