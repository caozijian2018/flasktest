from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)


# # 得到token
# @app.route('/gettoken', methods=['GET', 'POST'])
# def gettoken():
#     # req = request.json
#     # print(req)
#     # websiteURL = req['websiteURL']
#     # websiteKey = req['websiteKey']
#     # pageAction = req.get('pageAction', None)
#     # res = requests.post("http://api.anti-captcha.com/createTask",
#     #                     data={"clientKey": "2430681487daa93cd7a0490504f54af5", "task": {
#     #                         "type": "RecaptchaV3TaskProxyless",
#     #                         "websiteURL": websiteURL,
#     #                         "websiteKey": websiteKey,
#     #                         "pageAction": pageAction
#     #                     }})
#     # return res.text
#     secret = "2430681487daa93cd7a0490504f54af5"
#     url = "https://www.google.com/recaptcha/api/siteverify"
#     response = request.GET.get("g-recaptcha-response")
#
#     if request.META.get("HTTP_X_FORWARDED_FOR", None):
#         ip = request.META['HTTP_X_FORWARDED_FOR']
#     else:
#         ip = request.META.get("REMOTE_ADDR", "")
#
#     resp = requests.post(url=url, data={"secret": secret, "response": response, "remoteip": ip}).json()
#     return resp

@app.route('/')
def static_views():
    return render_template('ii.html')


@app.route('/gettoken', methods=['GET', 'POST'])
def gettoken():
    data = request.json
    token = data.get("token", "")
    key = data.get("key", "")
    vaify_url = "https://www.google.com/recaptcha/api/siteverify"
    res = requests.post(vaify_url,
                        data={"secret": "6LefJa0UAAAAANhH9-OH7A-o1BoWNUQMZ0x82L7P", "response": token,
                              "remoteip": "123"})
    res
    return json.dumps({"code": 1, "msg": "success"})


if __name__ == '__main__':
    app.run()
