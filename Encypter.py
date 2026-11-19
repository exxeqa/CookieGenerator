encrypted_password = ""

def stat_res():
    global statistic
    statistic = {
        "purchases": 0,
        "likes": 0,
        "chats": 0,
        "password": ""
    }

def decryptedCookieFileReset():
    with open("decryptedCookie_stats.txt", "w") as f:
        pass

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
    decryptedCookieFileReset()
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
        statistic["purchases"] = round(int(encrypt_cookie[0]) / key)
        statistic["likes"] = round(int(encrypt_cookie[1]) / key)
        statistic["chats"] = round(int(encrypt_cookie[2]) / key)
        password = encrypt_password(encrypt_cookie[3], key)
        statistic["password"] = password
        with open("decryptedCookie_stats.txt", "a") as file:
            file.write(str(f"{statistic}\n"))
        if mode == 1:
            print(str(statistic))

def encrypt_menu():
    while True:
        try:
            choose = int(input(f"Choose encryption mode\n1. String encrypt (cookie ---> stats)\n2. Multi encrypt from file"))
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
            break
        else:
            print("Please enter a number between 1 or 2")
            continue