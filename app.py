#!/usr/bin/env python

import json
import os
import requests
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    if req.get("result").get("action") == "Feedback":
        baseurl = "https://hooks.zapier.com/hooks/catch/2399943/wpr974/"
        r = requests.post(baseurl, data=json.dumps(req))
    elif req.get("result").get("action") == "RegisterOnline":
        baseurl = "https://hooks.zapier.com/hooks/catch/2399943/wp99ov/"
        r = requests.post(baseurl, data=json.dumps(req))
    else:
        return {}
    return r.text


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
