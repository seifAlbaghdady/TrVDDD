import pandas as pd
import re
from clean_gadget import clean_gadget
import os


def normalization(source):
    nor_code = []
    for fun in source["code"]:
        lines = fun.split("\n")
        # print(lines)
        code = ""
        for line in lines:
            line = line.strip()
            line = re.sub("//.*", "", line)
            code += line + " "
        # code = re.sub('(?<!:)\\/\\/.*|\\/\\*(\\s|.)*?\\*\\/', "", code)
        code = re.sub("/\\*.*?\\*/", "", code)
        code = clean_gadget([code])
        nor_code.append(code[0])
        # print(code[0])
    return nor_code


def mutrvd():

    test = pd.read_pickle("./dataset/trvd_test.pkl")

    if not os.path.exists("./dataset/mutrvd"):
        os.makedirs("./dataset/mutrvd")

    test["code"] = normalization(test)
    test.to_pickle("./dataset/mutrvd/test.pkl")


if __name__ == "__main__":
    mutrvd()
