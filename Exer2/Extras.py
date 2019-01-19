num = int(input("\nInput number: "))
check = int(input("Input checker number: "))

if num % check == 0:
    print(str(num) + " is divisible by " + str (check))
else:
    print(str(num) + " is not divisible by " + str (check))
