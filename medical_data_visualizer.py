import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv("medical_examination.csv")

# 2. Add 'overweight' column
bmi = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = (bmi > 25).astype(int)

# 3. Normalize cholesterol and gluc (0 = good, 1 = bad)
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


# 4. Categorical plot
def draw_cat_plot():
    # 5. Melt the required columns
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # 6. Group and reformat
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # 7. Create catplot
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    ).fig

    # 8. Do not change
    fig.savefig('catplot.png')
    return fig


# 9. Heat map
def draw_heat_map():
    # 10. Clean data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 11. Correlation matrix
    corr = df_heat.corr()

    # 12. Mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 14. Heatmap
    sns.heatmap(
        corr,
        annot=True,
        fmt=".1f",
        mask=mask,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.5}
    )

    # 15. Do not change
    fig.savefig('heatmap.png')
    return fig
