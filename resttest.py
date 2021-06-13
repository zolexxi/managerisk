import requests

resp = requests.get('http://192.168.0.106:8088/ari/endpoints?api_key=asterisk:asterisk')
jresp = resp.json()
print(jresp)