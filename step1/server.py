#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

import flask

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
    app.run(host='0.0.0.0', port=80, debug=True)