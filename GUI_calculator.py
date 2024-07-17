from tkinter import *

window=Tk()
window.title('Calculator')
window.geometry('500x500')
window.configure(bg='light green')

eqn=StringVar() #for taking input as string
txt_box=Entry(window,textvariable=eqn)
txt_box.grid(columnspan=4,ipadx=70)





window.mainloop()
