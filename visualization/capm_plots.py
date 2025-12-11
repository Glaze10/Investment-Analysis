"""CAPM Regression Plots"""

import numpy as np
import matplotlib.pyplot as plt


def plot_capm_regression(stock_returns, market_returns, ticker, alpha, beta, risk_free_rate=0.02):
    """
    Plot CAPM regression: scatter of excess returns + regression line.
    """

    rf_daily = (1 + risk_free_rate) ** (1/252) - 1
    stock_excess = stock_returns - rf_daily
    market_excess = market_returns - rf_daily

    # Regression line
    x_line = np.linspace(market_excess.min(), market_excess.max(), 200)
    y_line = alpha + beta * x_line

    plt.figure(figsize=(10, 7))

    # Scatter
    plt.scatter(market_excess, stock_excess, alpha=0.5, label="Excess Returns")

    # Regression line
    plt.plot(x_line, y_line, color='red', linewidth=2,
             label=f"CAPM Fit (β={beta:.2f}, α={alpha:.4f})")

    # Labels
    plt.title(f"CAPM Regression for {ticker}", fontsize=16, fontweight='bold')
    plt.xlabel("Market Excess Return (Market - RF)")
    plt.ylabel(f"{ticker} Excess Return (Stock - RF)")
    plt.grid(alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()
