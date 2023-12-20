wesee = {
    "名称": "海中匿影",
    "单个元素模板": "${名称}",
    "Wiki模板": "抽卡结果",
    "结果连接符": ",",
    "抽卡延时": 6000,
    "内容": {
        "R": {
            "可获取内容": []
        },
        "SR": {
            "可获取内容": []
        },
        "SSR": {
            "可获取内容": []
        },
        "UR": {
            "可获取内容": [],
            "特别内容": [],
            "结果预设": [
                {
                    "次数": -1,
                    "当前总抽数": 159,
                    "结果组合": [
                        [
                            0,
                            -1
                        ]
                    ]
                },
                {
                    "次数": 1,
                    "当前总抽数": -1,
                    "出货时全局重置": True,
                    "锁定预设": True,
                    "结果组合": [
                        [
                            1
                        ]
                    ]
                }
            ]
        }
    },
    "稀有度": {
        "R": {
            "权重": 5000
        },
        "SR": {
            "权重": 4200,
            "保底抽数": 10,
            "保底更高稀有度": True,
        },
        "SSR": {
            "权重": 600
        },
        "UR": {
            "权重": 200,
            "保底抽数": 80,
            "保底更高稀有度": True,
            "权重追加": 0
        }
    }
}

config = {
    "卡池路径": "https://wiki.biligame.com/fsdmn/index.php?title=${相对路径}&action=raw&ctype=json",
    "卡池列表": {

    }
}
import json
import os.path

import utilSimple.FileGetter

with open(r"wiki\custom\poolConfig.json", "r", encoding="utf-8") as f:
    poolConfig = json.load(f)
with open(r"wiki\custom\poolConfigAddition.json", "r", encoding="utf-8") as f:
    poolConfigAddition = json.load(f)
import wiki.upload as upload

alllist = []
for p in poolConfig:
    ss = wesee
    ss["名称"] = poolConfigAddition[p]["poolName"]
    ss["内容"]["R"]["可获取内容"] = poolConfig[p]["poolRoleRList"].split(";")
    ss["内容"]["SR"]["可获取内容"] = poolConfig[p]["poolRoleSRList"].split(";")
    ss["内容"]["SSR"]["可获取内容"] = poolConfig[p]["poolRoleSSRList"].split(";")
    ss["内容"]["UR"]["可获取内容"] = poolConfig[p]["poolRoleURList"].split(";")
    ss["内容"]["UR"]["特别内容"] = [poolConfig[p]["poolRoleURList"].split(";")[0]]
    alllist.append(upload.createPair("Data:{}.json".format(ss["名称"]), utilSimple.JsonTool.dictToJsonNoOpen(ss)))
    config["卡池列表"][p] = {}
    config["卡池列表"][p]["名称"] = ss["名称"]
    config["卡池列表"][p]["启用"] = True
    config["卡池列表"][p]["相对路径"] = "Data:{}.json".format(ss["名称"])
print(utilSimple.JsonTool.dictToJsonNoOpen(alllist))

config["卡池列表"]["1000"] = {
    "名称": "纪念卡池",
    "启用": True,
    "相对路径": "Data:纪念卡池.json"
}
config["卡池列表"]["1001"] = {
    "名称": "专武纪念卡池",
    "启用": True,
    "相对路径": "Data:专武纪念卡池.json"
}

alllist.append(upload.createPair("Data:GachaConfig.json", utilSimple.JsonTool.dictToJsonNoOpen(config)))
# print(alllist[-1])

upload.prepareUploadWiki(alllist)
