# Demo of if-elif-else loop

# Have user enter a number
numberentered = input("Please enter a number: ")
# print "The number entered was: ", numberentered

# Start if-elif-else loop
if (numberentered >0) and (numberentered<10):
    print "The number is between 0 and 10."
elif numberentered < 0:
    print "The number is less than 0."
elif numberentered >10:
    print "The number entered was greater than 10."
elif numberentered == 10:
    print "The number entered was 10."
else :
    print "The number entered was 0."

print "The number entered was: ", numberentered
