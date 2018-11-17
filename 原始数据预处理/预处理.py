# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import jieba
import pyecharts as pec

#读取数据
def get_data():
	comment_data=pd.read_excel('KJ.xls')
	return comment_data

data=get_data()
data=data.dropna()
data=data.reindex(columns=['hotelid','rating','content','class'], fill_value=2)
data.to_excel("KJ(修改后).xls")

# #读取数据
# def get_data():
# 	comment_data=pd.read_excel('评论数据.xls')
# 	return comment_data

# comment_data=get_data()
# print(comment_data['content'].isnull().value_counts())
# comment_data = comment_data.dropna(subset=['content'])
# print(comment_data['content'].isnull().value_counts())
# comment_data.to_excel("评论数据(修改后).xls")
