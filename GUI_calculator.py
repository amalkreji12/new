from tkinter import *

window=Tk()
window.title('Calculator')
window.geometry('500x500')
window.configure(bg='light green')

eqn=StringVar() #for taking input as string // used for hold string values
txt_box=Entry(window,textvariable=eqn)
txt_box.grid(columnspan=4,ipadx=70)





window.mainloop()


# help : https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/