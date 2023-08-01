import os.path

from slpp import slpp as lua
import utilSimple.FileGetter as fg
import utilSimple.JsonTool as jt

def dealLuaScript(lua_script00):
    linesScript = lua_script00.split("\n")
    tableName = ""
    # 目前担心table中包含，因此我们从文件尾部开始读取到包含return的行
    for i in range(len(linesScript) - 1, -1, -1):
        if "return" in linesScript[i]:
            tableName = linesScript[i].split("return")[1].strip()
            break
    # 这个写法仍然不够稳健，最好的方法是解析这个table对象
    # 目测可以通过{}匹配来完成解析，但是增加了时间消耗
    varTemp = lua_script00.split(tableName + ".Data")[1].split(tableName)[0]
    dataStartPos = varTemp.find("=")
    varTemp = varTemp[dataStartPos + 1:]
    dataTable = lua.decode(varTemp)
    return dataTable


def convertLuaToJson(file):
    print("正在转化"+file)
    textcontent=fg.getLuaWithGBKComment(file)
    dataTable=dealLuaScript(textcontent)
    jt.saveDictAsJson(fg.getWikiJsonDirPath() + "\\" + fg.getFileNameFromPath(file) + ".json", dataTable)