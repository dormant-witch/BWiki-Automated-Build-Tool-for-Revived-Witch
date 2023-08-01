import collections
import json

import utilSimple.FileGetter as fg

def readJsonFile(file):
    with open(file, "r", encoding="utf-8") as f:
        allJson = json.load(f, object_pairs_hook=collections.OrderedDict)
        f.close()
        return allJson

def saveDictAsJson(file, dict0):
    with open(file, "w", encoding="utf-8") as f:
        f.write(dictToJson(dict0))
        f.close()

def dictToJson(dict0):
    return json.dumps(dict0, ensure_ascii=False, sort_keys=False, indent=4, separators=(',',':'))

def dictToJsonNoOpen(dict0):
    return json.dumps(dict0, ensure_ascii=False, sort_keys=False)

def strToJson(jsonString):
    return json.dumps(json.loads(jsonString, object_pairs_hook=collections.OrderedDict), ensure_ascii=False, sort_keys=False)