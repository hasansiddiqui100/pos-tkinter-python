from tkinter import *
#question to goto either inventory or pos form
root=Tk()
root.geometry("200x200")
but1=Button(root,text="pos system",command=lambda:goto())
but1.pack()

but2=Button(root,text="inventory",command=lambda:goto2())
but2.pack()

def goto():
    root.destroy()
    import login_form
def goto2():
    root.destroy()
    import inventory_form

root.mainloop()