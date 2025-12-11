"""Monte Carlo simulation plots."""

import matplotlib.pyplot as plt

def plot_monte_carlo_paths(price_paths, ticker):
    """Plot multiple Monte Carlo paths for a stock."""

    plt.figure(figsize=(12, 7))
    plt.plot(price_paths[:200].T, alpha=0.1)   # show first 200 paths lightly

    plt.title(f"Monte Carlo Simulation — {ticker}", fontsize=16, fontweight="bold")
    plt.xlabel("Days")
    plt.ylabel("Simulated Price")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_monte_carlo_distribution(price_paths, ticker):
    """Plot distribution of final simulated prices."""

    final_prices = price_paths[:, -1]

    plt.figure(figsize=(10, 6))
    plt.hist(final_prices, bins=60, alpha=0.7, color='steelblue')

    plt.title(f"Distribution of Final Prices — {ticker}", fontsize=16, fontweight="bold")
    plt.xlabel("Final Price")
    plt.ylabel("Frequency")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
