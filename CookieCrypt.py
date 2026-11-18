cookie = ""

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

def crypt(statistic):
    global cookie
    crypted_password = ""
    password = statistic["password"]
    del statistic["password"]
    cookie += "DO_NOT_SHARE_THIS:___"
    key, number = key_gen()
    for i in statistic:
        crypted = statistic[i]
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
    with open("Cookie.txt", "a") as file:
        file.write(f"{cookie}\n")
    cookie = ""