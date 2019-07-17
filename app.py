from flask import Flask, request, render_template, make_response, jsonify
import requests
import json
import logging
# import pymongo
app = Flask(__name__)
# MONGO_CLI = pymongo.MongoClient(host='127.0.0.1', port='27017')
logging.basicConfig(filename="./logs/test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
# 设置log
@app.route('/')
def static_views():
    return render_template('ii.html')


@app.route('/gettoken', methods=['GET', 'POST'])
def gettoken():
    ip = request.remote_addr
    data = request.values
    token = data.get("token", "")
    vaify_url = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": "6LefJa0UAAAAANhH9-OH7A-o1BoWNUQMZ0x82L7P", "response": token,
                              "remoteip": ip}

    logging.info("data.{}".format(str(data)))
    res = requests.post(url=vaify_url, data=data).json()
    # root:INFO:返回.{'success': True, 'score': 0.9, 'hostname': 'static.humorboom.com', 'challenge_ts': '2019-07-16T09:16:04Z', 'action': 'homepage'}
    logging.info("返回.{}".format(str(res)))

    return jsonify(res)


@app.route('/getantitoken', methods=['POST'])
def getantitoken():
    url = "http://api.anti-captcha.com/createTask"
    data = {"clientKey": "2430681487daa93cd7a0490504f54af5", "task": {
        "type": "RecaptchaV3TaskProxyless",
        "websiteURL": "http://static.humorboom.com/testv3/index.html",
        "websiteKey": "6LefJa0UAAAAAOB06AdDI0L7krmqGle-gdob4WDw",
        "minScore": 0.3,
        "pageAction": "homepage"
    }}
    res = requests.post(url=url, data=data).json()
    logging.info("ANTItoken{}".format(str(res)))


@app.route('/get2captchaid', methods=['POST'])
def get2captchaid():
    data = request.values
    min_score = data.get('min_score', '0.3')
    pageurl = data.get('pageurl', '')

    url = "http://2captcha.com/in.php"
    data = {"key": "46f989bbda665e16b138119bd15c140e",
            "method": "userrecaptcha",
            "googlekey": "6LefJa0UAAAAAOB06AdDI0L7krmqGle-gdob4WDw",
            "pageurl": "http://static.humorboom.com/testv3/index.html",
            "version": "v3",
            "action": 'verify',
            "min_score": min_score
            }
    res = requests.post(url=url, data=data).text.split("|")[1]
    logging.info("ANTItoken{}".format(str(res)))
    return jsonify(res)

@app.route('/get2captcharesult', methods=['POST'])
def get2captcharesult():
    data = request.values
    taskid = data.get('taskid', '')
    url = "http://2captcha.com/res.php"
    data = {
        "key": "46f989bbda665e16b138119bd15c140e",
        "action": 'get',
        "taskinfo": 1,
        "json": 1,
        "id": taskid
    }
    res = requests.get(url=url, data=data).json()
    logging.info("ANTItoken{}".format(str(res)))
    return jsonify(res)


if __name__ == '__main__':
    app.run()


