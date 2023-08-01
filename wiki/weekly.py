
# 二阶段boss+maxStage得到下一阶段的id

import collections
import json

import requests
from requests import Session

import upload
with open("npc/cmonsterconfig.json", "r", encoding="utf-8") as f:
    cmonsterconfig = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cbattleinfo.json", "r", encoding="utf-8") as f:
    cbattleinfo = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cworddungeonselect_ch.json", "r", encoding="utf-8") as f:
    cworddungeonselect_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cwordhandbook_ch.json", "r", encoding="utf-8") as f:
    cwordhandbook_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cwordbattle_ch.json", "r", encoding="utf-8") as f:
    cwordbattle_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cmonster_handbook.json", "r", encoding="utf-8") as f:
    cmonster_handbook = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cwordskill_ch.json", "r", encoding="utf-8") as f:
    cwordskill_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cskillshow_common.json", "r", encoding="utf-8") as f:
    cskillshow_common = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/citemattr.json", "r", encoding="utf-8") as f:
    citemattr = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cwordbuff_ch.json", "r", encoding="utf-8") as f:
    cwordbuff_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/ccbuffconfig.json", "r", encoding="utf-8") as f:
    ccbuffconfig = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cbuffconflicts.json", "r", encoding="utf-8") as f:
    cbuffconflicts = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cweeklybossrushstagereward.json", "r", encoding="utf-8") as f:
    cweeklybossrushstagereward = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cworditem_ch.json", "r", encoding="utf-8") as f:
    cworditem_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cweeklybossrushstageshow.json", "r", encoding="utf-8") as f:
    cweeklybossrushstageshow = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cweeklybossrush.json", "r", encoding="utf-8") as f:
    cweeklybossrush = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cweeklybosscultivateskillmap.json", "r", encoding="utf-8") as f:
    cweeklybosscultivateskillmap = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()
def getwordquickly(WordId,cw):
    if WordId==-1:
        return ""
    if cw.get(str(WordId))==None:
        return ""
    return cw[str(WordId)]["text"]

def dealWithHp(hpValue):
    if not ";"in hpValue:
        return hpValue
    hpList=hpValue.split(";")
    return str(hpList[0])+" * "+str(len(hpList))

def gethandbookid(shapeID):
    for i in cmonster_handbook:
        if shapeID==getwordquickly(cmonster_handbook[i]["nameTextID"],cwordhandbook_ch):
            return int(i)
    return -1

def getSkillTextInMap(bossId,nodePosition):
    for i in cweeklybosscultivateskillmap:
        if cweeklybosscultivateskillmap[i]["mapID"]==int(bossId):
            if cweeklybosscultivateskillmap[i]["nodePosition"]==nodePosition:
                # return getwordquickly(cweeklybosscultivateskillmap[i]["buffDescriptionID"],cworddungeonselect_ch).replace(getwordquickly(cweeklybosscultivateskillmap[i]["buffNameID"],cworddungeonselect_ch).replace("破防","降低"),"{{橙色|"+getwordquickly(cweeklybosscultivateskillmap[i]["buffNameID"],cworddungeonselect_ch).replace("破防","降低")+"}}")
                return "{{橙色|"+getwordquickly(cweeklybosscultivateskillmap[i]["buffNameID"],cworddungeonselect_ch)+"}}<br>"+getwordquickly(cweeklybosscultivateskillmap[i]["buffDescriptionID"],cworddungeonselect_ch)
    return ""
# for i in cweeklybossrushstagereward:
#     print("|-")
#     stagecondition=i["stagecondition"]
#     if stagecondition<8:
#         print("|"+getwordquickly(cweeklybossrushstageshow[str(stagecondition)]["textID"],cworddungeonselect_ch))
#     else:
#         print("|噩梦"+str(stagecondition-7))
#     rewardids=i["rewardid"]
#     rewardnums=i["rewardnum"]
#     for j in range(len(rewardids)):
#         print("|{{图标|小|"+getwordquickly(citemattr[str(rewardids[j])]["nameTextID"],cworditem_ch)+"|"+str(rewardnums[j])+"}}")

def getmonsterHId(monsterId):
    jo=cmonsterconfig[str(monsterId)]
    return gethandbookid(getwordquickly(jo["nameTextID"],cwordbattle_ch)
                         .replace("地狱之焰 辛莫拉","地狱之焰-辛莫拉")
                         .replace("空之主宰 索拉迪乌斯","索拉迪乌斯")
                         .replace("守护者 埃舍雷","守护者埃舍雷")
                         .replace("司祭 弗莱尔","司祭弗莱尔"))

def getmonsterInfo(bossbattles,stage):
    monsterId=cbattleinfo[str(bossbattles[0])]["bossID"]
    monsterHId=getmonsterHId(monsterId)
    template="{{怪物-记忆再临<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    # template+="\n|名称="+getwordquickly(jo["nameTextID"],cwordbattle_ch).replace("司祭 弗莱尔","司祭弗莱尔")
    # template+="\n|类型=<!-- 可选 小怪/首领 -->首领"
    template+="\n|阶段="+str(stage)
    for j in range(stage):
        for i in bossbattles:
            bossID=str(cbattleinfo[str(i)]["bossID"]+j*18)
            textstage=""
            if j>0:
                textstage=str(j+1)+"阶段"
            template+="\n|$$=".replace("$$",textstage+"生命lv"+str(cmonsterconfig[bossID]["npcLevel"]))+dealWithHp(cmonsterconfig[bossID]["hpConstant"])
            template+="\n|$$=".replace("$$",textstage+"物理攻击lv"+str(cmonsterconfig[bossID]["npcLevel"]))+str(cmonsterconfig[bossID]["attackConstant"])
            template+="\n|$$=".replace("$$",textstage+"魔法攻击lv"+str(cmonsterconfig[bossID]["npcLevel"]))+str(cmonsterconfig[bossID]["magicattConstant"])
            template+="\n|$$=".replace("$$",textstage+"物理防御lv"+str(cmonsterconfig[bossID]["npcLevel"]))+str(cmonsterconfig[bossID]["defConstant"])
            template+="\n|$$=".replace("$$",textstage+"魔法防御lv"+str(cmonsterconfig[bossID]["npcLevel"]))+str(cmonsterconfig[bossID]["magicDefConstant"])
            template+="\n|$$=".replace("$$",textstage+"伤害减免lv"+str(cmonsterconfig[bossID]["npcLevel"]))+str(float(cmonsterconfig[bossID]["damagereduce"])/float(10))+"%"

    if monsterHId>0:
        var2=cmonster_handbook[str(monsterHId)]
        # template+="\n|编号=<!-- 游戏图鉴内可查看编号 -->"+var2["monsterNumber"]
        # template+="\n|描述="+getwordquickly(var2["descriptionTextID"],cwordhandbook_ch)
        # template+="\n|所处位置="+getwordquickly(var2["areaTextID"],cwordhandbook_ch)
        # template+="\n|怪物特性="+str([getwordquickly(k,cwordhandbook_ch) for k in var2["tag"]]).replace("[","").replace("]","").replace("\'","").replace(", ","，").replace("-","无")
        skills=var2["skillid"]
        for s in range(1,len(skills)+1,1):
            template+="\n|技能"+str(s)+"="+getwordquickly(cskillshow_common[str(skills[s-1])]["nameTextID"],cwordskill_ch)
            template+="\n|技能"+str(s)+"效果="+getwordquickly(cskillshow_common[str(skills[s-1])]["exDiscribeTextID"],cwordskill_ch)
        for s in range(10-len(skills)):
            template+="\n|技能"+str(s+len(skills)+1)+"="
            template+="\n|技能"+str(s+len(skills)+1)+"效果="
    else:
        return ""
    template+="\n}}"
    return template


templateList=[]
for boss in cweeklybossrush:
    bossbattleID=boss["bossbattleID"]
    template="{{面包屑|记忆再临图鉴}}\n<br>{{折叠面板|开始}}\n{{折叠面板|标题=挑战内容|选项=1|主框=1|样式=red|展开=是}}\n{{记忆再临挑战信息<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    template+="\n|挑战名称="+getwordquickly(boss["nameTextID"],cworddungeonselect_ch)
    template+="\n|挑战类型="+"轮回"
    template+="\n|挑战排序="+str(boss["id"])
    template+="\n|天赋养成技能树1-1="+getSkillTextInMap(boss["id"],"1;1")
    template+="\n|天赋养成技能树1-2="+getSkillTextInMap(boss["id"],"1;3")
    template+="\n|天赋养成技能树2-1="+getSkillTextInMap(boss["id"],"2;2")
    template+="\n|天赋养成技能树3-1="+getSkillTextInMap(boss["id"],"3;1")
    template+="\n|天赋养成技能树3-2="+getSkillTextInMap(boss["id"],"3;3")
    template+="\n|天赋养成技能树4-1="+getSkillTextInMap(boss["id"],"4;2")
    template+="\n|天赋养成技能树5-1="+getSkillTextInMap(boss["id"],"5;1")
    template+="\n|天赋养成技能树5-2="+getSkillTextInMap(boss["id"],"5;3")
    # template+="\n|类型=<!-- 可选 小怪/首领 -->首领"
    monsterId=cbattleinfo[str(bossbattleID[0])]["bossID"]
    monsterHId=getmonsterHId(monsterId)
    if monsterHId>0:
        var2=cmonster_handbook[str(monsterHId)]
    # template+="\n|Boss编号=<!-- 游戏图鉴内可查看编号 -->"+var2["monsterNumber"]
    template+="\n|描述="+getwordquickly(var2["descriptionTextID"],cwordhandbook_ch)
    template+="\n|所处位置="+getwordquickly(var2["areaTextID"],cwordhandbook_ch)
    template+="\n|怪物特性="+str([getwordquickly(k,cwordhandbook_ch) for k in var2["tag"]]).replace("[","").replace("]","").replace("\'","").replace(", ","，").replace("-","无")
    buffs=cmonsterconfig[str(cbattleinfo[str(bossbattleID[0])]["bossID"])]["defaultBuff"].split(";")
    if len(buffs)>0:
        template=template.replace("怪物特性=无","怪物特性=")
    for b in buffs:
        buffId=ccbuffconfig[b]["buffTextID"]
        if buffId>0:
            template+="，"+getwordquickly(buffId,cwordbuff_ch)
        else:
            if b=="20116":
                template+="，击飞免疫"
            # 这三个都是驱散狂暴buff，意味着超时狂暴
            elif b=="21761" or b=="21763" or b=="21756":
                template+="，超时狂暴{{#info:战斗超过3分钟进入狂暴状态|info}}"
            else:print(b)
            # template+="，"+cbuffconflicts[b]["name"].replace("大型怪免疫击飞","击飞免疫").replace("驱散狂暴调用连携-超大","超时狂暴{{#if:超过3分钟进入狂暴状态|info}}")

    template=template.replace("=，","=")
    template+="\n}}"
    template+="\n{{折叠面板|内容结束}}{{折叠面板|标题=任务奖励|选项=2|主框=1|样式=red}}\n{{#lst: 记忆再临-轮回-奖励 | 记忆再临-轮回-奖励 }}"
    needBreak=False
    stagecount=1
    # print()
    while not needBreak:
        if cmonsterconfig.get(str(cbattleinfo[str(bossbattleID[0])]["bossID"]+18*stagecount))==None:
            needBreak=True
            break
        if cmonsterconfig[str(cbattleinfo[str(bossbattleID[0])]["bossID"])]["nameTextID"]==cmonsterconfig[str(cbattleinfo[str(bossbattleID[0])]["bossID"]+18*stagecount)]["nameTextID"]:
            stagecount+=1
        else:
            needBreak=True
    # print(stagecount)
    template+="\n{{折叠面板|内容结束}}{{折叠面板|标题=Boss详情|选项=3|主框=1|样式=blue}}\n"+getmonsterInfo(bossbattleID,stagecount)+"\n{{折叠面板|内容结束}}\n{{折叠面板|结束}}"
    # for i in bossbattleID:
    #     print("|{{{生命|}}}".replace("生命","生命lv"+str(cmonsterconfig[str(cbattleinfo[str(i)]["bossID"])]["npcLevel"])))
    templateList.append(upload.createPair("记忆再临-轮回-"+getwordquickly(boss["nameTextID"],cworddungeonselect_ch),template))
    # print(template)


upload.prepareUploadWiki(templateList)
# print(getmonsterInfo(bossbattles,2))

# print("|-")
# for i in range(0,18,1):
#
#     stagecondition=int(i)
#     if stagecondition<8:
#         print("|"+getwordquickly(cweeklybossrushstageshow[str(i)]["textID"],cworddungeonselect_ch))
#     else:
#         print("|噩梦"+str(stagecondition-7))