# coding: utf-8

import os
import requests

files = {'files': open('submission.csv', 'rb')}

data = {
    # user_id is your username which can be found on the top-right corner on our website when you logged in.
    "user_id": os.environ['KDD_CUP_USER_ID'],
    "team_token": os.environ['KDD_CUP_TOKEN'],  # your team_token.
    "description": '2017 average sample',  # no more than 40 chars.
    "filename": "submission.csv",  # your filename
}

url = 'https://biendata.com/competition/kdd_2018_submit/'

response = requests.post(url, files=files, data=data)

print(response.text)
