# -*- coding: UTF-8 -*-
import pandas as pd


#建立中文停用词表 返回Series格式
def get_stop_words():
	chinese_stop_words=[]
	for line in open("chinese_stop_words.txt",'r'):
		chinese_stop_words.append(line[:-1])
	return pd.Series(chinese_stop_words)

chinese_stop_words=get_stop_words()
chinese_stop_words.to_csv('chinese_stop_words.csv',encoding='utf_8_sig')
