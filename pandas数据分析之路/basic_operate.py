#!/usr/bin/env python
# -*- coding:utf-8 -*-
#导入模块
import numpy as np
import pandas as pd
import xlrd
from openpyxl.workbook import Workbook
#序列Series数组[1,2,3,4,5] + 二维数组DataFrame(二维数组 表格  行*列)

#dice序列
# dict_a = {"a":1,"b":11,"c":3,"d":9,"e":17}
# s1 = pd.Series(dict_a)
# print(s1)

#list序列
# list_a = [i for i in range(10)]
# s2 = pd.Series(list_a)
# print(s2)

#DataFrame 二维数组 表格  行*列
# D1 = [[1,2],[3,4],[6,7]]
# df = pd.DataFrame(D1,index=["line1","line2","line3"],columns=["name","age"])#行名，列名
# print(df)
# print(df.index) #输出索引（行名）
# print(df.columns)#输出列名
# print(df.values)#输出值
#输出和操作10*10的表格
# index_name = pd.date_range('20180801',periods = 10)
# col_name = [chr(ord("A")+i) for i in range(10)]
# df_date = pd.DataFrame(np.random.randn(10,10),index=index_name,columns=col_name )
# print(df_date)
# print(df_date.head(3))#取前三行
# print(df_date.tail(5))#取后五行
#print(df_date.ix[pd.datetime(2018,8,10)])#取特定的行
# print(df_date["A"])#获取特定的一列
# print(df_date[["A","C"]])#获取多列
# print(df_date.ix[[pd.datetime(2018,8,5),pd.datetime(2018,8,9)],["A","C"]])#获取特定的行列
#print(df_date[(df_date["A"]>0) & (df_date["B"]>0)]) #对列进行条件过滤
# print(df_date.describe())#默认统计(总数，平均数，最小值，最大值......等等)
# print(df_date.var())#平均值


#表联接
# stu = {
#     "name":["eric","cici","ben"],
#     "age":[28,29,30],
#     "math":[75,85,97],
#     "chinese":[98,89,32]
# }
# df_stu = pd.DataFrame(stu)
# print(df_stu)
#
#
# stu_english = {
#     "name":["eric","cici","ben","danny"],
#     "english":[98,99,100,65]
# }
# df_eng = pd.DataFrame(stu_english)
# print(df_eng)
#
# #left为左连接,right为右连接,outer为外链接,inner为内连接
# st_all = pd.merge(df_stu,df_eng,how="left",on="name")
# print(st_all)
