Picture of Python Programming - break statement
# using the break statement

#  create a list of operating system names
operatingsystems = ["debian","ubuntu","opensuse","linuxmint","redhat","fedora",
                    "pclinuxos","clearos","centos","netbsd",
                    "freebsd", "openbsd", "kali"]

# create list that is going to be built by the program
# this list will have all of the operating systems with the letter "N" in it
OsesWithLetterN = []

# create 2 "for loops"
# start outer "for loop" below
# take each operating system name in the list into "for loop"
for alpha in operatingsystems:
    # if we set this to true, it would never get to the 2nd "if" statement
    haveletterN = False
    # start inner "for loop" below
    for character in alpha:
        # take each character and and check to see if it is the letter "n"
        if character in ["n"]:
            haveletterN = True
            # if it is the letter "n", add operating system name to new list
            OsesWithLetterN.append(alpha)
            print ("Found an operating system with 'n' in it:", alpha)
            break
        # this "if statement" prints out each letter to prove that it is not the letter "n"
        if haveletterN == False:
            print (character, "is not the letter 'n'.")

# print out the list of all the operating systems with the letter "n" in it
print ("The operating systems that have the letter 'n' in it are:", OsesWithLetterN)
