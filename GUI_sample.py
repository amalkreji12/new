from tkinter import *

window=Tk()
window.geometry('500x500')
window.title('Sample')

def hello():
    print('Hello')         #function for what to do when clicking the button



button1=Button(window,text='OK',command=hello) #;command is used to call the function
button2=Button(window,text='OK',command=hello)

label=Label(window,text='Welcome')

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)

#This code is used when we dont use 'grid' method
# button1.pack()
# button2.pack()
# label.pack()



window.mainloop()
