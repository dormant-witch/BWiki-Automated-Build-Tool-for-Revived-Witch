# magick超级
# magick "gacha23.png" -crop 1370x754+37+115 +repage -fill white -pointsize 99 -gravity northwest -encoding GBK -font "方正正中黑_GBK" -annotate +22+23 "梦境召唤" ( "smalltitle3.png" ) -compose over -geometry +22+80 -composite -pointsize 66  -annotate +900+473 "暗之艾妮萌" -pointsize 49.5  -annotate +989+543 "执行者" -pointsize 33  -annotate +1239+466 "刺杀型"   "charcisha.png" -compose over -geometry +1225+345  -composite  ( "GachaRank4.png" -resize 145x145 ) -compose over -geometry +1215+465  -composite   "GachaModelBack.png" -compose over -geometry +20+300  -composite  "gachaup3.png" -compose over -geometry +19+520   -composite  ( "暗之艾妮萌-像素小人.png" -resize 180x ) -compose over -geometry +90+340  -composite  "GachaTimeBack2.png" -compose over -geometry +59+632  -composite -pointsize 33  -annotate +71+642 "限时" -pointsize 33  -annotate +203+642 "2021/10/28 18:00 - 2021/11/04 3:59" "ac2.png"
import json
import os.path

from wand.image import Image

import utilSimple.FileGetter

from PIL import ImageFont, ImageDraw
from wand.drawing import Drawing

# 生成font
ttf_path = r'新建文件夹\fzzzhGBKjf.ttf'


def gettextWidth(ttf_path,text_size,textC):
    font = ImageFont.truetype(ttf_path, text_size)
    return font.getbbox(textC)[2]

with open(r"wiki\custom\poolConfig.json", "r", encoding="utf-8") as f:
    poolConfig = json.load(f)

baseDir = r'leiting\output'
outputDir = r'disunity_v0.3.4\ui'
# for p in poolConfig:
#     utilSimple.FileGetter.mycopyfile(os.path.join(baseDir,poolConfig[p]["CellImg"]["assetBundle"]),os.path.join(outputDir,poolConfig[p]["CellImg"]["assetBundle"].split("/")[1]))
#     utilSimple.FileGetter.mycopyfile(os.path.join(baseDir,poolConfig[p]["image"]["assetBundle"]),os.path.join(outputDir,poolConfig[p]["image"]["assetBundle"].split("/")[1]))
#     utilSimple.FileGetter.mycopyfile(os.path.join(baseDir,poolConfig[p]["waterLevelimg"]["assetBundle"]),os.path.join(outputDir,poolConfig[p]["waterLevelimg"]["assetBundle"].split("/")[1]))
#     if  poolConfig[p]["smalltitle"]is not None:
#         utilSimple.FileGetter.mycopyfile(os.path.join(baseDir,poolConfig[p]["smalltitle"]["assetBundle"]),os.path.join(outputDir,poolConfig[p]["smalltitle"]["assetBundle"].split("/")[1]))
#
pngDir = r'ExportedProject\Assets\gameassets'
# 0 背景文件地址
# 1 卡池类型
# 2 卡池小标题如果有的话，地址 "{}" -compose over -geometry +22+80 -composite
# 3 人物名字
# 4 人物称号 注意这里需要计算一下位置
# 5 人物类型
# 6 水位的图片地址
# 7/8 时间
# 9输出的结果名字
for p in poolConfig:
    print(p,poolConfig[p]["name"])
    consoleText = r'magick "{0}" -crop 1370x754+37+115 +repage {2} -fill white -pointsize 99 -gravity northwest -encoding GBK -font "方正正中黑_GBK" -annotate +22+23 "{1}"  -pointsize 66  -annotate +900+473 "{3}" -pointsize 49.5  -annotate +930+543 "{4}" -pointsize 33  -annotate +1235+468 "{5}"   "C:\Users\Admin\Downloads\新建文件夹 (6)\新建文件夹\类型\{5}.png" -compose over -geometry +1221+340  -composite  ( "C:\Users\Admin\Downloads\新建文件夹 (6)\新建文件夹\GachaRank4.png" -resize 145x145 ) -compose over -geometry +1215+465  -composite   "C:\Users\Admin\Downloads\新建文件夹 (6)\新建文件夹\GachaModelBack.png" -compose over -geometry +20+300  -composite  "{6}" -compose over -geometry +19+520   -composite  {11}  ( "C:\Users\Admin\Downloads\新建文件夹 (6)\新建文件夹\GachaTimeBack.png" -crop 50x54+150+0 +repage -resize {7}x54! ) -compose over -geometry +182+632  -composite  -pointsize 33  -annotate +203+642 "{8} - {9}" ( "C:\Users\Admin\Downloads\新建文件夹 (6)\新建文件夹\GachaTimeBack.png" -crop 123x54+0+0 +repage ) -compose over -geometry +59+632 -composite -pointsize 33 -fill black -annotate +73+642 "限时" "{10}"'
    mapInfo = {
        "0": os.path.realpath(
            os.path.join(pngDir,
                         poolConfig[p]["image"]["assetBundle"].replace(".", "\\").replace("\\assetbundle", ".png"))),
        "1":poolConfig[p]["poolType"],
        "2":'( "{}" -trim ) -compose over -geometry +22+120 -composite'.format(os.path.realpath(
            os.path.join(pngDir,
                         poolConfig[p]["smalltitle"]["assetBundle"].replace(".", "\\").replace("\\assetbundle", ".png"))))  if poolConfig[p]["smalltitle"] is not None else "",
        "3":poolConfig[p]["name"],
        "4":poolConfig[p]["roleTittle"],
        "5":poolConfig[p]["vocation"],
        "6": os.path.realpath(
            os.path.join(pngDir,
                         poolConfig[p]["waterLevelimg"]["assetBundle"].replace(".", "\\").replace("\\assetbundle", ".png"))),
        "7":gettextWidth(ttf_path,33,poolConfig[p]["rightTimeShowStart"]+" - "+poolConfig[p]["rightTimeShowEnd"])+40,
        "8":poolConfig[p]["rightTimeShowStart"],
        "9":poolConfig[p]["rightTimeShowEnd"],
        "10": os.path.join(r'C:\Users\Admin\Downloads\新建文件夹 (6)\新建文件夹\卡池背景',poolConfig[p]["poolName"]+".png"),
        "11":r'( "{}" ) -compose over -geometry +{}+{}  -composite'
    }
    pixelImg=r'放大小人\{}-像素小人.png'.format(mapInfo["3"])
    with Image(filename=pixelImg) as img:
        mapInfo["11"]=mapInfo["11"].format(pixelImg,155-img.size[0]/2,530-img.size[1])
    # print(mapInfo.values())
    consoleText=consoleText.format(mapInfo["0"],mapInfo["1"],mapInfo["2"],mapInfo["3"],mapInfo["4"],mapInfo["5"],mapInfo["6"],mapInfo["7"],mapInfo["8"],mapInfo["9"],mapInfo["10"],mapInfo["11"])
    # consoleText=consoleText.fo
    print(consoleText)
    os.system(consoleText)
    utilSimple.FileGetter.mycopyfile()
#     安格泠适用于 -crop 1370x754+37+140 ，此外奈解和灾厄医生的牌子有问题，处理了源文件
