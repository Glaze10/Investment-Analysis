'''config settings for PF analysis'''

import pandas as pd

TICKERS = ['MSGS', 'NKE', 'DIS', 'SPOT', 'IBM']
START_DATE = '2020-1-1'
END_DATE = '2024-12-31'

RISK_FREE_RATE = 0.02
TRADING_DAYS = 252

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
