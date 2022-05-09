import json
import unittest

import requests

url = "http://192.168.3.111:8062/api/iot/open"
body = {
    "adCode": "610726",
    "userCode": "张三",
    "userName": "",
    "initCode": "301011040956",
    "areaName": "",
    "areaCode": "",
    "address": "",
    "phone": "",
    "meterBase": "",
    "installDate": " "
}


def jsonpath(r2, param):
    pass


class Testopen(unittest.TestCase):
    def test_open(self):
        r = requests.post(url,json=body)
        r1 = r.text
        r2 = r.json()
        print(type(r1))
        print(type(r2))
        result = r2['message']


        print(result)
        ex ="行政区域编码不匹配"
        self.assertEqual(ex,result)




if __name__ == '__main__':
    unittest.main()