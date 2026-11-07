"""
Generates publication-quality charts for the Amazon Bestsellers dataset.
"""

import sys
from pathlib import Path

# Force UTF-8 stdout on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd

def generate_charts(csv_path: str = "bestsellers.csv", output_dir: str = "charts"):
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
    except ImportError:
        print("⚠️ Matplotlib or Seaborn not installed. Please install requirements.txt to generate charts.")
        return

    out_path = Path(output_dir)
    out_path.mkdir(exist_ok=True)

    df = pd.read_csv(csv_path)

    # Styling configuration
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams.update({
        "font.family": "sans-serif",
        "figure.titlesize": 14,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
    })

    # 1. Rating Distribution by Genre
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="User Rating", hue="Genre", kde=True, bins=15, multiple="stack")
    plt.title("Distribution of Amazon User Ratings by Genre (2009-2022)")
    plt.xlabel("User Rating (out of 5.0)")
    plt.ylabel("Book Count")
    plt.tight_layout()
    chart1 = out_path / "1_rating_distribution.png"
    plt.savefig(chart1, dpi=200)
    plt.close()
    print(f" Saved: {chart1.name}")

    # 2. Price Comparison by Genre
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x="Genre", y="Price", palette=["#3b82f6", "#10b981"])
    plt.title("Book Prices by Genre: Fiction vs. Non-Fiction")
    plt.ylabel("Price ($ USD)")
    plt.tight_layout()
    chart2 = out_path / "2_price_by_genre.png"
    plt.savefig(chart2, dpi=200)
    plt.close()
    print(f" Saved: {chart2.name}")

    # 3. Top 10 Bestselling Authors
    plt.figure(figsize=(10, 6))
    top_authors = df["Author"].value_counts().head(10).reset_index()
    top_authors.columns = ["Author", "Appearances"]
    sns.barplot(data=top_authors, x="Appearances", y="Author", color="#6366f1")
    plt.title("Top 10 Authors with Most Bestseller List Appearances")
    plt.xlabel("Number of Years on Bestseller List")
    plt.tight_layout()
    chart3 = out_path / "3_top_authors.png"
    plt.savefig(chart3, dpi=200)
    plt.close()
    print(f" Saved: {chart3.name}")

    # 4. Average Price Trend Over Time
    plt.figure(figsize=(9, 5))
    trend = df.groupby(["Year", "Genre"])["Price"].mean().reset_index()
    sns.lineplot(data=trend, x="Year", y="Price", hue="Genre", marker="o", linewidth=2.5)
    plt.title("Year-over-Year Average Price Trend by Genre")
    plt.ylabel("Average Price ($ USD)")
    plt.xticks(df["Year"].unique())
    plt.tight_layout()
    chart4 = out_path / "4_price_trend_over_time.png"
    plt.savefig(chart4, dpi=200)
    plt.close()
    print(f" Saved: {chart4.name}")

    print("🎉 All 4 charts successfully generated!")

if __name__ == "__main__":
    generate_charts()
