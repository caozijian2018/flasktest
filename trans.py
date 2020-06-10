import json
import urllib.request
import urllib.parse

# google翻译
from googletrans import Translator
translator = Translator()
f = open('./before.json', 'r+')
str_json = f.read()
# temp = str_json.replace("'", '"') # 将 单引号 替换为 双引号
temp = json.loads(str_json)
# print(temp)
for key in temp:
    result = translator.translate(temp[key], dest='fi').text
    print(result)
    temp[key] = result
    # print(key, temp[key])

print(temp)

try:
    f = open('result.json', 'w')
    print("打开文件成功")
    f.write(json.dumps(temp))
    f.close()
except OSError:
    print("打开文件失败")




# txt = input('请输入需要翻译的内容：')
# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
# data = {'from': 'AUTO', 'to': 'ar', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '1500092479607',
#         'sign': 'c98235a85b213d482b8e65f6b1065e26', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
#         'action': 'FY_BY_CL1CKBUTTON', 'typoResult': 'true', 'i': txt}

# data = urllib.parse.urlencode(data).encode('utf-8')
# wy = urllib.request.urlopen(url, data)
# html = wy.read().decode('utf-8')
# ta = json.loads(html)
# print(ta['translateResult'][0][0]['tgt'])
# print(ta)
