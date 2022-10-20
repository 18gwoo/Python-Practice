from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.04)                                        #Adds a delay
        bar['value']+=(speed/GB)*100                            #Increases value of progress bar
        download+=speed                                         #Same amount is being added to the bar as the rest of the variables
        percent.set(str(int((download/GB)*100))+"%")            #Sets what percent is during each iteration. int is used so that there is no decimal at the end of out %
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()                               #Used so that the progress bar is updated everytime the while loop iterates

window = Tk()

percent = StringVar()                                       #Allows us to update variable with some texts
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)      #Creates a progress bar
bar.pack(pady=10)                                           #Pads the bar in the y direction

percentLabel = Label(window,textvariable=percent).pack()    #Text variable is used so that label can be updated
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()