# 📚 Amazon Bestselling Books Analysis (Python + Pandas)

An Exploratory Data Analysis (EDA) project evaluating trends, ratings, and pricing models of Amazon's bestselling books from 2009 to 2022.

---

## 🚀 How to Run

1. **Set up virtual environment**:
   ```powershell
   cd "c:/Users/USER/Desktop/Github Projects/amazon-books-analysis"
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the Analysis Pipeline**:
   ```powershell
   python analysis.py
   ```
   *(This parses the CSV, validates data health, prints summary metrics, and generates `SUMMARY_STATS.md`)*

4. **Generate Visualization Charts**:
   ```powershell
   python visualize.py
   ```
   *(Creates high-resolution distribution, boxplot, and trend charts inside the `charts/` directory)*

---

## 📁 Project Structure

- [bestsellers.csv](file:///c:/Users/USER/Desktop/Github%20Projects/amazon-books-analysis/bestsellers.csv) – Primary dataset containing titles, authors, ratings, reviews, price, year, and genre.
- [analysis.py](file:///c:/Users/USER/Desktop/Github%20Projects/amazon-books-analysis/analysis.py) – Pandas analysis script with summary metrics and correlations.
- [visualize.py](file:///c:/Users/USER/Desktop/Github%20Projects/amazon-books-analysis/visualize.py) – Matplotlib and Seaborn plotting script.
- [REPORT.md](file:///c:/Users/USER/Desktop/Github%20Projects/amazon-books-analysis/REPORT.md) – Comprehensive narrative report explaining data trends.
- [requirements.txt](file:///c:/Users/USER/Desktop/Github%20Projects/amazon-books-analysis/requirements.txt) – Python package requirements.
