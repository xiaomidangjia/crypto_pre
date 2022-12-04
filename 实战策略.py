'''backtest
start: 2022-08-29 00:00:00
end: 2022-11-29 00:00:00
period: 1h
basePeriod: 15m
'''

import urllib
from urllib import request
import requests
import base64
import json
#每天定时监控下单
type_id = 'kong'
date_all = ['2022-10-01']
while True:
    Sleep(1000)
    date = str(_D())[0:10]
    # 加上一个开关，如果已经调用api了，当天就不再调用了
    date_all.append(date)
    date_all = date_all[-2:]
    if type_id == 'kong' and date_all[0] != date and date_all[1]==date:
        #调用接口  
        test_data_1 = {
            "type":"kong",
            "date": date
            }
        req_url = "http://8.219.61.64:80/crypto_pre"
        r = requests.post(req_url, data=test_data_1)
        api_res = r.content.decode('utf-8')
        api_res = json.loads(api_res)
        api_res = api_res['value']
        if api_res == 'error':
            Log('数据没有跑完')
            Sleep(23.5*60*60*1000)
        elif api_res == 9999999999999:
            Log('不需要下单')
            Sleep(23.5*60*60*1000)
        else:
            # 获得实时交易数据，进行下单判断
            ticker = _C(exchange.GetTicker)
            btc_price = ticker['Last']
            if btc_price < api_res:
                Log('不需要下单')
                Sleep(23.5*60*60*1000)
            else:
                Sleep(1000)
                order_id_all = []
                #查看订单状态，如果没有就继续下单
                orders = exchange.GetOrders()
                while len(orders) == 0:
                    #切换交易对,设置永续合约，加杠杆
                    exchange.IO("currency", "BTC_USDT")
                    exchange.SetContractType("swap")
                    #exchange.SetMarginLevel(10)
                    exchange.SetDirection("sell")
                    #合约卖出
                    sell_num = int(1000/(btc_price*0.01))
                    sell_id = exchange.Sell(-1,sell_num)
                    order_id_all.append(sell_id)
                #对订单是否要进行平仓进行判断
                while len(order_id_all)==1:
                    #目前的btc价格
                    Sleep(1000)
                    now_ticker = _C(exchange.GetTicker)
                    now_btc_price = now_ticker['Last'] 
                    bod = (now_btc_price - btc_price)/ btc_price
                    if bod >= 0.07:
                        Log('买入平空仓')
                        orders_have = exchange.GetOrders()
                        while len(orders_have) == 1:
                            exchange.SetDirection("closesell")
                            buy_id = exchange.Buy(-1,sell_num)
                            #删除该订单
                            del order_id_all[0] 
                        #如果没有订单了，退出监控
                    elif bod < -0.03:
                        Sleep(3*60*1000)
                        while len(order_id_all)==1:
                            Sleep(1000)
                            next_ticker = _C(exchange.GetTicker)
                            next_btc_price = now_ticker['Last'] 
                            next_bod = (next_btc_price - btc_price)/ btc_price
                            if next_bod <= -0.06 or next_bod >= -0.03:
                                Log('买入平空仓')
                                orders_have = exchange.GetOrders()
                                while len(orders_have) == 1:
                                    exchange.SetDirection("closesell")
                                    buy_id = exchange.Buy(-1,sell_num)
                                    del order_id_all[0]
                            else:
                                continue
                    else:
                        continue
        
    elif type_id == 'duo' and date_all[0] != date and date_all[1]==date:
        #调用接口  
        test_data_1 = {
            "type":"duo",
            "date": date
            }
        req_url = "http://8.219.61.64:80/crypto_pre"
        r = requests.post(req_url, data=test_data_1)
        api_res = r.content.decode('utf-8')
        api_res = json.loads(api_res)
        api_value1 = api_res['value_1']
        api_value2 = api_res['value_2']
        api_value3 = api_res['value_3']
        if api_value1 == 0 and api_value2 == 9999999999999 and api_value3 == 9999999999999:
            Log('不需要下单')
            Sleep(23.5*60*60*1000)
        else:
            # 获得实时交易数据，进行下单判断
            ticker = _C(exchange.GetTicker)
            btc_price = ticker['Last']
            if btc_price < api_value1 or (btc_price < api_value2 and btc_price > api_value3):
                Sleep(1000)
                order_id_all = []
                #查看订单状态，如果没有就继续下单
                orders = exchange.GetOrders()
                while len(orders) == 0:
                    #切换交易对,设置永续合约，加杠杆
                    exchange.IO("currency", "BTC_USDT")
                    exchange.SetContractType("swap")
                    #exchange.SetMarginLevel(10)
                    exchange.SetDirection("buy")
                    #合约买入
                    buy_num = int(100*10/(btc_price*0.01))
                    buy_id = exchange.Buy(-1,buy_num)
                    order_id_all.append(buy_id)
                #对订单是否要进行平仓进行判断
                while len(order_id_all)==1:
                    Sleep(1000)
                    #目前的btc价格
                    now_ticker = _C(exchange.GetTicker)
                    now_btc_price = now_ticker['Last'] 
                    bod = (now_btc_price - btc_price)/ btc_price
                    if bod <= -0.05:
                        Log('卖出平多仓')
                        orders_have = exchange.GetOrders()
                        while len(orders_have) == 1:
                            exchange.SetDirection("closebuy")
                            sell_id = exchange.Sell(-1,buy_num)
                            #删除该订单
                            del order_id_all[0] 
                        #如果没有订单了，退出监控
                    elif bod > 0.03:
                        Sleep(3*60*1000)
                        while len(order_id_all)==1:
                            Sleep(1000)
                            next_ticker = _C(exchange.GetTicker)
                            next_btc_price = now_ticker['Last'] 
                            next_bod = (next_btc_price - btc_price)/ btc_price
                            if next_bod >= 0.09 or next_bod <= 0.03:
                                Log('卖出平多仓')
                                orders_have = exchange.GetOrders()
                                while len(orders_have) == 1:
                                    exchange.SetDirection("closebuy")
                                    sell_id = exchange.Sell(-1,buy_num)
                                    del order_id_all[0]
                            else:
                                continue
                    else:
                        continue
            else:
                Log('不需要下单')
                Sleep(23.5*60*60*1000)
    else:
        continue
