from flask import Flask, request, render_template
import requests
import json
import logging
app = Flask(__name__)
# 设置log
handler = logging.FileHandler('./logs/flask.log', encoding='UTF-8')
handler.setLevel(logging.INFO)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)
@app.route('/')
def static_views():
    return render_template('ii.html')


@app.route('/gettoken', methods=['GET', 'POST'])
def gettoken():
    # if request.META.get("HTTP_X_FORWARDED_FOR", None):
    #     ip = request.META['HTTP_X_FORWARDED_FOR']
    # else:
    #     ip = request.META.get("REMOTE_ADDR", "")
    ip = request.remote_addr
    data = request.values
    token = data.get("token", "")
    vaify_url = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": "6LefJa0UAAAAANhH9-OH7A-o1BoWNUQMZ0x82L7P", "response": token,
                              "remoteip": ip}

    app.logger.info(str(data))
    res = requests.post(url=vaify_url, data=data)
    app.logger.info(str(res))
    return json.dumps({"code": 1, "msg": "success"})

if __name__ == '__main__':
    app.run()


