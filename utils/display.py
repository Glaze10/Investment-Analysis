'''format/display results'''

class ResultsFormatter:
    '''pretty print optimization results'''

    @staticmethod
    def display_pf_results(results):
        """Display pf results"""

        print("\n" + "=" * 70)
        print(f"PORTFOLIO OPTIMIZATION RESULTS: {results['method']}")
        print("=" * 70)

        print("\nOptimal Portfolio Weights:")
        print("-" * 70)
        for ticker, weight in results['weights'].items():
            bar = '█' * int(weight * 50)
            print(f"  {ticker:6s}: {weight:7.2%}  {bar}")

        print("\nPortfolio Performance Metrics:")
        print("-" * 70)
        print(f"  Expected Annual Return:  {results['expected_annual_return']:7.2%}")
        print(f"  Annual Volatility:       {results['annual_volatility']:7.2%}")
        print(f"  Sharpe Ratio:            {results['sharpe_ratio']:7.4f}")
        print(f"  Optimization Success:    {results['optimization_success']}")
        print("=" * 70 + "\n")

    @staticmethod
    def display_stock_statistics(stats_df):
        '''display individual stock stats'''

        print("\n" + "=" * 70)
        print("INDIVIDUAL STOCK STATISTICS")
        print("=" * 70)
        print(stats_df.to_string())
        print("=" * 70 + "\n")
