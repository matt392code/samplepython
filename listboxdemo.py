# Program to demonstrate list boxes in Python

# Import the tkinter module for GUI components
from tkinter import *

# Create ListBoxDemo class based on the Frame class
class ListBoxDemo(Frame):
    def __init__(self, master):
        super(ListBoxDemo, self).__init__(master)
        # Link frame to grid manager
        self.grid()
        # Create a Label
        Label(self, text="This is a list box demostration program.", font="Calibri 14").grid(row=1, sticky=N, columnspan=2)

        # Empty row
        Label(self).grid(row=2)

        # Set up label for list box widget
        Label(self, text="Click one or more of the operating systems below:", font="Calibri 12").grid(row=3, column=0,sticky=W)
        
        # Create listbox itself
        self.oslistbox = Listbox(self, height=10, selectmode=MULTIPLE)
        self.oslistbox.grid(column=0, row=5, sticky=N)
        
        # Fill the list box with operating systems
        # Use for loop
        for os in ["Ubunutu", "Mint", "Debian", "Redhat", "Fedora", "OpenSuse", "Xubuntu", "Puppy", "Kali"]:
            self.oslistbox.insert(END, os)

        # Create textbox to display chosen items
        self.chosenos = Text(self, width=20, height=6, wrap=WORD)
        self.chosenos.grid(row=10, column=0, sticky=N)

        # Run poll() method to pick up chosen operating systems
        self.poll()
    
    def updatetextbox(self):
            self.chosenos.delete(0.0, END)
            self.chosenos.insert(0.0, self.selectedos)

        # Define poll() method that was run above
    def poll(self):
            oslist = []
            self.selectedos = []
        # Run poll() method every 200 ms; can be any widget
            self.oslistbox.after(200, self.poll)

        # Create tuple of index of items chsen using curselection method
        # Convert to an integer then convert to a list and place on "oslist"
            oslist = list(map(int,self.oslistbox.curselection()))

        # start for loop
            for alpha in range(len(oslist)):
            # take numbers from "oslist" and get selected items from "oslistbox"
            # then append them to "selectedos"
                self.selectedos.append(self.oslistbox.get(oslist[alpha]))

            # update the text box with the selections
            self.updatetextbox()
            # end poll() method


#Main program
# Create a window; create an object called "root"
root = Tk()

# title of the GUI window
root.title("List box demonstration.")

# dimensions of the window
root.geometry("400x400")

# create ListBoxDemo object
listbox1=ListBoxDemo(root)

# command that will launch the GUI application
root.mainloop()
