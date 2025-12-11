"""Handle all plot functionality"""

import matplotlib.pyplot as plt

class PortfolioVisualizer:
    '''create visualizations for PF analysis'''

    def __init__(self, style = 'seaborn-v0_8-darkgrid'):
        plt.style.use(style)

    def plot_historical_prices(self, historical_data):
        '''plot normalized historical close prices'''

        plt.figure(figsize = (14, 7))

        normalized = (historical_data / historical_data.iloc[0]) * 100
        normalized.plot(linewidth = 2)

        plt.title('Historical Price Performance (Normalized)',
                  fontsize = 14, fontweight = 'bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Normalized Price', fontsize=12)
        plt.legend(loc='best', fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def plot_returns(self, daily_returns, cumulative_returns):
        '''plot daily and cumulative returns'''

        _, (ax1, ax2) = plt.subplots(2, 1, figsize = (14,10))

        #daily returns
        daily_returns.plot(ax=ax1, alpha=0.7, linewidth=1)
        ax1.set_title('Daily Returns', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Date', fontsize=12)
        ax1.set_ylabel('Daily Return', fontsize=12)
        ax1.legend(loc='best', fontsize=9)
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='black', linestyle='--', linewidth=0.8)

        # Cumulative returns
        (cumulative_returns * 100).plot(ax=ax2, linewidth=2)
        ax2.set_title('Cumulative Returns', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylabel('Cumulative Return (%)', fontsize=12)
        ax2.legend(loc='best', fontsize=9)
        ax2.grid(True, alpha=0.3)
        ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8)

        plt.tight_layout()
        plt.show()
