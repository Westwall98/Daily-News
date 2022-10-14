import requests
import json
import urllib3
from bs4 import BeautifulSoup
import lxml

def get_weixin():

    urllib3.disable_warnings()

    wechaturl = 'https://mp.weixin.qq.com/cgi-bin/appmsg'

    headers = {
        "Cookie": "appmsglist_action_3546538960=card; ptui_loginuin=591485253; RK=hSVMo6CFEV; ptcz=cf5c8868c68c4fb58ec979c903afaaf40661df73df8628bfd210033f84f4d083; ua_id=h6Iblk27r1q8qmgGAAAAAK9IeT6_-lEylpxO8jxZhxU=; wxuin=65750417591563; mm_lang=zh_CN; skey=@i6qYPoCrE; uin=o591485253; uuid=4b62143d6143aff2e1073f26f3ecea24; rand_info=CAESIPgN6zFWsnBu/B3V9DbmHNGZGwKENpW7rQ4ezNHivDyH; slave_bizuin=3546538960; data_bizuin=3546538960; bizuin=3546538960; data_ticket=WkOR00cxbqxzxFwIlC5Q3EzdIqklLsPJenV/U3h5nOJ+hlPKRgImdpntDEHeCqVw; slave_sid=UDh6amVfNVJVdTdFSUlEWFJKQ0o3eXI5VzFnMDlGODJZbVZudXhrU3FNbzVSb1FPZTNBbGtBaGtfUE1QdFZndGliektFVlVKWTNIVTJLWXV5S0txZTYwR19IN3FkX3BBZFhhS3RINDBzTGpIRkZoTjF5SHJ0ckFCSGl2aHJkWTFsWHhPQ0ZhdVMxMGtHODJN; slave_user=gh_93c255ad7491; xid=6e789a800540b99acefbaff7353d5b13; _clck=3546538960|1|f5p|0; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }

    token = '844699240'

    params = {'token': '{}'.format(token), 'lang': 'zh_CN', 'f': 'json', 'ajax': '1', 'action': 'list_ex', 'begin': '0', 'count': '1', 'query': '', 'fakeid': 'MzU3MjYzNjc0Nw==', 'type': '9'}

    content_json = requests.get(wechaturl, headers=headers, params=params,verify=False).json()

    # print(content_json['app_msg_list'][0]['link'])
    # print(content_json['app_msg_list'][0]['title'])

    global link

    link = content_json['app_msg_list'][0]['link']

    get_news()

def get_news():

    news_html = requests.get(link)
    soup = BeautifulSoup(news_html.text, "lxml")
    for i in range(5,20):
        print(soup.select('div section section p span')[i].text)

get_weixin()
