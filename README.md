# Portfolio Analysis & Investment Strategy Project
FIN 320 – Financial Data Analytics

------------------------------------------------------------

## Installation

Install required dependencies:

pip install numpy pandas matplotlib seaborn statsmodels yfinance

------------------------------------------------------------

## Running the Program

From the project root directory:

python main.py

When prompted, choose:

1. Sharpe Ratio Optimization
2. Equal Weight Portfolio

You must CLOSE each plot window to continue to the next plot.

------------------------------------------------------------

## Program Features

### 1. Individual Stock Statistics
The program calculates:
- Annual return
- Annual volatility
- Sharpe ratio

Displayed in a formatted table.

------------------------------------------------------------

### 2. Portfolio Optimization

Two supported strategies:

Sharpe Ratio Optimization:
- Maximizes risk-adjusted return
- Uses return means and covariance matrix
- Produces optimal portfolio weights

Equal Weight Portfolio:
- Assigns 20% to each stock

Outputs include expected return, volatility, Sharpe ratio, and weights.

------------------------------------------------------------

### 3. Efficient Frontier Analysis

The program generates:
- Random portfolios
- Efficient frontier curve
- Maximum Sharpe ratio portfolio
- Minimum volatility portfolio

Printed results include:
- Return
- Volatility
- Sharpe ratio
- Portfolio weights

A full efficient frontier scatter plot is shown.

------------------------------------------------------------

### 4. CAPM Regression Analysis

For each stock:
- Alpha
- Beta
- R-squared

Also includes:
- A CAPM summary table for all stocks
- Portfolio beta (weighted average beta)
- CAPM regression plot for each stock with fitted line

------------------------------------------------------------

### 5. Monte Carlo Simulations

For each ticker:
- 5000 simulated price paths
- 252-day forecast horizon
- Drift and volatility derived from historical returns

Plots include:
- All simulated paths
- Final price distribution histogram

------------------------------------------------------------

## Project Structure

project/
├── main.py
├── data/
│   └── data_loader.py
├── analysis/
│   ├── optimizer.py
│   ├── statistics.py
│   ├── efficient_frontier.py
│   ├── capm.py
│   └── monte_carlo.py
├── visualization/
│   ├── plots.py
│   ├── corr_plots.py
│   ├── efficient_frontier_plot.py
│   ├── capm_plots.py
│   └── monte_carlo_plots.py
└── utils/
    └── display.py

------------------------------------------------------------

## Summary

This project demonstrates the following financial analytics techniques:

- Portfolio optimization
- Efficient frontier modeling
- Risk and return metrics
- CAPM regression and portfolio beta estimation
- Monte Carlo simulation forecasting
- Financial data visualization

It provides a comprehensive, end-to-end workflow for evaluating investment strategies using Python.
