from json2html import *
import requests

resp = requests.get('http://192.168.0.106:8088/ari/asterisk/info?api_key=asterisk:asterisk')
jresp = resp.json()
print(json2html.convert(json = jresp))