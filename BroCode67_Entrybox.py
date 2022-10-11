from tkinter import *
#entry widget = text box that accepts a single line of user input

def submit():
   username =  entry.get() #returns a string
   print("Hello "+ username)
   #entry.config(state=DISABLED) #disables entry box
def delete():
    entry.delete(0,END) #deletes character 0 to end

def backspace():
    entry.delete(len(entry.get()) - 1) #entry.get returns length of entrybox

window = Tk()

entry = Entry(window, #Creates entry box
              font = ("Ariel",50),
              fg = "Green",
              bg = "black",
              show="*") #submits stuff as asterisks
entry.insert(0,"Spongebob")
entry.pack(side=LEFT) #packs/places entry box

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT) #add it to window

delete_button = Button(window, text = "delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "backspace", command = backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()