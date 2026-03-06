def main():
    try:
        # Ask for the total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))

        # Ask for expenses
        expenses = []
        print("Enter your expenses (type 'done' to finish):")
        while True:
            entry = input("> ").strip().lower()
            if entry == "done":
                break
            try:
                expenses.append(float(entry))
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")

        # Calculate remaining balance
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses

        # Display the remaining balance
        print(f"\nTotal Budget: {total_budget:.2f} LKR")
        print(f"Total Expenses: {total_expenses:.2f} LKR")
        print(f"Remaining Balance: {remaining_balance:.2f} LKR")

        if remaining_balance < 500:
            print("Warning: Low Funds")

    except ValueError:
        print("Invalid input. Please enter numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
