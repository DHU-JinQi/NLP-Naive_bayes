# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import jieba
import pyecharts as pec

#读取数据
def get_data():
	comment_data=pd.read_excel('评论数据.xls')
	return comment_data.loc[:,['hotelid','content']]

#建立中文停用词表 返回list格式
def get_stop_words():
	chinese_stop_words=[]
	for line in open("chinese_stop_words.txt",'r'):
		chinese_stop_words.append(line[:-1])
	return chinese_stop_words

#获取词频统计
def get_comment_keywords_counts(comment_data,chinese_stop_words):
	comment_list=comment_data.content
	comment_str_all=''
	for comment in comment_list:
		comment_str_all+=str(comment)+'\n'
	seg_list=list(jieba.cut(comment_str_all))
	# keywords_counts=pd.Series(seg_list)
	# keywords_counts=keywords_counts[keywords_counts.str.len()>1]
	# keywords_counts=keywords_counts[~keywords_counts.str.contains('|'.join(chinese_stop_words))]
	keywords_counts = [] 
	for word in seg_list:  
		if word not in chinese_stop_words:  
			if word != '\t':
				keywords_counts.append(word)
	keywords_counts=pd.Series(keywords_counts)
	keywords_counts=keywords_counts.value_counts()
	return keywords_counts[1:]

#词云图
def generate_wordcloud(keywords_counts,path_name):
	wordcloud =pec.WordCloud(path_name,width=1920, height=1080)
	# wordcloud.use_theme('dark')
	wordcloud.add("", keywords_counts.index, keywords_counts.values, word_size_range=[10, 200])
	wordcloud.render(path=path_name)

#统计各个酒店的评论数并绘制条形图
def get_hotel_list(comment_data):
	hotel_list=comment_data['hotelid'].value_counts()
	# hotel_list=hotel_list[hotel_list.values>min_comment_count]
	bar=pec.Bar(width=1920, height=1080)
	bar.add('各个酒店评论数条形图',hotel_list.index, hotel_list.values)
	# bar.use_theme('dark')
	bar.render(path='各个酒店评论数条形图.html')

#条形图
def generate_bar(keywords_counts,path_name):
	bar=pec.Bar(width=1920, height=1080)
	bar.add('',keywords_counts.index, keywords_counts.values)
	# bar.use_theme('dark')
	bar.render(path=path_name)

comment_data=get_data()
chinese_stop_words=get_stop_words()
keywords_counts=get_comment_keywords_counts(comment_data,chinese_stop_words)
get_hotel_list(comment_data)#统计各个酒店的评论数并绘制条形图
# generate_wordcloud(keywords_counts,'评论词云图.html')
generate_bar(keywords_counts,'评论条形图(all).html')

