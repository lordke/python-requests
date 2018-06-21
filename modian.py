# -*- coding: utf-8 -*-

import random
from requests import Request, Session,request, get
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import re

data ={
    'jsonpcallback': 'jQuery11110008175516701516505_1529158199871',
    'origin_id': '19179',
    'type': 'backer_list',
    'page': 1,
    'page_size': 20,
    'cate': 1,
    '_': 1529158199878
}

header ={
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'mdsa=MD-STICS-5ac43e39eb420; _ga=GA1.2.705727849.1522810426; PHPSESSID=n15bc9aplhoicu83uq3lq37t26; mdss=22-o; ci_session=ZgDJPdioEltoJlabzfE5dgl9iiavMxOfAAKWqc1NUiZO%2B%2FV%2Bm%2FiiWj4ZoU2lulBm7iFf9o%2BPUnL8dCddkULpBUcGrNkiKDzoGnzTNcNyGh4Jce%2BwsA7MTQyDz%2F4L7gcGAQ0v5VwdsXmq%2FNHk4kFghlmkGIZb1bd%2FOImFy0%2FaRijaxSvSaks%2FN4oMV8DvmtexR4%2FYmLQMx5Gm58ZvvMfD3SLe0O3OmbDPclCxC6LEKoIyfqgz4RwyWfIQH%2FnMiv7Pe%2FbVFGxPHIcnUbq22bUrVB3zNoB7DVjSomLQMd%2BGalg%2BE3oYh0gKMxN2F0HMuBmbLB9TqjTkgi54MnZxZytRKqo9ipTahHSNy851ZO%2BdrJyKkS%2FrLSlxW22J%2FXC0%2FLEAHqgeOn2WnfSoNiX2IHKxgsrv4V8TPTaOOVAdXCkVH%2F131IQ%2FpSHNe1bfuhVX19dSGGYC6cg3ML8BO%2FgMnGx2PA%3D%3D; _gid=GA1.2.139983120.1529158185; SERVERID=75c0ee4e77ef78c56ac6e5a297fdd0b8|1529158272|1529158181
    'DNT': '1',
    'Host': 'zhongchou.modian.com',
    'Pragma': 'no-cache',
    'Referer': 'https://zhongchou.modian.com/item/19179.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

res = get('https://zhongchou.modian.com/realtime/ajax_dialog_user_list', params=data, headers=header )
print(res.text)
pattern = re.compile(r'\<p\>(.+?)<\\/p>\\n')
results = pattern.findall(res.text)
for result in results:
    print(result.encode('latin-1').decode('unicode_escape'))



