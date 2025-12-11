"""CAPM Regression Calculations & Summaries"""

import pandas as pd
import statsmodels.api as sm

def compute_capm(stock_returns, market_returns, risk_free_rate=0.02):
    """
    Compute CAPM alpha, beta, and regression statistics.

    Returns dict with:
    - alpha
    - beta
    - r_squared
    - model (statsmodels OLS object)
    """

    # Convert risk-free rate to daily
    rf_daily = (1 + risk_free_rate) ** (1/252) - 1

    # Excess returns
    stock_excess = stock_returns - rf_daily
    market_excess = market_returns - rf_daily

    # CAPM regression: stock_excess ~ alpha + beta * market_excess
    X = sm.add_constant(market_excess)
    model = sm.OLS(stock_excess, X).fit()

    alpha = model.params.iloc[0]
    beta = model.params.iloc[1]
    r_squared = model.rsquared

    return {
        "alpha": alpha,
        "beta": beta,
        "r_squared": r_squared,
        "model": model
    }


def summarize_capm_table(daily_returns, market_returns, risk_free_rate=0.02):
    """
    Computes CAPM alpha, beta, R² for EACH stock in the dataset.
    Returns a DataFrame indexed by ticker.
    """

    rows = []

    for ticker in daily_returns.columns:
        stats = compute_capm(
            daily_returns[ticker],
            market_returns,
            risk_free_rate=risk_free_rate
        )

        rows.append({
            "Ticker": ticker,
            "Alpha": stats["alpha"],
            "Beta": stats["beta"],
            "R²": stats["r_squared"],
        })

    df = pd.DataFrame(rows)
    df = df.set_index("Ticker")
    return df


def compute_portfolio_beta(weights, beta_series):
    """
    Compute portfolio beta as weighted average of individual betas.
    weights: array-like corresponding to tickers
    beta_series: pandas Series with betas indexed by ticker
    """
    return float((weights * beta_series).sum())
