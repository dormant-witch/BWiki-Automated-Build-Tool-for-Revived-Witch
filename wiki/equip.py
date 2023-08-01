import collections
import math
import json

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg
import wiki.wikiTool as wt
import wiki.upload as upload

cequip_handbook = jt.readJsonFile(fg.join(wt.getHandbookDir(), "cequip_handbook.json"))

citemattr = jt.readJsonFile(fg.join(wt.getItemDir(), "citemattr.json"))
cequipitem = jt.readJsonFile(fg.join(wt.getItemDir(), "cequipitem.json"))
citemclasstoload = jt.readJsonFile(fg.join(wt.getItemDir(), "citemclasstoload.json"))

cequipscreeningconditions = jt.readJsonFile(fg.join(wt.getEquipDir(), "cequipscreeningconditions.json"))
cequipsuit = jt.readJsonFile(fg.join(wt.getEquipDir(), "cequipsuit.json"))
cequipsuitcfg = jt.readJsonFile(fg.join(wt.getEquipDir(), "cequipsuitcfg.json"))

cwordequip_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordequip_ch.json"))
cworditem_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cworditem_ch.json"))
cwordrole_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordrole_ch.json"))
cwordskill_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordskill_ch.json"))

cattreffectidname = jt.readJsonFile(fg.join(wt.getRolePath(), "cattreffectidname.json"))

cskillshow_common = jt.readJsonFile(fg.join(wt.getSkillPath(), "cskillshow_common.json"))


# 1500060是品质，1500061是种类，1500071是套装
def dealEquipType(id, type):
    typeId = int(id)
    for i in cequipscreeningconditions:
        if cequipscreeningconditions[i]["sort"] == typeId:
            if cequipscreeningconditions[i]["typename"] == type:
                return wt.getword(cequipscreeningconditions[i]["nameid"], cwordequip_ch)
    print(typeId, type)
    # return str(typeId)


def dealRarityAsInt(rarity):
    if Rarity == "蓝":
        return 1
    elif Rarity == "紫":
        return 2
    elif Rarity == "金":
        return 3
    else:
        return 4


def getMaxMultiple(Rarity):
    # 99,79,59,39
    if Rarity == "蓝":
        return 39
    elif Rarity == "紫":
        return 59
    elif Rarity == "金":
        return 79
    else:
        return 99


upList=[]
for i in cequip_handbook:
    if not cequip_handbook[i]["isShow"] == 1:
        continue
    # print(cequip_handbook[i])
    template = "{{装备<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    Name=wt.getword(cequip_handbook[i]["nameTextID"], cworditem_ch)
    template += "\n|名称=" + Name
    template += "\n|类型=<!-- 装备类型，可选填写 武器/防具/饰品 -->" + wt.getword(citemclasstoload[str(cequip_handbook[i]["itemType"])]["nameTextID"], cworditem_ch)
    template += "\n|编号=<!-- 游戏图鉴内可查看编号 -->" + cequip_handbook[i]["equipNumber"]
    rarityid = cequip_handbook[i]["rarity"]
    if rarityid == 5:
        rarityid = 1
    else:
        rarityid = 5 - rarityid
    Rarity = dealEquipType(rarityid, 1500060)
    template += "\n|稀有度=<!-- 背景颜色，可选填写 蓝/紫/金/传奇 -->" + Rarity
    # cequipsuitcfg是个数组，所以要-1
    template += "\n|适用职业=" + wt.getword(cequipsuitcfg[cequipitem[i]["equipAttrib"] - 1]["txtid"],
                                            cwordequip_ch)
    template += "\n|描述=" + wt.getword(cequip_handbook[i]["destribeTextID"], cworditem_ch)
    equipSuitid=cequipitem[i]["equipSuitid"]
    if equipSuitid>0:
        skillID1=cequipsuit[equipSuitid-1]["suitSkillID"][0]
        skillID2=cequipsuit[equipSuitid-1]["suitSkillID"][1]
        skillID3=cequipsuit[equipSuitid-1]["suitSkillID"][2]
        template += "\n|印记="+wt.getword(cequipsuit[equipSuitid - 1]["suitName"], cwordequip_ch)
        if skillID1>0:
            template += "\n|效果=1件:"+wt.getword(cskillshow_common[str(skillID1)]["exDiscribeTextID"], cwordskill_ch)
        if skillID2>0:
            template += "\n|效果=2件:"+wt.getword(cskillshow_common[str(skillID2)]["exDiscribeTextID"], cwordskill_ch)
        if skillID3>0:
            template += "\n3件:"+wt.getword(cskillshow_common[str(skillID3)]["exDiscribeTextID"], cwordskill_ch)
    else:
        template += "\n|印记=无"
        template += "\n|效果=无"
    var1 = cequipitem[i]["abilityID"]
    var2 = cequipitem[i]["abilityValue"]
    equipAttr1 = wt.getword(cattreffectidname[str(var1[0])]["classnameTextID"], cwordrole_ch)
    template += "\n|属性1=" + equipAttr1
    template += "\n|属性1初始=" + str(math.ceil(var2[0] * cequipitem[i]["initMagnify"]))
    template += "\n|属性1成长=" + str(math.ceil(var2[0]))
    template += "\n|属性1满破满级=" + str(math.ceil(var2[0] * getMaxMultiple(Rarity)))
    template += "\n|属性1突破1加成=+53%"
    if dealRarityAsInt(Rarity) > 1:
        template += "\n|属性1突破2加成=26%"
    else:
        template += "\n|属性1突破3加成=\\"
    if dealRarityAsInt(Rarity) > 2:
        template += "\n|属性1突破3加成=17%"
    else:
        template += "\n|属性1突破4加成=\\"
    if dealRarityAsInt(Rarity) > 3:
        template += "\n|属性1突破4加成=13%"
    else:
        template += "\n|属性1突破2加成=\\"
    # template+="\n|属性1突破5加成=/"
    equipAttr2 = wt.getword(cattreffectidname[str(var1[1])]["classnameTextID"], cwordrole_ch)
    template += "\n|属性2=" + equipAttr2
    template += "\n|属性2初始=" + str(math.ceil(var2[1] * cequipitem[i]["initMagnify"]))
    template += "\n|属性2成长=" + str(math.ceil(var2[1]))
    template += "\n|属性2满破满级=" + str(math.ceil(var2[1] * getMaxMultiple(Rarity)))
    template += "\n|属性2突破1加成=+53%"
    if dealRarityAsInt(Rarity) > 1:
        template += "\n|属性2突破2加成=26%"
    else:
        template += "\n|属性2突破3加成=\\"
    if dealRarityAsInt(Rarity) > 2:
        template += "\n|属性2突破3加成=17%"
    else:
        template += "\n|属性2突破4加成=\\"
    if dealRarityAsInt(Rarity) > 3:
        template += "\n|属性2突破4加成=13%"
    else:
        template += "\n|属性2突破2加成=\\"
    # template+="\n|属性2突破5加成=/"
    template += "\n}}"
    # print(template)
    upList.append(upload.createPair(Name,template))

upload.prepareUploadWiki(upList)
