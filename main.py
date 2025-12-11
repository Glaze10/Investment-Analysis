"""Main entry point."""

import pandas as pd

import yfinance as yf

from analysis.capm import compute_capm, compute_portfolio_beta, summarize_capm_table
from analysis.efficient_frontier import efficient_frontier
from analysis.monte_carlo import simulate_stock_paths
from analysis.optimizer import PortfolioOptimizer
from analysis.statistics import StockStatistics

from data.data_loader import DataLoader

from utils.display import ResultsFormatter

from visualization.capm_plots import plot_capm_regression
from visualization.corr_plots import plot_correlation_matrix
from visualization.efficient_frontier_plot import plot_efficient_frontier
from visualization.monte_carlo_plots import (
    plot_monte_carlo_distribution,
    plot_monte_carlo_paths,
)
from visualization.plots import PortfolioVisualizer

def main():
    """Main application workflow."""

    ResultsFormatter.header("PORTFOLIO ANALYSIS")

    # LOAD & PROCESS DATA
    loader = DataLoader()
    data = loader.get_all_data()

    # STOCK STATISTICS
    stock_stats = StockStatistics(data["daily_returns"])
    stats_df = stock_stats.calculate_stats()
    ResultsFormatter.display_stock_statistics(stats_df)

    # PORTFOLIO OPTIMIZATION
    optimizer = PortfolioOptimizer(data["daily_returns"])

    print("Select portfolio weighting method:")
    print("1. Sharpe Ratio Optimization (maximize risk-adjusted returns)")
    print("2. Equal Weight (20% each)")
    choice = input("Enter selection (1 or 2): ").strip()

    if choice == "1":
        results = optimizer.optimize_sharpe()
    elif choice == "2":
        results = optimizer.equal_weight()
    else:
        print("Invalid choice. Using Sharpe optimization by default.")
        results = optimizer.optimize_sharpe()

    ResultsFormatter.display_pf_results(results)

    # VISUALIZATIONS
    viz = PortfolioVisualizer()
    viz.plot_historical_prices(data["historical"])
    viz.plot_returns(data["daily_returns"], data["cumulative_returns"])

    plot_correlation_matrix(data["daily_returns"])
    viz.plot_rolling_metrics(data["daily_returns"])

    # EFFICIENT FRONTIER
    mean_returns = data["daily_returns"].mean()
    cov_matrix = data["daily_returns"].cov()

    ef_results, weight_records = efficient_frontier(mean_returns, cov_matrix)

    ResultsFormatter.summarize_efficient_frontier(
        ef_results,
        weight_records,
        loader.tickers
    )

    plot_efficient_frontier(mean_returns, cov_matrix, loader.tickers)

    # CAPM REGRESSION ANALYSIS
    ResultsFormatter.header("CAPM REGRESSION ANALYSIS")

    spy = yf.download("SPY", start=loader.start_date, end=loader.end_date)["Close"]
    market_returns = spy.pct_change().dropna()

    capm_table = summarize_capm_table(data["daily_returns"], market_returns)
    ResultsFormatter.display_capm_table(capm_table)

    # Portfolio Beta
    weights_series = pd.Series(results["weights"])[capm_table.index]
    pf_beta = compute_portfolio_beta(weights_series, capm_table["Beta"])
    ResultsFormatter.display_portfolio_beta(pf_beta)

    # Per-stock CAPM details + regression plot
    for ticker in loader.tickers:
        stock_ret = data["daily_returns"][ticker]
        stats = compute_capm(stock_ret, market_returns)

        ResultsFormatter.display_capm_stats(ticker, stats)

        plot_capm_regression(
            stock_returns=stock_ret,
            market_returns=market_returns,
            ticker=ticker,
            alpha=stats["alpha"],
            beta=stats["beta"]
        )

    # MONTE CARLO SIMULATION
    ResultsFormatter.header_monte_carlo()

    for ticker in loader.tickers:
        ResultsFormatter.mc_stock_header(ticker)

        last_price = data["historical"][ticker].iloc[-1]
        daily_ret = data["daily_returns"][ticker]

        paths = simulate_stock_paths(
            last_price=last_price,
            daily_returns=daily_ret,
            num_days=252,
            num_simulations=5000
        )

        plot_monte_carlo_paths(paths, ticker)
        plot_monte_carlo_distribution(paths, ticker)

if __name__ == '__main__':
    main()
