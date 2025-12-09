import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", s=10)

    # 3. Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    # Extend line to 2050
    years_extended = pd.Series(range(df["Year"].min(), 2051))
    ax.plot(
        years_extended,
        intercept + slope * years_extended,
        color="red",
        label="Fit All Data"
    )

    # 4. Create second line of best fit (from year 2000)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    years_extended_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_extended_recent,
        intercept2 + slope2 * years_extended_recent,
        color="green",
        label="Fit 2000+"
    )

    # 5. Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # 6. Save plot and return fig
    fig.savefig("sea_level_plot.png")
    return fig
