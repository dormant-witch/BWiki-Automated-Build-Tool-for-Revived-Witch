import os

import utilSimple.JsonTool as jt

import utilSimple.FileGetter as fg
import wiki.wikiTool as wt
from wiki import upload


citemattr = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "citemattr.json"))
cworditem_ch = jt.readJsonFile(fg.join(fg.getWikiJsonDirPath(), "cworditem_ch.json"))
cdormfurnituregroup = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "cdormfurnituregroup.json"))
cdormfurnituretype= jt.readJsonFile(fg.join(wt.getCourtyardPath(), "cdormfurnituretype.json"))
cwordyard_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordyard_ch.json"))

cfurnitureitem = jt.readJsonFile(fg.join(wt.getItemDir(), "cfurnitureitem.json"))


def getGrop(id):
    for i in cdormfurnituregroup:
        if int(id) in cdormfurnituregroup[i]["items"]:
            return wt.getword(cdormfurnituregroup[i]["nameTextID"], cwordyard_ch)
    else:
        return "特别家具"

def getGropTime(id):
    for i in cdormfurnituregroup:
        if int(id) in cdormfurnituregroup[i]["items"]:
            timetext=cdormfurnituregroup[i]["description"]
            # print(timetext)
            if "售卖时间:" in timetext:
                return timetext.split("售卖时间:")[-1].replace("。","")
            return "常驻"
    else:
        return "活动获取"
# for a in aa:
#     id=fg.getFileNameFromPath(a)
#     gr=getGrop(id)
#     if gr:
#         os.rename(a,fg.join(os.path.dirname(a),"{}-{}.webp".format(gr,wt.getword(citemattr[id]["nameTextID"],cworditem_ch))))
#     else:
#         os.rename(a,fg.join(os.path.dirname(a),"特别家具-{}.webp".format(wt.getword(citemattr[id]["nameTextID"],cworditem_ch))))
upList = []
for id in cfurnitureitem:
    template = "{{家具<!-- 此为填写帮助信息，请在下方=后填写相应的数据，无相应内容时，空出即可  -->"
    Name = wt.getword(citemattr[id]["nameTextID"], cworditem_ch)
    template += "\n|名称=" + Name
    gr=getGrop(id)
    template += "\n|主题=" + gr
    template += "\n|售卖时间=" + getGropTime(id)
    template += "\n|分类=" + wt.getword(cdormfurnituretype[cfurnitureitem[id]["type"]-1]["nameTextID"],cwordyard_ch)
    template += "\n|舒适度=" + str(cfurnitureitem[id]["comfortPoint"])
    template += "\n|尺寸=" + cfurnitureitem[id]["cover"]
    template += "\n|描述=" + wt.getword(citemattr[id]["destribeTextID"], cworditem_ch)

    template += "\n}}"
    # print(template)
    upList.append(upload.createPair("{}-{}".format(gr,Name), template))

upload.prepareUploadWiki(upList)
# for i in cdormfurnituregroup:
#     print("<div class=\"resp-tab-content\">\n{{家具图鉴展示|主题::{}}}\n</div>".format(cdormfurnituregroup[i]["name"]))
# print(upList)