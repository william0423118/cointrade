# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 01:48:26 2017

@author: Dan brother
"""
import ccxt
#bitso=getattr (ccxt, 'bitso') ()
id = 'bitso'
bitso = eval ('ccxt.%s ()' % id)
gdax_info=bitso.fetch_ticker('BTC/USD')