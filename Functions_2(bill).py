def display(name, account_number, amount, due_date):
    print(f"Hello Mr/Mrs {name}")
    print(f"Your account number is {account_number}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    print("Please pay your bill before the due date")
    print()

display("Alex", 123456789, 100.00, "2025-4-15")