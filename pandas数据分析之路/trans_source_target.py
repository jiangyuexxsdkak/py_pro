#!/usr/bin/env python
# -*- coding:utf-8 -*-
#目标：处理不同来源的数据，写入不同格式的数据
#dict,csv,excel,json,,sql,
import pandas as pd
import xlrd  #处理excel的模块

#字典构造DataFrame
score_dict = {
    "name":["eric","ben","cici"],
    "english":[78,86,99],
    "math":[89,88,78],
    "python":[99,99,99]
}
#index 行名称 columns 列名称
dict_df = pd.DataFrame(score_dict,index=score_dict['name'],columns=["name","english","math","python"])
# print(dict_df)
# print(type(dict_df))



#DataFrame --> dict
# a = dict_df.to_dict()
# b = dict_df.to_dict(orient='list')# 以list为参照
# print(a)
# print(b)

#DataFrame和csv互转
# dict_df.to_csv(r"C:\Users\Administrator\Desktop\score.csv")#存入csv
# print(pd.read_csv(r"C:\Users\Administrator\Desktop\score.csv"))#读取csv

#DataFrame和excel互转
# dict_df.to_excel(r"C:\Users\Administrator\Desktop\score.xlsx",sheet_name="成绩单")
# print(pd.read_excel(r"C:\Users\Administrator\Desktop\score.xlsx"))

#DataFrame和json互转
# dict_df.to_json(r"C:\Users\Administrator\Desktop\score.json",orient="records")
# print(pd.read_json(r"C:\Users\Administrator\Desktop\score.json"))

