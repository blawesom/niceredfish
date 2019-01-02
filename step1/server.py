#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import flask
import logging
from logging.handlers import RotatingFileHandler

# logger declaration
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# flask app is declared after the logger to catch it
app = flask.Flask(__name__)

# default route for server status
@app.route('/', methods=['GET'])
def status():
    return flask.jsonify({  'service': 'nice redfish',
                            'response': 'service alive'})

# dynamic route to respond to a first name 
@app.route('/<name>', methods=['GET'])
def hello(name):
    return flask.jsonify({  'service': 'nice redfish',
                            'response': 'hello {}'.format(name)})

if __name__ == '__main__':
    # configure log file to rotate in 5 files of 50MB
    file_handler = RotatingFileHandler('/tmp/server_activity.log', 'a', 50000000, 5)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # start application to be available from any IP on port 80
    app.run(host='0.0.0.0', port=80)