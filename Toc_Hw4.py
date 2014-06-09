#!/usr/bin/python
# -*- coding=utf-8 -*-

# dict [{"count":count, "maxPrice":max, "minPrice":min, "yearMonth":date}, { ... }, ...]


import urllib2
import json
import sys

def check_road(roadName):

	if roadName.find("路") != -1 :
		pos = roadName.find("路")
		return pos+3
	elif roadName.find("街") != -1 :
		pos = roadName.find("街")
		return pos+3
	elif roadName.find("巷") != -1 :
		pos = roadName.find("巷")
		return pos+3
	else :
		return -1


roadName = unicode("土地區段位置或建物區門牌", "utf-8")
yearMonth = unicode("交易年月", "utf-8")
price = unicode("總價元", "utf-8")

url = sys.argv[1]
response = urllib2.urlopen(url)
data = response.read()
jload = json.loads(data)

roadDict = dict()
x = 0

for column in jload:	

	road = str(column[roadName].encode("utf-8"))
	checkResult = check_road(road)

	x+=1

	if checkResult != -1 :
		road = road[0:checkResult]

		if not roadDict.has_key(road) :
			roadDict[road] = dict(count=1, maxPrice=column[price], minPrice=column[price], date=[column[yearMonth]])

		else :

			if roadDict[road]['date'].count(column[yearMonth]) == 0 :
				roadDict[road]['date'].append(column[yearMonth])
				roadDict[road]['count'] += 1
				roadDict[road]['maxPrice'] = max(roadDict[road]['maxPrice'], column[price])
				roadDict[road]['minPrice'] = min(roadDict[road]['minPrice'], column[price])



maxCount = 0

for road in roadDict:
	column =  roadDict[road]
	maxCount = max(maxCount, column['count'])


maxRoad = []

for road in roadDict:
	column = roadDict[road]
	if(column['count'] == maxCount):
		maxRoad.append(road)

for road in maxRoad:
	print "%s, 最高成交價:%d, 最低成交價:%d" %(road, roadDict[road]['maxPrice'], roadDict[road]['minPrice'])

#index = roadDict.find(maxRoad)
#print maxRoad
#print "最高成交價: %d" %(roaDict[index]

