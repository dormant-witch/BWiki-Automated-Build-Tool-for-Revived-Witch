import collections
import json

from difflib import SequenceMatcher

# import requests
from requests import Session

import utilSimple.JsonTool as jt

import upload

#
def noColorText(textALL):
    return textALL.replace("<color=#82C65D>", "").replace("</color>", "").replace("<color=#F5A09Bff>", "") \
        .replace("<color=#FBFAA5ff>", "") \
        .replace("<color=#8CECFAff>", "") \
        .replace("<color=#B4F59Bff>", "") \
        .replace("<color=#FFCA65ff>", "")


def getRealNum(word, startPos):
    endPos = startPos
    needStop = False
    while not needStop:
        try:
            endPos += 1
            if word[endPos:endPos + 1] != ".":
                int(word[endPos:endPos + 1])
        except:
            if not word[endPos:endPos + 1] == "%":
                needStop = True
    return word[startPos:endPos]


def compareTwoString(t1, t2):
    t1 = noColorText(t1)
    t2 = noColorText(t2)
    s = SequenceMatcher(None, t1, t2)
    # print(s.get_opcodes())
    # par=1
    var1 = []
    for op, i, j, k, l in s.get_opcodes():
        if op == "equal":
            continue
        # print(op,i,j,k,l )
        # print(getRealNum(t1,i))
        # par=par+1
        var1.append([i, j, k, l])
    # var的数量说明了变化的个数
    var2 = []
    for i in range(len(var1)):
        realNum = getRealNum(t1, var1[i][0])
        # 更新完整的替换文字位置
        var1[i][1] = var1[i][0] + len(realNum)
        realNum2 = getRealNum(t2, var1[i][2])
        var2.append(str(realNum) + ";" + str(realNum2))
    divideStr = t1
    if len(var2) > 0 and (len(var2[0].split(";")[0]) == 0 or len(var2[0].split(";")[1]) == 0):
        return ""
    # print(var1,var2)
    hasCut = 0
    restr = ""
    # 拆分来替换
    for i in range(len(var2)):
        # 这种意味着已经包含了，所以要continue
        if var1[i][0] - hasCut < 0:
            continue
        varT = var2[i].split(";")
        realNum = varT[0]
        realNum2 = varT[1]
        regexText = "{{红色|" + realNum + "}}/" + "{{红色|" + realNum2 + "}}"
        re1 = divideStr[:var1[i][0] - hasCut]
        re2 = divideStr[var1[i][1] - hasCut:]
        re3 = divideStr[var1[i][0] - hasCut:var1[i][1] - hasCut]
        hasCut += len(re1 + re3)
        divideStr = re2
        restr += re1 + regexText
        if i == len(var2) - 1:
            restr += re2
    # print(restr)
    return restr
    # print(result)


with open("wiki相关/common/cscreeningconditions.json", "r", encoding="utf-8") as f:
    cscreeningconditions = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/common/caffiliation_handbook.json", "r", encoding="utf-8") as f:
    caffiliation_handbook = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/common/cfavourpresenttype.json", "r", encoding="utf-8") as f:
    cfavourpresenttype = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/common/cwordyard_ch.json", "r", encoding="utf-8") as f:
    cwordyard_ch = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/common/cyardskill.json", "r", encoding="utf-8") as f:
    cyardskill = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/common/cattreffectidname.json", "r", encoding="utf-8") as f:
    cattreffectidname = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/custom/nickName.json", "r", encoding="utf-8") as f:
    nickName = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/custom/evaluationCollection.json", "r", encoding="utf-8") as f:
    evaluationCollection = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/custom/roleAccess.json", "r", encoding="utf-8") as f:
    roleAccess = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/roleconfig.json", "r", encoding="utf-8") as f:
    roleconfig = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cwordhandbook_ch.json", "r", encoding="utf-8") as f:
    cwordhandbook_ch = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cwordrole_ch.json", "r", encoding="utf-8") as f:
    cwordrole_ch = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/ccardroleconfig_handbook.json", "r", encoding="utf-8") as f:
    ccardroleconfig_handbook = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/citemattr.json", "r", encoding="utf-8") as f:
    citemattr = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cworditem_ch.json", "r", encoding="utf-8") as f:
    cworditem_ch = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cfavourpresent.json", "r", encoding="utf-8") as f:
    cfavourpresent = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cfavourskill.json", "r", encoding="utf-8") as f:
    cfavourskill = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cwordskill_ch.json", "r", encoding="utf-8") as f:
    cwordskill_ch = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cuniqueequipcfg.json", "r", encoding="utf-8") as f:
    cuniqueequipcfg = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cwordequip_ch.json", "r", encoding="utf-8") as f:
    cwordequip_ch = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cskillitem.json", "r", encoding="utf-8") as f:
    cskillitem = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cskillshow_common.json", "r", encoding="utf-8") as f:
    cskillshow_common = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cskillshow_soul.json", "r", encoding="utf-8") as f:
    cskillshow_soul = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/crolebreakcfg.json", "r", encoding="utf-8") as f:
    crolebreakcfg = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cskillshow_role.json", "r", encoding="utf-8") as f:
    cskillshow_role = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/ccostskill.json", "r", encoding="utf-8") as f:
    ccostskill = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/croleevolutioncfg.json", "r", encoding="utf-8") as f:
    croleevolutioncfg = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cskillmap.json", "r", encoding="utf-8") as f:
    cskillmap = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/cskin.json", "r", encoding="utf-8") as f:
    cskin = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/old/csoundlines_skin.json", "r", encoding="utf-8") as f:
    csoundlines_skin = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

# csoundlines 文件不记录缺失
with open("wiki相关/json/csoundlines.json", "r", encoding="utf-8") as f:
    csoundlines = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

with open("wiki相关/json/csoundcatalog.json", "r", encoding="utf-8") as f:
    csoundcatalog = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

import utilSimple.FileGetter as fg
import wiki.wikiTool as wt

cracecfg = jt.readJsonFile(fg.join(wt.getRolePath(), "cracecfg.json"))
cwordrole_ch2 = jt.readJsonFile(fg.join(wt.getRolePath(), "cwordrole_ch.json"))


# def getWordByID(textId):
#     for i in cwordhandbook_ch:
#         if textId==i:
#             return cwordhandbook_ch[i]["text"]
#     return None
# 502778元素，501837职业，501836稀有度
def dealType(id, type):
    typeId = int(id)
    for i in cscreeningconditions:
        if i["sort"] == typeId:
            if i["typename"] == type:
                return cwordrole_ch[str(i["nameid"])]["text"]
    print(typeId, type)


# 30-1,40-1,60-1,70-1,90-1,[15+1,30+1,70+1,150+1]
# 分别为0,1,2,3破满级状态
levelBonus = [30, 70 + 15, 130 + 15 + 30, 200 + 15 + 30 + 70]
breakBonus = [16, 31, 71, 151]


def dealAttrWithBreaking(breakLv, base, add):
    # print(base,add)
    # 上方是计算比例，但是很奇怪不对
    # return str(int((add*breakBonus[breakLv-1])/(base+add*levelBonus[breakLv-1])*100))
    return ""


class Nannar:  # 1.5 倍
    class base:
        hp: float
        attack: float
        physicalDef: float
        magicDef: float

    class bonus:
        hp: float
        attack: float
        physicalDef: float
        magicDef: float

    class breakBonus:
        hp: float
        attack: float
        physicalDef: float
        magicDef: float

    def __init__(self, datasGiven: list):  # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
        self.base.hp = datasGiven[0]
        self.base.attack = datasGiven[1]
        self.base.physicalDef = datasGiven[2]
        self.base.magicDef = datasGiven[3]
        self.bonus.hp = datasGiven[4]
        self.bonus.attack = datasGiven[5]
        self.bonus.physicalDef = datasGiven[6]
        self.bonus.magicDef = datasGiven[7]
        self.breakBonus.hp = datasGiven[8]
        self.breakBonus.attack = datasGiven[9]
        self.breakBonus.physicalDef = datasGiven[10]
        self.breakBonus.magicDef = datasGiven[11]


# 数据计算公式如下：
def getStatsAt(doll, ascension: int, level: int) -> (float, float, float, float):
    # 初始值+当前突破剩余的等级
    hp = doll.base.hp + level * doll.bonus.hp
    atk = doll.base.attack + level * doll.bonus.attack
    phydef = doll.base.physicalDef + level * doll.bonus.physicalDef
    magicdef = doll.base.magicDef + level * doll.bonus.magicDef

    # 参数校正
    if abs(doll.breakBonus.magicDef - 1.5 * doll.bonus.magicDef) < 0.2:
        defFactor = 1.5 * doll.bonus.magicDef / doll.bonus.physicalDef
        magicDefFactor = 1.5
    else:
        defFactor = 1
        magicDefFactor = 1

    maxlevel = [30, 40, 60, 70]
    breakgap = [15, 35, 70, 120]
    for i in range(ascension):
        hp += doll.bonus.hp * (maxlevel[i] + breakgap[i])
        atk += doll.bonus.attack * (maxlevel[i] + breakgap[i])
        phydef += doll.bonus.physicalDef * (maxlevel[i] + breakgap[i] * defFactor)
        magicdef += doll.bonus.magicDef * (maxlevel[i] + breakgap[i] * magicDefFactor)

    return (hp, atk, phydef, magicdef)


def getBreakMaterial(breakType, pos):
    for i in crolebreakcfg:
        if crolebreakcfg[i]["breakType"] == int(breakType):
            if crolebreakcfg[i]["breaklv"] == 3:
                BreakMaterialID = crolebreakcfg[i]["itemId"][pos]
                return cworditem_ch[str(citemattr[str(BreakMaterialID)]["nameTextID"])]["text"]


def getSkillLevelMaterial(roleID):
    SkillLevelMaterialID = cskillmap[str(roleID) + "020"]["itemID"][1]
    return cworditem_ch[str(citemattr[str(SkillLevelMaterialID)]["nameTextID"])]["text"]


def getGiftName(presenttype, presentuplevel):
    for i in cfavourpresenttype:
        if cfavourpresenttype[i]["presenttype"] == presenttype:
            if cfavourpresenttype[i]["presentuplevel"] == presentuplevel:
                favourgiftID = cfavourpresenttype[i]["id"]
                return cworditem_ch[str(citemattr[str(favourgiftID)]["nameTextID"])]["text"]


def clearColorText(textALL):
    return textALL \
        .replace("<color=#82C65D>", "{{红色|") \
        .replace("<color=#FBFAA5ff>", "{{橙色|") \
        .replace("<color=#8CECFAff>", "{{蓝色|") \
        .replace("<color=#B4F59Bff>", "{{红色|") \
        .replace("<color=#FFCA65ff>", "{{橙色|") \
        .replace("<color=#F5A09Bff>", "{{红色|") \
        .replace("</color>", "}}")


def getFavourSkill(idRole, levelRewardPos):
    levelRewardID = cfavourpresent[str(idRole)]["levelRewardID"][levelRewardPos - 1]
    levelRewardtextId = cfavourskill[str(levelRewardID)]["skillattributiontxt"]
    return clearColorText(cwordskill_ch[str(levelRewardtextId)]["text"])


def getUniqueequipAttr(UniqueequipId, lv):
    for i in cuniqueequipcfg:
        if cuniqueequipcfg[i]["UniqueEquipid"] == int(UniqueequipId):
            if cuniqueequipcfg[i]["level"] == int(lv):
                # a=[]
                # a.extend(i["attrid"])
                # a.extend(i["attrnum"])
                # a.append(i["skillid"])
                # 注意extend无返回值
                return cuniqueequipcfg[i]


# 这里attr需要是一个数组，包含所有的属性，依次排列
def replaceSkillAttrWord(word, attr, levelMax):
    if levelMax == 0:
        return word
    attrSize = int(len(attr) / levelMax)
    cword = word
    for i in range(attrSize):
        regexText = "<color=#82C65D>$parameter" + str(i + 1) + "$%</color>"
        attrText = "{{红色" + str(levelMax)
        for j in range(levelMax):
            attrText += "|" + str(attr[i + attrSize * j])
        attrText += "}}"
        cword = cword.replace(regexText, attrText)
        # print(attrText)
        regexText2 = "<color=#82C65D>$parameter" + str(i + 1) + "$</color>"
        if regexText2 in cword:
            attrText = ""
            for j in range(levelMax):
                attrText += "{{红色|" + str(attr[i + attrSize * j]) + "}}/"
            attrText = attrText[:-1]
            cword = cword.replace(regexText2, attrText)

        regexText3 = "<color=#82C65D>X</color>"
        if regexText2 in cword:
            attrText = ""
            for j in range(levelMax):
                attrText += "{{红色|" + str(attr[i + attrSize * j]) + "}}/"
            attrText = attrText[:-1]
            cword = cword.replace(regexText2, attrText)
        # print(cword)
    # 清理剩余的内容
    return noColorText(cword)


# 1是是否充能，2是需要多少能量
def getCost(skillId, type):
    v1 = ccostskill[skillId]["OrderCost"]
    v2 = ccostskill[skillId]["ChaosCost"]
    if v1 > 0:
        if type == 2:
            return str(v1)
        else:
            return ""
    elif v2 > 0:
        if type == 2:
            return str(v2)
        else:
            return ""
    else:
        if type == 1:
            return "4"
        else:
            return ""


def getEvolution(evolutionType, evolutionLevel):
    for i in croleevolutioncfg:
        if croleevolutioncfg[i]["evolutionType"] == int(evolutionType):
            if croleevolutioncfg[i]["evolutionLevel"] == int(evolutionLevel):
                addProperty = croleevolutioncfg[i]["addProperty"]
                addPropertyValue = croleevolutioncfg[i]["addPropertyValue"]
                # 这个21,31非常突兀，但是与cattreffectidname可以对应上
                return cwordrole_ch[str(cattreffectidname[str(addProperty - 1)]["classnameTextID"])][
                    "text"] + "+" + str(addPropertyValue)


# 3,5,8,10,12,13,15,17
def getSkillMapBonus(skillMapID):
    # print(skillMapID)
    skillID = str(cskillmap[str(skillMapID)]["skillID"])
    Bonusskilltext = cwordskill_ch[str(cskillshow_common[skillID]["exDiscribeTextID"])]["text"]
    regexText = str(cskillshow_soul[skillID]["attr"][0])
    return Bonusskilltext.replace("<color=#82C65D>$parameter1$</color>", regexText)


def getSkinName(skinId):
    if cskin.get(str(skinId)) == None:
        return ("", -1)
    else:
        return (cwordrole_ch[str(cskin[str(skinId)]["skinNameTextID"])]["text"], skinId)


# true or false
def getcwordhandbook_chquickly(WordId):
    if WordId == -1:
        return ""
    if cwordhandbook_ch.get(str(WordId)) == None:
        return ""
    return cwordhandbook_ch.get(str(WordId))["text"]


def isSkinWithSound(SkinID):
    try:
        return not csoundlines_skin.get(str(SkinID))["Introduction"] == None
    except:
        # print(SkinID)
        return False


def collectSound(SoundMemberID, isSkin, sign):
    jsonUsed = dict("")
    if isSkin:
        jsonUsed = csoundlines_skin
    else:
        jsonUsed = csoundlines
    if jsonUsed.get(SoundMemberID) == None:
        jsonUsed = csoundcatalog
        # return ""
    jsonObject = jsonUsed[SoundMemberID]
    template = "{{语音"
    template += "\n|文件标识名=" + sign
    template += "\n|羁绊语音1=" + getcwordhandbook_chquickly(jsonObject["Impression"][0])
    template += "\n|羁绊语音2=" + getcwordhandbook_chquickly(jsonObject["Impression"][1])
    template += "\n|羁绊语音3=" + getcwordhandbook_chquickly(jsonObject["Impression"][2])
    template += "\n|羁绊语音4=" + getcwordhandbook_chquickly(jsonObject["Impression"][3])
    template += "\n|羁绊语音5={{黑幕|" + getcwordhandbook_chquickly(jsonObject["Impression"][4]) + "}}"
    template += "\n|交互1=" + getcwordhandbook_chquickly(jsonObject["touch"][0])
    template += "\n|交互2=" + getcwordhandbook_chquickly(jsonObject["touch"][1])
    template += "\n|交互3=" + getcwordhandbook_chquickly(jsonObject["touch"][2])
    template += "\n|交互4=" + getcwordhandbook_chquickly(jsonObject["touch"][3])
    template += "\n|交互5=" + getcwordhandbook_chquickly(jsonObject["touch"][4])
    template += "\n|升级=" + getcwordhandbook_chquickly(jsonObject["LevelUp"])
    template += "\n|突破=" + getcwordhandbook_chquickly(jsonObject["LimitUp"])
    template += "\n|进化=" + getcwordhandbook_chquickly(jsonObject["RareUp"])
    template += "\n|赠送礼物1=" + getcwordhandbook_chquickly(jsonObject["NormalGift"])
    template += "\n|赠送礼物2=" + getcwordhandbook_chquickly(jsonObject["FavoriteGift"])
    template += "\n|闲置=" + getcwordhandbook_chquickly(jsonObject["Standby"])
    template += "\n|魔女庭院1=" + getcwordhandbook_chquickly(jsonObject["YardTouch"][0])
    template += "\n|魔女庭院2=" + getcwordhandbook_chquickly(jsonObject["YardTouch"][1])
    template += "\n|魔女庭院3=" + getcwordhandbook_chquickly(jsonObject["Dispatch"])
    template += "\n|魔女庭院4=" + getcwordhandbook_chquickly(jsonObject["Withdraw"])
    template += "\n|登场=" + getcwordhandbook_chquickly(jsonObject["Summory"])
    template += "\n|编队=" + getcwordhandbook_chquickly(jsonObject["Formation"])
    template += "\n|探索地宫=" + getcwordhandbook_chquickly(jsonObject["Adventure"])
    template += "\n|圣坛=" + getcwordhandbook_chquickly(jsonObject["LifeHealing"])
    template += "\n|交谈1=" + getcwordhandbook_chquickly(jsonObject["Conversation"][0])
    template += "\n|交谈2=" + getcwordhandbook_chquickly(jsonObject["Conversation"][1])
    template += "\n|交谈3=" + getcwordhandbook_chquickly(jsonObject["Conversation"][2])
    template += "\n|交谈4=" + getcwordhandbook_chquickly(jsonObject["Conversation"][3])
    template += "\n|情绪1=" + getcwordhandbook_chquickly(jsonObject["Emotion"][0])
    template += "\n|情绪2=" + getcwordhandbook_chquickly(jsonObject["Emotion"][1])
    template += "\n|介绍自己=" + getcwordhandbook_chquickly(jsonObject["Introduction"])
    template += "\n|标题=" + getcwordhandbook_chquickly(jsonObject["Login"])
    template += "\n|开始战斗=" + getcwordhandbook_chquickly(jsonObject["BattleStart"])
    template += "\n|技能1=" + getcwordhandbook_chquickly(jsonObject["SkillCV"][0])
    template += "\n|技能2=" + getcwordhandbook_chquickly(jsonObject["SkillCV"][1])
    template += "\n|受击=" + getcwordhandbook_chquickly(jsonObject["Attacked"][0])
    template += "\n|复活=" + getcwordhandbook_chquickly(jsonObject["Revive"])
    template += "\n|战斗胜利=" + getcwordhandbook_chquickly(jsonObject["Victory"])
    template += "\n|战斗失败=" + getcwordhandbook_chquickly(jsonObject["Defeat"])
    template += "\n|击杀目标=" + getcwordhandbook_chquickly(jsonObject["BattleKill"])
    template += "}}"
    return template


def outputRoleInfo(id):
    template = "{{人偶<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    try:
        sortID = ccardroleconfig_handbook[id]["sortID"]
        if sortID > 1000:
            return
        template += "\n|序号=" + str(sortID)
    except:
        return
    Name = str(cwordrole_ch[str(roleconfig[id]["nameTextID"])]["text"]) \
        .replace("<b>·</b>", "·").replace("$heroine$", "魔女")
    template += "\n|名称=" + Name
    # print(id)
    template += "\n|称号=" + str(cwordrole_ch[str(roleconfig[id]["titleTextID"])]["text"])
    # 502778元素，501837职业，501836稀有度，写id是为了快速在数组中定位
    rarityID = roleconfig[id]["rarity"]
    if rarityID < 5:
        rarityID = 5 - rarityID
    template += "\n|稀有度=" + dealType(rarityID, 501836)
    vocationID = roleconfig[id]["vocation"]
    if vocationID > 4:
        vocationID += 1
    template += "\n|类型=" + dealType(vocationID, 501837)
    template += "\n|代称=" + nickName[str(sortID)]["NickName"]
    template += "\n|属性=" + dealType(roleconfig[id]["element"], 502778)
    template += "\n|生命=<!-- =后填写人偶的1级初始数据即可 -->" + str(
        int(roleconfig[id]["hp"] + roleconfig[id]["breakaddhp"]))
    template += "\n|攻击=" + str(int(roleconfig[id]["attack"] + roleconfig[id]["breakaddattack"]))
    template += "\n|物理防御=" + str(int(roleconfig[id]["def"] + roleconfig[id]["breakadddef"]))
    template += "\n|魔法防御=" + str(int(roleconfig[id]["magicDef"] + roleconfig[id]["breakaddmagicDef"]))
    template += "\n|生命成长=<!-- =后填写人偶的每级属性差值数据即可，注意有小数点 -->" + str(roleconfig[id]["addhp"])
    template += "\n|攻击成长=" + str(roleconfig[id]["addattack"])
    template += "\n|物理防御成长=" + str(roleconfig[id]["adddef"])
    template += "\n|魔法防御成长=" + str(roleconfig[id]["addmagicDef"])
    template += "\n|生命突破成长=<!-- =后填写人偶的每级属性差值数据即可，注意有小数点 -->" + str(
        roleconfig[id]["breakaddhp"])
    template += "\n|攻击突破成长=" + str(roleconfig[id]["breakaddattack"])
    template += "\n|物理防御突破成长=" + str(roleconfig[id]["breakadddef"])
    template += "\n|魔法防御突破成长=" + str(roleconfig[id]["breakaddmagicDef"])
    doll = Nannar([roleconfig[id]["hp"], roleconfig[id]["attack"], roleconfig[id]["def"], roleconfig[id]["magicDef"],
                   roleconfig[id]["addhp"], roleconfig[id]["addattack"], roleconfig[id]["adddef"],
                   roleconfig[id]["addmagicDef"],
                   roleconfig[id]["breakaddhp"], roleconfig[id]["breakaddattack"], roleconfig[id]["breakadddef"],
                   roleconfig[id]["breakaddmagicDef"]])
    dollStats = getStatsAt(doll, 4, 90)
    template += "\n|生命MAX=<!-- =后填写人偶的满突破90级数据即可 -->" + str(int(dollStats[0]))
    template += "\n|攻击MAX=" + str(int(dollStats[1]))
    template += "\n|物理防御MAX=" + str(int(dollStats[2]))
    template += "\n|魔法防御MAX=" + str(int(dollStats[3]))
    template += "\n|暴击率=<!-- 不填时，默认为8% -->"
    template += "\n|暴击程度=<!-- 不填时，默认为150% -->"
    # 真正的技能在这里
    contractskillid1 = str(roleconfig[id]["contractskillid"])
    contractskillid1 = str(cskillitem[contractskillid1]["assistskillID"][0])[:-2]
    template += "\n|1技能=" + cwordskill_ch[str(cskillshow_common[str(contractskillid1) + "01"]["nameTextID"])]["text"]
    template += "\n|1技能充能=<!-- 填写充能层数，例：4 -->" + getCost(contractskillid1 + "01", 1)
    template += "\n|1技能消耗=<!-- 填写消耗数，例：2 -->" + getCost(contractskillid1 + "01", 2)
    template += "\n|1技能类型=" + cwordskill_ch[str(cskillshow_role[contractskillid1 + "01"]["typeTextID"])]["text"]
    template += "\n|1技能范围=" + cwordskill_ch[str(cskillshow_role[contractskillid1 + "01"]["rangeTextID"])]["text"]
    skill1Text = cwordskill_ch[str(cskillshow_common[str(contractskillid1) + "01"]["exDiscribeTextID"])]["text"]
    skill1Attr = []
    skill1Attr.extend(cskillshow_role[contractskillid1 + "01"]["attr"])
    skill1Attr.extend(cskillshow_role[contractskillid1 + "02"]["attr"])
    skill1Attr.extend(cskillshow_role[contractskillid1 + "03"]["attr"])
    skill1Attr.extend(cskillshow_role[contractskillid1 + "04"]["attr"])
    skill1Attr.extend(cskillshow_role[contractskillid1 + "05"]["attr"])
    template += "\n|1技能效果=" + replaceSkillAttrWord(skill1Text, skill1Attr, 5).replace("\\n", "<br>")
    contractskillid2 = str(roleconfig[id]["contractskillid2"])
    contractskillid2 = str(cskillitem[contractskillid2]["assistskillID"][0])[:-2]
    template += "\n|2技能=" + cwordskill_ch[str(cskillshow_common[str(contractskillid2) + "01"]["nameTextID"])]["text"]
    template += "\n|2技能充能=" + getCost(contractskillid2 + "01", 1)
    template += "\n|2技能消耗=" + getCost(contractskillid2 + "01", 2)
    template += "\n|2技能类型=" + cwordskill_ch[str(cskillshow_role[contractskillid2 + "01"]["typeTextID"])]["text"]
    template += "\n|2技能范围=" + cwordskill_ch[str(cskillshow_role[contractskillid2 + "01"]["rangeTextID"])]["text"]
    skill2Text = cwordskill_ch[str(cskillshow_common[str(contractskillid2) + "01"]["exDiscribeTextID"])]["text"]
    skill2Attr = []
    skill2Attr.extend(cskillshow_role[contractskillid2 + "01"]["attr"])
    skill2Attr.extend(cskillshow_role[contractskillid2 + "02"]["attr"])
    skill2Attr.extend(cskillshow_role[contractskillid2 + "03"]["attr"])
    skill2Attr.extend(cskillshow_role[contractskillid2 + "04"]["attr"])
    skill2Attr.extend(cskillshow_role[contractskillid2 + "05"]["attr"])
    template += "\n|2技能效果=" + replaceSkillAttrWord(skill2Text, skill2Attr, 5).replace("\\n", "<br>")
    # 玛特薇芙被动存在例外
    # contractskillid3=str(roleconfig[id]["contractskillid3"])[:-2]
    contractskillid3_1 = str(cskillmap[id + "007"]["skillID"])
    contractskillid3_2 = str(cskillmap[id + "018"]["skillID"])
    template += "\n|3技能=" + cwordskill_ch[str(cskillshow_common[contractskillid3_1]["nameTextID"])]["text"]
    template += "\n|3技能消耗="
    template += "\n|3技能类型=被动"
    template += "\n|3技能范围="

    skill3Text = cwordskill_ch[str(cskillshow_common[contractskillid3_1]["exDiscribeTextID"])]["text"]
    skill3Text2 = cwordskill_ch[str(cskillshow_common[contractskillid3_2]["exDiscribeTextID"])]["text"]
    compareResult = compareTwoString(skill3Text, skill3Text2)
    # print(skill3Text, skill3Text2)
    if not compareResult == "":

        template += "\n|3技能效果=" + compareResult.replace("\\n", "<br>")
    else:
        skill3Attr = []
        skill3Attr1 = cskillshow_soul[contractskillid3_1]["attr"]
        skill3Attr.extend(skill3Attr1)
        skill3Attr2 = cskillshow_soul[contractskillid3_2]["attr"]
        # skill3Attr.extend(cskillshow_soul[contractskillid3_2]["attr"])
        skill3Attr.extend(skill3Attr2)
        if len(skill3Attr1) == len(skill3Attr2):
            template += "\n|3技能效果=" + replaceSkillAttrWord(skill3Text, skill3Attr, 2).replace("\\n", "<br>")
        else:
            template += "\n|3技能效果=1级：" + replaceSkillAttrWord(skill3Text, skill3Attr1, len(skill3Attr1)).replace(
                "\\n", "<br>")
            template += "<br>2级：" + replaceSkillAttrWord(skill3Text2, skill3Attr2, len(skill3Attr2)).replace("\\n",
                                                                                                              "<br>")
    template += "\n|进化1=<!-- 填写进化增加的属性，例：生命+620 -->" + getEvolution(roleconfig[id]["evolutionType"], 1)
    template += "\n|进化2=" + getEvolution(roleconfig[id]["evolutionType"], 2)
    template += "\n|进化3=" + getEvolution(roleconfig[id]["evolutionType"], 3)
    hasBreak = False
    skin0 = getSkinName(str(9000 + int(id)) + "03")[0]
    if skin0[0] != "":
        if (cskin[str(9000 + int(id)) + "03"]["shapeID"] == cskin[str(9000 + int(id)) + "02"]["shapeID"]) or Name in [
            "阿墨莱", "阿鵺伦", "艾妮萌", "拉芬", "梅莫菲斯", "莎诺","希奈缇娅","玉"]:
            skin0 = ("", (-1))
    template += "\n|突破造型=<!-- 没有就不写，有的话写文件名，推荐写突破造型，其余内容会自动补全 -->" + skin0[0]
    skin1 = getSkinName(str(9000 + int(id)) + "11")
    if skin1[0] == "甜蜜的时光" and Name == "奥塔薇娅":
        skin1 = ("", (-1))
    skin2 = getSkinName(str(9000 + int(id)) + "12")
    skin3 = getSkinName(str(9000 + int(id)) + "13")
    skin4 = getSkinName(str(9000 + int(id)) + "14")
    skin5 = getSkinName(str(9000 + int(id)) + "15")
    skin6 = getSkinName(str(9000 + int(id)) + "16")
    template += "\n|皮肤1=<!-- 填写皮肤名，例：炫酷墨镜 -->" + skin1[0]
    template += "\n|皮肤2=" + skin2[0]
    template += "\n|皮肤3=" + skin3[0]
    template += "\n|皮肤4=" + skin4[0]
    template += "\n|皮肤5=" + skin5[0]
    template += "\n|皮肤6=" + skin6[0]
    template += "\n|好感属性1=<!-- 填写图鉴内好感增加的属性 -->" + getFavourSkill(id, 1)
    template += "\n|好感属性5=" + getFavourSkill(id, 5)
    template += "\n|性别=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["sexTextID"])]["text"]
    template += "\n|年龄=" + ccardroleconfig_handbook[id]["age"]
    template += "\n|身高=" + ccardroleconfig_handbook[id]["weight"]
    template += "\n|生日=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["birthday"])]["text"]
    template += "\n|出身=" + cwordhandbook_ch[
        str(caffiliation_handbook[str(ccardroleconfig_handbook[id]["affiliation"])]["nameTextID"])]["text"]
    template += "\n|喜好=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["hobbyTextID"])]["text"]
    template += "\n|设计=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["artistTextID"])]["text"]
    template += "\n|声优中=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["cvTextIDChs"])]["text"]
    template += "\n|声优日=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["cvTextIDJpn"])]["text"]
    template += "\n|故事一=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["backStoryTextID"][0])][
        "text"].replace("$B$", "").replace("\\n\\n", "<br>").replace("\\n", "<br>")
    template += "\n|故事二=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["backStoryTextID"][1])][
        "text"].replace("$B$", "").replace("\\n\\n", "<br>").replace("\\n", "<br>")
    template += "\n|故事三=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["backStoryTextID"][2])][
        "text"].replace("$B$", "").replace("\\n\\n", "<br>").replace("\\n", "<br>")
    template += "\n|故事四=" + cwordhandbook_ch[str(ccardroleconfig_handbook[id]["backStoryTextID"][3])][
        "text"].replace("$B$", "").replace("\\n\\n", "<br>").replace("\\n", "<br>")
    # 30-1,40-1,60-1,70-1,90-1,[15+1,30+1,70+1,150+1]
    # 分别为0,1,2,3破满级状态
    levelBonus = [29, 29 + 16 + 39, 29 + 16 + 39 + 31 + 59, 29 + 16 + 39 + 31 + 59 + 71 + 69]
    template += "\n|突破1生命=37%" + dealAttrWithBreaking(1, roleconfig[id]["hp"], roleconfig[id]["breakaddhp"])
    template += "\n|突破1物攻=37%" + dealAttrWithBreaking(1, roleconfig[id]["attack"], roleconfig[id]["breakaddattack"])
    template += "\n|突破1物防=37%" + dealAttrWithBreaking(1, roleconfig[id]["def"], roleconfig[id]["breakadddef"])
    template += "\n|突破1魔防=37%" + dealAttrWithBreaking(1, roleconfig[id]["magicDef"],
                                                          roleconfig[id]["breakaddmagicDef"])
    template += "\n|突破2生命=43%" + dealAttrWithBreaking(2, roleconfig[id]["hp"], roleconfig[id]["breakaddhp"])
    template += "\n|突破2物攻=43%" + dealAttrWithBreaking(2, roleconfig[id]["attack"], roleconfig[id]["breakaddattack"])
    template += "\n|突破2物防=43%" + dealAttrWithBreaking(2, roleconfig[id]["def"], roleconfig[id]["breakadddef"])
    template += "\n|突破2魔防=43%" + dealAttrWithBreaking(2, roleconfig[id]["magicDef"],
                                                          roleconfig[id]["breakaddmagicDef"])
    template += "\n|突破3生命=40%" + dealAttrWithBreaking(3, roleconfig[id]["hp"], roleconfig[id]["breakaddhp"])
    template += "\n|突破3物攻=25%" + dealAttrWithBreaking(3, roleconfig[id]["attack"], roleconfig[id]["breakaddattack"])
    template += "\n|突破3物防=25%" + dealAttrWithBreaking(3, roleconfig[id]["def"], roleconfig[id]["breakadddef"])
    template += "\n|突破3魔防=25%" + dealAttrWithBreaking(3, roleconfig[id]["magicDef"],
                                                          roleconfig[id]["breakaddmagicDef"])
    template += "\n|突破4生命=48%" + dealAttrWithBreaking(4, roleconfig[id]["hp"], roleconfig[id]["breakaddhp"])
    template += "\n|突破4物攻=16%" + dealAttrWithBreaking(4, roleconfig[id]["attack"], roleconfig[id]["breakaddattack"])
    template += "\n|突破4物防=16%" + dealAttrWithBreaking(4, roleconfig[id]["def"], roleconfig[id]["breakadddef"])
    template += "\n|突破4魔防=16%" + dealAttrWithBreaking(4, roleconfig[id]["magicDef"],
                                                          roleconfig[id]["breakaddmagicDef"])
    template += "\n|突破4材料=" + getBreakMaterial(roleconfig[id]["breakType"], 1)
    template += "\n|技能彩色材料=" + getSkillLevelMaterial(id)
    # 3,5,8,10,12,13,15,17
    template += "\n|技能树2-1=<!-- 填写技能树内对应层数的属性提升（默认无视技能提升），第一个数字代表层数，第二个数字代表左右，2-1是第二层第一个属性提升，例：物理防御增加28 -->" + getSkillMapBonus(
        id + "003")
    template += "\n|技能树3-1=" + getSkillMapBonus(id + "005")
    template += "\n|技能树5-1=" + getSkillMapBonus(id + "008")
    template += "\n|技能树5-2=" + getSkillMapBonus(id + "013")
    template += "\n|技能树7-1=" + getSkillMapBonus(id + "010")
    template += "\n|技能树7-2=" + getSkillMapBonus(id + "015")
    template += "\n|技能树9-1=" + getSkillMapBonus(id + "012")
    template += "\n|技能树9-2=" + getSkillMapBonus(id + "017")
    uniqueequipid = roleconfig[id]["uniqueequipid"]
    if uniqueequipid > 0:
        template += "\n|专武名=" + cworditem_ch[str(citemattr[str(uniqueequipid)]["nameTextID"])]["text"]
        template += "\n|专武故事=" + cworditem_ch[str(citemattr[str(uniqueequipid)]["destribeTextID"])]["text"]
        var1 = getUniqueequipAttr(uniqueequipid, 1)
        equSkillId = str(var1["skillid"])[:-2]
        equSkillAttrs = []
        equSkillAttrs.extend(cskillshow_soul[equSkillId + "01"]["attr"])
        equSkillAttrs.extend(cskillshow_soul[equSkillId + "02"]["attr"])
        equSkillAttrs.extend(cskillshow_soul[equSkillId + "03"]["attr"])
        equSkillAttrs.extend(cskillshow_soul[equSkillId + "04"]["attr"])
        equSkillAttrs.extend(cskillshow_soul[equSkillId + "05"]["attr"])
        equSkillAttrs.extend(cskillshow_soul[equSkillId + "06"]["attr"])
        # print(equSkillAttrs)
        uniWord = cwordskill_ch[str(cskillshow_common[str(var1["skillid"])]["exDiscribeTextID"])]["text"]
        uniWord = replaceSkillAttrWord(uniWord, equSkillAttrs, 6)
        # print(uniWord)
        evnum = var1["evolutionnum"]
        if ";" in evnum[1]:
            uniWord_breakingBonusText = cwordequip_ch[str(var1["evolutiontext"])]["text"]
            var123 = uniWord_breakingBonusText.split("$parameter1$")
            evList = []
            size = len(evnum[1].split(";"))
            for i in range(size):
                evList.append("0")
                var123[i] = var123[i] + "<color=#82C65D>$parameter" + str(i + 1) + "$</color>"
            evList.extend(evnum[1].split(";"))
            evList.extend(evnum[2].split(";"))
            evList.extend(evnum[3].split(";"))
            uniWord_breakingBonusText = ""
            for i in range(size + 1):
                uniWord_breakingBonusText += var123[i]
            # 由于分割必须保证正确，因此需要处理这个意外
            uniWord_breakingBonusText = uniWord_breakingBonusText.replace("</color>%", "%</color>")
            uniWord += "\n" + replaceSkillAttrWord(uniWord_breakingBonusText.replace("</color>%", "%</color>"), evList,
                                                   4)
        else:
            uniWord_breakingBonus = "{{红色4|" + evnum[0] + "|" + evnum[1] + "|" + evnum[2] + "|" + evnum[3] + "}}"
            uniWord += "\n" + cwordequip_ch[str(var1["evolutiontext"])]["text"].replace("$parameter1$%",
                                                                                        uniWord_breakingBonus)
        # uniWord+=cwordequip_ch[str(var1["noevolutiontext"])]["text"]
        template += "\n|专武效果=" + uniWord
        var4 = getUniqueequipAttr(uniqueequipid, 4)["attrnum"]
        var60 = getUniqueequipAttr(uniqueequipid, 60)["attrnum"]
        template += "\n|专武生命初始=" + str(var4[0])
        template += "\n|专武生命成长=" + str(int((var60[0] - var4[0]) / 14))
        template += "\n|专武生命最大=" + str(var60[0])
        template += "\n|专武攻击初始=" + str(var4[1])
        template += "\n|专武攻击成长=" + str(int((var60[1] - var4[1]) / 14))
        template += "\n|专武攻击最大=" + str(var60[1])
        equipAttr3 = cwordrole_ch[str(cattreffectidname[str(var1["attrid"][2])]["classnameTextID"])]["text"]
        template += "\n|专武属性3=" + equipAttr3
        if "暴击" in equipAttr3:
            template += "\n|专武属性3初始=" + str(float(var4[2] / 10)) + "%"
            template += "\n|专武属性3成长=" + str(float(int((var60[2] - var4[2]) / 14) / 10)) + "%"
            template += "\n|专武属性3最大=" + str(float(var60[2] / 10)) + "%"
        else:
            template += "\n|专武属性3初始=" + str(var4[2])
            template += "\n|专武属性3成长=" + str(int((var60[2] - var4[2]) / 14))
            template += "\n|专武属性3最大=" + str(var60[2])
        equipAttr4 = cwordrole_ch[str(cattreffectidname[str(var1["attrid"][3])]["classnameTextID"])]["text"]
        template += "\n|专武属性4=" + equipAttr4
        if "暴击" in equipAttr4:
            template += "\n|专武属性4初始=" + str(float(var4[3] / 10)) + "%"
            template += "\n|专武属性4成长=" + str(float(int((var60[3] - var4[3]) / 14) / 10)) + "%"
            template += "\n|专武属性4最大=" + str(float(var60[3] / 10)) + "%"
        else:
            template += "\n|专武属性4初始=" + str(var4[3])
            template += "\n|专武属性4成长=" + str(int((var60[3] - var4[3]) / 14))
            template += "\n|专武属性4最大=" + str(var60[3])
    else:
        # 留空白在这里补充
        template += "\n|专武名=" + "\n|专武效果=" + "\n|专武生命初始=" + "\n|专武生命成长=" + "\n|专武生命最大=" + "\n|专武攻击初始=" + "\n|专武攻击成长=" + "\n|专武攻击最大=" + "\n|专武属性3=" + "\n|专武属性3初始=" + "\n|专武属性3成长=" + "\n|专武属性3最大=" + "\n|专武属性4=" + "\n|专武属性4初始=" + "\n|专武属性4成长=" + "\n|专武属性4最大="
    yardskillid = roleconfig[id]["yardskillid"][0]
    template += "\n|庭院技能=<!-- 这里写类型，下面写具体效果 -->" + noColorText(
        cwordyard_ch[str(cyardskill[str(yardskillid)]["nameTextID"])]["text"])
    template += "\n|庭院技能效果=" + clearColorText(
        cwordyard_ch[str(cyardskill[str(yardskillid)]["descTextID"])]["text"])
    template += "\n|喜欢的礼物=" + getGiftName(roleconfig[id]["favourgift"], 1)
    template += "\n|比较喜欢的礼物=" + getGiftName(roleconfig[id]["favourgift"], 2)
    template += "\n|最喜欢的礼物=" + getGiftName(roleconfig[id]["favourgift"], 3)
    template += "\n|小贴士=" + evaluationCollection[str(sortID)]["Comment"]
    template += "\n|角色评价=" + evaluationCollection[str(sortID)]["Evaluation"]
    if not evaluationCollection[str(sortID)].get("UniqueEquipEvaluation") == None:
        template += "\n|专武评价=" + evaluationCollection[str(sortID)]["UniqueEquipEvaluation"]
    else:
        template += "\n|专武评价="
    template += "\n|实装日期=" + roleAccess[str(sortID)]["UnlockTime"]
    # 相关活动仅包含限定获取、限定卡池角色
    template += "\n|相关活动=" + roleAccess[str(sortID)]["Access"]
    # 仅包含其他获取方式
    template += "\n|其他途径=" + roleAccess[str(sortID)]["OtherAccess"]

    # print(cwordrole_ch[str(cracecfg[ccardroleconfig_handbook[id]["race"]-1]["nameTextID"])])
    template += "\n|种族=" + wt.getword(cracecfg[ccardroleconfig_handbook[id]["race"] - 1]["nameTextID"], cwordrole_ch2)
    # print(cwordrole_ch[nameTextID]["text"])
    template += "\n}}"
    template += "\n<div id=\"audioContainer\">\n<tabber >"
    template += "\n初始语音=\n" + collectSound(id, False, Name)
    if skin1[1] != -1 and isSkinWithSound(skin1[1]):
        template += "\n|-|\n" + skin1[0] + "皮肤语音=\n" + collectSound(skin1[1], True, Name + "-" + skin1[0])
    template += "\n</tabber>\n</div>"
    template += "\n{{人偶图鉴导航}}"
    return template
    # print(template)
    # print(roleconfig[id]["nameTextID"])


def outRoleIdByRealName(name):
    for id in roleconfig:
        if 1 > 0:
            # if id=="45":
            # try:
            if ccardroleconfig_handbook.get(id) == None:
                continue
            isShow = ccardroleconfig_handbook[id]["isShow"]
            if isShow == 0:
                continue
            nameText = str(cwordrole_ch[str(roleconfig[id]["nameTextID"])]["text"]) \
                .replace("<b>·</b>", "·").replace("$heroine$", "魔女")
            if nameText == name:
                return outputRoleInfo(id)
                break
            else:
                pass
                # print(nameText)
        # except:
        #     print(roleconfig[id]["name"])
        #     pass
        # print("",id)


# for r in sorted(roleconfig.keys()):
#     outputRoleInfo(r)

def getRoleIdByRealID(name):
    for id in ccardroleconfig_handbook:
        if 1 > 0:
            if ccardroleconfig_handbook.get(id) == None:
                continue
            isShow = ccardroleconfig_handbook[id]["isShow"]
            if isShow == 0:
                continue
            sortID = ccardroleconfig_handbook[id]["sortID"]
            if sortID == int(name):
                return id
            else:
                pass


def getRoleIdByRealName(name):
    for id in roleconfig:
        if 1 > 0:
            # if id=="45":
            # try:
            if ccardroleconfig_handbook.get(id) == None:
                continue
            isShow = ccardroleconfig_handbook[id]["isShow"]
            if isShow == 0:
                continue
            nameText = str(cwordrole_ch[str(roleconfig[id]["nameTextID"])]["text"]).replace("<b>·</b>", "·").replace(
                "$heroine$", "魔女")
            if nameText == name:
                sortID = ccardroleconfig_handbook[id]["sortID"]
                if sortID > 1000:
                    return str(-1)
                return str(sortID)
            else:
                pass




# https://pastebin.com/8S6aE2UX 旧代码
def collect_then_upload(allList):
    taskList=[]
    for r in allList:
        rr = r
        try:
            int(rr)
        except:
            rr = getRoleIdByRealName(rr)
        if roleconfig.get(str(rr)) == None:
            continue
        # 强制跳过梅莫菲斯，似乎问题很大，目前已经解决
        # if int(rr)==48:
        #     continue
        id = getRoleIdByRealID(str(rr))
        tt = outputRoleInfo(str(id))
        titles = nickName[str(rr)]["Name"]
        taskList.append(upload.createPair(titles, tt))
    upload.prepareUploadWiki(taskList)


# 梅莫菲斯的roleconfig里面不对劲
# collect_then_upload(["达奈莉姆"])
# collect_then_upload(["精灵凝莎"])
# collect_then_upload(list(range(1,105,1)))
# print(getRoleIdByRealName("梅莫菲斯"))
# print(getRoleIdByRealName("梅莫菲斯"))
# outputRoleInfo("6")
# inputRoleName=input("请输入想要整理资料的人偶：")
# getRoleIdByRealName("埃列什嘉尔")
# print(outputRoleInfo("126"))
# print(outputRoleInfo("130"))
# for i in cskillshow_soul:
#     print(cskillshow_soul[i]["attr"])
