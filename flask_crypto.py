
# coding: utf-8

import json
import base64
from flask import Flask, request
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route("/crypto_pre", methods=['post'])
def crypto_pre():
    date = request.form.get('date')
    type_ = request.form.get('type')

    if type_ == 'kong':
        res_data = pd.read_csv('res_kong.csv')
        res_data['date'] = pd.to_datetime(res_data['date'])
        
        value = res_data[res_data.date==pd.to_datetime(date)]['value'][0]
        
        res_dict = {'value':value}
        
        ans_str = json.dumps(res_dict)
    else:
        res_data = pd.read_csv('res_duo.csv')
        res_data['date'] = pd.to_datetime(res_data['date'])
        
        value = res_data[res_data.date==pd.to_datetime(date)]['value'][0]
        
        res_dict = {'value':value}
        
        ans_str = json.dumps(res_dict)
    return ans_str

if __name__ == '__main__':
    app.run("172.23.198.69", port=80)


