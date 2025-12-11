"""Initialize correlation plots"""

import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(daily_returns):
    """plot correlation heatmap"""

    plt.figure(figsize=(10, 8))
    sns.heatmap(daily_returns.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix of Returns", fontsize=14, fontweight="bold")
    plt.tight_layout()

    plt.show()
