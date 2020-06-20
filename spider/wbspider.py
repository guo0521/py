import requests
import time
from urllib.parse import urlencode
from multiprocessing import Pool

def a(since_id='',uid=0,):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://m.weibo.cn'
    }
    params={
        'uid':uid,
        'luicode':10000011,
        'lfid':'231093_-_selffollowed',
        'type':int(uid),
        'value':5743555203,
        'containerid':'107603'+str(uid),
        'since_id':since_id
    }
    lv=[]
    url='https://m.weibo.cn/api/container/getIndex?'+urlencode(params)
    req=requests.get(url,headers=headers)
    req=req.json()  #since_id
    since_id=req.get('data').get('cardlistInfo').get('since_id')
    imgs=req.get('data').get('cards')
    for i in imgs:
        try:
            i=i.get('mblog').get('pics')
            for v in i :
                v=v.get('large').get('url')
                lv.append(v)
        except:
            continue
    time.sleep(0.5)
    return lv,since_id

def down(isd='',lio=''):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://m.weibo.cn',

    }
    re = requests.get(isd, headers=headers, )
    print(re)
    name = str(lio) + '.jpg'
    with open(name, 'wb')as f:
        f.write(re.content)
    print('-' * 10)
    time.sleep(0.5)

if __name__ == '__main__':
    lvvv=[]
    t=0
    sw=0
    u = eval(input('输入uid:'))
    p = eval(input('输入页数/10:'))
    try:
        s = a(since_id='', uid=u)
        lvvv.extend(s[0])
        for o in range(p):
            sw+=1
            s = a(since_id=s[1], uid=u)
            lvvv.extend(s[0])
            print(sw)
    except:pass
    for i in range(len(lvvv)):
        down(lvvv[i],i)