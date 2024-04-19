import pickle
import pandas as pd


test_data_single_row = {
    "label": [0],
    "code": [
        "fileNotFound: function(connection){return connection.localize(['That file is not found (%s)', connection.params.file]);},"
    ],
}

df = pd.DataFrame(test_data_single_row)
with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
