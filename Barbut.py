import random
from random import choice, randint

bot_list = ['Ekrem Abi', 'Ganyotçu', 'Hüseyin Kardeş', 'Sabri Abi', 'Galerici Şahin']
from random import randint
from pprint import pprint

users = {
    1: {
        "email": "email",
        "password": "password",
        "safe": 1000000000
    },

    2: {
        "email": "johndoe@email.com",
        "password": "pass123",
        "safe": 1000000000000
    }
}


def dice_game(bet: int, dict_id: int, bot: str) -> int:

    min_bet = 100
    max_bet = users[dict_id]["safe"]
    result = 0
    if max_bet >= bet >= min_bet:
        print("Rolling dice ...")
        users_dice = random.randint(1, 6)
        print(f"You have rolled {users_dice}")
        print(f"Now {bot} is rolling dice ...")
        bots_dice = random.randint(1, 6)
        print(f"{bot} has rolled {bots_dice}")
        if users_dice > bots_dice:
            result = 1
        elif bots_dice > users_dice:
            result = 2
        elif bots_dice == users_dice:
            result = 0

        return result
    else:
        print("You have entered a wrong bet!")

def play_again(douwanna: str) -> int:

    if douwanna == "yes":
        flag = 1
    elif douwanna == "no":
        flag = 0
    else:
        flag = 2
    return flag


def check_email():

    user_name_list = []
    for i in range(1, len(users) + 1):
        user_name_list.append(users.get(i).get("email"))

    return user_name_list


def sign_up(email: str, password: str) -> None:
    """
    sign up man
    :param email: str
    :param password: str
    :param password_again: str
    :return:
    """
    if email in check_email():
        print("Email has already been used")
    else:
        users[len(users) + 1] = {
            "email": email,
            "password": password,
            "safe": 100000
                }
        print(f"Thanks for signing up !")


def sign_in(email=str, password=str):
    """
    sign in
    :param email: str
    :param password: str
    :return: None
    """
    flag = 0
    for i in range(1, len(users) + 1):
        if email == users[i].get("email") and password == users[i].get("password"):
            dict_id = i
            flag += 1
    if flag >= 1:
        print("Welcome Home, you have gained your daily login bonus 100$")
        users[dict_id]["safe"] += 100
        while True:
            wanna_play = input("Do you wanna a play a game? ")
            if wanna_play.lower() == "yes":
                bot = choice(bot_list)
                print(f"You have matched with {bot}")
                bet = int(input(f"Please enter a bet between 100 and {users[dict_id]['safe']}: "))
                res = dice_game(bet, dict_id, bot)
                if res == 1:
                    print("You have won!")
                    users[dict_id]["safe"] += bet
                    print(f"You have {users[dict_id]['safe']}$")
                elif res == 2:
                    print("You have lost :(")
                    users[dict_id]["safe"] -= bet
                    print(f"You have {users[dict_id]['safe']}$")
                elif res == 0:
                    print("It is a draw")
                    print(f"You have {users[dict_id]['safe']}$")
            elif wanna_play.lower() == "no":
                break
            else:
                print("Please enter yes or no")
    else:
        print("Wrong email or password!")


def main():
    while True:
        process = input("Enter a process: ")
        if process == "exit":
            break
        elif process.lower() == "sign in":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            sign_in(email, password)
        elif process.lower() == "sign up":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            sign_up(email, password)
        elif process.lower() == "read":
            pprint(users)
        else:
            print("Enter a proper process!")


main()
