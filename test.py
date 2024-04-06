import pickle
import pandas as pd

##add another row
test_data_single_row = {
    "label": [0],
    "code": [
        'window.intercomSettings = { app_id: appId, name: myUserName, email: myUserEmail, user_hash: "my-user-hash" };'
    ],
}
df = pd.DataFrame(test_data_single_row)


with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
