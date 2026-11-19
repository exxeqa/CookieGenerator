import random
from statistics import mode
from CookieCrypt import crypt_menu, crypt
from Encypter import encrypt_menu

alph = "abcdefghijklmnopqrstuvwxyz"

def stat_res():
    global statistic
    statistic = {
        "purchases": 0,
        "likes": 0,
        "chats": 0,
        "password": ""
    }

def CookieFileReset():
    with open("Cookie.txt", "w") as f:
        pass

def SessionFileReset():
    with open("SessionStatistic.txt", "w") as f:
        pass

def random_activity_gen(generations, mode):
    global statistic
    print(mode)
    print(generations)
    stat_res()
    CookieFileReset()
    SessionFileReset()
    for gen in range(generations):
        password = ""
        statistic["purchases"] += random.randint(0, 95)
        statistic["likes"] += random.randint(0, 250)
        statistic["chats"] += random.randint(0, 55)
        for i in range(random.randint(8, 16)):
            password += "".join(random.choice(alph))
        statistic["password"] = password
        with open("SessionStatistic.txt", "a") as f:
            f.write(str(f"{statistic}\n"))
        if mode == 1:
            print(statistic)
        stat_res()
    print(mode)
    if mode == 2:
        crypt(statistic, mode)

def activity_gen_menu():
    while True:
        try:
            choose = int(input("Choose mode\n1.Single generation\n2.Multi random active generations + auto convert to cookie"))
        except ValueError:
            print("Enter a number!")
            continue
        if choose == 1:
            amount = 1
            random_activity_gen(amount, choose)
            break
        if choose == 2:
            while True:
                try:
                    amount = int(input("Generations amount"))
                except ValueError:
                    print("Enter a number!")
                    continue
                random_activity_gen(amount, choose)
                break
        break

def start():
    while True:
        try:
            choose = int(input(f"choose mode\n1.Activity gen menu\n2.Crypt menu\n3.Encrypt menu\n4.Encrypt result\n5.Exit"))
            if choose == 1:
                activity_gen_menu()
                continue
            elif choose == 2:
                crypt_menu()
                continue
            elif choose == 3:
                encrypt_menu()
                continue
            elif choose == 4:
                with open("decryptedCookie_stats.txt", "r") as f:
                    print(f.read())
            elif choose == 5:
                break
            else:
                print("choose must be 1 - 5")
                continue
        except ValueError:
            print("Enter a number!")
            continue

start()