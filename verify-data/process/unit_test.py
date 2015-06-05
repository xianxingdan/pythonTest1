'''
Created on 2015-6-4

@author: dequality
'''
import urllib
import urllib2
import unittest
from unittest import TestSuite
import json
from collections import OrderedDict

class VefifyJsonDataTest(unittest.TestCase):
    def setUp(self):
        print "Create a interface json data test....."
        try:
            url = "http://quote.gf.com.cn/kline/daily/sz/000776/20"
            req = urllib2.Request(url)
            res_data = urllib2.urlopen(req)
            self.res = res_data.read()
            #return res
        except Exception,e:
            print e    
        
    def tearDown(self):
        print "Destroying a interface json data test....."

    def test_verify_data(self):
        value = json.loads(self.res,object_pairs_hook=OrderedDict)
        for obj in value:
            low = float(obj["low"])
            avg = float(obj["avg"])
            high = float(obj["high"])
        #verify the data
            #self.assertTrue(avg>=low and high>=avg)
            if avg>=low and high>=avg:
                obj["result"] = "sucess"
            else:
                obj["result"] = "fail"
            print obj
    
if __name__ == '__main__':
    unittest.main()
    suite = TestSuite()
    suite.addTest(test_verify_data())