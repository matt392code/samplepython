# Licensed under the General Public License

print ("Demonstration of the break statement.")

# While loop will stay true and keep running until it is stopped by the break
# statement

while True:
    print ("Starting the loop.")
    print ("Do you want to continue the loop?")
    yesorno = input("Enter yes or no: ")
    if yesorno == "yes":
        print ("Ok, going around again!")
    elif yesorno == "no":
        print("Breaking out...now!")
        break
        # while loop will stop here
    else:
        print("Please be sure to enter yesornow, not:", yesorno)
# End while loop here

print ("Broke out of loop.")
print ("Ending program here.") 
