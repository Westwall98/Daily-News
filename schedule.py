import requests
import json

def run():
    payload = json.dumps({"ref": "main"})
    header = {'Authorization': 'Bearer SECRETS',"Accept": "application/vnd.github+json"}
    response_decoded_json = requests.post(f'https://api.github.com/repos/Westwall98/Daily-News/actions/workflows/main.yml/dispatches',data=payload, headers=header)

run()
