# ThouCount.py
print ("This program will count the number of 'Thou' and 'thou' in ")
print ("the works of Shakespeare.")
thefile = open("Shakespeare.txt")
ThouCount = 0

# for each line in the file
for line in thefile:
    # split the line into words
    splitline = line.split()
    # check to see if word is "Thou" or "thou"
    for word in splitline:
        if word == ("thou"):
            print("Instance of lowercase thou found!")
            ThouCount = ThouCount + 1
            print ("Count is:", ThouCount)
        elif word == ("Thou"):
            print ("Instance of Thou with capital 'T' found")
            ThouCount = ThouCount + 1
            print ("Count is:", ThouCount)
            
print ("The total count of 'Thou' and 'thou' in all of Shakespeare's works is:", ThouCount)
