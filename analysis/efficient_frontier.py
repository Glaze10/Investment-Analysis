"""Handle efficient frontier and tangency portfolio"""

import numpy as np

def compute_portfolio_performance(weights, mean_returns, cov_matrix):
    """Compute portfolio performance"""

    returns = np.sum(mean_returns * weights) * 252
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = returns / volatility
    return volatility, returns, sharpe_ratio


def efficient_frontier(mean_returns, cov_matrix, iterations=5000):
    """Calculate efficient frontier"""

    results = np.zeros((3, iterations))
    weight_records = []

    num_assets = len(mean_returns)

    for i in range(iterations):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        weight_records.append(weights)

        vol, ret, sharpe = compute_portfolio_performance(weights, mean_returns, cov_matrix)

        results[0][i] = vol
        results[1][i] = ret
        results[2][i] = sharpe

    return results, weight_records

