import sys
import os
import time
import codecs
import csv
import urllib
import urllib2
import json

#get data accordding the url
def initialUrl():
    try:
        url = "http://quote.gf.com.cn/kline/daily/sz/000776/20"
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        return res
    except Exception,e:
        print e
        
#parse the data from json
def verifyJsonData(jsonData):
    value = json.loads(jsonData)
    for obj in value:
        low = float(obj["low"])
        avg = float(obj["avg"])
        high = float(obj["high"])
        #verify the data
        if avg>=low and high>=avg:
            obj["result"] = "pass"
        else:
            obj["result"] = "fail"
        print obj
    return value
    
def writeCsvFile(value):
    tempFile = codecs.open('G:\\workspace\\verify-data\\data-result\\result.csv', 'wb', "utf-8")
    #tempFile = codecs.open('home/workspace/verify-data/data-result/result.csv', 'wb', "utf-8")
    writer = csv.writer(tempFile, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    writer.writerow(['time', 'pclose', 'open', 'close', 'high', 'low', 'avg', 'volume', 'amount', 'result'])
    
    for obj in value:
        #print time.strftime("%Y-%m-%d", obj["time"])
        print obj["time"]
        sortedValues = []
        sortedValues.append(obj["time"])
        sortedValues.append(obj["pclose"])
        sortedValues.append(obj["open"])
        sortedValues.append(obj["close"])
        sortedValues.append(obj["high"])
        sortedValues.append(obj["low"])
        sortedValues.append(obj["avg"])
        sortedValues.append(obj["volume"])
        sortedValues.append(obj["amount"])
        sortedValues.append(obj["result"])
        writer.writerow(sortedValues)
        
if __name__ == "__main__":
    data = initialUrl()
    result = verifyJsonData(data)
    writeCsvFile(result)
    