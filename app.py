from flask import Flask, request, render_template
import requests
import json
import logging
app = Flask(__name__)
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
    logging.info("返回.{}".format(str(res)))

    return json.dumps({"code": 1, "msg": "success"})

if __name__ == '__main__':
    app.run()


