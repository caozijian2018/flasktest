from flask import Flask, request
import requests

app = Flask(__name__)


# 得到token
@app.route('/gettoken', methods=['GET', 'POST'])
def gettoken():
    req = request.json
    print(req)
    websiteURL = req['websiteURL']
    websiteKey = req['websiteKey']
    pageAction = req.get('pageAction', None)
    res = requests.post("http://api.anti-captcha.com/createTask",
                        data={"clientKey": "2430681487daa93cd7a0490504f54af5", "task": {
                            "type": "RecaptchaV3TaskProxyless",
                            "websiteURL": websiteURL,
                            "websiteKey": websiteKey,
                            "pageAction": pageAction
                        }})
    return res.text


if __name__ == '__main__':
    app.run()
