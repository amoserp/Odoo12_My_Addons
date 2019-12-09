# -*- coding: utf-8 -*-
# http://www.cnblogs.com/shapeL/p/9037035.html

import requests

# url  = 'http://127.0.0.1:8069/api/user/get_token?login=admin&password=1'
# response = requests.get(url=url)
# print(response.text)

token = '08cf3b66093441e9a5ea07ae719aec49'
url  = 'http://127.0.0.1:8069/api/user/delete_token?token=' +token
response = requests.get(url=url)
print(response.text)



url  = 'http://127.0.0.1:8069/api/user/refresh_token?token=24e635ff9cc74429bed3d420243f5aa6'
response = requests.get(url=url)
print(response.text)