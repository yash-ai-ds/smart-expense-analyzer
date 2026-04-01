import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DATA_FILE = 'expenses.csv'

def init_data_file():
    """Initializes the CSV file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=['Date', 'Category', 'Amount'])
        df.to_csv(DATA_FILE, index=False)

def add_expense():
    """Prompts user to add a new expense."""
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
        
    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            # Validate date format
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
            
    # Append to CSV
    new_expense = pd.DataFrame([{'Date': date_str, 'Category': category, 'Amount': amount}])
    new_expense.to_csv(DATA_FILE, mode='a', header=not os.path.exists(DATA_FILE), index=False)
    print("Expense added successfully!\n")

def load_data():
    """Loads expense data using pandas."""
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame(columns=['Date', 'Category', 'Amount'])
    return pd.read_csv(DATA_FILE)

def view_summary():
    """Displays data summaries."""
    df = load_data()
    if df.empty:
        print("No expenses recorded yet.\n")
        return
        
    print("\n--- Expense Summary ---")
    
    # Total Expenses
    total = df['Amount'].sum()
    print(f"Total Expenses: ${total:.2f}")
    
    # Category-wise spending
    print("\nCategory-wise Spending:")
    category_summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    for cat, amt in category_summary.items():
        print(f"  - {cat}: ${amt:.2f}")
        
    # Highest spending category
    if not category_summary.empty:
        highest_cat = category_summary.idxmax()
        highest_amt = category_summary.max()
        print(f"\nHighest Spending Category: {highest_cat} (${highest_amt:.2f})")
    
    # Monthly Summary
    print("\nMonthly Summary:")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_summary = df.groupby('Month')['Amount'].sum()
    for month, amt in monthly_summary.items():
        print(f"  - {month}: ${amt:.2f}")
    print("-----------------------\n")

def show_graphs():
    """Shows simple graphs for expense visualization."""
    df = load_data()
    if df.empty:
        print("No expenses recorded to graph.\n")
        return
        
    category_summary = df.groupby('Category')['Amount'].sum()
    
    # Plotting Pie Chart
    plt.figure(figsize=(8, 6))
    category_summary.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Paired')
    plt.title("Expense Distribution by Category")
    plt.ylabel('')  # Hide y-label for pie chart
    plt.tight_layout()
    print("Close the graph window to continue.")
    plt.show()

def predict_expense():
    """Predicts next month's expense using a simple moving average."""
    df = load_data()
    if df.empty:
        print("Not enough data to predict expenses.\n")
        return
        
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    
    monthly_totals = df.groupby('Month')['Amount'].sum()
    
    if len(monthly_totals) < 2:
        print("\nNot enough monthly data to make a reliable prediction. Need at least 2 different months.")
        print("Based on limited data, your current month's total is the best estimate.\n")
        
    # Basic logic: Average of the monthly spending
    avg_expense = monthly_totals.mean()
    last_month_expense = monthly_totals.iloc[-1]
    
    print("\n--- Expense Prediction ---")
    print(f"Your historical average monthly spending is: ${avg_expense:.2f}")
    print(f"Your last recorded month's spending was: ${last_month_expense:.2f}")
    print(f"\n--> Predicted expense for next month: ${avg_expense:.2f}")
    print("--------------------------\n")

def main_menu():
    init_data_file()
    
    while True:
        print("=============================")
        print("   Smart Expense Analyzer")
        print("=============================")
        print("1. Add a New Expense")
        print("2. View Expense Summary")
        print("3. Show Expense Graphs")
        print("4. Predict Next Month's Expense")
        print("5. Exit")
        print("=============================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            show_graphs()
        elif choice == '4':
            predict_expense()
        elif choice == '5':
            print("Exiting Smart Expense Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.\n")

if __name__ == "__main__":
    main_menu()
