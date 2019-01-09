#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import os
import flask
import logging
from logging.handlers import RotatingFileHandler

# logger declaration
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Entries, Base

# configure log file to rotate in 5 files of 5MB
file_handler = RotatingFileHandler('/var/log/redfish/server_activity.log', 'a', 5000000, 5)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# connect to local sqlite db
engine = create_engine('sqlite:////tmp/redfish.db')
if not os.path.isfile('/tmp/redfish.db'):
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# flask app is declared after the logger to catch it
app = flask.Flask(__name__)

# query db to return list of entry for a given ip
def get_entry_list(ip, name):
    return session.query(Entries).filter_by(ip=ip, name=name).all()

# default route for server status
@app.route('/', methods=['GET'])
def status():
    return flask.jsonify({  'service': 'nice redfish',
                            'response': 'service alive'})

# dynamic route to respond to a first name 
@app.route('/<name>', methods=['GET'])
def hello(name):
    if get_entry_list(flask.request.remote_addr, name):
        response = 'nice to see you again {}'.format(name)
    else:
        response = 'nice to meet you {}'.format(name)

    # add entry for this request
    entry = Entries(ip=flask.request.remote_addr, name=name)
    session.add(entry)
    session.commit()

    return flask.jsonify({  'service': 'nice redfish',
                            'response': response})

if __name__ == '__main__':

    # start application to be available from any IP on port 80
    # used only when server.py is directly called
    # all other configuration has been moved to be imported in the package
    app.run(host='127.0.0.1', port=8080)