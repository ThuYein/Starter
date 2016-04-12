
name = input("Enter Name : ").strip()
with open("name.txt","w") as fname:
    fname.write(name)

print("--------")
print("Reading file : name.txt")
namefound = open("name.txt","r").read()
print("Your name is : %s" % namefound)

print("--------")
print("Writing 17 & 42 inside number.txt")
with open("numbers.txt","w") as number:
    number.write(str(17)+"\n"+str(42)+"\n")

print("--------")
print("Reading and counting the sum")
numberlist = [int(i.strip("\n")) for i in open("numbers.txt","r").readlines()]

print("Sum is : %d" % sum(numberlist))