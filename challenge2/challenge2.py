sid = input("Enter Student ID: ")
mail = input("Enter Email ID: ")
pwd = input("Enter Password: ")
refcode = input("Enter Referral Code: ")
status = False
if len(sid)==7 and sid[0] == "C" and sid[1] == "S" and sid[2] == "E" and sid[3] == "-" and sid[4].isdigit() and sid[5].isdigit() and sid[6].isdigit():
    if  mail.count("@") == 1 and mail.count(".") >= 1 and  mail[-4] == "." and mail[-3] == "e" and mail[-2] == "d" and mail[-1] == "u" and  mail[0] != "@":
        if len(pwd) >= 8 and pwd[0].isupper() and  (pwd.count("0") >= 1 or pwd.count("1") >= 1 or pwd.count("2") >= 1 or pwd.count("3") >= 1 or pwd.count("4") >= 1 or pwd.count("5") >= 1 or pwd.count("6") >= 1 or pwd.count("7") >= 1 or pwd.count("8") >= 1 or pwd.count("9") >= 1):
            if len(refcode)==6 and refcode[0] == "R" and refcode[1] == "E" and refcode[2] == "F" and refcode[3].isdigit() and refcode[4].isdigit() and refcode[5] == "@":
                status = True
if status:
    print("APPROVED")
else:
    print("REJECTED")
