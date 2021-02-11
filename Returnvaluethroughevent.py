from tkinter import*
root=Tk()
val=StringVar()
def show():
  x=val.get()
  print(x)
r1=Radiobutton(root,text='male',variable=val,value='female',command=show)
r1.pack()
r2=Radiobutton(root,text='female',variable=val,value='female',command=show)
r2.pack()
root.state('zoomed')
root.mainloop()