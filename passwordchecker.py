import string

LOWER = 5
UPPER = 15

print("""
Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
1 or more uppercase characters
1 or more lowercase characters
1 or more numbers
and 1 or more special characters:   !@#$%^&*()_-­‐=+`~,./o'[]\<>?{}|""")

    
def CheckPass(Password):
    upper = False
    lower = False
    number = False
    wrange = False
    special = False

    for i in string.ascii_uppercase:
        if i in Password:
            upper = True
            break
    for i in string.ascii_lowercase:
        if i in Password:
            lower = True
            break
    for i in string.digits:
        if i in Password:
            number = True
            break
    for i in string.punctuation:
        if i in Password:
            special = True
            break
    if LOWER <= len(Password) <= UPPER:
        wrange = True

    if not upper: print("One Uppercase letter required")
    if not lower: print("One Lowercase letter required")
    if not number: print("One Digit required")
    if not special: print("One Special character required")
    if not wrange: print("Password need to be between {}~{} characters long".format(LOWER,UPPER))

    return True if upper and lower and number and wrange and special else False

def main():
    while True:
        password = input("Enter password : ")
        if CheckPass(password):
            print("Valid password = %s" % password)
            break

main()
