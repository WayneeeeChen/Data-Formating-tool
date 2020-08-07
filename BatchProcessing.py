#! /usr/bin/env python
#coding=utf-8
import pandas as pd 
import numpy as np 
import os
import time

os.getcwd()  
path = 'Crawldata'
os.listdir(path)

datalist = []
for i in os.listdir(path):
    if os.path.splitext(i)[1] == '.txt':   
        datalist.append(i)
#print(datalist)
#print(len(datalist))



for data in datalist:

	dataRe = data.strip('.txt')

	flag = 0
	getData = open("Crawldata/"+data,"r").readline().strip('listPriceData: ').replace("[{","").replace("{","\n").replace("},","").replace('"s":',"").replace(',"e":',"\n")
	f = open("register/Reorganize.txt","w")
	f.write(getData)
	f.close()
	for y in open("register/Reorganize.txt","r"):
		flag = flag+1
		x = time.localtime(int(y[:10]))
		
		ok = time.strftime('%Y-%m-%d %H:%M:%S',x)

		if flag % 2 == 1:
			print("s:",ok)
			f = open("Output/"+dataRe+"_con"+".txt","a")
			f.write("S:"+ok+" ")
		else:
			print("e:",ok)
			f = open("Output/"+dataRe+"_con"+".txt","a")
			f.write("E:"+ok+" ")
			

			printprice = str(y)[18::]
			print("price:",printprice)
			f = open("Output/"+dataRe+"_con"+".txt","a")
			f.write("Price:"+printprice)
		


	f.close()
