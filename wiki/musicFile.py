import os

import utilSimple.JsonTool as jt
import utilSimple.FileGetter as fg
import wiki.wikiTool as wt
from wiki import upload

caudioplayer = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayer.json"))
caudioplayercell = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayercell.json"))
caudioplayeralbum = jt.readJsonFile(fg.join(wt.getCourtyardPath(), "caudioplayeralbum.json"))

cwordyard_ch = jt.readJsonFile(fg.join(wt.getWordPath(), "cwordyard_ch.json"))

csoundsource = jt.readJsonFile(fg.join(wt.getSoundPath(), "csoundsource.json"))


# newPath=fg.join(fg.getCacheDirPath(),"musicBox")
# os.makedirs(newPath)
# #
# ass={}
# for i in a:
#     if fg.getFileTypeFromPath(i) == ".wav":
#         fileName= fg.getFileNameFromPath(i)
#         ass[fileName]=i
#
# print(ass)
# for audio in caudioplayercell:
#
#     albumName=wt.getword(caudioplayeralbum[str(audio["album"])]["albumName"], cwordyard_ch)
#     name1=wt.getword(audio["audioName"], cwordyard_ch)
#     name2 = str(csoundsource[str(audio["audioID"])]["cueName"])
#     if ass.get(name2)==None:
#         continue
#     cueSheet = csoundsource[str(audio["audioID"])]["cueSheet"]
#     print(ass[name2],fg.join(newPath,"音乐-"+albumName+"-"+name1+".wav"))
#     fg.mycopyfile(ass[name2],fg.join(newPath,"音乐-"+albumName+"-"+name1+".wav"))
    # print(template)

import utilSimple.FileGetter as fg
# use your path
a=fg.readDir(r"C:\MusicBox")
aa=""
for i in a:
    base=fg.getFileNameFromPath(i).split("-")
    album=base[1]
    songName=base[2]
    # print(album+"-"+songName)
    aa+=album+"-"+songName+","
print(aa)
