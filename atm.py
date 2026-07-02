# ===========================
# ATM Machine
# ===========================

# This function adds the deposit amount to the balance.
def deposit(balance, deposit_amount):
    try:
        # float() converts the user's input into a decimal number.
        # Example: "100" -> 100.0
        balance = float(balance) + float(deposit_amount)

        # return sends the new balance back to where the function was called.
        return balance

    # ValueError happens when float() can't convert text into a number.
    # Example: float("hello")
    except ValueError:
        print("Brother, numbers only 🥐🥐🥐🥐🥐")
        return balance   # Return the old balance so nothing changes.


# This function subtracts money from the balance.
def withdrawal(withdraw_amount, balance):
    try:
        balance = float(balance) - float(withdraw_amount)
        return balance

    except ValueError:
        print("Brother, numbers only 🥐🥐🥐🥐🥐")
        return balance


# Starting balance
balance = 500.0


# while True means "repeat forever"
# The loop only stops when it reaches a break statement.
while True:

    print(
        "\n======== MENU ========\n"
        "1. Check Balance\n"
        "2. Deposit Money\n"
        "3. Withdraw Money\n"
        "4. Exit\n"
    )

    choice = input("Choose what you want: ")

    if choice == "1":
        print(f"Current Balance: ${balance:.2f}")

    elif choice == "2":
        amtdep = input("How much would you like to deposit? ")

        # The function returns the new balance.
        # We save it back into the balance variable.
        balance = deposit(balance, amtdep)

        print(f"Successfully deposited! Current balance: ${balance:.2f}")

    elif choice == "3":
        amtwith = input("How much would you like to withdraw? ")

        try:
            # Convert the input to a number once.
            amtwith = float(amtwith)

            # Check if the user has enough money.
            if amtwith > balance:
                print("Insufficient funds 🥐")

            else:
                # Update the balance.
                balance = withdrawal(amtwith, balance)

                print(f"Successfully withdrew money! Current balance: ${balance:.2f}")

        except ValueError:
            print("Brother, numbers only 🥐🥐🥐")

    elif choice == "4":
        print("Thank you for using Python Bank!")
        break

    else:
        # This happens if they type anything besides 1-4.
        print("Invalid option. Please choose 1, 2, 3, or 4.")