import pickle
import pandas as pd


test_data_single_row = {
    "label": [0],
    "code": [
        'api.fileServer.followFileToServe=function(api,fileName,connection,next){api.fs.stat(fileName,function(err,stats){if(err!=null){api.fileServer.sendFileNotFound(api,connection,next);}else{if(stats.isDirectory()){if(fileName[fileName.length-1]!="/"){fileName+="/";}api.fileServer.followFileToServe(api,fileName+api.configData.commonWeb.directoryFileType,connection,next);}else if(stats.isSymbolicLink()){api.fs.readLink(fileName,function(err,truePath){if(err!=null){api.fileServer.sendFileNotFound(api,connection,next);}else{api.fileServer.followFileToServe(api,truePath,connection,next);}});}else if(stats.isFile()){api.fileServer.sendFile(api,fileName,connection,next);}else{api.fileServer.sendFileNotFound(api,connection,next);}}});}'
    ],
}

df = pd.DataFrame(test_data_single_row)
with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
