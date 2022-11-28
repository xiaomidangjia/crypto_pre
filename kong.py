
# coding: utf-8

# In[1]:

import json
import requests
import pandas as pd
import time
import numpy as np
import os
import re
from tqdm import tqdm
import datetime

url_address = [ 'https://api.glassnode.com/v1/metrics/market/price_usd_ohlc']
url_name = ['k_fold']
# insert your API key here
API_KEY = '26BLocpWTcSU7sgqDdKzMHMpJDm'
data_list = []
for num in range(len(url_name)):
    print(num)
    addr = url_address[num]
    name = url_name[num]
    # make API request
    res_addr = requests.get(addr,params={'a': 'BTC', 'api_key': API_KEY})
    # convert to pandas dataframe
    ins = pd.read_json(res_addr.text, convert_dates=['t'])
    #ins.to_csv('test.csv')
    #print(ins['o'])
    ins['date'] =  ins['t']
    ins['value'] =  ins['o']
    ins = ins[['date','value']]
    data_list.append(ins)
result_data = data_list[0][['date']]
for i in range(len(data_list)):
    df = data_list[i]
    result_data = result_data.merge(df,how='left',on='date')
#last_data = result_data[(result_data.date>='2016-01-01') & (result_data.date<='2020-01-01')]
last_data = result_data[(result_data.date>='2021-11-30')]
last_data = last_data.sort_values(by=['date'])
last_data = last_data.reset_index(drop=True)
#print(type(last_data))
date = []
open_p = []
close_p = []
high_p = []
low_p = []
for i in range(len(last_data)):
    date.append(last_data['date'][i])
    open_p.append(last_data['value'][i]['o'])
    close_p.append(last_data['value'][i]['c'])
    high_p.append(last_data['value'][i]['h'])
    low_p.append(last_data['value'][i]['l'])
res_data = pd.DataFrame({'date':date,'open':open_p,'close':close_p,'high':high_p,'low':low_p})
# 价格不能在最低点
# 价格大于过去两天
# 价格超过5日均线值

low_price = np.min(res_data['close']) * 1.05
two_max = np.max(res_data['close'][-2:])
mean_5_day = 0.97 * np.mean(res_data['close'][-5:])

value_1 = np.max([low_price,two_max])
value_2 = np.max([low_price,mean_5_day])

last_value = np.min([value_1,value_2])
date_value = res_data['date'][len(res_data)-1]

judge_res = pd.DataFrame({'date':date_value,'value':last_value},index=[0])
judge_res.to_csv('res_kong.csv')



