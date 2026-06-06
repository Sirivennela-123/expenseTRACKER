expenses = []  # List of expenses in the form of dictionary
print("**********************")
print("Welcome to your expense tracker 💰")
print("Track your spending, save smarter, and stay in control!")
print("Let's get started")

while True:
    print("\n         ✨ Expense Tracker ✨        ")
    print("[1] ➕ Add a New Expense")
    print("[2] 📋 View All Expenses")
    print("[3] 📊 Analyze Spending")
    print("[4] 💾 Export Data")
    print("[5] 🚪 Exit")

    option = input("Enter your choice (1-5): ")

    if option == "1":
        print("Adding a new expense...")
        amount = input("Enter the amount: ")
        category = input("Enter the category (Food, holiday trip, movie etc.): ")
        date = input("Enter the date (DD/MM/YYYY): ")
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        print("✅ Expense added successfully!")
        print(f"💰 {amount} spent on {category} at {date}")

    elif option == "2":
        print("📋 Displaying all expenses...")
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['category']} - {exp['amount']} on {exp['date']}")

    elif option == "3":
        print("📊 Analyzing your spending habits...")
        if not expenses:
            print("No expenses to analyze.")
        else:
            amounts = [float(exp['amount']) for exp in expenses]
            total_spending = sum(amounts)

            # Category totals
            category_totals = {}
            for exp in expenses:
                category = exp['category']
                category_totals[category] = category_totals.get(category, 0) + float(exp['amount'])

            print(f"\n📊 Total spending: {total_spending}")
            print("\n📂 Spending by category:")
            for cat, amt in category_totals.items():
                print(f"- {cat}: {amt}")

            # Largest expense
            largest_amount = max(amounts)
            print(f"\n💰 Largest expense: {largest_amount}")

            # Average spending
            average = total_spending / len(amounts)
            print(f"📈 Average spending per expense: {average:.2f}")

    elif option == "4":
        print("💾 Export feature coming soon...")

    elif option == "5":
        print("👋 Thank you! Stay smart with your money.")
        break

    else:
        print("❌ Invalid option! Please try again...")




