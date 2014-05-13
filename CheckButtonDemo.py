# Program to demonstrate check buttons in Python

# Import the tkinter module for GUI components
from tkinter import *

# Create CheckButtonDemo class based on the Frame class
class CheckButtonDemo(Frame):
    def __init__(self, master):
        super(CheckButtonDemo, self).__init__(master)
        # Link frame to grid manager
        self.grid()
        # Create a Label
        Label(self, text="This is a check button demostration program.", font="Calibri 14").grid(row=1, sticky=N, columnspan=2)

        # Empty row
        Label(self).grid(row=2)

        # Set up label for entry widget
        Label(self, text="Click one or more check buttons below:", font="Calibri 12").grid(row=3, column=0,sticky=W)
        
        # 1st Tk class variable as BooleanVar() object to store 1st check button selection
        self.firstcheckbutton = BooleanVar()
        
        # Create check buttons to run methods when clicked
        # 1st check button
        Checkbutton(self, text="1st button", variable=self.firstcheckbutton, command=self.firstcheckbuttonselection).grid(row=6, column=0, sticky=W)

        # 2nd Tk class variable as BooleanVar() object to store check button selection and create 2nd check button
        self.secondcheckbutton = BooleanVar()
        Checkbutton(self, text="2nd button", variable=self.secondcheckbutton, command=self.secondcheckbuttonselection).grid(row=7, column=0, sticky=W)

        # 3rd Tk class variable as BooleanVar() object to store check button selection and create 3rd check button
        self.thirdcheckbutton = BooleanVar()
        Checkbutton(self, text="3rd button", variable=self.thirdcheckbutton, command=self.thirdcheckbuttonselection).grid(row=8, column=0, sticky=W)

        # 4th Tk class variable as BooleanVar() object to store check button selection and create 4th radio button
        self.fourthcheckbutton = BooleanVar()
        Checkbutton(self, text="4th button", variable=self.fourthcheckbutton, command=self.fourthcheckbuttonselection).grid(row=9, column=0, sticky=W)

        # 1st message box/text widget object
        self.firstcheckbuttontextwidget = Text(self, width=45, height=1)
        self.firstcheckbuttontextwidget.grid(row=11, column=0, columnspan=2, sticky=N)

        # 2nd message box/text widget object
        self.secondcheckbuttontextwidget = Text(self, width=45, height=1)
        self.secondcheckbuttontextwidget.grid(row=12, column=0, columnspan=2, sticky=N)

        # 3rd message box/text widget object
        self.thirdcheckbuttontextwidget = Text(self, width=45, height=1)
        self.thirdcheckbuttontextwidget.grid(row=13, column=0, columnspan=2, sticky=N)

        # 4th message box/text widget object
        self.fourthcheckbuttontextwidget = Text(self, width=45, height=1)
        self.fourthcheckbuttontextwidget.grid(row=14, column=0, columnspan=2, sticky=N)


    # 1st check button method that will be called when 1st check button is selected
    def firstcheckbuttonselection(self):
        # Take what was entered into "firstcheckbutton" and put it into "selection" variable
        selection = self.firstcheckbutton.get()
        firstcheckbuttonmessage = "1 means you checked the 1st button: ", selection
        # Delete what was in the text widget box
        self.firstcheckbuttontextwidget.delete(0.0, END)
        # Print out/send "firstcheckbuttonmessage" variable to text widget object 
        self.firstcheckbuttontextwidget.insert(0.0, firstcheckbuttonmessage)

    # 2nd check button method that will be called when 2nd check button is selected
    def secondcheckbuttonselection(self):
        # Take what was entered into "secondcheckbutton" and put it into "selection" variable
        selection = self.secondcheckbutton.get()
        secondcheckbuttonmessage = "1 means you checked the 2nd button: ", selection
        # Delete what was in the text widget box
        self.secondcheckbuttontextwidget.delete(0.0, END)
        # Print out/send "secondcheckbuttonmessage" variable to text widget object 
        self.secondcheckbuttontextwidget.insert(0.0, secondcheckbuttonmessage)

    # 3rd check button method that will be called when 3rd check button is selected
    def thirdcheckbuttonselection(self):
        # Take what was entered into "thirdcheckbutton" and put it into "selection" variable
        selection = self.thirdcheckbutton.get()
        thirdcheckbuttonmessage = "1 means you checked the 3rd button: ", selection
        # Delete what was in the text widget box
        self.thirdcheckbuttontextwidget.delete(0.0, END)
        # Print out/send "thirdcheckbuttonmessage" variable to text widget object 
        self.thirdcheckbuttontextwidget.insert(0.0, thirdcheckbuttonmessage)

    # 4th check button method to be called when 4th check button is selected
    def fourthcheckbuttonselection(self):
        # Take what was entered into "fourthcheckbutton" and put it into "selection" variable
        selection = self.fourthcheckbutton.get()
        fourthcheckbuttonmessage = "1 means you checked the 4th button!", selection
        # Delete what was in the text widget box
        self.fourthcheckbuttontextwidget.delete(0.0, END)
        # Print out/send "selection" variable to text widget object 
        self.fourthcheckbuttontextwidget.insert(0.0, fourthcheckbuttonmessage)


# Main program
# Create a window; create an object called "root"
root = Tk()

# title of the GUI window
root.title("Check buttons demonstration.")

# dimensions of the window
root.geometry("400x400")

# create CheckButtonDemo object
checkbuttongroup1 = CheckButtonDemo(root)

# command that will launch the GUI application
root.mainloop()
