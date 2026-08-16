from src.bankaccount import BankAccount


def main():
    ani = BankAccount(name="Aniket", balance=1000)
    amit = BankAccount(name="Amit", balance=100)

    print(f"Aniket's balance before transfer: {ani.check_balance()}")
    print(f"Amit's balance before transfer: {amit.check_balance()}")
    print()

    amit.transfer_money(50,ani)

    print(f"Aniket's balance after transfer: {ani.check_balance()}")
    print(f"Amit's balance after transfer: {amit.check_balance()}")

    amit.withdraw(50)
    print(f"Amit's balance after withdraw: {amit.check_balance()}")



if __name__ == "__main__":
    main()