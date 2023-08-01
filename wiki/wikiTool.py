import utilSimple.FileGetter as fg


def noFormatText(textALL):
    return textALL.replace("<color=#82C65D>", "").replace("</color>", "").replace("<color=#F5A09Bff>", "") \
        .replace("<color=#FBFAA5ff>", "") \
        .replace("<color=#8CECFAff>", "") \
        .replace("<color=#B4F59Bff>", "") \
        .replace("<color=#FFCA65ff>", "") \
        .replace("$B$", "").replace("\\n\\n", "<br>").replace("\\n", "<br>")


def getword(WordId, cw):
    if WordId == -1:
        return ""
    if cw.get(str(WordId)) == None:
        return ""
    return cw[str(WordId)]["text"]


def calculateRoleLvText(lv: int):
    if lv <= 30:
        return "lv." + str(lv) + " 突破0"
    elif lv <= 70:
        return "lv." + str(lv-30) + " 突破1"
    elif lv <= 130:
        return "lv." + str(lv-70) + " 突破2"
    elif lv <= 200:
        return "lv." + str(lv-130) + " 突破3"
    else:
        return "lv." + str(lv-200) + " 突破4"


def getExcelDataDir():
    return fg.join(fg.getWikiDirPath(), "exceldata")


def getEquipDir():
    return fg.join(getExcelDataDir(), "equip")


def getItemDir():
    return fg.join(getExcelDataDir(), "item")


def getHandbookDir():
    return fg.join(getExcelDataDir(), "handbook")


def getWordPath():
    return fg.join(getExcelDataDir(), "word")
def getDialogPath():
    return fg.join(getExcelDataDir(), "dialog")

def getRolePath():
    return fg.join(getExcelDataDir(), "role")


def getSkillPath():
    return fg.join(getExcelDataDir(), "skill")


def getDungeonselectPath():
    return fg.join(getExcelDataDir(), "dungeonselect")

def getCourtyardPath():
    return fg.join(getExcelDataDir(), "courtyard")

def getSoundPath():
    return fg.join(getExcelDataDir(), "sound")