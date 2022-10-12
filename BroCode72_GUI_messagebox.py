from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    #messagebox.showinfo(title='This is an info message box',message='You are a person')  #displays simple message
    #messagebox.showwarning(title='WARNING!',message='You have A VIRUS!!!!')              #Gives a warning message
    #messagebox.showerror(title='ERROR!',message='something went wrong :(')               #Gives an error message

    #if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):        #Returns true or false based on choices ok and cancel
        #print('You did a thing!')
    #else:
        #print('You canceled a thing! :(')

    #if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):    #Similar as previous except retry and cancel
        #print('You retried a thing!')
    #else:
        #print('You canceled a thing! :(')

    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):                     #Yes or no and returns a boolean
        #print('I like cake too :)')
    #else:
        #print('Why do you not like cake? :(')

    #answer = messagebox.askquestion(title='ask question',message='Do you like pie?')               #Returns a string of yes or no
    #if(answer == 'yes'):
        #print('I like pie too :)')
    #else:
        #print('Why do you not like pie? :(')

    #answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question') #Returns true, false, or none. Icon can be changed based on presets
    #if(answer==True):                                                                                         #Like warning or question
        #print("You like to code :)")
    #elif(answer==False):
        #print("Then why are you watching a video on coding?")
    #else:
        #print("You have dodged the question ")

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()