
# password strenght checker 


password=input("enetr your password :")




p_len=len(password)

if p_len<6:
    print("your passwprd is weak")
elif p_len<10:
    print(" your password is medium")
elif p_len>10:
    print("your passwprd is strong ")

    