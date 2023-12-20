import json

import utilSimple.JsonTool
import wiki.wikiTool as wt
from datetime import datetime

with open(r"wiki\json\roleconfig.json", "r", encoding="utf-8") as f:
    roleconfig = json.load(f)

with open(r"wiki\json\cwordrole_ch.json", "r", encoding="utf-8") as f:
    cwordrole_ch = json.load(f)

with open(r"wiki\json\cworditem_ch.json", "r", encoding="utf-8") as f:
    cworditem_ch = json.load(f)

with open(r"wiki\json\ccardpool.json", "r", encoding="utf-8") as f:
    cardpool = json.load(f)

with open(r"wiki\json\cnpcshape.json", "r", encoding="utf-8") as f:
    cnpcshape = json.load(f)

with open(r"wiki\json\cimagepath.json", "r", encoding="utf-8") as f:
    cimagepath = json.load(f)

with open(r"wiki\json\ccardroleconfig_handbook.json", "r", encoding="utf-8") as f:
    ccardroleconfig_handbook = json.load(f)

with open(r"wiki\custom\rolePoolInfo.json", "r", encoding="utf-8") as f:
    rolePoolInfo = json.load(f)

with open(r"wiki\custom\roleAccess.json", "r", encoding="utf-8") as f:
    roleAccess = json.load(f)


def parseTime(timeStr):
    format = "%Y年%m月%d日"
    date_object = datetime.strptime(timeStr, format)
    return date_object


def getRoleNickName(roleid):
    # print(type(roleid))
    c = str(roleid)
    return roleconfig[c]["nameTextID"]


def getRealName(roleid):
    # print(type(roleid))
    c = str(roleid)
    return cwordrole_ch[c]["text"].replace("<b>·</b>", "·")


def poolName(poolName):
    for key in roleconfig:
        nameTextID = roleconfig[key]["nameTextID"]
        titleTextID = roleconfig[key]["titleTextID"]
        if getRealName(nameTextID) in poolName:
            return getRealName(nameTextID)
        if getRealName(titleTextID) in poolName:
            return getRealName(nameTextID)


def isRoleShow():
    try:
        # sortID = ccardroleconfig_handbook[id]["sortID"]
        # if sortID > 1000:
        #     return None
        return ccardroleconfig_handbook[id]["sortID"] == 1
    except:
        return False


def getImage(imageId):
    if cimagepath.get(str(imageId)) is not None:
        return {"assetName": cimagepath[str(imageId)]["assetName"],
                "assetBundle": cimagepath[str(imageId)]["assetBundle"]}
    else:
        return None


def getPool(roleShapeId):
    poolList = {}
    for p in cardpool:
        if cardpool[p]["roleshow"] == int(roleShapeId) and cardpool[p]["rightTimeShow"] != "-":
            poolList["poolName"] = cardpool[p]["poolName"]
            poolList["poolType"] = wt.getword(cardpool[p]["poolNameTextID"], cworditem_ch)
            poolList["rightTimeShowStart"] = cardpool[p]["rightTimeShow"].split(" - ")[0]
            poolList["rightTimeShowEnd"] = cardpool[p]["rightTimeShow"].split(" - ")[1]
            poolList["CellImg"] = getImage(cardpool[p]["CellImgID"])
            poolList["image"] = getImage(cardpool[p]["imageID"])
            poolList["waterLevelimg"] = getImage(cardpool[p]["waterLevelimg"])
            poolList["smalltitle"] = getImage(cardpool[p]["smalltitle"])
            break
    return poolList


def getRoleIdByRealID(name):
    for id in ccardroleconfig_handbook:
        if 1 > 0:
            if ccardroleconfig_handbook.get(id) == None:
                continue
            isShow = ccardroleconfig_handbook[id]["isShow"]
            if isShow == 0:
                continue
            sortID = ccardroleconfig_handbook[id]["sortText"]
            if sortID == name:
                return id
            else:
                pass


def creatPoolList(role):
    nameList = [[], [], [], [rolePoolInfo[role]["Name"]]]
    for rp in rolePoolInfo:
        if parseTime(roleAccess[rp]["UnlockTime"]) > parseTime(roleAccess[role]["UnlockTime"]) or rp == role:
            continue
        if rolePoolInfo[rp]["OtherAccess"] == "常驻卡池":
            if rolePoolInfo[rp]["Rarity"] == "R":
                nameList[0].append(rolePoolInfo[rp]["Name"])
            if rolePoolInfo[rp]["Rarity"] == "SR":
                nameList[1].append(rolePoolInfo[rp]["Name"])
            if rolePoolInfo[rp]["Rarity"] == "SSR":
                nameList[2].append(rolePoolInfo[rp]["Name"])
            if rolePoolInfo[rp]["Rarity"] == "UR":
                nameList[3].append(rolePoolInfo[rp]["Name"])
    return nameList


output = {}
output_addition = {}
for r in rolePoolInfo:
    role = getRoleIdByRealID(r)
    if (role is None):
        continue
    poolList = getPool(role)
    poolList2 = getPool(roleconfig[role]["uniqueequipid"]) if roleconfig[role]["uniqueequipid"] > 0 else None
    if (len(poolList) > 0):
        poolList["roleTittle"] = wt.getword(roleconfig[role]["titleTextID"], cwordrole_ch)
        poolList["roleID"] = role
        poolList["sortID"] = r
        poolList["name"] = wt.getword(roleconfig[role]["nameTextID"], cwordrole_ch)
        poolList["vocation"] = rolePoolInfo[r]["Vocation"]
        poolrolelist = creatPoolList(r)
        poolList["poolRoleRList"] = ";".join(poolrolelist[0])
        poolList["poolRoleSRList"] = ";".join(poolrolelist[1])
        poolList["poolRoleSSRList"] = ";".join(poolrolelist[2])
        poolList["poolRoleURList"] = ";".join(poolrolelist[3])
        output[r] = poolList

        # poolList_addtion={}
        # poolList_addtion["sortID"] = r
        # poolList_addtion["name"] = poolList["name"]
        # poolList_addtion["poolName"] = poolList["roleTittle"]
        # output_addition[r]=poolList_addtion

print(utilSimple.JsonTool.dictToJsonNoOpen(output))
utilSimple.JsonTool.saveDictAsJson("wiki/custom/poolConfig.json",output)
# utilSimple.JsonTool.saveDictAsJson("wiki/custom/poolConfigAddition.json",output_addition)
# print(rolePoolInfo.keys())
