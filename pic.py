import requests
import json
import os

url = 'POSTURL'

if not os.path.exists('./picsave'):
    os.mkdir('./picsave')

imgdata = requests.get('https://api.vvhan.com/api/60s').content

imgname = '1.png'

path = './picsave/'+imgname

with open(path,'wb') as img:
    img.write(imgdata)

files=[('image',('today.png',open('./picsave/1.png','rb'),'image/png'))]

response = requests.post(url,files=files)
print(response.text)
