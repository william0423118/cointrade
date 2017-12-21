# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import ccxt
import time
gdax = getattr (ccxt, 'gdax') ()
bithumb = getattr (ccxt, 'bithumb') ()
markets = bithumb.load_markets ()
markets = bithumb.load_markets ()

while 1:
    gdax_info=gdax.fetch_ticker('BTC/USD')
    bithumb_info=bithumb.fetch_ticker('BTC/KRW')
    rate=1.0/0.00092
    gdax_price=gdax_info['bid']
    bithumb_price=bithumb_info['bid']/rate
    gLTC=gdax.fetch_ticker('LTC/USD')['bid']
    gETH=gdax.fetch_ticker('ETH/USD')['bid']
    bLTC=bithumb.fetch_ticker('LTC/KRW')['bid']/rate
    bETH=bithumb.fetch_ticker('ETH/KRW')['bid']/rate
    print('GDAX_BTC:',gdax_price,'Bithumb_BTC:',bithumb_price)
    print('LTC',gLTC,bLTC,'ETH',gETH,bETH)
    benifit=(-gdax_price+bithumb_price)/gdax_price
    print('benifit:',benifit)
    spread_LTC=(gLTC-bLTC)/bLTC
    spread_ETH=(gETH-bETH)/bETH
    print('spread_LTC:',spread_LTC,'spread_ETH:',spread_ETH)
    if spread_LTC>spread_ETH:
        choose='spread_LTC'
        spread=spread_LTC
    else:
        choose='spread_ETH'
        spread=spread_ETH
    final=benifit+spread
    id = 'bitstamp'
    bitstamp = eval ('ccxt.%s ()' % id)
    humbXRP=bithumb.fetch_ticker('XRP/KRW')['bid']/rate
    stampXRP=bitstamp.fetch_ticker('XRP/USD')['bid']
    spread=(-stampXRP+humbXRP)/stampXRP
    print('humbXRP:',humbXRP,'StampXRP:',stampXRP)
    print('spread:',spread)
    print('final benefit:',final)
    print('_______________________')
    time.sleep(5)