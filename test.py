import pickle
import pandas as pd


test_data_single_row = {
    "label": [0],
    "code": [
        'var vulnerableFunction=function(input){var data=input.split(" ");var result="";for(var i=0;i<data.length;i++){result+=data[i];}return result;};var userInput="Hello World";var output=vulnerableFunction(userInput);console.log(output);'
    ],
}

df = pd.DataFrame(test_data_single_row)
with open("./dataset/trvd_test.pkl", "wb") as f:
    pickle.dump(df, f)
