setwd("C:\\Users\\Administrator\\Desktop\\文本挖掘项目1\\绘图")

library(xlsx)
library(tm)
library(wordcloud2)
library(Rwordseg)
library(jiebaR)

data=read.xlsx('C:\\Users\\Administrator\\Desktop\\文本挖掘项目1\\绘图\\评论数据.xls',sheetName=1,encoding='UTF-8')
data=as.character(data$content)
data=gsub("[[:digit:]]*","",data) 
data=gsub("[a-zA-Z]","",data)
data=gsub("\\.\\.","",data)

stopwords_CN<-read.csv('C:\\Users\\Administrator\\Desktop\\文本挖掘项目1\\绘图\\chinese_stop_words.csv',sep='\n',header=FALSE)
stopwords_CN=as.vector(stopwords_CN[,1])
stopwords_CN=as.character(stopwords_CN)


w <- segmentCN(data, returnType = "tm")

seg_list <- list()
for (i in 1:length(w)) {
  seg_list <- c(seg_list, strsplit(w[i]," ")[[1]])
}

result <- seg_list[!seg_list %in% stopwords_CN]
result <- as.character(result)
f <- freq(result)##统计词频
f <- f[order(f$freq, decreasing=TRUE),]
wordcloud2(f[1:100,],size=1.2)
