import random
from CookieCrypt import crypt
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

def random_activity():
    global statistic
    stat_res()
    password = ""
    statistic["purchases"] += random.randint(0, 95)
    statistic["likes"] += random.randint(0, 250)
    statistic["chats"] += random.randint(0, 55)
    for i in range(random.randint(8, 16)):
        password += "".join(random.choice(alph))
    statistic["password"] = password
    with open("SessionStatistic.txt", "w") as f:
        f.write(str(statistic))
    crypt(statistic)
    print("Cookie created")

def start():
    while True:
        try:
            choose = int(input(f"choose mode\n1.Random activity\n2.Crypted stat -> Cookie\n3.Encrypt menu\n4.Encrypt result\n5.Exit"))
            if choose == 1:
                random_activity()
                continue
            elif choose == 2:
                with open("Cookie.txt", "r") as f:
                    print(f.read())
            elif choose == 3:
                encrypt_menu()
                continue
            elif choose == 4:
                with open("decryptedCookie_stats.txt", "r") as f:
                    print(f.read())
            else:
                print("choose must be 1 - 3")
                continue
        except ValueError:
            print("Enter a number!")
            continue

start()