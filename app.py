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
    message = req.get("result").get("fulfillment").get("messages")[0]["speech"]
    responseMessage = json.dumps({
        "speech": message,
        "displayText": message,
        "messages": {
            "type": 1,
            "title": "card title",
            "subtitle": "card text",
            "imageUrl": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png"
        },
        "data": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": message
                            }
                        }
                    ]
                }
            },
            "facebook": {
                "text": message
            },
            "slack": {
                "text": message
            }
        },
        "contextOut": [],
        "source": "example.com",
        "followupEvent": {}
    })
    if req.get("result").get("action") == "Feedback":
        baseurl = "https://hooks.zapier.com/hooks/catch/3544928/wvzqh2/"
        r = requests.post(baseurl, data=json.dumps(req))
    elif req.get("result").get("action") == "RegisterOnline":
        baseurl = "https://hooks.zapier.com/hooks/catch/3544928/wvk6pa/"
        r = requests.post(baseurl, data=json.dumps(req))
    return responseMessage


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
