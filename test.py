import pickle
import pandas as pd


test_data_single_row = {
    "label": [0],
    "code": [
        "Object.keys(err).forEach(function(key){if(self.exclude.indexOf(key)>=0){return;}cgiData['err.'+key]=err[key];});"
    ],
}

df = pd.DataFrame(test_data_single_row)
with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
