
lower,upper = input("Enter a number (10 --- 100):").strip().split(" ")

for i in range(int(lower),int(upper)+1):
    print("| {} : {} |".format(i,chr(i)))