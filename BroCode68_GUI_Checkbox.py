from tkinter import *

def display():
    if(x.get()==1): #x.get for intvar. If using boolean dont need ==1
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar() #can also use Stringvar or Booleanvar. Makes x a variable

python_photo = PhotoImage(file='GUI_Icon.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x, #chooses variable
                           onvalue=1, #what happens if this variable is chosen. Can also use strings as well as True and False
                           offvalue=0, #what happens if it is off
                           command=display, #the checkbuttons function
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00', #for if checkbox is active
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left') #prevents overlapping of text and image
check_button.pack()


window.mainloop()