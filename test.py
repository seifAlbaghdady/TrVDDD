import pickle
import pandas as pd

# code in js got vulnerability
test_data_single_row = {
    "label": [0],
    "code": [
        "for (var i = 1; i <= 5; i++) {setTimeout(() => {console.log('Vulnerability!')}, 1000 * i);}"
    ],
}
df = pd.DataFrame(test_data_single_row)


with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
