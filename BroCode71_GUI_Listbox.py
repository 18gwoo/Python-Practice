# listbox = A listing of selectable text items within it's own container

def submit():

    #print(listbox.get(listbox.curselection())) #Prints current selection from listbox

    #following it to accommodate multiple selection
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get()) #listbox.size acts as an index number
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection()) #deletes selected in listbox
    # following it to accommodate multiple selection
    for index in reversed(listbox.curselection()): #need the reversed otherwise indexes changing after each delete plays a factor. Doing reversed starts the process at the last
        listbox.delete(index)                      #index so deletion will not effect it

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE) #select multiple items from listbox
listbox.pack()

listbox.insert(1,"pizza") #inserts items into list box
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size()) #changes height to the size of the list box dynamically

entryBox = Entry(window) #creates an entry box
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()