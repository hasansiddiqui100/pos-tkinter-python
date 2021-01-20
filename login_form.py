from tkinter import *
from tkinter import messagebox


class login_form:
	def __init__(self,root):
		self.root=root
		root.configure(bg="azure")
		# login label
		login_label=Label(root,text="Login",font="arial 30 bold",bg="azure")
		login_label.place(x=250,y=20)
		#user label
		user_label=Label(root,text="User :",font="helvetica 15 ",bg="azure")
		user_label.place(x=200,y=150)

		global  user_inp
		global  pass_inp
		user_inp=StringVar()
		pass_inp=StringVar()
		# entry widget for user
		user_e=Entry(root,textvariable=user_inp)
		user_e.place(x=260,y=153,height=25)
#pin label
		pass_label=Label(root,text="Pin :",font="helvetica 15 ",bg="azure")
		pass_label.place(x=210,y=200)

		# entry widget for pin
		pass_e=Entry(root,textvariable=pass_inp)
		pass_e.place(x=260,y=200,height=25)

		login_b=Button(root,text="Login",font="helvetica 18 ",bg="light steel blue",command=lambda :self.login())
		login_b.place(x=250,y=300)
		# button for exit
		exit_b=Button(root,text="Exit",font="helvetica 15 ",bg="light steel blue",command=lambda :self.destroy())
		exit_b.place(x=260,y=400)

	#login  function for authentication
	def login(self):
		if user_inp.get() == "hasan" and pass_inp.get() == "1234":
			root.destroy()
			import pos_form
		else:
			messagebox.showinfo('Error','Authentication Failed')
			user_inp.set("")
			pass_inp.set("")


	def destroy(self):
		root.destroy()


root = Tk()
obj2=login_form(root)
root.geometry("600x500")
root.mainloop()