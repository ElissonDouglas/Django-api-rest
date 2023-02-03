import requests


r = requests.get('http://127.0.0.1:8000/albums/')
for res in r.json():
    print(res['title'])
