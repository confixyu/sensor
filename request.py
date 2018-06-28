import requests
import json

if __name__=='__main__':
    
    url = 'http://192.168.0.194:5000/sensor'
    payload = {'statu':'300','voltage':'1','time':'2018-12-12'}
    r = requests.post(url, json=payload)
    print(r.content)
