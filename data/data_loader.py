"""File which handles data loading"""

import yfinance as yf
from config.settings import TICKERS, START_DATE, END_DATE

class DataLoader:
    """Data downloading and processing."""

    def __init__(self, tickers=None, start_date=None, end_date=None):
        self.tickers = tickers or TICKERS
        self.start_date = start_date or START_DATE
        self.end_date = end_date or END_DATE

        self.hist_data = None
        self.daily_returns = None
        self.cumulative_returns = None

    def get_data(self):
        """Download historical price data."""
        self.hist_data = yf.download(
            self.tickers,
            start=self.start_date,
            end=self.end_date,
        )["Close"]

        return self.hist_data

    def calculate_returns(self):
        """Calculate daily and cumulative returns."""
        if self.hist_data is None:
            raise ValueError("Historical data not loaded. Call get_data() first.")

        self.daily_returns = self.hist_data.pct_change().dropna()
        self.cumulative_returns = (1 + self.daily_returns).cumprod() - 1

        return self.daily_returns, self.cumulative_returns

    def get_all_data(self):
        """Fetch and process all data."""
        self.get_data()
        self.calculate_returns()

        return {
            "historical": self.hist_data,
            "daily_returns": self.daily_returns,
            "cumulative_returns": self.cumulative_returns,
        }
