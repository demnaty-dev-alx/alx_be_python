class BankAccount:
    def __init__(self, account_balance = 0):
        self._account_balance = account_balance

    def deposit(self, amount):
        self._account_balance += amount

    def withdraw(self, amount):
        if amount > self._account_balance:
            return False
        self._account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
