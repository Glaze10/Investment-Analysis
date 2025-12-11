'''main entry point'''

from data.data_loader import DataLoader
from analysis.optimizer import PortfolioOptimizer
from analysis.statistics import StockStatistics
from visualization.plots import PortfolioVisualizer
from utils.display import ResultsFormatter

def main():
    '''main app workflow'''

    print('=' * 70)
    print('PORTFOLIO ANALYSIS')
    print("=" * 70 + "\n")

    #load/process data
    loader = DataLoader()
    data = loader.get_all_data()

    #calculate individual stock stats
    stock_stats = StockStatistics(data['daily_returns'])
    stats_df = stock_stats.calculate_stats()
    ResultsFormatter.display_stock_statistics(stats_df)

    #optimize PF
    optimizer = PortfolioOptimizer(data['daily_returns'])

    print("Select portfolio weighting method:")
    print("1. Sharpe Ratio Optimization (maximize risk-adjusted returns)")
    print("2. Equal Weight (20% each)")
    choice = input("Enter selection (1 or 2): ").strip()

    if choice == '1':
        results = optimizer.optimize_sharpe()
    elif choice == '2':
        results = optimizer.equal_weight()
    else:
        print("Invalid choice. Using Sharpe optimization by default.")
        results = optimizer.optimize_sharpe()

    #display results
    ResultsFormatter.display_pf_results(results)

    #visualization
    viz = PortfolioVisualizer()
    viz.plot_historical_prices(data['historical'])
    viz.plot_returns(data['daily_returns'], data['cumulative_returns'])

if __name__ == '__main__':
    main()
