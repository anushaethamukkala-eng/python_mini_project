def show_menu():
    print("===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


balance = 10000

while True:
    show_menu()
    option = int(input("Select an option: "))

    if option == 1:
        print("Current Balance:", balance)

    elif option == 2:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount")
        else:
            balance += amount
            print("Deposit successful")
            print("Updated Balance:", balance)

    elif option == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("Updated Balance:", balance)

    elif option == 4:
        print("Thank you!")
        break

    else:
        print("Invalid option")
