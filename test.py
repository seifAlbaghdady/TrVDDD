import pickle
import pandas as pd

# code in js got vulnerability
test_data_single_row = {
    "label": [0],
    "code": [
        "for (var i = 1; i <= 5; i++) {eval('alert(\"Vulnerability!\")'); console.log(i);}"
    ],
}
df = pd.DataFrame(test_data_single_row)


with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
