class BankAccount:

    __min_balance = 100
    def __init__(self, name:str, balance:float):
        self.name = name
        self.__balance = balance

    def deposit(self, amount:float | int):
        self.__balance += amount

    def check_balance(self):
        return self.__balance

    def withdraw(self, amount:float | int):
        if self.__balance <= BankAccount.__min_balance:
            print(f"Minimum balance need to maintain is {BankAccount.__min_balance} and your balance is : {self.check_balance()}")
            print("If you want to continue the withdraw, press 1 ")
            print("If you want to cancel the withdraw, press 2 ")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if amount > self.__balance:
                    print("Insufficient balance")
                else:
                    self.__balance -= amount
            elif choice == 2:
                print("Withdrawal cancelled")


    def transfer_money(self, amount:float|int, reciever:BankAccount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            reciever.deposit(amount)
            self.__balance -= amount
