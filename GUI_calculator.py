from tkinter import *

window=Tk()
window.title('Calculator')
window.geometry('500x500')
window.configure(bg='light green')

eqn=StringVar() #for taking input as string // used for hold string values
txt_box=Entry(window,textvariable=eqn)
txt_box.grid(columnspan=4,ipadx=70)


exp=""

def btn_click(num):
    global exp
    exp=exp+str(num)
    eqn.set(exp)

def equal_val():
    try:
        global exp
        total=str(eval(exp))
        eqn.set(total)
        exp=""
    
    except:
        eqn.set("Error")
        exp=""

def clear_val():
    global exp
    exp=""
    eqn.set("")




btn1=Button(window,text='1',fg='black',bg='white',command=lambda:btn_click(1),height=1,width=8)
btn1.grid(row=2,column=0)
btn2=Button(window,text='2',fg='black',bg='white',command=lambda:btn_click(2),height=1,width=8)
btn2.grid(row=2,column=1)
btn3=Button(window,text='3',fg='black',bg='white',command=lambda:btn_click(3),height=1,width=8)
btn3.grid(row=2,column=2)

btn4=Button(window,text='4',fg='black',bg='white',command=lambda:btn_click(4),height=1,width=8)
btn4.grid(row=3,column=0)
btn5=Button(window,text='5',fg='black',bg='white',command=lambda:btn_click(5),height=1,width=8)
btn5.grid(row=3,column=1)
btn6=Button(window,text='6',fg='black',bg='white',command=lambda:btn_click(6),height=1,width=8)
btn6.grid(row=3,column=2)

btn7=Button(window,text='7',fg='black',bg='white',command=lambda:btn_click(7),height=1,width=8)
btn7.grid(row=4,column=0)
btn8=Button(window,text='8',fg='black',bg='white',command=lambda:btn_click(8),height=1,width=8)
btn8.grid(row=4,column=1)
btn9=Button(window,text='9',fg='black',bg='white',command=lambda:btn_click(9),height=1,width=8)
btn9.grid(row=4,column=2)

btn0=Button(window,text='0',fg='black',bg='white',command=lambda:btn_click(0),height=1,width=8)
btn0.grid(row=5,column=0)

plus=Button(window,text='+',fg='black',bg='white',command=lambda:btn_click('+'),height=1,width=8)
plus.grid(row=2,column=3)
minus=Button(window,text='-',fg='black',bg='white',command=lambda:btn_click('-'),height=1,width=8)
minus.grid(row=3,column=3)
multiply=Button(window,text='*',fg='black',bg='white',command=lambda:btn_click('*'),height=1,width=8)
multiply.grid(row=4,column=3)
divide=Button(window,text='/',fg='black',bg='white',command=lambda:btn_click('/'),height=1,width=8)
divide.grid(row=5,column=3)
equal=Button(window,text='=',fg='black',bg='white',command=equal_val,height=1,width=8)
equal.grid(row=5,column=3)
clear=Button(window,text='Clear',fg='black',bg='white',command=clear_val,height=1,width=8)
clear.grid(row=5,column=2)




window.mainloop()


# help : https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/