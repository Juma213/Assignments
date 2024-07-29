# Here is to display the user's balance
balance = 1000

# The function to enable display of the menu and get the user's choice
def display_menu():
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    choice = input("Please choose an option (1-4): ")
    return choice

# This is the main loop to present the menu to the user repeatedly after transacting
while True:
    user_choice = display_menu()
    
    # Check balance
    if user_choice == '1':
        print(f"\nYour current balance is Ksh.{balance}")
    
    # Deposit money
    elif user_choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"\nKsh.{deposit_amount} has been deposited to your account.")
        else:
            print("\nInvalid amount. Please enter a positive number.")
    
    # Withdraw money
    elif user_choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if 0 < withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"\nKsh.{withdraw_amount} has been withdrawn from your account.")
        elif withdraw_amount > balance:
            print("\nInsufficient funds. Please enter an amount less than or equal to your balance.")
        else:
            print("\nInvalid amount. Please enter a positive number.")
    
    # Exit
    elif user_choice == '4':
        print("\nThank you for using our ATM services. Goodbye!")
        break
    
    # Invalid choice
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")


