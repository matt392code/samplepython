Short program that demonstrates use of lists in Python.

# testing lists
operatingsystems = ["Debian", "Fedora", "OpenSUSE", "Ubuntu", "LinuxMint", "FreeBSD"] 
print ("The list of operating systems is: ", operatingsystems)

number = 0

for element in operatingsystems: 
  print (("Operating system list element:"), number, "is", operatingsystems[number])
  number = number + 1
