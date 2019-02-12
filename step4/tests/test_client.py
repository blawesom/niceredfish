#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import sys, os
import json
import requests
import random
import time

domain = 'redfish.blawesom.com'

lines = open('/usr/share/dict/words').read().splitlines()
new_name =random.choice(lines)


def test_root():        
    response = requests.get('https://{}/'.format(domain))
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['response'] == "service alive"

def test_hello():        
    response = requests.get('https://{}/{}'.format(domain, new_name))
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['response'] == "nice to meet you {}".format(new_name)

def test_hello_2():        
    response = requests.get('https://{}/{}'.format(domain, new_name))
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['response'] == "nice to see you again {}".format(new_name)

