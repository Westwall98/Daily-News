import requests
import json
import os
import datetime

apiurl = os.getenv('URL')

url = os.getenv('POSTURL')

jsstr = json.loads(requests.get(apiurl).text)

filename = str(datetime.date.today()) +'.txt'

if not os.path.exists('./picsave'):
    os.mkdir('./picsave')

path = './picsave/'+filename

with open(path,'w') as fp:
	for i in range(15):
		fp.write(str(i+1)+'、'+jsstr["data"][i]+'\n\n')

files=[('file',(filename,open(path,'r'),'text/plain'))]

response = requests.post(url,files=files)

print(response.text)
