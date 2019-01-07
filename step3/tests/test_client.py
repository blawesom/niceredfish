#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import sys, os
import json
import requests
import random
import time

with open('inventory', 'r') as inv:
    ip = inv.readlines()[1]

lines = open('/usr/share/dict/words').read().splitlines()
new_name =random.choice(lines)

def test_root():        
    response = requests.get('http://{}:80/'.format(ip))
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['response'] == "service alive"

def test_hello():        
    response = requests.get('http://{}:80/{}'.format(ip, new_name))
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['response'] == "nice to meet you {}".format(new_name)

def test_hello_2():        
    response = requests.get('http://{}:80/{}'.format(ip, new_name))
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['response'] == "nice to see you again {}".format(new_name)