#Determines if user input is odd or even

input = int(input("Enter an integer. "))
#Insert error catching line here
eval = input % 2
if eval == 0:
    #Extras
    if input % 4 == 0:
        print("The input is an even number divisible by 4.")
    else:
        print("The input is an even number.")
else:
    print("The input is an odd number.")
