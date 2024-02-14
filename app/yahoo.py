import yahoo_fin.stock_info as si
import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def get_symbols()->dict:
    '''
        We'll fetch all the symbols from nasdaq, nyse, amex and organize them into all_symbols
    '''
    all_symbols = {} ### key: CQL_Symbol, value: nasdaq_symbol, nyse_symbol, amex_symbol
    pd_nasdaq_tickers = si.tickers_other("nasdaq")[['ACT Symbol', 'CQS Symbol', 'NASDAQ Symbol']]
    pd_nyse_tickers   = si.tickers_other("nyse")[['ACT Symbol', 'CQS Symbol', 'NASDAQ Symbol']]
    pd_amex_tickers   = si.tickers_other("amex")[['ACT Symbol', 'CQS Symbol', 'NASDAQ Symbol']]

    ### Store nasdaq symbol
    for i in pd_nasdaq_tickers.index:
        data = pd_nasdaq_tickers.loc[i]
        cqs_symbol = data['CQS Symbol']
        nasdaq_symbol = data['ACT Symbol']
        symbol_dict = all_symbols.setdefault(cqs_symbol, {})
        symbol_dict['nasdaq_symbol'] = nasdaq_symbol

    ### Store nyse symbol
    for i in pd_nyse_tickers.index:
        data = pd_nyse_tickers.loc[i]
        cqs_symbol = data['CQS Symbol']
        nyse_symbol = data['ACT Symbol']
        symbol_dict = all_symbols.setdefault(cqs_symbol, {})
        symbol_dict['nyse_symbol'] = nyse_symbol

    ### Store amex symbol
    for i in pd_amex_tickers.index:
        data = pd_nyse_tickers.loc[i]
        cqs_symbol = data['CQS Symbol']
        amex_symbol = data['ACT Symbol']
        symbol_dict = all_symbols.setdefault(cqs_symbol, {})
        symbol_dict['amex_symbol'] = amex_symbol
    return all_symbols

def get_ticker_detail(ticker_symbol: str)->dict:
    ticker = yf.Ticker(ticker_symbol)
    tickerInfo = ticker.info
    industry = tickerInfo.get('industry')
    ipoDate = tickerInfo.get('firstTradeDateEpochUtc', None)
    if ipoDate:
        ipoDate = datetime.utcfromtimestamp(ipoDate / 1000).strftime('%Y-%m-%d')
    return {
        'industry': industry,
        'ipoData': ipoDate
    }