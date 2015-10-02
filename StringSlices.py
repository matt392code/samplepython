print ("This program will print slices (segments) of strings.")

StringEntered = input("Enter a word or phrase: ") 
StringLength = len(StringEntered) 
print ("The length of the string is: ", StringLength)

# Calculate half the length of the string and round it off 
HalfLengthOfString=StringLength/2 
RoundedNumber = round(HalfLengthOfString)
print ("Half the length of the string (rounded) is approximately: ", RoundedNumber)

# Break out the first portion 
print ("The first portion of the string is: ") 
print (StringEntered[0:RoundedNumber])

# Break out the second portion 
print ("The second portion of the string is: ") 
print (StringEntered[RoundedNumber:])
