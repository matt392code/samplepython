# Program to demonstrate radio buttons in Python

# Import the tkinter module for GUI components
from tkinter import *

# Create RadioButtonDemo class based on the Frame class
class RadioButtonDemo(Frame):
    def __init__(self, master):
        super(RadioButtonDemo, self).__init__(master)
        # Link frame to grid manager
        self.grid()
        # Create a Label
        Label(self, text="This is a radio button demostration program.", font="Calibri 14").grid(row=1, sticky=N, columnspan=2)

        # Empty row
        Label(self).grid(row=2)

        # Set up label for entry widget
        Label(self, text="Click radio button below:", font="Calibri 12").grid(row=3, column=0,sticky=W)
        
        # *** Create Tk class variable as StringVar object to store radio button selection ***
        self.radiobuttonstorage = StringVar()
        
        # Create radio buttons to run "radiobuttonselection" method when clicked
        # Create 1st radio button
        Radiobutton(self, text="1st button", variable=self.radiobuttonstorage, value="1st button", command=self.radiobuttonselection).grid(row=6, column=0, sticky=W)

        # Create 2nd radio button
        Radiobutton(self, text="2nd button", variable=self.radiobuttonstorage, value="2nd button", command=self.radiobuttonselection).grid(row=7, column=0, sticky=W)

        # Create 3rd radio button
        Radiobutton(self, text="3rd button", variable=self.radiobuttonstorage, value="3rd button", command=self.radiobuttonselection).grid(row=8, column=0, sticky=W)

        # Create 4th radio button
        Radiobutton(self, text="4th button", variable=self.radiobuttonstorage, value="4th button", command=self.radiobuttonselection).grid(row=9, column=0, sticky=W)

        # Set up label for message box/text widget object
        Label(self, text="The button you selected is:", font="Calibri 12").grid(row=10, column=0, sticky=W)
        # Set up message box/text widget object
        self.radiobuttonmessage = Text(self, width=45, height=1)
        self.radiobuttonmessage.grid(row=11, column=0, columnspan=2, sticky=N)

    # Method to be called when radio button is selected
    def radiobuttonselection(self):
        # Take what was entered into "radiobuttonstorage" and put it into "selection" variable
        selection = self.radiobuttonstorage.get()
        # Delete what was in the text widget box
        self.radiobuttonmessage.delete(0.0, END)
        # Print out/send "selection" variable to text widget object 
        self.radiobuttonmessage.insert(0.0, selection)

# Main program
# Create a window; create an object called "root"
root = Tk()

# title of the GUI window
root.title("Radio buttons demonstration.")

# dimensions of the window
root.geometry("400x400")

# create ButtonDemo object
buttongroup1 = RadioButtonDemo(root)

# command that will launch the GUI application
root.mainloop()
