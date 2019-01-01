#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import flask
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def status():
    return flask.jsonify({  'service': 'nice redfish',
                            'response': 'service alive'})

@app.route('/<name>', methods=['GET'])
def hello(name):
    return flask.jsonify({  'service': 'nice redfish',
                            'response': 'hello {}'.format(name)})

if __name__ == '__main__':
    file_handler = RotatingFileHandler('/tmp/server_activity.log', 'a', 50000000, 5)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    app.run(host='0.0.0.0', port=80, debug=True)