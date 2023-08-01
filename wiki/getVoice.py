import os

import utilSimple.JsonTool as jt

import utilSimple.FileGetter as fg
import wiki.wikiTool as wt

roleconfig = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "roleconfig.json"))
cwordrole_ch = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "cwordrole_ch.json"))

ccardroleconfig_handbook = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "ccardroleconfig_handbook.json"))

cskin = jt.readJsonFile(fg.join(wt.getRolePath(), "cskin.json"))

csoundlines_skin = jt.readJsonFile(fg.join(wt.getSoundPath(), "csoundlines_skin.json"))
csoundlines = jt.readJsonFile(fg.join(wt.getSoundPath(), "csoundlines.json"))
csoundcatalog = jt.readJsonFile(fg.join(wt.getSoundPath(), "csoundcatalog.json"))
csoundcatalog_skin = jt.readJsonFile(fg.join(wt.getSoundPath(), "csoundcatalog_skin.json"))
cvoicesource_zh_hans = jt.readJsonFile(fg.join(wt.getSoundPath(), "cvoicesource_zh_hans.json"))

aa = open(r"a.csv").readlines()
listType = []
for a in aa:
    listType.append(a.split(",")[:2])
print(listType)


# for path in p:
#     path2=path
#     for cc in list:
#         path2=path2.replace(cc[0],cc[1])
#     a = os.rename(startPath+"\\"+path, startPath+"\\"+path2)
def isShow(roleID):
    # print(roleID, ccardroleconfig_handbook[str()]["sortID"])
    try:
        sortID = ccardroleconfig_handbook[str(roleID)]["sortID"]
        if sortID > 1000:
            return False
        return True
    except:
        return False

def getName(roleID):
    if isShow(roleID):
        return wt.getword(roleconfig[str(roleID)]["nameTextID"], cwordrole_ch) \
        .replace("<b>·</b>", "·").replace("$heroine$", "魔女")
    else:
        print(roleID)


def getSkinName(skinId):
    if cskin.get(str(skinId)) == None:
        return None
    else:
        return (cwordrole_ch[str(cskin[str(skinId)]["skinNameTextID"])]["text"], cskin[str(skinId)]["roleid"])


def getNameByVoiceID(sheetName, cueName):
    id = -1
    for i in cvoicesource_zh_hans:
        if sheetName == cvoicesource_zh_hans[i]["cueSheet"].split("/")[2]:
            if cueName == cvoicesource_zh_hans[i]["cueName"]:
                id = i
    # print(cueName,id)
    for i in csoundcatalog:
        if str(csoundcatalog[i]["Adventure"]) == str(id):
            # print(i,getName(i))
            return getName(i)
    for i in csoundcatalog_skin:
        if str(csoundcatalog_skin[i]["Adventure"]) == str(id):
            # print(i,getSkinName(i))
            varl = getSkinName(i)
            if not varl == None:
                return getName(varl[1]) + "-" + varl[0]





#
def collectSound(SoundMemberID, isSkin):
    jsonUsed = dict("")
    if isSkin:
        jsonUsed = csoundlines_skin
    else:
        jsonUsed = csoundlines
    if jsonUsed.get(SoundMemberID) == None:
        jsonUsed = csoundcatalog
        # return ""
    jsonObject = jsonUsed[SoundMemberID]
    return ""


def addSign(text):
    return "\"" + text + "\""

# hca.exe path
workPath = r"hca.exe"
os.chdir(fg.getFileParentPathFromPath(workPath))
# files path
basePath = r"myfiles"
extraStart = r"_vgmt_acb_ext_"
middle = r'\acb\awb'
# output path
endPath = r'aaaa'


def createCommand(file1, file2):
    return workPath + " " + addSign(file1) + ">" + addSign(file2)


def isNum(vars):
    try:
        int(vars)
        return True
    except:
        return False


def getVoiceType(voiceName):
    type = voiceName.split("_")
    if not isNum(type[-1]):
        return voiceName.split("_")[-1:][0]
    else:
        return type[-2:][0] + "_" + type[-1:][0]


def getVoiceName(voicType):
    # print(voicType)
    # 奇怪，怎么有情绪三
    if voicType == "Emotion_3" or voicType == "ManaTree" \
            or voicType == "OpenBox" or voicType == "Skill_3" or voicType == "Skill_4" \
            or voicType == "Skill_5" or "00043" in voicType:
        return -1
    if voicType=="Attacked_1":
        voicType="Attacked"
    for i in listType:
        if i[0] == voicType:
            return i[1]


files = os.listdir(basePath)
all = []
for i in files:
    if "_vgmt_acb_ext_" in i:
        all.append(os.path.basename(i))
    else:
        pass

# print(all)
# for i in all:
#     filePath = basePath + "\\" + i + middle
#     files = fg.readDir(filePath)
#     hcas = []
#     for j in files:
#         if ".hca" == fg.getFileTypeFromPath(j):
#             hcas.append(j)
#     cueSheetName = fg.getFileNameFromPath(hcas[0]).replace(extraStart, "")
#     for h in hcas:
#         if "Adventure" in cueSheetName:
#             break
#         if "Adventure" in fg.getFileNameFromPath(h):
#             cueSheetName = fg.getFileNameFromPath(h).replace(extraStart, "")
#             break
#
#     roleName = getNameByVoiceID(i.replace(extraStart, ""), cueSheetName)
#     if roleName == None:
#         # print(i,cueSheetName)
#         continue
#     else:
#         print(roleName)
#     for h in hcas:
#         hcaType = getVoiceName(getVoiceType(fg.getFileNameFromPath(h)))
#         if hcaType == -1:
#             continue
#         os.system(createCommand(h, endPath + "\\" + roleName + "-语音-" + hcaType + ".wav"))
# 补充好像>没法用，所以手动挪个位置
for i in all:
    filePath = basePath + "\\" + i + middle
    files = fg.readDir(filePath)
    hcas = []
    for j in files:
        if ".wav" == fg.getFileTypeFromPath(j):
            hcas.append(j)
    if len(hcas)==0:
        continue
    cueSheetName = fg.getFileNameFromPath(hcas[0]).replace(extraStart, "")
    for h in hcas:
        if "Adventure" in cueSheetName:
            break
        if "Adventure" in fg.getFileNameFromPath(h):
            cueSheetName = fg.getFileNameFromPath(h).replace(extraStart, "")
            break

    roleName = getNameByVoiceID(i.replace(extraStart, ""), cueSheetName)
    if roleName == None:
        # print(i,cueSheetName)
        continue
    else:
        print(roleName)
    for h in hcas:
        hcaType = getVoiceName(getVoiceType(fg.getFileNameFromPath(h)))
        if hcaType == -1:
            continue
        fg.mycopyfile(h, endPath + "\\" + roleName + "-语音-" + hcaType + ".wav")
    # break

# for i in roleconfig:
#     if not isShow(i):
#         # print(i)
#         continue
#     print(getName(i))
#     shapeID = str(roleconfig[i]["shapeID"])
#     shapeName = cnpcshape[shapeID]["assetBundleName"].split("/")[1].split(".")[0]
