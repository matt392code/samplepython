# Program to demonstrate the close and iconify methods in Python

# Import the tkinter module for GUI components
from tkinter import *

# Create CloseIconButtonDemo class based on the Frame class
class CloseIconButtonDemo(Frame):
    def __init__(self, master):
        super(CloseIconButtonDemo, self).__init__(master)
        # Link frame to grid manager
        self.grid()
         # Empty row
        Label(self).grid(row=2)

        # Set up label for close button
        Label(self, text="Click button below to close:", font="Calibri 12").grid(row=3, column=0,sticky=W)

        # Create close button and call method
        Button(self, text="Close", command=self.closewindow).grid(row=4, column=0, sticky=N)

        # Set up label for iconify button
        Label(self, text="Click button below to iconify:", font="Calibri 12").grid(row=5, column=0, sticky=W)

        # Create inconify button and call method
        Button(self, text="Iconify", command=self.makewindowicon).grid(row=6, column=0, sticky=N)

    # method to close window
    def closewindow(self):
        root.destroy()

    # method to make window an icon
    def makewindowicon(self):
        root.iconify()

# Main program below
# Create a window; create an object called "root"
root = Tk()

# title of the GUI window
root.title("Close button demonstration.")

# dimensions of the window
root.geometry("300x300")

# create ListBoxDemo object
listbox1=CloseIconButtonDemo(root)

# command that will launch the GUI application
root.mainloop()
