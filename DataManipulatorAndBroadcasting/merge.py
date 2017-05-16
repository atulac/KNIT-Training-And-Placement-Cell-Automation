from pandas import DataFrame
import pandas as pd

def execute(path1,path2,path3):

    backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

    for key,value in backslash_map.items():
        path1=path1.replace(key,value)
        path2=path2.replace(key,value)
        path3=path3.replace(key,value)

    f1=pd.read_excel(path1)
    f2=pd.read_excel(path2)
    f3= f1.merge(f2, on="ROLL", how="outer")
    f3.to_excel(path3,index=False)


