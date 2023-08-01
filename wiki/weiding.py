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

with open("npc/cweidingbattleconfig.json", "r", encoding="utf-8") as f:
    cweidingbattleconfig = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("npc/cweidingsort.json", "r", encoding="utf-8") as f:
    cweidingsort = json.load(f,object_pairs_hook=collections.OrderedDict)
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

with open("npc/centryconfig.json", "r", encoding="utf-8") as f:
    centryconfig = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cwordskill_ch.json", "r", encoding="utf-8") as f:
    cwordskill_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("json/cskillshow_common.json", "r", encoding="utf-8") as f:
    cskillshow_common = json.load(f,object_pairs_hook=collections.OrderedDict)
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
    # 弗莱尔的外形有所不同
    if int(shapeID)==20016:
        shapeID=20089
    for i in cmonster_handbook:
        if str(shapeID)==str(cmonster_handbook[i]["shapeID"]):
            return int(i)
    return -1

def isNotUniqueType(entryId):
    var0=0
    for i in range(len(centryconfig)):
        if not centryconfig[i]["entrygroup"] ==centryconfig[int(entryId)-1]["entrygroup"]:
            continue
        if centryconfig[i]["entrytype"]==centryconfig[int(entryId)-1]["entrytype"]:
                var0+=1
    # print(entryId,var0)
    if var0>1:
        return "否"
    else:
        return "是"

# print(isNotUniqueType(0))

def getmonsterInfo(monsterId):
    jo=cmonsterconfig[str(monsterId)]
    monsterHId=gethandbookid(jo["shapeID"])
    template="{{怪物1<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    template+="\n|名称="+getwordquickly(jo["nameTextID"],cwordbattle_ch).replace("司祭 弗莱尔","司祭弗莱尔")
    template+="\n|等级="+str(jo["npcLevel"])
    template+="\n|生命="+dealWithHp(jo["hpConstant"])
    template+="\n|物理攻击="+jo["attackConstant"]
    template+="\n|魔法攻击="+jo["magicattConstant"]
    template+="\n|物理防御="+jo["defConstant"]
    template+="\n|魔法防御="+jo["magicDefConstant"]
    bossOrNot=jo["bossOrNot"]
    if bossOrNot==0:
        template+="\n|类型=<!-- 可选 小怪/首领 -->小怪"
    else:
        template+="\n|类型=<!-- 可选 小怪/首领 -->首领"

    if monsterHId>0:
        var2=cmonster_handbook[str(monsterHId)]
        template+="\n|编号=<!-- 游戏图鉴内可查看编号 -->"+var2["monsterNumber"]
        template+="\n|描述="+getwordquickly(var2["descriptionTextID"],cwordhandbook_ch)
        template+="\n|所处位置="+getwordquickly(var2["areaTextID"],cwordhandbook_ch)
        template+="\n|怪物特性="+str([getwordquickly(k,cwordhandbook_ch) for k in var2["tag"]]).replace("[","").replace("]","").replace("\'","").replace(", ","，").replace("-","无")
        skills=var2["skillid"]
        for s in range(1,len(skills)+1,1):
            template+="\n|技能"+str(s)+"="+getwordquickly(cskillshow_common[str(skills[s-1])]["nameTextID"],cwordskill_ch)
            template+="\n|技能"+str(s)+"效果="+getwordquickly(cskillshow_common[str(skills[s-1])]["exDiscribeTextID"],cwordskill_ch)
        for s in range(10-len(skills)):
            template+="\n|技能"+str(s+len(skills)+1)+"="
            template+="\n|技能"+str(s+len(skills)+1)+"效果="
    else:
        template+="\n|编号=<!-- 游戏图鉴内可查看编号 -->\n|描述=\n|所处位置=\n|怪物特性=\n|技能1=\n|技能1效果=\n|技能2=\n|技能2效果=\n|技能3=\n|技能3效果=\n|技能4=\n|技能4效果=\n|技能5=\n|技能5效果=\n|技能6=\n|技能6效果=\n|技能7=\n|技能7效果=\n|技能8=\n|技能8效果=\n|技能9=\n|技能9效果=\n|技能10=\n|技能10效果="
    template+="\n}}"
    return template


def getTargetInfo(battleID):
    template="{{挑战条件<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    # print(cweidingbattleconfig[battleID]["nameTextID"])
    tittle=""
    template+="\n|挑战名称="+getwordquickly(cweidingbattleconfig[battleID]["nameTextID"],cworddungeonselect_ch)
    sort=cweidingsort[battleID]["sort"]
    if sort==1:
        template+="\n|挑战类型=周常"
    else:
        template+="\n|挑战类型=日常"+str(sort-1)
    template+="\n|挑战排序="+str(sort)
    template+="\n|组合="+str(cweidingbattleconfig[battleID]["type"])
    points=int(cweidingbattleconfig[battleID]["points"])
    entryList=cweidingbattleconfig[battleID]["entryId"]
    # print(getwordquickly(cweidingbattleconfig[battleID]["nameTextID"],cworddungeonselect_ch),battleID,len(entryList),entryList)
    for ii in range(int(len(entryList)/3)):
        allowMul=isNotUniqueType(entryList[ii*3])
        template+="\n|词条选项" + str(ii) +"是否多选=" + allowMul
        entryMyPoints=[]
        for k in range(1,4,1):
            currentEntryId=entryList[ii*3+k-1]-1
            # print(centryconfig[currentEntryId]["textID"])
            template+="\n|词条选项"+str(ii)+"-"+str(k)+"="+getwordquickly(centryconfig[currentEntryId]["textID"],cworddungeonselect_ch)
            template+="\n|词条选项"+str(ii)+"-"+str(k)+"分数="+str(centryconfig[currentEntryId]["bonusPoints"])
            entryMyPoints.append(centryconfig[currentEntryId]["bonusPoints"])
        if allowMul=="是":
            points+=entryMyPoints[0]+entryMyPoints[1]+entryMyPoints[2]
        else:points+=max(entryMyPoints)
    template+="\n|基础分数="+str(cweidingbattleconfig[battleID]["points"])
    template+="\n|最高分数="+str(points)
    template+="\n}}"
    return template


def prepareUploadWiki():
    allList=[]
    for i in cweidingbattleconfig:
        if cweidingbattleconfig[i]["type"]>2:
            continue
    # if not cweidingbattleconfig[i]["type"]==2:
    #     continue
        enemyList=[]
        for j in cbattleinfo[i]["enemyPositions"][1:]:
            if not j=="0":
                enemyList.append(j.split("@")[0])
        text0="{{面包屑|未定之路图鉴}}\n<br>{{折叠面板|开始}}\n{{折叠面板|标题=挑战内容|选项=1|主框=1|样式=red|展开=是}}\n"
        text0+=getTargetInfo(i)+"\n{{折叠面板|内容结束}}{{折叠面板|标题=Boss详情|选项=2|主框=1|样式=blue}}\n"
        a=""
        for j in enemyList:
            text0+=getmonsterInfo(j)
        text0+="\n{{折叠面板|内容结束}}\n{{折叠面板|结束}}"
        sort=cweidingsort[i]["sort"]
        titles=""
        if sort==1:
            titles+="未定之路-周常"
        else:
            titles+="未定之路-日常"+str(sort-1)
        titles+="-"+getwordquickly(cweidingbattleconfig[i]["nameTextID"],cworddungeonselect_ch)

        allList.append(upload.createPair(titles,text0))
    upload.prepareUploadWiki(allList)

prepareUploadWiki()
# print(getTargetInfo("6363"))