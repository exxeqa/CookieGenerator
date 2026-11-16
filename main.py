import random
from CookieCrypt import crypt

alph = "abcdefghijklmnopqrstuvwxyz"

statistic = {
    "purchases": 0,
    "likes": 0,
    "chats": 0,
    "password": ""
}

def random_activity():
    global statistic
    password = ""
    statistic["purchases"] += random.randint(0, 15)
    statistic["likes"] += random.randint(0, 150)
    statistic["chats"] += random.randint(0, 15)
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
            choose = int(input(f"choose mode\n1.Random activity\n2.Cookie"))
            if choose == 1:
                random_activity()
                continue
            elif choose == 2:
                with open("Cookie.txt", "r") as f:
                    print(f.read())
            else:
                print("choose must be 1 or 2")
                continue
        except ValueError:
            print("Enter a number!")
            continue

start()