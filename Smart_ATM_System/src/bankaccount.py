class BankAccount:

    __min_balance = 100

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def check_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if self.__balance - amount < BankAccount.__min_balance:
            return False

        self.__balance -= amount
        return True

    def transfer_money(self, amount, receiver):
        if amount > self.__balance:
            return False

        self.__balance -= amount
        receiver.deposit(amount)

        return True