from tkinter import *
from tkinter import messagebox as msg
root = Tk()
r1 = Radiobutton(root, text='male', value='male')
r1.pack()
r2 = Radiobutton(root, text='female', value='female')
r2.pack()


def sayhello():
    print('hello')


def hello():
    uid = t1.get()
    msg.showinfo('message', 'thanks for login ' + uid)


l1 = Label(root,
           text='login id',
           bg='light blue',
           fg='red',
           font=('algerian,16'))
l1.pack()
t1 = Entry(root, bg='light grey', bd=5, insertwidth=6, justify='center')
t1.pack()
l2 = Label(root, text='Password')
l2.pack()
t2 = Entry(root, show='*')
t2.pack()
b1 = Button(root, text='login', command=hello)
b1.pack()
root.title('banking')
root.geometry('300x300')
root.mainloop()
