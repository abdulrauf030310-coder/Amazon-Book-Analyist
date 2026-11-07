"""
Amazon Bestselling Books (2009-2022) Data Analysis
Performs data cleaning, exploratory data analysis, and statistical evaluation using pandas.
"""

import sys
from pathlib import Path

# Force UTF-8 stdout on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd
import numpy as np

def run_analysis(csv_path: str = "bestsellers.csv"):
    print("=" * 60)
    print(" [ANALYSIS] AMAZON BESTSELLING BOOKS (2009 - 2022)")
    print("=" * 60)

    # 1. Load Data
    path = Path(csv_path)
    if not path.exists():
        print(f"Error: {csv_path} not found.")
        sys.exit(1)

    df = pd.read_csv(path)
    print(f"\n[1] DATASET OVERVIEW:")
    print(f"Total Entries: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst 3 rows:")
    print(df.head(3).to_string(index=False))

    # 2. Data Cleaning & Sanity Checks
    print("\n" + "-" * 60)
    print("[2] DATA HEALTH & VALIDATION:")
    missing = df.isnull().sum()
    print("Missing Values Per Column:")
    print(missing)

    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate full records: {duplicate_rows}")

    unique_titles = df['Name'].nunique()
    unique_authors = df['Author'].nunique()
    print(f"Unique Book Titles: {unique_titles}")
    print(f"Unique Authors: {unique_authors}")

    # 3. Descriptive Statistics
    print("\n" + "-" * 60)
    print("[3] NUMERICAL METRICS SUMMARY:")
    num_cols = ['User Rating', 'Reviews', 'Price']
    stats_df = df[num_cols].describe().round(2)
    print(stats_df)

    # 4. Fiction vs Non-Fiction Breakdown
    print("\n" + "-" * 60)
    print("[4] GENRE BREAKDOWN & COMPARISON:")
    genre_group = df.groupby('Genre').agg(
        Total_Books=('Name', 'count'),
        Avg_Rating=('User Rating', 'mean'),
        Median_Rating=('User Rating', 'median'),
        Avg_Price=('Price', 'mean'),
        Median_Price=('Price', 'median'),
        Avg_Reviews=('Reviews', 'mean')
    ).round(2)
    print(genre_group)

    # 5. Top 10 Authors by Bestseller Appearances
    print("\n" + "-" * 60)
    print("[5] TOP 10 MOST FREQUENT BESTSELLING AUTHORS:")
    top_authors = df['Author'].value_counts().head(10)
    for rank, (author, count) in enumerate(top_authors.items(), 1):
        author_rating = df[df['Author'] == author]['User Rating'].mean()
        print(f"{rank:2d}. {author:<28} | Appearances: {count:2d} | Avg Rating: {author_rating:.2f}")

    # 6. Highest Rated Books (4.9 Rating Club)
    print("\n" + "-" * 60)
    print("[6] THE 4.9 RATING CLUB (TOP REVIEWED HIGHEST RATED):")
    top_rated = df[df['User Rating'] >= 4.9].drop_duplicates(subset=['Name']).sort_values(by='Reviews', ascending=False)
    for idx, row in top_rated.head(5).iterrows():
        print(f"★ {row['User Rating']} | {row['Name'][:45]:<45} by {row['Author'][:20]:<20} ({row['Reviews']:,} reviews)")

    # 7. Price Correlation & Outliers
    print("\n" + "-" * 60)
    print("[7] CORRELATION & PRICING INSIGHTS:")
    corr_matrix = df[['User Rating', 'Reviews', 'Price', 'Year']].corr().round(3)
    print("Correlation Matrix:")
    print(corr_matrix)

    priciest_book = df.loc[df['Price'].idxmax()]
    print(f"\nMost Expensive Bestseller: '{priciest_book['Name']}' at ${priciest_book['Price']} ({priciest_book['Year']})")

    cheapest_book = df.loc[df['Price'].idxmin()]
    print(f"Lowest Priced Bestseller: '{cheapest_book['Name']}' at ${cheapest_book['Price']} ({cheapest_book['Year']})")

    # 8. Export Summary Table to Markdown
    summary_md_path = path.parent / "SUMMARY_STATS.md"
    with open(summary_md_path, "w", encoding="utf-8") as f:
        f.write("# Amazon Bestsellers Analysis - Summary Metrics\n\n")
        f.write("## 1. Overall Statistics\n\n")
        f.write(stats_df.to_markdown())
        f.write("\n\n## 2. Fiction vs Non-Fiction Comparison\n\n")
        f.write(genre_group.to_markdown())
        f.write("\n\n## 3. Correlation Matrix\n\n")
        f.write(corr_matrix.to_markdown())
        f.write("\n")

    print(f"\n[OK] Summary metrics exported to {summary_md_path.name}")
    print("=" * 60)

if __name__ == "__main__":
    run_analysis()
