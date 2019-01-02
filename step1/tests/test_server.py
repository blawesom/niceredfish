#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

from server import app
from flask import json

def test_root():        
    response = app.test_client().get('/')

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['response'] == "service alive"

def test_hello():        
    response = app.test_client().get('/test_name')

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['response'] == "hello test_name"
