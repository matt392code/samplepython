# Dictionaries in Python; exercise from Chapter 3 in "Learn Python Quickly"
# Have a few for loops in these that can print values vertically

print ("Creating dictionary now.")
telnums = {}

print ("Populating the dictionary.")
telnums = {"Bob":"867-5209", "Cheryl":"555-3434", "Tammy":"765-3232", "Susan":"876-4545", "Caroline":"987-2312"}

print ("The dictionary is: ")
print (telnums.items())

print ("The dictionary printed vertically is: ")
for alpha in telnums:
    print(alpha, telnums[alpha] )
   
print ("Now we are going to update Bob.")
telnums["Bob"] = "786-9025"

print ("Changing Bob:")
print (telnums.items())

print ("Now we are going to retrieve a phone number for Bob:")
print (telnums ["Bob"] )

print ("Deleting Bob from dictionary.")
del telnums["Bob"]

print ("The dictionary now reads: ")
print (telnums.items() )

print ("Listing the dictionary key names:")
print (telnums.keys() )

print ("Printing the key names vertically: ")
for item in telnums:
    print (item)

print ("Vertical list of the phone numbers: ")
for item in telnums:
    print (telnums[item])

print ("Empty the dictionary: ")
telnums.clear()
print ("Checking to see if it has been cleared: ")
print (telnums.items() )
