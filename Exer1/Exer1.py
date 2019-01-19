#Character Input
#User enters input and number of copies to be printed

NameInput = input("Input your name: ")
AgeInput = int(input("Input your age: "))
Yearby100 = str(2019 + (100-AgeInput))
print(NameInput + ", you will turn 100 years old in " + Yearby100)


#Extras
#CharInput = input("Input characters: ")
#CopyInput = int(input("Input number of copies: "))
#Simple Way
#print(CopyInput*(CharInput+"\n"))

#Better Output - no blank at the end
#for i in range(CopyInput):
#    print(CharInput)
#    if i == CopyInput:
#        break
