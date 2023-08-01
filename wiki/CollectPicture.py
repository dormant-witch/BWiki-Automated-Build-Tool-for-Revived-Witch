import collections
import json
import time
from random import random


with open("../备份/wiki相关/json/cwordrole_ch.json", "r", encoding="utf-8") as f:
    cwordrole_ch = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("../备份/wiki相关/json/cskin.json", "r", encoding="utf-8") as f:
    cskin = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

with open("../备份/wiki相关/json/ccardroleconfig_handbook.json", "r", encoding="utf-8") as f:
    ccardroleconfig_handbook = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()
with open("../备份/wiki相关/json/roleconfig.json", "r", encoding="utf-8") as f:
    roleconfig = json.load(f,object_pairs_hook=collections.OrderedDict)
    f.close()

# 已脱敏
def savePic(imageId,name):
    time.sleep(random()*3)
    try:
        print("下好了"+name)
    except:
        print("不存在"+name)

# 是否有突破造型取决于是否909903和909902npcshape相同
def getSkinName(skinId):
    if  cskin.get(str(skinId))==None:
        return ("",-1)
    else:
        return (cwordrole_ch[str(cskin[str(skinId)]["skinNameTextID"])]["text"],skinId)

for id in roleconfig:
    # if int(id)>10:
    #     break
    try:
        sortID=ccardroleconfig_handbook[id]["sortID"]
        if sortID>1000:
            continue
        name=str(cwordrole_ch[str(roleconfig[id]["nameTextID"])]["text"]) \
            .replace("<b>·</b>","·").replace("$heroine$","魔女")
    except:
        continue
    savePic(id,name)
    skin0=getSkinName(str(9000+int(id))+"03")[0]
    if(skin0!=""):
        savePic(id+"4",name+"-突破造型")
    skin1=getSkinName(str(9000+int(id))+"11")
    if(skin1[0]!=""):
        savePic(cskin[str(skin1[1])]["skinNameTextID"],name+"-"+skin1[0])
    skin2=getSkinName(str(9000+int(id))+"12")
    if(skin2[0]!=""):
        savePic(cskin[str(skin2[1])]["skinNameTextID"],name+"-"+skin2[0])
    skin3=getSkinName(str(9000+int(id))+"13")
    if(skin3[0]!=""):
        savePic(cskin[str(skin3[1])]["skinNameTextID"],name+"-"+skin3[0])
    skin4=getSkinName(str(9000+int(id))+"14")
    if(skin4[0]!=""):
        savePic(cskin[str(skin4[1])]["skinNameTextID"],name+"-"+skin4[0])
    # skin5=getSkinName(str(9000+int(id))+"15")
    # skin6=getSkinName(str(9000+int(id))+"16")



