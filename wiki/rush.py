
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

with open("npc/cbossrushstagereward.json", "r", encoding="utf-8") as f:
    cbossrushstagereward = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cworditem_ch.json", "r", encoding="utf-8") as f:
    cworditem_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cbossrushstageshow.json", "r", encoding="utf-8") as f:
    cbossrushstageshow = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cbossrush.json", "r", encoding="utf-8") as f:
    cbossrush = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cimagepath.json", "r", encoding="utf-8") as f:
    cimagepath = json.load(f,object_pairs_hook=collections.OrderedDict)
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

# for i in cbossrushstagereward:
#     print("|-")
#     stagecondition=i["stagecondition"]
#     if stagecondition<8:
#         print("! style=\"background-color: #f8f9fa;font-weight: normal;\"|"+getwordquickly(cbossrushstageshow[str(stagecondition)]["textID"],cworddungeonselect_ch))
#     else:
#         print("! style=\"background-color: #f8f9fa;font-weight: normal;\"|噩梦"+str(stagecondition-7))
#     rewardids=i["rewardid"]
#     rewardnums=i["rewardnum"]
#     for j in range(len(rewardids)):
#         print("|{{图标|小|"+getwordquickly(citemattr[str(rewardids[j])]["nameTextID"],cworditem_ch)+"|"+str(rewardnums[j])+"}}")

def getmonsterHId(monsterId):
    jo=cmonsterconfig[str(monsterId)]
    return gethandbookid(getwordquickly(jo["nameTextID"],cwordbattle_ch)
                         .replace("地狱之焰 辛莫拉","地狱之焰-辛莫拉")
                         .replace("空之主宰 索拉迪乌斯","索拉迪乌斯").replace("【绝境】","")
                         .replace("守护者 埃舍雷","守护者埃舍雷")
                         .replace("司祭 弗莱尔","司祭弗莱尔")
                         .replace("卡蜜莉安","守护者 卡蜜莉安"))

# 没有分割符号
def dealSimpleformulaString(formulaString,lv):
    # print(formulaString)
    base=int(formulaString.split("+")[0])
    baseLv=int(formulaString.split("+(lv-")[1].split(")*")[0])
    add=int(formulaString.split("+(lv-")[1].split(")*")[1])
    textAll=str(base+(lv-baseLv)*add)
    return textAll

def dealattrWithLevel(formulaString,lv):
    textAll=""
    if not "lv" in formulaString:
        return formulaString
    if ";"in formulaString:
        testList=formulaString.split(";")
        tlist=[]
        for i in testList:
            tlist.append(dealSimpleformulaString(i,lv))
        if tlist[0]==tlist[1]:
            textAll=tlist[0]+" * "+str(len(tlist))
        else:
            for k in tlist:
                textAll+="/"+k
            textAll=textAll[1:]
    else:
        textAll=dealSimpleformulaString(formulaString,lv)

    return textAll



def getmonsterInfo(bossbattles,stage):
    monsterId=bossbattles
    monsterHId=getmonsterHId(monsterId)
    template="{{怪物-记忆再临-常驻<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    # template+="\n|名称="+getwordquickly(jo["nameTextID"],cwordbattle_ch).replace("司祭 弗莱尔","司祭弗莱尔")
    # template+="\n|类型=<!-- 可选 小怪/首领 -->首领"
    template+="\n|阶段="+str(stage)
    # for j in range(stage):
    for i in range(18):
        bossID=monsterId
            # textstage=""
            # if j>0:
            #     textstage=str(j+1)+"阶段"
        npcLevel=cmonsterconfig[bossID]["npcLevel"]+i*20
        template+="\n|等级stage"+str(i+1)+"="+str(npcLevel)
        template+="\n|$$=".replace("$$","生命stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["hpConstant"],npcLevel)
        template+="\n|$$=".replace("$$","物理攻击stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["attackConstant"],npcLevel)
        template+="\n|$$=".replace("$$","魔法攻击stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["magicattConstant"],npcLevel)
        template+="\n|$$=".replace("$$","物理防御stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["defConstant"],npcLevel)
        template+="\n|$$=".replace("$$","魔法防御stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["magicDefConstant"],npcLevel)
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

idlist=[]
for boss in cbossrush:
    idlist.append(cbossrush[boss]["sortID"])
idlist=sorted(idlist)
templateList=[]
for boss in cbossrush:
    bossbattleID=cbossrush[boss]["bossbattleID"]
    template="{{面包屑|记忆再临图鉴}}\n<br>{{折叠面板|开始}}\n{{折叠面板|标题=挑战内容|选项=1|主框=1|样式=red|展开=是}}\n{{记忆再临常驻挑战信息<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    template+="\n|挑战名称="+getwordquickly(cbossrush[boss]["nameTextID"],cworddungeonselect_ch)
    template+="\n|挑战类型="+"常驻"
    template+="\n|挑战排序="+str(idlist.index(cbossrush[boss]["sortID"]))
    # template+="\n|类型=<!-- 可选 小怪/首领 -->首领"

    enemyList=[]
    for j in cbattleinfo[str(bossbattleID)]["enemyPositions"][1:]:
        if not j=="0":
            enemyList.append(j.split("@")[0])
    monsterId=enemyList[0]
    monsterHId=getmonsterHId(monsterId)
    # print(monsterId,monsterHId)
    if monsterHId>0:
        var2=cmonster_handbook[str(monsterHId)]
    # template+="\n|Boss编号=<!-- 游戏图鉴内可查看编号 -->"+var2["monsterNumber"]
        template+="\n|描述="+getwordquickly(var2["descriptionTextID"],cwordhandbook_ch)
        template+="\n|所处位置="+getwordquickly(var2["areaTextID"],cwordhandbook_ch)
        template+="\n|怪物特性="+str([getwordquickly(k,cwordhandbook_ch) for k in var2["tag"]]).replace("[","").replace("]","").replace("\'","").replace(", ","，").replace("-","无")
    buffs=cmonsterconfig[str(enemyList[0])]["defaultBuff"].split(";")
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
            # 不考虑孢子爆炸免疫控制
            elif b=="20115":
                pass
            else:print(b)
            # template+="，"+cbuffconflicts[b]["name"].replace("大型怪免疫击飞","击飞免疫").replace("驱散狂暴调用连携-超大","超时狂暴{{#if:超过3分钟进入狂暴状态|info}}")

    template=template.replace("=，","=")
    template+="\n}}"
    template+="\n{{折叠面板|内容结束}}{{折叠面板|标题=任务奖励|选项=2|主框=1|样式=red}}\n{{#lst: 记忆再临-常驻-奖励 | 记忆再临-常驻-奖励 }}"
    needBreak=False
    stagecount=1
    # print()
    while not needBreak:
        if cmonsterconfig.get(str(int(enemyList[0])+1*stagecount))==None:
            needBreak=True
            break
        if cmonsterconfig[str(int(enemyList[0]))]["nameTextID"]==cmonsterconfig[str(int(enemyList[0])+1*stagecount)]["nameTextID"]:
            stagecount+=1
        else:
            needBreak=True
    # print(stagecount)
    template+="\n{{折叠面板|内容结束}}{{折叠面板|标题=Boss详情|选项=3|主框=1|样式=blue}}\n"+getmonsterInfo(enemyList[0],stagecount)+"\n{{折叠面板|内容结束}}\n{{折叠面板|结束}}"
    # for i in bossbattleID:
    #     print("|{{{生命|}}}".replace("生命","生命lv"+str(cmonsterconfig[str(cbattleinfo[str(i)]["bossID"])]["npcLevel"])))
    templateList.append(
        upload.createPair("记忆再临-"+getwordquickly(cbossrush[boss]["nameTextID"],cworddungeonselect_ch),template))
    # print(template)



upload.prepareUploadWiki(templateList)
# print(getmonsterInfo(bossbattles,2))
# print(templateList)
# for boss in cbossrush:
#     bossbattleID=cbossrush[boss]["bossbattleID"]
#     enemyList=[]
#     for j in cbattleinfo[str(bossbattleID)]["enemyPositions"][1:]:
#         if not j=="0":
#             enemyList.append(j.split("@")[0])
#     monsterId=enemyList[0]
#     monsterHId=getmonsterHId(monsterId)
#     if monsterHId>0:
#         var2=cmonster_handbook[str(monsterHId)]
#         print(cimagepath[str(var2["miniIcon"])]["assetBundle"])
template=""
for i in range(18):
    bossID="63012"
    bossID2="63013"
    bossID3="63014"
    # textstage=""
    # if j>0:
    #     textstage=str(j+1)+"阶段"
    npcLevel=cmonsterconfig[bossID]["npcLevel"]+i*20
    template+="\n|等级stage"+str(i+1)+"="+str(npcLevel)
    template+="\n|$$=".replace("$$","生命stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["hpConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID2]["hpConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID3]["hpConstant"],npcLevel)
    template+="\n|$$=".replace("$$","物理攻击stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["attackConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID2]["attackConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID3]["attackConstant"],npcLevel)
    template+="\n|$$=".replace("$$","魔法攻击stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["magicattConstant"],npcLevel)
    # template+="/"+dealattrWithLevel(cmonsterconfig[bossID2]["magicattConstant"],npcLevel)
    # template+="/"+dealattrWithLevel(cmonsterconfig[bossID3]["magicattConstant"],npcLevel)
    template+="\n|$$=".replace("$$","物理防御stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["defConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID2]["defConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID3]["defConstant"],npcLevel)
    template+="\n|$$=".replace("$$","魔法防御stage"+str(i+1))+dealattrWithLevel(cmonsterconfig[bossID]["magicDefConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID2]["magicDefConstant"],npcLevel)
    template+="/"+dealattrWithLevel(cmonsterconfig[bossID3]["magicDefConstant"],npcLevel)
print(template)