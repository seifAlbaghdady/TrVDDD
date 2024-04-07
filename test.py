import pickle
import pandas as pd


test_data_single_row = {
    "label": [0],
    "code": [
        'var userInput = "\'; DROP TABLE users; --"; var query = "SELECT * FROM users WHERE username = \'" + userInput + "\'";'
    ],
}

df = pd.DataFrame(test_data_single_row)
with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
