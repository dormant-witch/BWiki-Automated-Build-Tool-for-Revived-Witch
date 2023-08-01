import collections
import os

import json

import utilSimple.FileGetter as fg
import utilSimple.JsonTool as jt

roleconfig = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "json\\roleconfig.json")
ccardroleconfig_handbook = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "json\\ccardroleconfig_handbook.json")
citemattr = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "json\\citemattr.json")
cworditem_ch = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "json\\cworditem_ch.json")
cwordrole_ch = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "json\\cwordrole_ch.json")
cscreeningconditions = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "common\\cscreeningconditions.json")
ccardpool = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "common\\ccardpool.json")
nickName = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "custom\\nickName.json")
evaluationCollection = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "custom\\evaluationCollection.json")
roleAccess = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "custom\\roleAccess.json")
rolePoolInfo = jt.readJsonFile(fg.getWikiDirPath() + "\\" + "custom\\rolePoolInfo.json")


# 502778元素，501837职业，501836稀有度
def dealType(id, type):
    typeId = int(id)
    for i in cscreeningconditions:
        if i["sort"] == typeId:
            if i["typename"] == type:
                return cwordrole_ch[str(i["nameid"])]["text"]
    print(typeId, type)


def saveDictByOder(dictA, file):
    dictB = collections.OrderedDict()
    for i in range(200):
        if dictA.get(str(i)) == None:
            continue
        else:
            dictB[str(i)] = dictA.get(str(i))
    jt.saveDictAsJson(fg.join(fg.getWikiCustomDirPath(), file), dictB)


def getRoleNameByRealID(id):
    return cwordrole_ch[str(roleconfig[id]["nameTextID"])]["text"] .replace("<b>·</b>", "·").replace("$heroine$", "魔女")


def updateNickName():
    a = collections.OrderedDict()
    for id in roleconfig:
        # if 1>0:
        try:
            sortID = str(ccardroleconfig_handbook[id]["sortID"])
            if int(sortID) > 1000:
                continue
            k = collections.OrderedDict()
            k["sortID"] = int(sortID)
            Name = getRoleNameByRealID(id)
            k["Name"] = Name
            # 昵称
            if not nickName.get(sortID) == None:
                k["NickName"] = nickName[sortID]["NickName"]
            else:
                k["NickName"] = ""
            a[str(sortID)] = k
        except:
            pass
    saveDictByOder(a, "nickName.json")


def updatVoteInfo():
    a = collections.OrderedDict()
    for id in roleconfig:
        # if 1>0:
        try:
            sortID = str(ccardroleconfig_handbook[id]["sortID"])
            if int(sortID) > 1000:
                continue
            Name = getRoleNameByRealID(id)
            # 投票
            if a.get(Name) == None:
                a[Name] = []

        except:
            pass
    # saveDictByOder(a, "voteInfo.json")
    # 只需要简单存储即可
    jt.saveDictAsJson(fg.join(fg.getWikiCustomDirPath(), "voteInfo.json"), a)

def updateRoleAccess():
    a = collections.OrderedDict()
    for id in roleconfig:
        # if 1>0:
        try:
            sortID = str(ccardroleconfig_handbook[id]["sortID"])
            if int(sortID) > 1000:
                continue
            k = collections.OrderedDict()
            k["sortID"] = int(sortID)
            Name = getRoleNameByRealID(id)
            k["Name"] = Name
            # 获取方式
            if not roleAccess.get(sortID) == None:
                k["UnlockTime"] = roleAccess[sortID]["UnlockTime"]
                k["Access"] = roleAccess[sortID]["Access"]
                k["OtherAccess"] = roleAccess[sortID]["OtherAccess"]

            else:
                ut = ccardroleconfig_handbook[id]["unlockTime"].split(" ")[0]
                ut = ut.split("-")
                if len(ut[1]) == 1:
                    ut[1] = "0" + ut[1]
                if len(ut[2]) == 1:
                    ut[2] = "0" + ut[2]
                k["UnlockTime"] = ut[0] + "年" + ut[1] + "月" + ut[2] + "日"
                k["Access"] = ""
                k["OtherAccess"] = ""
            a[str(sortID)] = k
        except:
            pass
    saveDictByOder(a, "roleAccess.json")


def updatEvaluationCollection():
    a = collections.OrderedDict()
    for id in roleconfig:
        # if 1>0:
        try:
            sortID = str(ccardroleconfig_handbook[id]["sortID"])
            if int(sortID) > 1000:
                continue
            k = collections.OrderedDict()
            k["sortID"] = int(sortID)
            Name = getRoleNameByRealID(id)
            k["Name"] = Name
            # 昵称
            if not evaluationCollection.get(sortID) == None:
                k["Evaluation"] = evaluationCollection[sortID]["Evaluation"]
                k["UniqueEquipName"] = evaluationCollection[sortID]["UniqueEquipName"]
                k["UniqueEquipEvaluation"] = evaluationCollection[sortID]["UniqueEquipEvaluation"]
                k["Comment"] = evaluationCollection[sortID]["Comment"]
            else:
                # 评价体系
                k["Evaluation"] = ""
                # if not roleeva.get(Name)==None:
                #     k["Evaluation"]=roleeva.get(Name)
                uniqueequipid = roleconfig[id]["uniqueequipid"]
                if uniqueequipid > 0:
                    k["UniqueEquipName"] = cworditem_ch[str(citemattr[str(uniqueequipid)]["nameTextID"])]["text"]
                else:
                    k["UniqueEquipName"] = ""
                k["UniqueEquipEvaluation"] = ""
                # if not equeva.get(Name)==None:
                #     k["UniqueEquipEvaluation"]=equeva.get(Name)
                k["Comment"] = ""
            a[str(sortID)] = k

        except:
            pass
    saveDictByOder(a, "evaluationCollection.json")


def updateRolePoolInfo():
    a = collections.OrderedDict()
    for id in roleconfig:
        # if 1>0:
        try:
            sortID = str(ccardroleconfig_handbook[id]["sortID"])
            if int(sortID) > 1000:
                continue
            k = collections.OrderedDict()
            k["sortID"] = int(sortID)
            Name = getRoleNameByRealID(id)
            k["Name"] = Name
            # 抽奖模拟器
            # 502778元素，501837职业，501836稀有度，写id是为了快速在数组中定位
            rarityID = roleconfig[id]["rarity"]
            if rarityID < 5:
                rarityID = 5 - rarityID
            k["Rarity"] = dealType(rarityID, 501836)
            vocationID = roleconfig[id]["vocation"]
            if vocationID > 4:
                vocationID += 1
            k["Vocation"] = dealType(vocationID, 501837)
            k["Element"] = dealType(roleconfig[id]["element"], 502778)
            k["Access"] = roleAccess[str(sortID)]["Access"].replace("[[", "").replace("]]", "")
            k["OtherAccess"] = roleAccess[str(sortID)]["OtherAccess"]
            a[str(sortID)] = k
        except:
            pass
    saveDictByOder(a, "rolePoolInfo.json")
