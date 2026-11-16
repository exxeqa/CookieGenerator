cookie = ""

def crypt(statistic):
    global cookie
    with open("Cookie.txt", "w") as file:
        pass
    crypted_password = ""
    password = statistic["password"]
    del statistic["password"]
    cookie += "DO_NOT_SHARE_THIS:___"
    for i in statistic:
        crypted = statistic[i]
        crypted *= 19
        cookie += str(crypted)
        cookie += "~|~"
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in password:
        letter = alph.index(i)
        crypted_password += alph[(letter + 8) % len(alph)]
    cookie += str(crypted_password)
    cookie += "___"
    with open("Cookie.txt", "w") as file:
        file.write(cookie)
    cookie = ""