cookie = ""

import ast
import random

def key_gen():
    alph = "abcdefghijklmnopqrstuvwxyz"
    spec = "_!@#$%^&*()-{}[]<>?"
    number = random.randint(359, 23494)
    key = ""
    for i in str(number):
        key += i
        key += str(random.randint(0,9))
        for letter in range(random.randint(1, 3)):
            key += "".join(random.choice(alph))
        for symbol in range(random.randint(1, 3)):
            key += "".join(random.choice(spec))
    key = f"XxX-KEY.{key}~"
    return key, number



def crypt(statistic, mode):
    global cookie
    amount = 0

    if mode == 1:
        amount = 1
    elif mode == 2:
        with open("SessionStatistic.txt", "r") as file:
            statistic = file.read().splitlines()
        amount = len(statistic)

    for x in range(0, amount):
        if mode == 1:
            stat = ast.literal_eval(statistic)
        elif mode == 2:
            stat_str = statistic[x]
            stat = ast.literal_eval(stat_str)
        crypted_password = ""
        password = stat["password"]
        del stat["password"]
        cookie += "DO_NOT_SHARE_THIS:___"
        key, number = key_gen()
        for i in stat:
            crypted = stat[i]
            crypted *= number
            cookie += str(crypted)
            cookie += "~|~"
        alph = "abcdefghijklmnopqrstuvwxyz"

        for i in password:
            letter = alph.index(i)
            crypted_password += alph[(letter + number) % len(alph)]
        if password == crypted_password:
            crypted_password = ""
            for i in password:
                letter = alph.index(i)
                crypted_password += alph[(letter + (number - 1)) % len(alph)]

        cookie += str(crypted_password)
        cookie += "___"
        cookie += key

        if mode == 1:
            print(cookie)
        elif mode == 2:
            with open("Cookie.txt", "a") as file:
                file.write(f"{cookie}\n")

        cookie = ""

def crypt_menu():
    while True:
        try:
            choose = int(input(f"Choose encyption mode\n1. String crypt (stats ---> cookie)\n2. Multi file crypt"))
        except ValueError:
            print("Please enter a number")
            continue
        if choose == 1:
            statistic = input("Enter a statistic: ")
            crypt(statistic, choose)
            break
        elif choose == 2:
            with open("SessionStatistic.txt", "r") as file:
                statistic = file.read().splitlines()
            crypt(statistic, choose)
            break
        else:
            print("Please enter a number between 1 and 2")
            continue