import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "data" / "budget_vs_actual.csv"

df = pd.read_csv(csv_path)

df["Variance_$"] = df["Actual"] - df["Budget"]
df["Variance_%"] = (df["Variance_$"] / df["Budget"]).replace([float("inf"), -float("inf")], 0) * 100

summary = (df.groupby("Category")[["Budget", "Actual", "Variance_$"]]
             .sum()
             .sort_values("Variance_$", ascending=False))

print("\n=== Budget vs Actual Summary (by Category) ===")
print(summary.round(2))

top = df.reindex(df["Variance_$"].abs().sort_values(ascending=False).head(5).index)
print("\n=== Top 5 Variances (by Month/Category) ===")
print(top[["Month", "Category", "Budget", "Actual", "Variance_$", "Variance_%"]].round(2))

# Simple chart: total variance by category
ax = summary["Variance_$"].plot(kind="bar")
plt.title("Variance ($) by Category")
plt.ylabel("Variance ($)")
plt.tight_layout()
plt.savefig("variance.png")
print("\nSaved chart: variance.png")
