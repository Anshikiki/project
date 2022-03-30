#this program shows grid manger- which helps us to orgainse our widgets
#foormatting our title, label and button plaements
from tkinter import *
from tkinter import ttk

root = Tk()

#create entries
entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

# create placeholder
entry.insert(0, "please enter your name")
entry2.insert(0, "please enter your password")

#create button and labels
#where do we want it- in root and the text
button = ttk.Button(root, text="enter")
lbltitle = ttk.Label(text='our title here', font=(('arial'), 30))
lblname = ttk.Label(text='your name :')
lblpass = ttk.Label(text='your password:') 

#position of the buttons, labels and entries as outcome by using geometry manager for grid
#move title to the 2nd column
lbltitle.grid(row=0, column=0, columnspan=2, pady=10)
lblname.grid(row=1, column=0, sticky=W) #w - left
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid (row=3, column=1, sticky=E, pady=5) 
root.geometry( '500x400' )
root.mainloop()

