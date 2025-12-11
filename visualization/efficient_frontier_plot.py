"""Efficient Frontier plotting functionality"""

import numpy as np
import matplotlib.pyplot as plt

def compute_portfolio_stats(weights, mean_returns, cov_matrix):
    """Return volatility, return, sharpe_ratio"""

    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_vol
    return portfolio_vol, portfolio_return, sharpe_ratio


def generate_random_portfolios(mean_returns, cov_matrix, n_portfolios=5000):
    """Generate random portfolios for frontier scatter"""

    n_assets = len(mean_returns)

    results = np.zeros((3, n_portfolios))
    weight_list = []

    for i in range(n_portfolios):
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)

        vol, ret, sharpe = compute_portfolio_stats(weights, mean_returns, cov_matrix)

        results[0, i] = vol
        results[1, i] = ret
        results[2, i] = sharpe
        weight_list.append(weights)

    return results, weight_list


def plot_efficient_frontier(mean_returns, cov_matrix, tickers):
    """Plots:
        - Random portfolios
        - Efficient frontier curve
        - Max Sharpe portfolio
        - Min Vol portfolio
        - Individual stock points
    """

    # Random portfolios
    results, _ = generate_random_portfolios(mean_returns, cov_matrix)

    vol_arr = results[0]
    ret_arr = results[1]
    sharpe_arr = results[2]

    # Identify special portfolios
    max_sharpe_idx = np.argmax(sharpe_arr)
    min_vol_idx = np.argmin(vol_arr)

    max_sharpe_point = (vol_arr[max_sharpe_idx], ret_arr[max_sharpe_idx])
    min_vol_point = (vol_arr[min_vol_idx], ret_arr[min_vol_idx])

    # Calculate efficient frontier curve
    frontier_vol = np.linspace(min(vol_arr), max(vol_arr), 200)
    frontier_ret = []

    for target_vol in frontier_vol:
        # Solve minimum return for each volatility (approximate frontier)
        idx = (np.abs(vol_arr - target_vol)).argmin()
        frontier_ret.append(ret_arr[idx])

    frontier_ret = np.array(frontier_ret)

    plt.figure(figsize=(14, 9))

    scatter = plt.scatter(
        vol_arr, ret_arr, c=sharpe_arr, cmap="viridis", s=10, alpha=0.7
    )

    # Efficient frontier curve
    plt.plot(frontier_vol, frontier_ret, linestyle='--', color='black', linewidth=2)

    # Highlight max Sharpe
    plt.scatter(*max_sharpe_point, marker='^', color='red', s=200, label="Max Sharpe Ratio")

    # Highlight minimum vol
    plt.scatter(*min_vol_point, marker='^', color='green', s=200, label="Minimum Volatility")

    # Label individual stocks
    for _, ticker in enumerate(tickers):
        stock_vol = np.sqrt(cov_matrix[ticker][ticker] * 252)
        stock_ret = mean_returns[ticker] * 252
        plt.scatter(stock_vol, stock_ret, s=120, color='blue')
        plt.text(stock_vol, stock_ret, f" {ticker}", fontsize=10)

    cbar = plt.colorbar(scatter)
    cbar.set_label("Sharpe Ratio")

    plt.title("Efficient Frontier with Key Portfolios", fontsize=16, fontweight="bold")
    plt.xlabel("Annualized Volatility", fontsize=13)
    plt.ylabel("Annualized Return", fontsize=13)
    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
