
# coding: utf-8

import json
import base64
from flask import Flask, request
import numpy as np
import pandas as pd
import csv

app = Flask(__name__)


@app.route("/crypto_pre", methods=['post'])
def crypto_pre():
    date = request.form.get('date')
    type_ = request.form.get('type')
    crypto = request.form.get('crypto')

    if type_ == 'kong' and crypto == 'btc':

        p = []
        with open("/root/crypto_pre/res_btc_kong.csv", 'r', encoding="UTF-8") as fr:
            reader = csv.reader(fr)
            for index, line in enumerate(reader):
                if index == 0:
                    continue
                p.append(line)
        res_data = pd.DataFrame(p)
        res_data['date'] = res_data.iloc[:,1]
        res_data['status'] = res_data.iloc[:,2]
        res_data['today_price'] = res_data.iloc[:,3]
        res_data['up_close_date'] = res_data.iloc[:,7]
        res_data['up_start_price'] = res_data.iloc[:,8]

        res_data['date'] = pd.to_datetime(res_data['date'])

        res_data = res_data[res_data.date==pd.to_datetime(date)]
        if len(res_data) == 0:
            r_value = 'error'
            today_price = 0
            up_close_date = 0
            up_start_price = 0
        else:
            r_value = res_data['status'][0]
            today_price = res_data['today_price'][0]
            up_close_date = res_data['up_close_date'][0]
            up_start_price = res_data['up_start_price'][0]

        res_dict = {'value':r_value,'today_price':today_price,'up_close_date':up_close_date,'up_start_price':up_start_price}

        ans_str = json.dumps(res_dict)
    elif type_ == 'duo' and crypto == 'btc':
        p = []
        with open("/root/crypto_pre/res_btc_duo.csv", 'r', encoding="UTF-8") as fr:
            reader = csv.reader(fr)
            for index, line in enumerate(reader):
                if index == 0:
                    continue
                p.append(line)
        res_data = pd.DataFrame(p)
        res_data['date'] = res_data.iloc[:,1]
        res_data['status'] = res_data.iloc[:,2]
        res_data['today_price'] = res_data.iloc[:,3]
        res_data['up_close_date'] = res_data.iloc[:,7]
        res_data['up_start_price'] = res_data.iloc[:,8]

        res_data['date'] = pd.to_datetime(res_data['date'])
        #res_data['up_date'] = pd.to_datetime(res_data['up_date'])
        res_data = res_data[res_data.date==pd.to_datetime(date)]

        if len(res_data) == 0:
            r_value = 'error'
            today_price = 0
            up_close_date = 0
            up_start_price = 0
        else:   
            r_value = res_data['status'][0]
            today_price = res_data['today_price'][0]
            up_close_date = res_data['up_close_date'][0]
            up_start_price = res_data['up_start_price'][0]

        res_dict = {'value':r_value,'today_price':today_price,'up_close_date':up_close_date,'up_start_price':up_start_price}

        ans_str = json.dumps(res_dict)
    elif type_ == 'kong' and crypto == 'eth':

        p = []
        with open("/root/crypto_pre/res_eth_kong.csv", 'r', encoding="UTF-8") as fr:
            reader = csv.reader(fr)
            for index, line in enumerate(reader):
                if index == 0:
                    continue
                p.append(line)
        res_data = pd.DataFrame(p)
        res_data['date'] = res_data.iloc[:,1]
        res_data['status'] = res_data.iloc[:,2]
        res_data['today_price'] = res_data.iloc[:,3]
        res_data['up_close_date'] = res_data.iloc[:,7]
        res_data['up_start_price'] = res_data.iloc[:,8]

        res_data['date'] = pd.to_datetime(res_data['date'])

        res_data = res_data[res_data.date==pd.to_datetime(date)]
        if len(res_data) == 0:
            r_value = 'error'
            today_price = 0
            up_close_date = 0
            up_start_price = 0
        else:
            r_value = res_data['status'][0]
            today_price = res_data['today_price'][0]
            up_close_date = res_data['up_close_date'][0]
            up_start_price = res_data['up_start_price'][0]

        res_dict = {'value':r_value,'today_price':today_price,'up_close_date':up_close_date,'up_start_price':up_start_price}

        ans_str = json.dumps(res_dict)
    else:
        p = []
        with open("/root/crypto_pre/res_eth_duo.csv", 'r', encoding="UTF-8") as fr:
            reader = csv.reader(fr)
            for index, line in enumerate(reader):
                if index == 0:
                    continue
                p.append(line)
        res_data = pd.DataFrame(p)
        res_data['date'] = res_data.iloc[:,1]
        res_data['status'] = res_data.iloc[:,2]
        res_data['today_price'] = res_data.iloc[:,3]
        res_data['up_close_date'] = res_data.iloc[:,7]
        res_data['up_start_price'] = res_data.iloc[:,8]

        res_data['date'] = pd.to_datetime(res_data['date'])
        #res_data['up_date'] = pd.to_datetime(res_data['up_date'])
        res_data = res_data[res_data.date==pd.to_datetime(date)]

        if len(res_data) == 0:
            r_value = 'error'
            today_price = 0
            up_close_date = 0
            up_start_price = 0
        else:   
            r_value = res_data['status'][0]
            today_price = res_data['today_price'][0]
            up_close_date = res_data['up_close_date'][0]
            up_start_price = res_data['up_start_price'][0]

        res_dict = {'value':r_value,'today_price':today_price,'up_close_date':up_close_date,'up_start_price':up_start_price}

        ans_str = json.dumps(res_dict)
    return ans_str

if __name__ == '__main__':
    app.run("0.0.0.0", port=80)


