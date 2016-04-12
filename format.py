def getnumber():
    num1 = input("Enter lower number (10-50): ")
    while not num1.isdecimal() or not 10<int(num1)<50:
        print("Please enter a valid number!")
        num1 = input("Enter a number (10-50): ")

    num2 = input("Enter higher number (10-50): ")
    while not num2.isdecimal() or not 10<int(num2)<50 or int(num1) > int(num2):
        print("Please enter a valid number!")
        num2 = input("Enter a number (10-50): ")
    return int(num1),int(num2)

lower, upper = getnumber()

for i in range(lower,upper+1):
    print("| {} : {} |".format(i,chr(i)))
