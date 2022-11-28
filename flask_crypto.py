
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

        p = []
        with open("/root/crypto_pre/res_kong.csv", 'r', encoding="UTF-8") as fr:
            reader = csv.reader(fr)
            for index, line in enumerate(reader):
                if index == 0:
                    continue
                p.append(line)
        res_data = pd.DataFrame(p)
        res_data['date'] = res_data.iloc[:,0]
        res_data['value'] = res_data.iloc[:,1]
        res_data['status'] = res_data.iloc[:,2]
        res_data['up_date'] = res_data.iloc[:,3]

        res_data['date'] = pd.to_datetime(res_data['date'])
        res_data['up_date'] = pd.to_datetime(res_data['up_date'])
        
        value = res_data[res_data.date==pd.to_datetime(date)]['value'][0]

        if res_data['status'][0]==2:
            r_value = 0
        elif res_data['status'][0]==0:
            if (pd.to_datetime(res_data['date'][0]) - pd.to_datetime(res_data['up_date'][0]) ).days >= 6:
                r_value = value
            else:
                r_value = 0 
        else:
            r_value = value

        res_dict = {'value':r_value}
        
        ans_str = json.dumps(res_dict)
    else:
        p = []
        with open("/root/crypto_pre/res_duo.csv", 'r', encoding="UTF-8") as fr:
            reader = csv.reader(fr)
            for index, line in enumerate(reader):
                if index == 0:
                    continue
                p.append(line)
        res_data = pd.DataFrame(p)
        res_data['date'] = res_data.iloc[:,0]
        res_data['value_1'] = res_data.iloc[:,1]
        res_data['value_2'] = res_data.iloc[:,2]
        res_data['value_3'] = res_data.iloc[:,3]
        res_data['status'] = res_data.iloc[:,4]
        res_data['up_date'] = res_data.iloc[:,5]


        res_data['date'] = pd.to_datetime(res_data['date'])
        res_data['up_date'] = pd.to_datetime(res_data['up_date'])
        
        if res_data['status'][0]==2:
            r_value_1 = 0
            r_value_2 = 0
            r_value_3 = 9999999999
        elif res_data['status'][0]==0:
            if (pd.to_datetime(res_data['date'][0]) - pd.to_datetime(res_data['up_date'][0]) ).days >= 6:
                r_value_1 = res_data['value_1'][0]
                r_value_2 = res_data['value_2'][0]
                r_value_3 = res_data['value_3'][0]
            else:
                r_value_1 = 0
                r_value_2 = 0
                r_value_3 = 9999999999
        else:
            r_value_1 = res_data['value_1'][0]
            r_value_2 = res_data['value_2'][0]
            r_value_3 = res_data['value_3'][0]

        res_dict = {'value_1':r_value_1,'value_2':r_value_2,'value_3':r_value_3}
        
        ans_str = json.dumps(res_dict)
    return ans_str

if __name__ == '__main__':
    app.run("8.219.61.64", port=80)


