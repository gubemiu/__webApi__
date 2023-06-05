from . import api1
import pandas as pd
from flask import json


@api1.route("/stockCode")
def stockCode():
    code_dataFrame=pd.read_csv("api/codeSearch.csv")
    code_dataFrame1=code_dataFrame[['code','name']]
    all_list=code_dataFrame1.values.tolist()
    python_list=[{item[0]:item[1]} for item in all_list] #python的資料結構

    return json.dumps(python_list,ensure_ascii=False)


@api1.route("/stockCode/<int:code>")
def stockName(code):
    code_dataFrame=pd.read_csv("api/codeSearch.csv")
    code_dataFrame1=code_dataFrame[['code','name']]
    # code=2330
    try:
        name=code_dataFrame1.query('code == @code')['name'].values[0]
    except IndexError:
        return f"豬頭，沒有{code}"        
    return name