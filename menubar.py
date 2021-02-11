from tkinter import *
root=Tk()

menubar=Menu()
filemenu=Menu(root,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", underline=0,menu=filemenu)

editmenu=Menu(root,tearoff=1)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paster")
menubar.add_cascade(label="Edit", underline=1,menu=editmenu)

root.title('Menu')
root.config(menu=menubar)
root.state('zoomed')
root.mainloop()