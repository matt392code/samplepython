print("This program will print out each letter in an entered word or phrase.")
    
EnteredString = input("Enter a word or phrase: ")
    
print ("The string entered is: ", EnteredString)
    
# This for loop will print out each letter on a line
for EachLetter in EnteredString:
    print("The letter is:", EachLetter)
        
LengthOfString = len(EnteredString)
print ("The number of characters is: ", LengthOfString)
