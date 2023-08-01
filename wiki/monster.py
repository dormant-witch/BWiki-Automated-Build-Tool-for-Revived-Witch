import collections
import math
import json

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg
import wiki.wikiTool as wt
import wiki.upload as upload

cwordhandbook_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordhandbook_ch.json"))
cmonster_handbook = jt.readJsonFile(fg.join(wt.getHandbookDir(), "cmonster_handbook.json"))

cwordskill_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordskill_ch.json"))

cskillshow_common = jt.readJsonFile(fg.join(wt.getSkillPath(), "cskillshow_common.json"))

def dealNumberScore(score):
    if score>0.86:
        return "极高"
    elif score>0.72:
        return "高"
    elif score>0.58:
        return "较高"
    elif score>0.44:
        return "一般"
    elif score>0.29:
        return "较低"
    elif score>0.15:
        return "低"
    elif score>0:
        return "极低"
    else:
        return "无"

def collectAreaByName(name):
    areaArray=[]
    for i in cmonster_handbook:
        if wt.getword(cmonster_handbook[i]["nameTextID"], cwordhandbook_ch).replace("艾迪恩", "艾迪恩（敌方）")==name:
            areaArray.append(wt.getword(cmonster_handbook[i]["areaTextID"], cwordhandbook_ch))
    areaArray=list(set(areaArray))
    areaArray.reverse()
    areaText0=""
    for i in areaArray:
        areaText0+=i+"；"
    return areaText0[:-1]

# 关于序号问题，这个是根据怪物添加顺序来的，具体可以参考json表中顺序
# 如果要建立序号表，注意要选择最前的序号
def getmonsterInfo(monsterHId):
    var2=cmonster_handbook[str(monsterHId)]
    template="{{怪物<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    Name=wt.getword(var2["nameTextID"], cwordhandbook_ch).replace("艾迪恩", "艾迪恩（敌方）")
    template+="\n|名称="+Name
    template+="\n|生命="+dealNumberScore(var2["hpScore"])
    template+="\n|物攻="+dealNumberScore(var2["adScore"])
    template+="\n|魔攻="+dealNumberScore(var2["apScore"])
    bossOrNot=cmonster_handbook[monsterHId]["monsterType"]
    if bossOrNot==0:
        template+="\n|类型=<!-- 可选 小怪/首领 -->小怪"
    else:
        template+="\n|类型=<!-- 可选 小怪/首领 -->首领"

    template+="\n|编号=<!-- 游戏图鉴内可查看编号 -->"+var2["monsterNumber"]
    template+="\n|描述="+wt.getword(var2["descriptionTextID"], cwordhandbook_ch)
    template+="\n|所处位置="+collectAreaByName(Name)
    template+="\n|怪物特性="+str([wt.getword(k, cwordhandbook_ch) for k in var2["tag"]]).replace("[", "").replace("]", "").replace("\'", "").replace(", ", "，").replace("-", "无")
    skills=var2["skillid"]
    for s in range(1,len(skills)+1,1):
        template+="\n|技能"+str(s)+"="+wt.getword(cskillshow_common[str(skills[s - 1])]["nameTextID"], cwordskill_ch)
        template+="\n|技能"+str(s)+"效果="+wt.getword(cskillshow_common[str(skills[s - 1])]["exDiscribeTextID"], cwordskill_ch)
    for s in range(10-len(skills)):
        template+="\n|技能"+str(s+len(skills)+1)+"="
        template+="\n|技能"+str(s+len(skills)+1)+"效果="
    template+="\n}}"
    # print(template)
    return upload.createPair(Name,template)

allList=[]
for i in cmonster_handbook:
    if cmonster_handbook[i]["isShow"]==1:
        allList.append(getmonsterInfo(i))
upload.prepareUploadWiki(allList)