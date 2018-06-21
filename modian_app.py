# -*- coding: utf-8 -*-

import requests
import re
import json
from pymongo import MongoClient
import pprint
from datetime import date
# from apscheduler.schedulers.background import BackgroundScheduler
# sched = BackgroundScheduler()
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

pid = '22904'
post_id = {}
lastId= {}
url = 'http://mapi.modian.com/v41/product/backer_ranking_list'

refreshUrl = 'http://mapi.modian.com/v41/product/comment_list'

productUrl = 'http://mapi.modian.com/v41/product'



header = {
    'nettype': 'WIFI',
    'channel': 'yingyongbao',
    'client': '2',
    'imei': '354268095484445',
    'sdk': '8.0.0',
    'version': '4.2.1',
    'device': 'SM-G9650',
    'mac': '02:00:00:00:00:00',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G9650 Build/R16NW)',
    'Host': 'mapi.modian.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '139'
}
def connectDB():
    client = MongoClient('mongodb://localhost:27017/',
                         # username='modian',
                         # password='modianpwd',
                         # authSource='modian_rank',
                         )
    db = client['modian_rank']
    return db

def initProject(pid):
    rankData = {
        'code': '11e09ec6c849c90c',
        'pro_id': pid,
        'user_id': 1750914,
        'page_index': 0,
        'page_rows': 20,
        'client': '2',
        'type': 'amount',
        'token': 't-9f4c9e59d1eafb31ad9d674ac4694e08'
    }
    productData = {
        'code': '6103ea3c10c2d8f6',
        'pro_id': pid,
        'user_id': '1750914',
        'client': '2',
        'token': 't-9f4c9e59d1eafb31ad9d674ac4694e08',
    }

    refreshData = {
        'code': '43426afbbfdb036a',
        'pro_id': pid,
        'user_id': 1750914,
        'moxi_post_id': 34741,
        'page_index': 0,
        'page_rows': 20,
        'client': '2',
        'pro_class': 202,
        'token': 't-9f4c9e59d1eafb31ad9d674ac4694e08'
    }

    global post_id
    global lastId
    page = 0
    result = []
    # rankData['pro_id'] = pid
    # productData['pro_id'] = pid
    refreshData['pro_id'] = pid
    # rankData['page_index'] = 0

    # 获取postId
    product = requests.post(productUrl, data=productData, headers=header,timeout=5)
    post_id[pid] = json.loads(json.loads(product.text)['data'])['product_info']['moxi_post_id']
    print(post_id)
    refreshData['moxi_post_id'] = post_id[pid]
    print(pid +'---postId---'+str(post_id[pid]))

    res = requests.post(url, data=rankData, headers=header,timeout=5)
    list = json.loads(json.loads(res.text)['data'])['ranking_list']
    # list = None
    # print(res.text)
    if list == None:
        lastId[pid] = 0
    else:
        #更新lastId
        lastIdRes = requests.post(refreshUrl, data=refreshData, headers=header,timeout=5)
        lastId[pid] = int(json.loads(json.loads(lastIdRes.text)['data'])[0]['id'])
        db['lastId'].update_one({'pid':pid},{ '$set':{'lastId':lastId[pid]} },True)
    print(lastId)

    #更新明细
    while list != None:
        for index, item in enumerate(list):
            user = {
                'uid': item['user_id'],
                'money': float(item['back_money']),
                # 'rank': page * 20 + index + 1,
                'nickName': item['nickname']
            }
            result.append(user)
        # print(len(list))
        if len(list) != 20:
            break
        else:
            page = page + 1
            rankData['page_index'] = page * 20
            res = requests.post(url, data=rankData, headers=header,timeout=5)
            list = json.loads(json.loads(res.text)['data'])['ranking_list']

    db[pid].drop()
    if result != []:
        insert = db[pid].insert_many(result)

    # print( lastId )
    # print(len(insert.inserted_ids))
# print(json.loads(json.loads(res.text)['data'])['ranking_list'])
# print(len(json.loads(json.loads(res.text)['data'])['ranking_list']))

def job(pid):
    def refresh():
        refreshData = {
            'code': '43426afbbfdb036a',
            'pro_id': pid,
            'user_id': 1750914,
            'moxi_post_id': 34741,
            'page_index': 0,
            'page_rows': 20,
            'client': '2',
            'pro_class': 202,
            'token': 't-9f4c9e59d1eafb31ad9d674ac4694e08'
        }
        global post_id
        global lastId
        page = 0
        refreshData['pro_id'] = pid
        refreshData['moxi_post_id'] = post_id[pid]
        refreshData['page_index'] = 0
        lastIdRes = requests.post(refreshUrl, data=refreshData, headers=header,timeout=5)
        realTimes = json.loads(json.loads(lastIdRes.text)['data'])
        # testz = db[pid].update_one({'uid':'6666'},{'$set':{'nickName':'哈哈哈哈'},'$inc':{'money':1000/100}}, True)
        # print(db[pid].find_one({'uid': '6666'}))
        recent = lastId[pid]
        end = False
        while len(realTimes) != 0:
            for index, item in enumerate(realTimes):
                # print('********')
                # print('this:'+ str(item['id'])  )
                # print(index)
                # print( lastId )
                # print('********')

                if int(item['id'])  > recent:
                    updateRes = db[pid].update_one({'uid':str(item['user_id'])},{'$inc':{'money':int(item['pay_amount'])/100}, '$set':{'nickName':item['user_info']['username']}}, True)
                    # print( updateRes.modified_count )
                    if updateRes.upserted_id != None:
                        print('add')
                    else:
                        print('update')
                    print(pid + '---' + str(item['user_info']['username'] + '----' + str(int(item['pay_amount'])/100)))
                    if index == 0 and page == 0:
                        print(pid + '---refresh lastId---'+ str(item['id']))
                        lastId[pid] = int(item['id'])
                        db['lastId'].update_one({'pid': pid}, {'$set': {'lastId': item['id']}}, True)
                else:
                    print('out')
                    end = True
                    break
            if end:
                break
            page = page + 1
            refreshData['page_index'] = page * 20
            lastIdRes = requests.post(refreshUrl, data=refreshData, headers=header, timeout=5)
            realTimes = json.loads(json.loads(lastIdRes.text)['data'])
    return refresh

db = connectDB()


# initProject('22680')
# sched.add_job(job('22680'), 'interval', seconds=3, start_date='2018-06-21 14:08:00', end_date='2019-06-21 20:55:00',max_instances=3)


#
initProject('23292')
initProject('20994')
initProject('22680')
initProject('20957')
sched.add_job(job('20957'), 'interval', seconds=3, start_date='2018-06-22 11:55:00', end_date='2018-06-23 11:30:00',max_instances=3)
sched.add_job(job('22680'), 'interval', seconds=3, start_date='2018-06-22 11:55:00', end_date='2018-06-23 11:30:00',max_instances=3)
sched.add_job(job('23292'), 'interval', seconds=3, start_date='2018-06-21 14:08:00', end_date='2018-06-22 12:30:00',max_instances=3)
sched.add_job(job('20994'), 'interval', seconds=3, start_date='2018-06-21 14:08:00', end_date='2018-06-22 12:30:00',max_instances=3)
sched.start()
# refresh('19179')
# refresh('19179')
# refresh('19179')
