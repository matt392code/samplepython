# Program to demonstrate entry, button and text widgets in Python

# Import the tkinter module for GUI components
from tkinter import *

# Create ButtonDemo class based on the Frame class
class ButtonDemo(Frame):
    def __init__(self, master):
        super(ButtonDemo, self).__init__(master)
        # Link frame to grid manager
        self.grid()
        # Create a Label
        Label(self, text="This is a button demostration program.", font="Calibri 14").grid(row=1, sticky=N, columnspan=2)

        # Empty row
        Label(self).grid(row=2)

        # Set up label for entry widget
        Label(self, text="Enter test text:", font="Calibri 12").grid(row=3, column=0,sticky=W)
        # Set up entry widget
        self.testtext = Entry(self)
        self.testtext.grid(row=4, column=0, columnspan=3, sticky=W)

        # Create empty row
        Label(self).grid(row=5)
        
        # Create label for button
        Label(self, text="Click button below to submit test text:", font="Calibri 12").grid(row=6, column=0, sticky=W)
        # Create button itself and set it to run "submittext" method when clicked
        Button(self, text="Click here", font="Calibri 12", command=self.submittext).grid(row=7, column=0, sticky=W)

        # Create empty row
        Label(self).grid(row=8)

        # Set up label for message box/text widget object
        Label(self, text="You entered this text:", font="Calibri 12").grid(row=9, column=0, sticky=W)
        # Set up message box/text widget object
        self.testmessage = Text(self, width=45, height=1)
        self.testmessage.grid(row=10, column=0, columnspan=2, sticky=N)

    # Method to run when button is clicked
    def submittext(self):
        # Take what was entered and put it into "sampletext" variable
        sampletext = self.testtext.get()
        # Delete what was in the text widget box
        self.testmessage.delete(0.0, END)
        # Print out/send "sampletext" variable to text widget object 
        self.testmessage.insert(0.0, sampletext)
        


# Main program
# Create a window; create an object called "root"
root = Tk()

# title of the GUI window
root.title("Button demonstration.")

# dimensions of the window
root.geometry("400x400")

# create ButtonDemo object
button1 = ButtonDemo(root)

# command that will launch the GUI application
root.mainloop()
        
