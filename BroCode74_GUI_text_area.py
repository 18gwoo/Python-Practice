# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0",END) #1.0 denotes beginning index/the first line
    print(input)

window = Tk()
text = Text(window,                          #Gives a text area to enter stuff in
            bg="light yellow",
            font=("ariel",25),
            height=10,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()
window.mainloop()