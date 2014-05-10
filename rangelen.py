# Program using range and len

# Create a list
linuxdistros = ["ubunutu", "debian", "linuxmint", "knoppix", "puppy", "fedora",
               "redhat", "kali", "pclinuxos", "gentoo", "slackware", "dsl"]

print (linuxdistros)

# find the length of the list
lengthlinuxdistros = len(linuxdistros)
print ("The length of the linuxdistro list is:", lengthlinuxdistros)

# find the length of list to determine the number for range
for n in range(len(linuxdistros) ):
    print ("Linux distros:", n )

# print the list
print ("\nThe linuxdistro list is: ")
number = 1
for alpha in linuxdistros:
    print (number,":",alpha)
    number = number + 1
