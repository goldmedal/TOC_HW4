#!/usr/bin/python
# -*- coding=utf-8 -*-

# dict [{"count":count, "maxPrice":max, "minPrice":min, "yearMonth":date}, { ... }, ...]


import urllib2
import json
import sys

def check_road(roadName):

	if pos = roadName.find("路") != -1 :
		return pos
	else if pos = raodName.find("街") != -1 :
		return pos
	else if pos = roadName.find("巷") != -1 :
		return pos
	else
		return -1

url = sys.argv[1]
response = urllib2.urlopen(url)
data = response.read()
jload = json.loads(data)

roadName = unicode("土地區端位置或建物區門牌", "utf-8")
yearMonth = unicode("交易年月", "utf-8")
price = unicode("總價元", "utf-8")

roadDict = dict()

for column in jload:	
	
	road = str(column[roadName].encode("utf-8"))
	checkResult = check_road(road)

	if checkResult != -1 :
		road = road[0:checkResult]

		if not roadDict.has_key(road) :
			roadDict[road] = dict(count=1, maxPrice=column[price], minPrice=column[price], yearMonth=[column[yearMonth]])
		else

			if roadDict[road][yearMonth].count(column[yearMonth]) == 0 : 
				roadDict[road][count] += 1
				roadDict[road][maxPrice] = max(roadDict[road][maxPrice], column[price])
				roadDict[road][minPrice] = min(roadDict[road][minPrice], column[pirce])


