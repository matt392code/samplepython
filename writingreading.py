print ("We are going to write and read a file. ")
keepgoing = "y"
while keepgoing == "y":
     shortsent = input("Enter a short sentence. ")
     # open a text file to append
     openfile = open("testfile.txt", "a")
     # write sentence to file
     openfile.write(shortsent)
     openfile.close()
     keepgoing  =  input("Enter another? y or n: ")
     print ("The sentence entered is: ", shortsent)

# open the file to read
openfile = open("testfile.txt")
# read the file into a variable
linesread = openfile.readlines()
print ("The file now reads: ", linesread)
