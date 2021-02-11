from tkinter import*
root=Tk()
r1=radiobutton(root,text='male',value='male')
r1.pack()
r2=radiobutton(root,text='female',value='male')
r2.pack()
root.state('zoomed')
root.mainloop()