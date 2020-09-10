# coding: utf-8

from flask import Flask, render_template, request, jsonify

import urllib3

data_dic={}

app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_object(Config)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/data_request', methods=['GET', 'POST'])
def data_request():
    if request.method == 'GET':
        data_interface_ip=request.args.get('ip')
        str_login_url=f'http://{data_interface_ip}:12122/login'

        #通过urllib3爬取网络资源
        http = urllib3.PoolManager()
        response = http.request('GET', str_login_url)

        #将数据存放在data
        if response.status == 200:
            data_dic['login_text']=response.data.decode()[1:7]
            data_dic['login_status']=response.status
        else:
            data_dic['login_status']=response.status
        print(data_dic)
    return 'data'

@app.route('/data_response', methods=['GET', 'POST'])
def data_response():
    return jsonify(data_dic)



app.run()