# variance_analyzer.py
Python tool that analyzes budget vs actual performance, calculates variances, and generates summary insights and visual output for FP&amp;A-style reporting.

--

# Budget vs Actual Variance Analyzer
A lightweight Python tool that performs budget vs actual analysis, calculates financial variances, and generates a summary table and visualization commonly used in FP&A and financial analyst workflows.

---

## What This Project Does
- Reads monthly budget and actual data from a CSV file
- Calculates dollar and percentage variances
- Summarizes results by category to identify key drivers
- Generates a variance bar chart for quick visual insight

---

## Tech Stack
- Python
- pandas
- matplotlib

---

## Project Structure
variance-analyzer/
├── variance_analyzer.py
├── data/
│ └── budget_vs_actual.csv
└── README.md

---

## How to Run
1. Clone the repository
2. Place your CSV file in the `data` folder
3. Run the script: python3 variance_analyzer.py
4. The script will print summary tables to the terminal and save a variance chart as `variance.png`.

---

## Input Data Format
The CSV file should contain the following columns: Month, Category, Budget, Actual
Example:2025-10,Revenue,120000,126500

---

## Output
- Terminal summary of budget vs actual performance by category
- Top variance drivers highlighted
- Bar chart visualization of total variance by category

---

## Future Improvements
- Export results to Excel
- Add variance threshold flags
- Support command-line CSV input




