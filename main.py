from tkinter import*
from tkinter import messagebox as msg
root=Tk()
def sayhello():
  print('hello')
def hello():
  uid=t1.get()
  msg.showinfo('message','thanks for login ' + uid)
l1=Label(root,text='login id',bg='light blue',fg='red',font=('algerian,16'))
l1.pack()
t1=Entry(root)
t1.pack()
l2=Label(root,text='Password')
l2.pack()
t2=Entry(root,show='*')
t2.pack()
b1=Button(root,text='login',command=hello)
b1.pack()
root.title('banking')
root.geometry('300x300')
root.mainloop()
