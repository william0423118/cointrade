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
#market1 = bitso.load_markets ()
#print(market1)
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
    benifit=(-gdax_price+bithumb_price)/gdax_price
    spread_LTC=(gLTC-bLTC)/gLTC
    spread_ETH=(gETH-bETH)/gETH
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
    stampLTC=bitstamp.fetch_ticker('LTC/USD')['bid']
    spread2=(stampLTC-bLTC)/stampLTC
    stampETH=bitstamp.fetch_ticker('ETH/USD')['bid']
    spreadETH=(stampETH-bETH)/stampETH
    #-----------------------------
    BTCash_gdax=gdax.fetch_ticker('BCH/USD')['bid']
    BTCash_humb=bithumb.fetch_ticker('BCH/KRW')['bid']/rate
    BTCash_stamp=bitstamp.fetch_ticker('BCH/USD')['bid']
    spread_g=(-BTCash_gdax+BTCash_humb)/BTCash_gdax
    spread_s=(-BTCash_stamp+BTCash_humb)/BTCash_stamp
    
    print('GDAX_BTC:',gdax_price,'Bithumb_BTC:',bithumb_price)
    print('benifit:',benifit)    
    print('LTC_gdax',gLTC,'LTC_humb:',bLTC)
    print('ETH_gdax',gETH,'ETH_humb:',bETH)
    print('spread_LTC:',spread_LTC,'spread_ETH:',spread_ETH)
    print('_______________________')    
    print('humbXRP:',humbXRP,'StampXRP:',stampXRP)
    print('spread:',spread)
    print('stampsLTC',stampLTC,'LTC_humb:',bLTC)
    print('Spread_LTC(stamp)',spread2)
    print('Spread_ETH(stamp)',spreadETH)
    print('_______________________')
    print('BCH:','gdax:',BTCash_gdax,'stamp:',BTCash_stamp,'humb:',BTCash_humb)
    print('spread_gdax:',spread_g,'spread_stamp:',spread_s)
    print('_______________________')
    time.sleep(5)
