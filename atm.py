users = {
    "1234": {"pin": "0000", "balance": 5000},
    "5678": {"pin": "1111", "balance": 3000}
}

def atm():
    print("Welcome to Python ATM!")
    user_id = input("Enter your User ID: ")

    if user_id in users:
        pin = input("Enter your PIN: ")
        if pin == users[user_id]['pin']:
            print("\nLogin successful!")
            while True:
                print("\n1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    print("Your balance is ₹", users[user_id]['balance'])

                elif choice == "2":
                    amount = float(input("Enter amount to deposit: ₹"))
                    users[user_id]['balance'] += amount
                    print("Deposit successful! New balance is ₹", users[user_id]['balance'])

                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: ₹"))
                    if amount <= users[user_id]['balance']:
                        users[user_id]['balance'] -= amount
                        print("Withdrawal successful! New balance is ₹", users[user_id]['balance'])
                    else:
                        print("Insufficient funds.")

                elif choice == "4":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Wrong PIN.")
    else:
        print("User not found.")

atm()