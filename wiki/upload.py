from requests import Session

import wiki.GetCookie as ck
import utilSimple.JsonTool as jt

host = "https://wiki.biligame.com/fsdmn/api.php?"
headers = {
    # "Cookie":SESSDATA,
    "User-Agent": "MagicCat Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
}
sessdata = Session()
sessdata.cookies.update({"SESSDATA": ck.main()})
tokenParams = {
    'action': 'query',
    'format': 'json',
    'meta': 'tokens',
}


# csrftoken=""

def uploadtoWiki(titles, tt, csrftoken):
    # if csrftoken=="":
    #     tokenresponse = requests.post(host, headers=headers, data=tokenParams)
    #     csrftoken=tokenresponse.json()['query']['tokens']['csrftoken']
    # # 进行编辑
    editTittle = {
        'action': 'edit', 'title': titles, 'format': 'json',
        'summary': '自动化编辑', 'text': tt,
        'token': csrftoken
    }
    #
    res = sessdata.post(host, data=editTittle, headers=headers)
    print(jt.strToJson(res.text) + ",")


def prepareUploadWiki(allList):
    tokenresponse = sessdata.post(host, headers=headers, data=tokenParams)
    csrftoken = tokenresponse.json()['query']['tokens']['csrftoken']
    print("[")
    for r in allList:
        uploadtoWiki(r["tittle"], r["text"], csrftoken)
    print("]")


def createPair(tittle, text):
    return {"tittle": tittle, "text": text}
