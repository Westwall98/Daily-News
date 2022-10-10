import requests
import json
import os

apiurl = os.getenv('URL')

url = os.getenv('POSTURL')

pic = (json.loads(requests.get(apiurl).text))['imageUrl']

if not os.path.exists('./picsave'):
    os.mkdir('./picsave')

img = requests.get(pic).content

imgname = '1.png'

path = './picsave/'+imgname

with open(path,'wb') as fp:
    fp.write(img)

files=[('image',('1.png',open('./picsave/1.png','rb'),'image/png'))]

response = requests.post(url,files=files)
print(response.text)
