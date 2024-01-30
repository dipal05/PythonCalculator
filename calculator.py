from tkinter import *

i=0
def show(value):
    string=entry.get()
    if(string=='Error'):
        clear_all()
    global i
    entry.insert(i,value)
    i+=1

def answer():
    string=entry.get()
    try:
     result=eval(string)
     clear_all()
     entry.insert(0,result)
    except Exception:
        clear_all()
        entry.insert(0,'Error')

def clear_all():
    entry.delete(0, END)

def delete():
    string = entry.get()
    if(string=='Error'):
        clear_all()
    elif len(string):
        new_string = string[:-1]
        clear_all()
        entry.insert(0,new_string)
    else:
        clear_all()
        entry.insert(0,"Error")


root = Tk()
root.title('Calculator by Dipal')
root.geometry('500x400')

label=Label(text='Calculator',font=('Helvetica',14)).pack()

frame=Frame(root,bg='#050505',padx=10,width=300,height=400)
frame.pack()

entry=Entry(frame,width=36,font=('Helvetica'),justify=RIGHT)
entry.focus()
entry.grid(row=0,column=0,columnspan=4,pady=10,ipady=8)

button_7=Button(frame,text=7,width=10,height=3,command=lambda : show(7)).grid(row=1,column=0,pady=2)
button_8=Button(frame,text=8,width=10,height=3,command=lambda :show(8)).grid(row=1,column=1,pady=2)
button_9=Button(frame,text=9,width=10,height=3,command=lambda : show(9)).grid(row=1,column=2,pady=2)
button_divide=Button(frame,text='/',width=10,height=3,command=lambda : show('/')).grid(row=1,column=3,pady=2)

button_4=Button(frame,text=4,width=10,height=3,command=lambda : show(4)).grid(row=2,column=0,pady=2)
button_5=Button(frame,text=5,width=10,height=3,command=lambda : show(5)).grid(row=2,column=1,pady=2)
button_6=Button(frame,text=6,width=10,height=3,command=lambda : show(6)).grid(row=2,column=2,pady=2)
button_x=Button(frame,text='*',width=10,height=3,command=lambda : show('*')).grid(row=2,column=3,pady=2)

button_1=Button(frame,text=1,width=10,height=3,command=lambda : show(1)).grid(row=3,column=0,pady=2)
button_2=Button(frame,text=2,width=10,height=3,command=lambda : show(2)).grid(row=3,column=1,pady=2)
button_3=Button(frame,text=3,width=10,height=3,command=lambda : show(3)).grid(row=3,column=2,pady=2)
button_add=Button(frame,text='+',width=10,height=3,command=lambda : show('+')).grid(row=3,column=3,pady=2)

button_del=Button(frame,text='Del',width=10,height=7,bg='#fe9037',command=lambda : delete()).grid(row=4,column=0,pady=2,rowspan=2)
button_0=Button(frame,text=0,width=10,height=3,command=lambda : show(0)).grid(row=4,column=1,pady=2)
button_dot=Button(frame,text='.',width=10,height=3,command=lambda : show('.')).grid(row=4,column=2,pady=2)
button_sub=Button(frame,text='-',width=10,height=3,command=lambda : show('-')).grid(row=4,column=3,pady=2)

button_clear=Button(frame,text='C',width=10,height=3,bg="#3697f5",command=lambda : clear_all()).grid(row=5,column=1,pady=2)
button_ans=Button(frame,text='=',width=22,height=3,bg='#fe9037',command=lambda : answer()).grid(row=5,column=2,pady=2,columnspan=2)

root.mainloop()
