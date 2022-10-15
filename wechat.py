import requests
import json
import urllib3
from bs4 import BeautifulSoup
import lxml

def get_weixin():

    urllib3.disable_warnings()

    wechaturl = 'https://mp.weixin.qq.com/cgi-bin/appmsg'

    headers = {
        "Cookie": "ua_id=RITu2IbP6WnFRhvFAAAAAN1Q0z-1CUh9-DpkoMRpiFQ=; wxuin=65816475654888; uuid=93bf6ddc11321744e343eee077050e2e; rand_info=CAESIJggHKgjjgywS6JhOoZp1JvQ0GSm/NgCCU3IrLwU1oMc; slave_bizuin=3546538960; data_bizuin=3546538960; bizuin=3546538960; data_ticket=nhJ3QHXotYjae3mIjmkc+/vofkZGH5zuARAQIgL98i7XRJD7JXpMcu/a4OSln0Bl; slave_sid=ZTlvdUhhbjFzZkUzQURkQXRGRWxoMzVYdmVDMVV0RHZaVFNUWGFON0xrTUJ1VXJBQUc1Z2VDYkE5N1dHZk5lMGpwRjhIaHJkRVRkMG1HSnBoekFDVWducDVrM01QWlYxMUNjVWJoa0tDc0dvaTJ2ZjdTcGFpYWNtVllGTWYzNmhwZ2NsYTQxT2VRbURTaGtq; slave_user=gh_93c255ad7491; xid=b2a158ccc7423e891f3e13e6c0803588; mm_lang=zh_CN; _clck=3546538960|1|f5q|0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }

    token = '131441509'

    fakeid = 'Mzg3NTQ0MjQwNg=='

    params = {'token': '{}'.format(token), 'lang': 'zh_CN', 'f': 'json', 'ajax': '1', 'action': 'list_ex', 'begin': '1', 'count': '1', 'query': '', 'fakeid': '{}'.format(fakeid), 'type': '9'}

    content_json = requests.get(wechaturl, headers=headers, params=params,verify=False).json()

    # print(content_json['app_msg_list'][0]['link'])
    # print(content_json['app_msg_list'][0]['title'])

    global link

    link = content_json['app_msg_list'][0]['link']

    get_news()

def get_news():

    news_html = requests.get('https://mp.weixin.qq.com/s?__biz=Mzg3NTQ0MjQwNg==&mid=2247485689&idx=1&sn=039bf94b16362731cc7329947c93c39b&chksm=cec03170f9b7b8666e26b5bf519828c9a3d387fe6e68148a5d2862d093c39df6bbe415cd68d0&token=131441509&lang=zh_CN#rd')
    soup = BeautifulSoup(news_html.text, "lxml")

    for i in range(2,19):
        print(soup.select('body div div div div div div p span')[i].text)

get_news()
