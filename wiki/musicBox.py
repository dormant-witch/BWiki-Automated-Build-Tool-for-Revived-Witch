import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg
import wiki.wikiTool as wt
import wiki.upload as upload

cdungeonselectmainline = jt.readJsonFile(fg.join(wt.getDungeonselectPath(), "cdungeonselectmainline.json"))
cworddungeonselect_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cworddungeonselect_ch.json"))

caudioplayer = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayer.json"))
caudioplayerachievement = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayerachievement.json"))
caudioplayercell = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayercell.json"))
caudioplayeralbum = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayeralbum.json"))

cwordyard_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordyard_ch.json"))

csoundsource = jt.readJsonFile(fg.join(wt.getSoundPath(), "csoundsource.json"))

cworditem_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cworditem_ch.json"))
citemattr = jt.readJsonFile(fg.join(wt.getItemDir(), "citemattr.json"))


def getItemNames(itemList, numsList):
    itemString = ""
    if not numsList == None:
        for i in range(len(itemList)):
            itemString += "{{图标|小|" + wt.getword(citemattr[str(itemList[i])]["nameTextID"],
                                                    cworditem_ch) + "|" + str(numsList[i]) + "}}，"
    else:
        for i in range(len(itemList)):
            itemString += "{{图标|小|" + wt.getword(citemattr[str(itemList[i])]["nameTextID"],
                                                    cworditem_ch) + "|}}，"
    return itemString[:-1]


def getUnlockFloor(musicCellId: int):
    for i in caudioplayer:
        if musicCellId in caudioplayer[i]["cellID"]:
            return caudioplayer[i]["floor"]
    return -1


allText = '{{面包屑}}{| class="wikitable" style="width:100%;text-align: center;"\n|+\n!序号\n!所属世界\n!名称\n!作者\n!别名\n!分类\n!解锁条件1\n!解锁条件2\n!试听'
import re
for audio in caudioplayercell:
    template = "\n|-"
    template += "\n|" + str(audio["id"])
    album=wt.getword(caudioplayeralbum[str(audio["album"])]["albumName"], cwordyard_ch)
    template += "\n|" + album
    name1=wt.getword(audio["audioName"], cwordyard_ch)
    template += "\n|" + wt.getword(audio["audioName"], cwordyard_ch)
    template += "\n|" + wt.getword(audio["author"], cwordyard_ch)
    name2 = str(csoundsource[str(audio["audioID"])]["cueName"])
    for i in range(2):
        name2 = name2[name2.find("_") + 1:]
    name2New = re.sub(r'\d+', '', name2[:-1].replace("_"," "))+name2[-1:]
    template += "\n|" + (name2New if not name1== name2New else "")
    cueSheet = csoundsource[str(audio["audioID"])]["cueSheet"]
    # Ost还是要大写
    template += "\n|" + cueSheet.replace("main:BGM/", "").title().replace("Ost","OST")
    # 解锁条件--关卡、资源消耗
    floorID = getUnlockFloor(audio["id"])
    if floorID > 0:
        floor = cdungeonselectmainline[floorID - 1]
        template += "\n|通关  " + floor["floor"] + " " + wt.getword(floor["nameTextID"], cworddungeonselect_ch)
    else:
        template += "\n|默认解锁"
    template += "\n|style=\"text-align:left;\"|" + getItemNames(audio["unlockItems"], audio["itemsAmount"])
    template +="\n|{{Player1|音乐盒-"+album+"-"+name1+"|nobar=1}}"
    allText += template
    # print(template)
allText+="\n|}"

print(allText)
# upload.prepareUploadWiki([upload.createPair("音乐盒",allText)])
