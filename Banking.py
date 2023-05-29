import pprint

baris = {
    "account_id": 2003,
    "username": "bsever",
    "password": "hebanuren1",
    "full_name": "Barış Sever",
    "account_balance": 5000,
    "additional_balance": 1000
}

nursel = {
    "account_id": 1976,
    "username": "nsever",
    "password": "hebanuren2",
    "full_name": "Nursel Sever",
    "account_balance": 7500,
    "additional_balance": 1000
}

helin = {
    "account_id": 2008,
    "username": "hsever",
    "password": "hebanuren3",
    "full_name": "Helin Sever",
    "account_balance": 2500,
    "additional_balance": 1000
}

enver = {
    "account_id": 1975,
    "username": "esever",
    "password": "hebanuren4",
    "full_name": "Enver Sever",
    "account_balance": 10000,
    "additional_balance": 1000
}

users = [enver, baris, helin, nursel]


def sign_in(username: str, password: str) -> dict:

    for i in users:
        if i["username"] == username and i["password"] == password:
            account = i
            return account
            break
    else:
        print("Wrong password or username!")


def show_balance(account: dict):

    print(f"Hello {account['full_name'].split()[0]}, your balance is {account['account_balance']} and your additional balance is {account['additional_balance']}")


def withdraw_money(account: dict, amount: int):

    if account["account_balance"] >= amount:
        print(f"Withdrawing {amount} from your account, please take the money!")
        account["account_balance"] -= amount
        show_balance(account)
    else:
        if account["account_balance"] + account["additional_balance"] >= amount:
            while True:
                douwanna = input("You have additional balance, do you wanna use it? ")
                if douwanna == "yes":
                    print(f"Withdrawing {amount} from your account, please take the money!")
                    account["additional_balance"] = account["additional_balance"] - (amount - account["account_balance"])
                    account["account_balance"] = 0
                    show_balance(account)
                    break
                elif douwanna == "no":
                    break
                else:
                    print("Please enter yes or no.")
        elif account["account_balance"] + account["additional_balance"] < amount:
            print("You have insufficient balance.")


def send_money(account: dict, iban: int, amount: int):
    for i in users:
        if iban == i["account_id"]:
            send_acc = i
            if account["account_balance"] >= amount:
                print(f"Sending {amount} from your account to {send_acc['username']}")
                account["account_balance"] -= amount
                send_acc["account_balance"] += amount
                show_balance(account)
                break
            else:
                if account["account_balance"] + account["additional_balance"] >= amount:
                    while True:
                        douwanna = input("You have additional balance, do you wanna use it?")
                        if douwanna == "yes":
                            print(f"Sending {amount} from your account to {send_acc['username']}")
                            account["additional_balance"] = account["additional_balance"] - (amount - account["account_balance"])
                            account["account_balance"] = 0
                            send_acc["account_balance"] += amount
                            show_balance(account)
                            break
                        elif douwanna == "no":
                            break
                        else:
                            print("Please enter yes or no.")
                    break
                elif account["account_balance"] + account["additional_balance"] < amount:
                    print("You have insufficient balance.")
                    break
    else:
        print("You have entered a wrong account id!")


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    account = sign_in(username, password)
    if account is not None:
        while True:
            process = input("Enter a process: ")
            if process == "show balance":
                show_balance(account)
            elif process == "withdraw":
                amount = int(input("Enter a amount to withdraw: "))
                withdraw_money(account, amount)
            elif process == "send money":
                iban = int(input("Enter an account id that you want to send money: "))
                amount = int(input("Enter a amount to send: "))
                send_money(account, iban, amount)
            elif process == "exit":
                break
            else:
                print("Enter a proper process.")


main()
