import tkinter
from tkinter import *
import tkinter.font as tkFont


top =Tk()
top.config(bg='#030303')
top.title('Standard Calculator')
enter = Entry(top,width=40,borderwidth=0,font='20')
enter.grid(row=0,column=0,columnspan=4,padx=10,pady=20,ipady=15)
enter.config(bg='#030303',fg='#ffffff')
global equal
equal=False
def click_button(number):
    global equal

    if(equal):
        enter.delete(0,END)
        equal=False

    current= enter.get()
    enter.delete(0,END)
    if(number=='.' and str(current).count('.')>=1):
        enter.insert(0,str(current))
    else:
        enter.insert(0,str(current)+str(number))

def clear_screen():
    enter.delete(0,END)

def operator_button(op):
    global first_num
    global operator    
    operator=op
    first_num=enter.get()   
    enter.delete(0,END)




def button_equal():
   second_num=enter.get()
   enter.delete(0,END)
   global equal
   equal=True

   if(operator=='+'):
        ans= eval(first_num)+eval(second_num)
   elif(operator=='-'):
       ans= eval(first_num)-eval(second_num)
   elif(operator=='x'):
       ans= eval(first_num)*eval(second_num)
   elif(operator=='/'):
       if(eval(second_num)==0):
        ans='Error'
       else:
        ans= eval(first_num)/eval(second_num)    
   enter.insert(0,ans)

def button_neg():
    num = enter.get()
    num =-1* eval(num)
    enter.delete(0,END)
    enter.insert(0,num)

def button_percent():
    num = enter.get()
    num = eval(num)/100
    enter.delete(0,END)
    enter.insert(0,num)
#define 0-9 Buttons
button1= Button(top,text='1',font='15',padx=53,pady=30,command=lambda:click_button(1),bg='#d4d4d2')
button2= Button(top,text='2',font='15',padx=58,pady=30,command=lambda:click_button(2),bg='#d4d4d2')
button3= Button(top,text='3',font='15',padx=55,pady=30,command=lambda:click_button(3),bg='#d4d4d2')
button4= Button(top,text='4',font='15',padx=53,pady=30,command=lambda:click_button(4),bg='#d4d4d2')
button5= Button(top,text='5',font='15',padx=58,pady=30,command=lambda:click_button(5),bg='#d4d4d2')
button6= Button(top,text='6',font='15',padx=55,pady=30,command=lambda:click_button(6),bg='#d4d4d2')
button7= Button(top,text='7',font='15',padx=53,pady=30,command=lambda:click_button(7),bg='#d4d4d2')
button8= Button(top,text='8',font='15',padx=58,pady=30,command=lambda:click_button(8),bg='#d4d4d2')
button9= Button(top,text='9',font='15',padx=55,pady=30,command=lambda:click_button(9),bg='#d4d4d2')
button0= Button(top,text='0',font='15',padx=125,pady=30,command=lambda:click_button(0),bg='#d4d4d2')

button_point= Button(top,text='.',font='15',padx=59,pady=30,command=lambda:click_button('.'),bg='#d4d4d2')

#define operator button
button_sign= Button(top,text='+/-',font='15',padx=50,pady=30,command=button_neg,bg='#858585')
button_percent=Button(top,text='%',font='15',padx=52,pady=30,command=button_percent,bg='#858585')
button_clear=Button(top,text='C',font='15',padx=53,pady=30,command=clear_screen,bg='#858585')

button_add= Button(top,text='+',font='15',padx=55,pady=30,command=lambda:operator_button('+'),bg='#ff9500',fg='#ffffff')
button_minus= Button(top,text='-',font='15',padx=57,pady=30,command=lambda:operator_button('-'),bg='#ff9500',fg='#ffffff')
button_mutiple= Button(top,text='x',font='15',padx=55,pady=30,command=lambda:operator_button('x'),bg='#ff9500',fg='#ffffff')
button_divide= Button(top,text='÷',font='35',padx=55,pady=30,command=lambda:operator_button('/'),bg='#ff9500',fg='#ffffff')

button_equal= Button(top,text='=',font='35',padx=55,pady=30,command=button_equal,bg='#ff9500',fg='#ffffff')

helv36 = tkFont.Font( size=30)

#put buttons on the screen
button1.grid(row=4 ,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4 ,column=2)

button4.grid(row=3 ,column=0)
button5.grid(row=3 ,column=1)
button6.grid(row=3 ,column=2)

button7.grid(row=2 ,column=0)
button8.grid(row=2 ,column=1)
button9.grid(row=2 ,column=2)


button0.grid(row=5 ,column=0,columnspan=2)
button_point.grid(row=5,column=2)

#put operator buttons
button_clear.grid(row=1,column=0)
button_sign.grid(row=1,column=1)
button_percent.grid(row=1,column=2)

button_divide.grid(row=1,column=3)
button_mutiple.grid(row=2,column=3)
button_minus.grid(row=3,column=3)
button_add.grid(row=4,column=3)
button_equal.grid(row=5,column=3)

top.mainloop()
