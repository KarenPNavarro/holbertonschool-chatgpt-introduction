#!/usr/bin/python3

class Checkbook:
    """
    Description:
        Represents a simple checkbook account that supports
        deposits, withdrawals, and balance checks.

    Parameters:
        None

    Returns:
        None
    """

    def __init__(self):
        """
        Description:
            Initializes the checkbook with a starting balance of 0.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Description:
            Adds money to the account balance.

        Parameters:
            amount (float): Amount to deposit.

        Returns:
            None
        """

        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount

        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Description:
            Removes money from the account balance if sufficient
            funds are available.

        Parameters:
            amount (float): Amount to withdraw.

        Returns:
            None
        """

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount

            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Description:
            Displays the current account balance.

        Parameters:
            None

        Returns:
            None
        """

        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Description:
        Runs the main checkbook application loop and handles
        user commands safely using error handling.

    Parameters:
        None

    Returns:
        None
    """

    cb = Checkbook()

    while True:

        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            print("Goodbye!")
            break

        elif action.lower() == 'deposit':

            try:
                amount = float(
                    input("Enter the amount to deposit: $")
                )

                cb.deposit(amount)

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action.lower() == 'withdraw':

            try:
                amount = float(
                    input("Enter the amount to withdraw: $")
                )

                cb.withdraw(amount)

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    """
    Description:
        Starts the checkbook application.

    Parameters:
        None

    Returns:
        None
    """

    main()
    