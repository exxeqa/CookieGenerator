encrypted_password = ""

def stat_res():
    global statistic
    statistic = {
        "purchases": 0,
        "likes": 0,
        "chats": 0,
        "password": ""
    }

def encrypt_password(crypt_password):
    global encrypted_password
    encrypted_password = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in crypt_password:
        letter = alph.index(i)
        encrypted_password += alph[(letter - 8) % len(alph)]
    return encrypted_password

def encrypt(mode, cookie):
    statistic = {
        "purchases": 0,
        "likes": 0,
        "chats": 0,
        "password": ""
    }
    for i in range(0, len(cookie)):
        encrypt_cookie = cookie[i]
        encrypt_cookie = encrypt_cookie.split("___")[1]
        encrypt_cookie = encrypt_cookie.split("~|~")
        statistic["purchases"] += int(encrypt_cookie[0]) / 19
        statistic["likes"] += int(encrypt_cookie[1]) / 19
        statistic["chats"] += int(encrypt_cookie[2]) / 19
        password = encrypt_password(encrypt_cookie[3])
        statistic["password"] = password
        with open("decryptedCookie_stats.txt", "a") as file:
            file.write(str(statistic))

def encrypt_menu():
    while True:
        try:
            choose = int(input(f"Choose encyption mode\n1. String encrypt (cookie ---> stats)\n2. Multi encypt from file"))
        except ValueError:
            print("Please enter a number")
            continue
        if choose == 1:
            cookie = input("Enter all Cookie: ")
            encrypt(choose, cookie)
            break
        elif choose == 2:
            with open("Cookie.txt", "r") as file:
                cookie = file.read().splitlines()
            encrypt(choose, cookie)
        else:
            print("Please enter a number between 1 and 2")
            continue