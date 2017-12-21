#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:50:15 2017

@author: DanWang
"""
import ccxt
bithumb1 = ccxt.bithumb ()
bithumb1.apiKey = '8c53afc7449b4bd8c4a9654aa0a2480b'
bithumb1.secret = '5d6c3ddee73deefc46d93fb3774e73f7'
balance=bithumb1.fetch_balance ()
btc=balance['info']['data']['total_btc']
print(btc)
bithumb1.create_market_buy_order('LTC/KRW', 1, {'trading_agreement': 'agree'})
#bithumb1.fetchMyTrades (symbol = undefined, since = undefined, limit = undefined,params = {})

