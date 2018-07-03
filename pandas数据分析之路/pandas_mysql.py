#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import pymysql

from sqlalchemy import create_engine
from pandas.io.sql import read_sql

#字典构造DataFrame
score_dict = {
    "name":["eric","ben","cici"],
    "english":[78,86,99],
    "math":[89,88,78],
    "python":[99,99,99]
}
#index 行名称 columns 列名称
dict_df = pd.DataFrame(score_dict,index=score_dict['name'],columns=['name','english','math','python'])


#写入mysql
# engine = create_engine("mysql+pymysql://jiangyue:jiangyue@192.168.19.159:3306/paydb?charset=utf8",echo=False)
# dict_df.to_sql(name="python_score",con=engine,if_exists="append",index=False)#index 行名称

#从mysql读数据
db = pymysql.connect("192.168.19.159","jiangyue","jiangyue","paydb",charset = 'utf8')
db_df = read_sql("select name,english,python from python_score",db)
print(db_df)


