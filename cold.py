# -*- coding: utf-8 -*-

import random
from requests import Request, Session,request
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import re
import pprint
# proxies = {"http":"http://127.0.0.1:1087"}

sched = BlockingScheduler()
url ='http://user.snh48.com/Login/plogin/'
url_2 ='https://m.48.cn/Account'
#订单请求页面
# url = 'https://m.48.cn/TOrder/add'
# url = 'http://checkip.dyndns.org/'
#开始刷票时间
start_date='2017-10-17 20:00:00'
start_date_2='2017-10-17 20:00:00'

#用户cookie
data = {
    # 'username':'snh48082304083',
    # 'password':'19960921Hero48',
    # 'code':''
    'username': 'joewood',
    'password': '19960921Heroasd',
    'code': ''
}

#Post数据
# data = {
#     # 场次id
#     'id':1420,
#     #订购数量
#     'num':1,
#     #座位等级 2：VIP； 3：普座 4：站票
#     'seatType':3,
#     #团体代号
#     'brand_id':3,
#     'r':random.random()
# }
# data2 = {
#     # 场次id
#     'id': 1422,
#     # 订购数量
#     'num': 1,
#     # 座位等级 2：VIP； 3：普座 4：站票
#     'seatType': 3,
#     # 团体代号
#     'brand_id': 3,
#     'r': random.random()
# }
header = {
    # 'Host':'m.48.cn',
    'referer':'http://user.snh48.com/Login/index.html?return_url=https://m.48.cn/home/index',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

req = Request('POST',url,
              data = data,
              headers = header,
              # cookies = cookie
              )
s = Session()
prepped = s.prepare_request(req)

# req2 = Request('POST',url,
#               data = data2,
#               headers = header,
#               cookies = cookie
#               )
# s2 = Session()
# prepped2 = s2.prepare_request(req2)




# res = s.send(prepped)

def workstop(id):
    sched.remove_job(id)
    sched.add_jov()

def work():
    res = s.send(prepped)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # print('status_code')
    # print(res.status_code)
    # print('url')
    # print(res.url)
    print(res.text)
    if datetime.now().strftime("%Y-%m-%d %H:%M:%S") == '2017-09-06 20:05:00':
        sched.add_job(workstop,args=['work_id'])

# def work2():
#     res = s2.send(prepped2)
#     print('********  '+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     # print('status_code')
#     # print(res.status_code)
#     # print('url')
#     # print(res.url)
#     print('********  '+res.text)
#     if datetime.now().strftime("%Y-%m-%d %H:%M:%S") == '2017-09-06 20:05:00':
#         sched.add_job(workstop, args=['work_id_2'])
# def work2():
#
#     res = request('post',url,
#               data = data,
#               headers = header,
#               cookies = cookie,
#               proxies=proxies)
#     print('*****'+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     # print('status_code')
#     # print(res.status_code)
#     # print('url')
#     # print(res.url)
#     print('text')
#     print(res.text)
#     if datetime.now().strftime("%Y-%m-%d %H:%M:%S") == '2017-08-24 19:30:35':
#         sched.add_job(workstop,args=['work_id_2'])


sched.add_job(work, 'interval', seconds=10,id='work_id',start_date=start_date,max_instances=10)
# sched.add_job(work2, 'interval', seconds=2,id='work_id_2',start_date=start_date_2,max_instances=10)


# sched.start()
# # sched.shutdown()
# sched.start()
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
res = s.send(prepped)
print(res.text)
pattern = re.compile(r'src=\\\"(\S*)\\\"\s')
result = pattern.findall(res.text)
# pprint.pprint(result)

for eachurl in result:
    pp = re.compile(r'\\/')
    eachurl = pp.sub(r'/', eachurl)
    print('each   '+eachurl)
    ress = s.request('GET',eachurl,headers=header)


res2 = s.request('GET',url_2,headers=header)
print(res2.url)
print(res2.text)

def login():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # 获取验证网址设置cookie
    res = s.send(prepped)
    pattern = re.compile(r'src=\\\"(\S*)\\\"\s')
    urls = pattern.findall(res.text)

    for eachurl in urls:
        pt = re.compile(r'\\/')
        eachurl = pp.sub(r'/', eachurl)
        print('each   ' + eachurl)
        # 访问验证网址设置cookie
        s.request('GET', eachurl, headers=header)



