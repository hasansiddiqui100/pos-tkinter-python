from tkinter import *
root=Tk()
root.geometry("1100x600")
root.title("inventory")
bottom_frame1=Frame(root,width=1060,height=200,bg="blue")
bottom_frame1.place(x=20,y=380)
#
label_inv=Label(bottom_frame1,text="invoice number")
label_inv.place(x=50,y=30)

label_total=Label(bottom_frame1,text="total")
label_total.place(x=300,y=30)
#
label_time=Label(bottom_frame1,text="Time")
label_time.place(x=500,y=30)

inv_e1=Entry(bottom_frame1)
inv_e1.place(y=30,x=150)
#
total_e1=Entry(bottom_frame1)
total_e1.place(y=30,x=340)
#
time_e1=Entry(bottom_frame1)
time_e1.place(y=30,x=540)

up_b=Button(bottom_frame1,text="update")
up_b.place(x=50,y=75)
del_b=Button(bottom_frame1,text="delete")
del_b.place(x=130,y=75)

show=Text(root,height=20,width=50)
show.place(x=400,y=0)


root.mainloop()
def update():
    pass
