#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 03:15:25 2020

@author: konark
"""

import requests

api_key = '74fc6d1eca2e4a7acd645eb1e540dcb285680882'
endpoint = 'https://comicvine.gamespot.com/api/'

payload = {'api_key':api_key, 'format':'json'}

resource = 'characters/'

headers = {
    'User-Agent': 'Python API Requests',
    'From': 'konark@gmail.com'  # This is another valid field
}


url = endpoint + resource

response = requests.get(url, params = payload, headers = headers)

print(response.text)

