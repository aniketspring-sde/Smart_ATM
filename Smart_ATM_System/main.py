from src.bankaccount import BankAccount


def main():

    ani = BankAccount("Aniket", 1000)
    amit = BankAccount("Amit", 100)

    print("Before transfer:")
    print("Aniket:", ani.check_balance())
    print("Amit:", amit.check_balance())

    if amit.transfer_money(50, ani):
        print("Transfer successful")
    else:
        print("Insufficient balance")

    print("After transfer:")
    print("Aniket:", ani.check_balance())
    print("Amit:", amit.check_balance())

    if amit.withdraw(50):
        print("Withdrawal successful")
    else:
        print("Minimum balance must be maintained")

    print("Amit:", amit.check_balance())


if __name__ == "__main__":
    main()