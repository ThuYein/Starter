number = input("Enter a number (10-50) : ")

while not number.isdecimal() or not 10<number<50:
    print("Please enter a valid number!")
    number = input("Enter a number (10-50) : ")
number = int(number)

print("{}".format(chr(number)))
# for i in range(int(lower),int(upper)+1):
#     print("| {} : {} |".format(i,chr(i)))
