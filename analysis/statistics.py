"""Handle stock statistics"""

import pandas as pd
import numpy as np
from config.settings import RISK_FREE_RATE, TRADING_DAYS

class StockStatistics:
    '''calculate individual stock stats'''

    def __init__(self, daily_returns, risk_free_rate = RISK_FREE_RATE):

        self.daily_returns = daily_returns
        self.risk_free_rate = risk_free_rate

    def calculate_stats(self):
        '''annual returns, volatility, and sharpe ratio'''

        annual_returns = self.daily_returns.mean() * TRADING_DAYS
        annual_vol = self.daily_returns.std() * np.sqrt(TRADING_DAYS)
        sharpe_ratio = (annual_returns - self.risk_free_rate) / annual_vol

        stats_df = pd.DataFrame({
            'Annual Return' : annual_returns,
            'Annual Volatility' : annual_vol,
            'Sharpe Ratio' : sharpe_ratio
        })

        return stats_df
