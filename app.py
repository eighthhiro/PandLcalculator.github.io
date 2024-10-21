def calculate_profit_loss():
    try:
        # Get total income and total expenses from the user
        total_income = float(input("Enter total income: "))
        total_expenses = float(input("Enter total expenses: "))

        # Calculate profit or loss
        profit_loss = total_income - total_expenses

        # Determine if it's a profit or loss
        if profit_loss > 0:
            print(f"Profit: ${profit_loss:.2f}")
        elif profit_loss < 0:
            print(f"Loss: ${-profit_loss:.2f}")
        else:
            print("Break-even: No profit, no loss.")
    except ValueError:
        print("Please enter valid numeric values for income and expenses.")
        
calculate_profit_loss()