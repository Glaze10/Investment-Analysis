"""Unified display + pretty-print utilities."""

class ResultsFormatter:
    """Pretty-print analysis outputs."""

    # GENERAL HEADERS

    @staticmethod
    def header(title: str):
        """Generate headers"""

        print("\n" + "=" * 70)
        print(title)
        print("=" * 70 + "\n")

    # STOCK STATISTICS

    @staticmethod
    def display_stock_statistics(stats_df):
        """Display individual stock statistics."""
        ResultsFormatter.header("INDIVIDUAL STOCK STATISTICS")
        print(stats_df.to_string())
        print("=" * 70 + "\n")

    # PORTFOLIO OPTIMIZATION

    @staticmethod
    def display_pf_results(results):
        """Display portfolio optimization results."""

        ResultsFormatter.header(
            f"PORTFOLIO OPTIMIZATION RESULTS: {results['method']}"
        )

        print("Optimal Portfolio Weights:")
        print("-" * 70)
        for ticker, weight in results['weights'].items():
            bar_visual = "█" * int(weight * 50)
            print(f"  {ticker:6s}: {weight:7.2%}  {bar_visual}")

        print("\nPortfolio Performance Metrics:")
        print("-" * 70)
        print(f"  Expected Annual Return:  {results['expected_annual_return']:7.2%}")
        print(f"  Annual Volatility:       {results['annual_volatility']:7.2%}")
        print(f"  Sharpe Ratio:            {results['sharpe_ratio']:7.4f}")
        print(f"  Optimization Success:    {results['optimization_success']}")
        print("=" * 70 + "\n")

    # EFFICIENT FRONTIER SUMMARY

    @staticmethod
    def summarize_efficient_frontier(ef_results, weight_records, tickers):
        """Pretty-print max Sharpe & min volatility portfolios."""

        vol_arr, ret_arr, sharpe_arr = ef_results

        # Max Sharpe
        max_idx = sharpe_arr.argmax()
        max_w = weight_records[max_idx]

        # Min vol
        min_idx = vol_arr.argmin()
        min_w = weight_records[min_idx]

        ResultsFormatter.header("EFFICIENT FRONTIER SUMMARY")

        print("Max Sharpe Ratio Portfolio:")
        print(f"  Expected Return:   {ret_arr[max_idx]:.4f}")
        print(f"  Volatility:        {vol_arr[max_idx]:.4f}")
        print(f"  Sharpe Ratio:      {sharpe_arr[max_idx]:.4f}")
        print("\n  Weights:")
        for t, w in zip(tickers, max_w):
            print(f"   • {t}: {w:.2%}")

        print("\nMinimum Volatility Portfolio:")
        print(f"  Expected Return:   {ret_arr[min_idx]:.4f}")
        print(f"  Volatility:        {vol_arr[min_idx]:.4f}")
        print(f"  Sharpe Ratio:      {sharpe_arr[min_idx]:.4f}")
        print("\n  Weights:")
        for t, w in zip(tickers, min_w):
            print(f"   • {t}: {w:.2%}")

        print("=" * 70 + "\n")

    # CAPM SUMMARY

    @staticmethod
    def display_capm_table(capm_table):
        """Display the capm table"""

        ResultsFormatter.header("CAPM REGRESSION ANALYSIS")
        print(capm_table.to_string())
        print()

    @staticmethod
    def display_portfolio_beta(beta):
        """Display portfolio beta"""

        print(f"Portfolio Beta (Weighted Avg.): {beta:.4f}\n")

    @staticmethod
    def display_capm_stats(ticker, stats):
        """Display capm stats"""

        print(f"\nCAPM Results for {ticker}:")
        print(f"  Alpha:     {stats['alpha']:.6f}")
        print(f"  Beta:      {stats['beta']:.4f}")
        print(f"  R-Squared: {stats['r_squared']:.4f}")

    # MONTE CARLO SUMMARY

    @staticmethod
    def header_monte_carlo():
        """Header for monte carlo"""

        ResultsFormatter.header("MONTE CARLO SIMULATIONS")

    @staticmethod
    def mc_stock_header(ticker):
        """mc stock header"""

        print(f"Monte Carlo Simulation for {ticker}...")
