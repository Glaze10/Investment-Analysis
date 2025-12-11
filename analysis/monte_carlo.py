"""Monte Carlo price simulation for individual stocks."""

import numpy as np
import pandas as pd


def simulate_stock_paths(
    last_price: float,
    daily_returns: pd.Series,
    num_days: int = 252,
    num_simulations: int = 5000
):
    """
    Monte Carlo simulation of future stock prices.

    Parameters:
        last_price: most recent close price
        daily_returns: historical daily returns (used to estimate mu & sigma)
        num_days: number of forecast days (default 1 year)
        num_simulations: number of random paths

    Returns:
        numpy array of shape (num_simulations, num_days)
    """

    mu = daily_returns.mean()
    sigma = daily_returns.std()

    # Random normal returns for all simulations
    random_returns = np.random.normal(mu, sigma, (num_simulations, num_days))

    # Convert returns to price paths
    price_paths = last_price * np.exp(np.cumsum(random_returns, axis=1))

    return price_paths
