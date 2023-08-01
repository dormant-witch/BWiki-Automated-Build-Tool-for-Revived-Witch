import os

import utilSimple.JsonTool as jt

import utilSimple.FileGetter as fg
import wiki.wikiTool as wt

crolelevelcfg = jt.readJsonFile(fg.join(wt.getRolePath(), "crolelevelcfg.json"))

croleadvancedbase = jt.readJsonFile(fg.join(wt.getRolePath(), "croleadvancedbase.json"))

cuniqueequipcfg = jt.readJsonFile(fg.join(wt.getEquipDir(), "cuniqueequipcfg.json"))
which=[]

for i in crolelevelcfg:
    # id=str(i[id])
    which.append(i["URexp"])

# print(which)

# print(jt.dictToJson(which))
seeRune=[]
for i in range(301,351,1):
    id=str(i)
    runesUpItemNum=croleadvancedbase[id]["runesUpItemNum"]
    runesUpItem=croleadvancedbase[id]["runesUpItem"]
    # if runesUpItem==31383:
    #     print("|-\n|{}\n|{}\n|0\n|0\n|0".format(i-300,runesUpItemNum))
    # if runesUpItem==31384:
    #     print("|-\n|{}\n|0\n|{}\n|0\n|0".format(i-300,runesUpItemNum))
    # if runesUpItem==31385:
    #     print("|-\n|{}\n|0\n|0\n|{}\n|0".format(i-300,runesUpItemNum))
    # if runesUpItem==31412:
    #     print("|-\n|{}\n|0\n|0\n|0\n|{}".format(i-300,runesUpItemNum))
    seeRune.append([runesUpItem,runesUpItemNum])

# print("|}")
runes={}
allR=["31383","31384","31385","31412"]
for i in allR:
    runes[str(i)]=[]

def appendRun(tur):
    # print(runes)
    runes[str(tur[0])].append(tur[1])
    for i in allR:
        if not tur[0]==i:
            runes[str(i)].append(0)


for i in seeRune:
    appendRun(i)

unis={"mana":[0],"95071":[1],"79001":[0],"79002":[0],"79004":[0]}
uu=["95071","79001","79002","79004"]
# for i in uu:
#     unis[str(i)]=[]

def appendU(itemList,numList):
    for i in uu:
        if not int(i) in itemList:
            unis[str(i)].append(0)
    for i in range(len(itemList)):
        unis[str(itemList[i])].append(numList[i])


need=[]
for u in cuniqueequipcfg:
    if not u["UniqueEquipid"]==95071:
        continue
    unis["mana"].append(u["mana"])
    # for i in range(len(u["itemId"])):
    appendU(u["itemId"],u["itemNum"])
    # if len(u["itemId"])>0:
    #     unis[str(i)].append(u["itemNum"][0])
    # if len(u["itemId"])>1:
    #     unis[str(i)].append(u["itemNum"][0])
    # need.append([u["itemId"],u["itemId"]])


print(jt.dictToJsonNoOpen(unis))

# print(79004 in [79001, 79002])
# 这个是标准格式
# print(jt.dictToJson(runes))

# print(seeRune)
# print(jt.dictToJson(seeRune))