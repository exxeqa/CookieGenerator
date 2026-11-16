import random
import time

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

def start():
    while True:
        try:
            choose = int(input(f"choose mode\n1.Random activity\n2.Real activity"))
            if choose == 1:
                random_activity()
                break
            elif choose == 2:
                break
            else:
                print("choose must be 1 or 2")
                continue
        except ValueError:
            print("Enter a number!")
            continue

start()