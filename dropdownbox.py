from tkinter import *
root=Tk()
def show(event):
    value=val.get()
    print(value)

val = StringVar(root)
choice={'Python','Java','.Net','Django','DS'}
val.set('select')
combo=OptionMenu(root,val,*choice,command=show)
combo.pack()
root.geometry('250x250')
root.mainloop()