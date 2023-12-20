import json
import os.path

import utilSimple.FileGetter

with open(r"wiki\custom\poolConfig.json", "r", encoding="utf-8") as f:
    poolConfig = json.load(f)
with open(r"wiki\custom\poolConfigAddition.json", "r", encoding="utf-8") as f:
    poolConfigAddition = json.load(f)

outputDir = r'新建文件夹\小标题背景'

pngDir = r'ExportedProject\Assets\gameassets'

bgDir = r'新建文件夹\卡池背景'
bgDir2 = r'新建文件夹\卡池背景2'

template='{{卡池一览|'
te2=''
tt=[]
for p in poolConfig:
    print(p)
    mapInfo = {
        "0": os.path.realpath(
            os.path.join(pngDir,
                         poolConfig[p]["CellImg"]["assetBundle"].replace(".", "\\").replace("\\assetbundle", ".png")))
    }
    # print(mapInfo.values())
    # consoleText=consoleText.fo
    # print(consoleText)
    #
    cellImg= '{}-{}-{}.png'.format(poolConfig[p]["poolType"],
                                   poolConfigAddition[p]["poolName"],
                                   poolConfig[p]["name"])
    utilSimple.FileGetter.mycopyfile(mapInfo["0"], os.path.join(outputDir,cellImg))
    utilSimple.FileGetter.mycopyfile(os.path.join(bgDir,"{}.png".format(poolConfig[p]["poolName"])), os.path.join(bgDir2,"卡池-{}-背景.png".format(poolConfigAddition[p]["poolName"])))
    tt.append("{}+{}+{}+{}".format(poolConfigAddition[p]["poolName"],cellImg.split(".png")[0],poolConfig[p]["rightTimeShowStart"][5:],poolConfig[p]["rightTimeShowEnd"][5:]))
    te2+='#table_gacha[class*="{0}"] {background: url("https://wiki.biligame.com/fsdmn/Special:FilePath/卡池-{0}-背景.png") center top / cover no-repeat;} \n'.replace("{0}",poolConfigAddition[p]["poolName"])
tt.reverse()
template+=(",".join(tt)) +",纪念卡池+灵魂召唤++,专武纪念卡池+回忆召唤++}}"
print(template)
print(te2)