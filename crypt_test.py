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
        alph = "abcdefghijklmnopqrstuvwxyz"
        topA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        snum = "1234567890"
        symbol_sp = "!@#$^%&*(){}:[]<>?,./|`~-_"
        crypted_stat = ""
        key, number = key_gen()
        for numberX in str(number)[:3]:
            for i in stat:
                crypted = stat[i]
                crypted *= number
                crypted_stat = ""
                for numberY in str(crypted):
                    letter = alph[(int(numberY) + int(numberX)) % len(alph)]
                    crypted_stat += letter
            cookie += str(crypted_stat)
            cookie += "~|~"
        for i in password:
            if i in alph:
                letter = alph.index(i)
                crypted_password += alph[(letter + number) % len(alph)]
            elif i in topA:
                letter = topA.index(i)
                crypted_password += topA[(letter + number) % len(topA)]
            elif i in snum:
                letter = snum.index(i)
                crypted_password += snum[(letter + number) % len(snum)]
            elif i in symbol_sp:
                letter = symbol_sp.index(i)
                crypted_password += symbol_sp[(letter + number) % len(symbol_sp)]
        if password == crypted_password:
            crypted_password = ""
            for i in password:
                letter = alph.index(i)
                crypted_password += alph[(letter + (number - 1)) % len(alph)]

        cookie += str(crypted_password)
        cookie += "___"
        cookie += key

        print(cookie)
        cookie = ""

crypt("", 2)

def encrypt_key(crypted_key):
    key = crypted_key.split(".")[1]
    numbers = ""
    for i in key:
        if i in "1234567890":
            numbers += i
        else:
            pass
    x = 2
    key = ""
    for i in numbers:
        if x % 2 == 0:
            key += i
        x += 1
    return int(key)

# exp. DO_NOT_SHARE_THIS:___1804418~|~5249216~|~1265436~|~pjjislcrhnihcawd___XxX-KEY.23c*@39kn>47ug?@-30wju&%(42u%_~

def encrypt_password(crypt_password, key):
    global encrypted_password
    encrypted_password = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    topA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    snum = "1234567890"
    symbol_sp = "!@#$^%&*(){}:[]<>?,./|`~-_"
    for i in crypt_password:
        if i in alph:
            letter = alph.index(i)
            encrypted_password += alph[(letter - key) % len(alph)]
        elif i in topA:
            letter = topA.index(i)
            encrypted_password += topA[(letter - key) % len(topA)]
        elif i in snum:
            letter = snum.index(i)
            encrypted_password += snum[(letter - key) % len(snum)]
        elif i in symbol_sp:
            letter = symbol_sp.index(i)
            encrypted_password += symbol_sp[(letter - key) % len(symbol_sp)]
    return encrypted_password

def encrypt(mode, cookie):
    alph = "abcdefghijklmnopqrstuvwxyz"
    statistic = {
        "purchases": 0,
        "likes": 0,
        "chats": 0,
        "password": ""
    }
    if mode == 1:
        encrypts_amount = 1
    elif mode == 2:
        encrypts_amount = len(cookie)
    for i in range(encrypts_amount):
        if mode == 1:
            encrypt_cookie = cookie
        elif mode == 2:
            encrypt_cookie = cookie[i]
        crypted_key = encrypt_cookie.split("___")[2]
        key = encrypt_key(crypted_key)
        encrypt_cookie = encrypt_cookie.split("___")[1]
        encrypt_cookie = encrypt_cookie.split("~|~")
        if encrypt_cookie and encrypt_cookie[-1] == "":
            encrypt_cookie.pop()
        x = 0
        encrypt_stat = ""
        first_digit = int(str(key)[0])
        stats_decoded = []
        for numberX in str(key)[:1]:
            x += 1
            for numberY in encrypt_cookie[:3]:
                for y in numberY:
                    numb = (alph.index(y) - first_digit) % len(alph)
                    encrypt_stat += str(numb)
                stats_decoded.append(round(int(encrypt_stat) / key))
                encrypt_stat = ""
        statistic["purchases"] = stats_decoded[0]
        statistic["likes"] = stats_decoded[1]
        statistic["chats"] = stats_decoded[2]
        password = encrypt_password(encrypt_cookie[3], key)
        statistic["password"] = password
        print(str(statistic))

with open("Cookie.txt", "r") as file:
    cock = file.read().splitlines()
encrypt(2, cock)