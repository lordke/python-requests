import requests
import re
import json
from pymongo import MongoClient
import pprint

data ={
    'code':'43426afbbfdb036a',
    'pro_id':'20507',
    'user_id':1750914,
    'moxi_post_id':	34741,
    'page_index':0,
    'page_rows'	:20,
    'client':'2',
    'pro_class':    202,
    'token':'t-9f4c9e59d1eafb31ad9d674ac4694e08'
}

header= {
    'nettype':	'WIFI',
    'channel':	'yingyongbao',
    'client':	'2',
    'imei':	'354268095484445',
    'sdk':	'8.0.0',
    'version':	'4.2.1',
    'device':	'SM-G9650',
    'mac':	'02:00:00:00:00:00',
    'Content-Type':	'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':	'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G9650 Build/R16NW)',
    'Host':	'mapi.modian.com',
    'Connection':	'Keep-Alive',
    'Accept-Encoding':	'gzip',
    'Content-Length':	'139'
}

url = 'http://mapi.modian.com/v41/product/comment_list'

res = requests.post(url, data=data, headers=header)

print(json.loads(json.loads(res.text)['data']))

# for item in json.loads(json.loads(res.text)['data']:
