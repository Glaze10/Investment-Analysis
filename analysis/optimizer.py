"""handle all optimization function"""

import numpy as np
from scipy.optimize import minimize
from config.settings import RISK_FREE_RATE, TRADING_DAYS

class PortfolioOptimizer:
    '''optimize portfolio weight'''

    def __init__(self, daily_returns, risk_free_rate = RISK_FREE_RATE):
        self.daily_returns = daily_returns
        self.risk_free_rate = risk_free_rate
        self.mean_returns = daily_returns.mean() * TRADING_DAYS
        self.cov_matrix = daily_returns.cov() * TRADING_DAYS
        self.n_assets = len(daily_returns.columns)

    def portfolio_stats(self, weights):
        '''calculate return, volatility, and Sharpe'''

        portfolio_return = np.dot(weights, self.mean_returns)
        portfolio_std = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        sharpe_ratio = (portfolio_return - self.risk_free_rate) / portfolio_std
        return portfolio_return, portfolio_std, sharpe_ratio

    def _negative_sharpe(self, weights):
        '''calculate negative sharpe'''

        return -self.portfolio_stats(weights)[2]

    def optimize_sharpe(self):
        '''optimize for for max sharpe ratio'''

        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        bounds = tuple((0, 1) for _ in range(self.n_assets))
        initial_weights = np.array([1 / self.n_assets] * self.n_assets)

        result = minimize(
            self._negative_sharpe,
            initial_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        return self._build_results(result.x, 'Sharpe Ratio Optimization', result.success)

    def equal_weight(self):
        '''optimize for equal weights'''

        weights = np.array([1 / self.n_assets] * self.n_assets)

        return self._build_results(weights, "Equal Weight", True)

    def _build_results(self, weights, method_name, success):
        '''build results dict'''

        pf_return, pf_vol, pf_sharpe = self.portfolio_stats(weights)

        return {
            'method': method_name,
            'weights': dict(zip(self.daily_returns.columns, weights)),
            'expected_annual_return': pf_return,
            'annual_volatility': pf_vol,
            'sharpe_ratio': pf_sharpe,
            'optimization_success': success
        }
