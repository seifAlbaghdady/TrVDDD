import pickle
import pandas as pd


test_data_single_row = {
    "label": [0],
    "code": [
        'var code = "function FUN1(VAR1) { var VAR3 = VAR1.VAR4; delete VAR3; }";'
    ],
}

df = pd.DataFrame(test_data_single_row)
with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
