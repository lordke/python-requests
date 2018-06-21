# -*- coding: utf-8 -*-

import random
from requests import Request, Session,request
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# proxies = {"http":"http://127.0.0.1:1087"}

sched = BlockingScheduler()
url ='https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22ggTAyJ5g3o8QQdD7CAwM4m2siZ8%22%2C%22from%22%3A%22H5node%22%2C%22scene%22%3A%224%22%2C%22cpId%22%3A%22JBE_qzq7mq%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22116.270628%22%2C%22lat%22%3A%2240.040671%22%7D%2C%22siteClient%22%3A%22apple%22%2C%22siteClientVersion%22%3A%226.5.1%22%7D&client=wh5&clientVersion=1.0.0&sid=d7fb658423d6a1da85586e645852308w&uuid=1445829561181-f1eac5aabee3087646.528.1509587850992&area=1_2901_4135_0&_=1509587852868&callback=jsonp11'
# url = 'https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22ggTAyJ5g3o8QQdD7CAwM4m2siZ8%22%2C%22from%22%3A%22H5node%22%2C%22scene%22%3A%224%22%2C%22cpId%22%3A%22JBE_qzq7mq%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22116.270628%22%2C%22lat%22%3A%2240.040671%22%7D%2C%22siteClient%22%3A%22apple%22%2C%22siteClientVersion%22%3A%226.5.1%22%7D&client=wh5&clientVersion=1.0.0&sid=d7fb658423d6a1da85586e645852308w&uuid=1445829561181-f1eac5aabee3087646.528.1509587850992&area=1_2901_4135_0&_=1509587852868&callback=jsonp11'.strip()
#订单请求页面
# url = 'https://m.48.cn/TOrder/add'
# url = 'http://checkip.dyndns.org/'
#开始刷票时间
start_date='2017-10-17 20:00:00'
start_date_2='2017-10-17 20:00:00'

#用户cookie
# cookie = {
#     # 'route':'7317c4b93b94800f61ea7f54b5887351',
#     # 'ASP.NET_SessionId':'0ls1rhem242i2bvgei5e0s2n',
#     # '.AspNet.ApplicationCookie':'xczb2G9VJgaSAnZkV6z-azzlXJJy-2rNPUAWuDx4FRajjQ-6G7GHbGkKBIgwb-ks-uFPc55-GuIZtAQvTa0hCkFWrPlFwms1B11cWaSjqZQKK2dANq62P8BUZrmE1K0fnaBoZ8HrNEIggV2LmA97itsVdNmmNNAyuHNCZGlHicTly3KSTUwfZK3k5ADC_SGYz3Aq4wZonGzJZ5rPUMALDpjI7wfws_UVIMK7XEBv-Sd4he9apbecRaGdSdHJdeWJnGUIqBHES2rlO-gvpJNYWFKUqmNhOEudAynOWISWW6-G4wry0V_RHhOHZnpuxDSVcHbLnFsUQA2ExPnOP5ERwmmP7pWwMBeI1UGHeDPxhlL8NC8jArPu0wzZTlGJ--TgQcoOpnUJgnpdlkOKXpcsc5bQaOx8Ko3leWec_P4lOKKztLv0C4CCGBnfO-6s4Woq8rAspHhPvm7lo7CvdS1xz9O4SiWXpZSGOBX-n2GQKjiIfNPToqoPzj6ogwRDgkWTmcdUZBgKq_EKgJdjqRqavKaDUe1YOsIZBSUaXCtVzag'
#     'route':'72b22cfe13b6559dd934c0716c55a35b',
#     'ASP.NET_SessionId': 'pkvugcisiwlvfaot32xrz4si',
#     '.AspNet.ApplicationCookie': 'qiOetHxKDBqHsEVCsiQkCHx86CEx0O4wBeNou9xCuUg-q-G7hmkFk7OfqjeIcL10BndAkiupBTYjpf4ShnQ_jsHm9PLnxHrzHLV2hjRy9w7OKz3aAkmP2jGHft6AmunWwmYeJaPv9LjooqIL7vHcqb2F5Vaz592iDqhkfV-S1hS2XlYkqe3Zpv1AF1YgC4wrYlOcQN4Wr6D0Cl_24x8QUE4Sc9qOiMexIcfdE8D8SEjs4A4VO0-iUbxFX-8gwWCCtp3h_KidUPFGmC0mgENbIFAHgp0Cz8hzW7JwIm8Q0TuanPm2RdhB0fliY3wa1nfMIFrExNHXlYlxhZJ_MhomDlx-hzF0fsLGlkbKPWJtdaexScnmnCSdhzBua7Oj2_zO66YgSyW-A8u_FI6JbdO4H06DAOKH8F5qsSc_z8CyhNw5xmzfYqBmrGyDOv65xrUhy7D_m4HRgmnKABAB2LCwT1kaI34nsDxA_1zhjYeFw12jirAdljTXnpJrtxvimttKUyWgyOyWyBmkp705CYIwnhbl7dWnu-S0Qsdzprr_3tXuFbHbrhrsk3s1eDb6ahXZagN8xb3OI1mglq6tbplWTq7S4oAnxSqio18dtxVPGxY'
# }
cookie = dict(mba_muid="1445829561181-f1eac5aabee3087646.528.1509587850992", mba_sid="528.7", __jdu="0x92664a2e192a59da", __jda="168871293.0x92664a2e192a59da.1445829561.1509551777.1509587070.99", __jdb="168871293.2.0x92664a2e192a59da|99.1509587070", __jdc="168871293", __jdv="168871293|kong|t_1000165215_keplersdk|huqiapp|notset|1509587365000", pre_seq='0', pre_session="c5700af0d7b66e4fe76fe242f6aa56fb0fb76eb2|607", pt_key="app_openAAFZ9x4BADCQdRKU1MFifwo4ZM1nj3BIfGh6Aq0WSCA8gWMqf9qshgB4TYFfPeCi6K5v0z4cJv4", pt_pin="honorhero", pwdt_id="honorhero", sid="d7fb658423d6a1da85586e645852308w", _jrda='2', shshshfpa="9dfc61b7-2371-2bb5-bd7a-a226f4b080f6-1478831300", shshshfpb="11993f0ccc39d4163aa78326e8722d458ea0de9546c38613458252cc45", __utmmobile="0x73b2b8a45f45a0d4.1446953341237.1465922756131.1466179361826.15", abtest="20151108112901040_33", webp='0', visitkey='19131516654044176')
print(cookie)

#Post数据
data = {
    # 场次id
    'id':1420,
    #订购数量
    'num':1,
    #座位等级 2：VIP； 3：普座 4：站票
    'seatType':3,
    #团体代号
    'brand_id':3,
    'r':random.random()
}
data2 = {
    # 场次id
    'id': 1422,
    # 订购数量
    'num': 1,
    # 座位等级 2：VIP； 3：普座 4：站票
    'seatType': 3,
    # 团体代号
    'brand_id': 3,
    'r': random.random()
}
header = {
    # 'Host':'m.48.cn',
    'referer':'https://pro.m.jd.com/mall/active/ggTAyJ5g3o8QQdD7CAwM4m2siZ8/index.html?has_native=0&client=apple&clientVersion=6.5.1&networkType=4g&lng=116.270628&lat=40.040671&un_area=1_2901_4135_0&sid=d7fb658423d6a1da85586e645852308w&client=apple&clientVersion=6.5.1&networkType=4g&lng=116.270628&lat=40.040671&un_area=1_2901_4135_0&sid=d7fb658423d6a1da85586e645852308w',
    'User-Agent':'jdapp;iPhone;6.5.1;11.0.2;c5700af0d7b66e4fe76fe242f6aa56fb0fb76eb2;network/4g;ADID/21E774DA-5CB2-4E2B-922A-29B9DC0A4CD3;supportApplePay/2;hasUPPay/0;pushNoticeIsOpen/0;pv/528.5;pap/JA2015_311210|155446|IOS 11.0.2;psn/c5700af0d7b66e4fe76fe242f6aa56fb0fb76eb2|607;psq/0;ads/;ref/;jdv/0|kong|t_1000165215_keplersdk|huqiapp|notset|1509587365;usc/kong;adk/;umd/huqiapp;ucp/t_1000165215_keplersdk;utr/notset;Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A421;supportJDSHWK/1'
}

req = Request('Get',url,
              # data = data,
              headers = header,
              cookies = cookie
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


sched.start()
# sched.shutdown()
sched.start()