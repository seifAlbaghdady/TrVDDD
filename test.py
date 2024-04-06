import pickle
import pandas as pd

# code in js got vulnerability
test_data_single_row = {
    "label": [1],
    "code": [
        'var userInput = document.getElementById("userInput").value; document.write("Hello, " + userInput + "!");'
    ],
}
df = pd.DataFrame(test_data_single_row)


with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
