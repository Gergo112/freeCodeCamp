import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar

df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df.index, df["value"], color="red", linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_grouped.plot(kind="bar", figsize=(12, 10)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        title="Months",
        labels=[calendar.month_name[i] for i in range(1, 13)]
    )

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    df_box["month"] = pd.Categorical(
        df_box["month"],
        categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        ordered=True
    )

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    sns.boxplot(
        ax=axes[0],
        x="year",
        y="value",
        data=df_box
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        ax=axes[1],
        x="month",
        y="value",
        data=df_box
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig

