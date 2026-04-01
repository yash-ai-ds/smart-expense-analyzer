# Smart Expense Analyzer 💰

A beginner-friendly Command Line Interface (CLI) application written in Python to track, analyze, and visualize your daily expenses.

## Features
- **Add Expenses:** Log your expenses with amount, category, and date.
- **Data Storage:** Uses a robust CSV backing format, storing your data efficiently.
- **Data Loading:** Employs `pandas` to load, structure, and query expense data.
- **Detailed Summary:** 
  - View total expenses
  - Breakdown of category-wise spending
  - Identify your highest spending category
  - See your monthly summary aggregate
- **Advanced Graphing:** Generates neat simple pie chart visualizations using `matplotlib` to let you quickly see where your money goes.
- **Predictive Engine:** Uses basic rolling average logic to predict your next month's expected expenses based on your past behavior.

## Technologies Used
- **Python 3.x**
- **pandas:** For structural data manipulation, aggregation, and loading CSV files.
- **matplotlib:** For creating clean graphical distributions.

## Setup and Installation

1. Clone the repository or download the source code.
2. Initialize and open a terminal inside the project directory.
3. Install the necessary dependencies (we recommend doing this in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python expense_analyzer.py
   ```

## Usage Example

When you run the script, you will be presented with an interactive menu. Enter the numeral corresponding to the action you wish to perform. Your expenses are persistently saved in an `expenses.csv` file created locally adjacent to the script.

```text
=============================
   Smart Expense Analyzer
=============================
1. Add a New Expense
2. View Expense Summary
3. Show Expense Graphs
4. Predict Next Month's Expense
5. Exit
=============================
Enter your choice (1-5): 
```

**Adding an Expense:**
```text
Enter amount: 15.50
Enter category (e.g., Food, Transport, Utilities): Food
Enter date (YYYY-MM-DD) or press Enter for today: 2023-10-15
Expense added successfully!
```

**Viewing Summary:**
```text
--- Expense Summary ---
Total Expenses: $15.50

Category-wise Spending:
  - Food: $15.50

Highest Spending Category: Food ($15.50)

Monthly Summary:
  - 2023-10: $15.50
-----------------------
```
