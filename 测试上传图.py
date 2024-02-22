import wiki.upload as upload


with open("91881.png","rb") as f:
    chunk=f.read()
upload.prepareUploadWikiWithFile([upload.createPairWithFile("50px-玛特薇芙.png","50px-玛特薇芙.png",chunk)])