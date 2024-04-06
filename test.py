import pickle
import pandas as pd

# code in js got vulnerability
test_data_single_row = {
    "label": [1],
    "code": ['console.log("Received input: " + "User input");'],
}
df = pd.DataFrame(test_data_single_row)


with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
