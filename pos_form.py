from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from random import randint


class Pos:
    def __init__(self, window):
        self.window = window
        # master window size
        window.geometry("1220x800")
        window.title("Pos System")
        color = "firebrick3"
        window.resizable(width=FALSE, height=FALSE)
        window.configure(bg=color)
        # top fram california label
        top_frame = Frame(window, bg=color, width=1200, height=50)
        top_frame.pack(side=TOP)
        # california lebel in top frame
        title_label = Label(top_frame, text="CALIFORNIA PIZZA.", font=("Aisha Latin Semibold", 20, "bold"), bg=color,
                            pady=10)
        # left frame for
        left_frame = Frame(window, bg="PaleVioletRed4", width=600, height=600)
        left_frame.place(x=10, y=50)
        title_label.pack(side=TOP)
        #bottom frame for buttons
        bottom_frame = Frame(window, bg="bisque", height=130, width=1205)
        bottom_frame.place(x=10, y=660)
        # notbook widget tabarent
        tabs_parent = ttk.Notebook(window, height=575, width=595)
        tabs_parent.place(x=10, y=50)
        # tab1234 in notbook wigget tab parent
        tab1 = Frame(tabs_parent, bg="bisque")
        # label flavour in tab parent
        label = Label(tab1, text="Flavours", font="Helvetica 15 bold italic", bg="black", fg="white")
        label.place(x=0, y=0)
        tab2 = Frame(tabs_parent, bg="bisque")
        tab3 = Frame(tabs_parent, bg="bisque")
        tab4 = Frame(tabs_parent, bg="bisque")
        tab1.pack(fill="both", expand=1)
        tab2.pack(fill="both", expand=1)
        tab3.pack(fill="both", expand=1)
        tab4.pack(fill="both", expand=1)
        tabs_parent.add(tab1, text="pizza")
        tabs_parent.add(tab2, text="beverages")
        tabs_parent.add(tab3, text="salads")
        tabs_parent.add(tab4, text="Deals")

        # checkbuttons for pizza in tab1 located in tab parent
        self.piz_ch_bt_1 = IntVar()
        piz1 = Checkbutton(tab1, text="Fajita", variable=self.piz_ch_bt_1, font="Helvetica 12 bold italic", bg="bisque")

        piz1.place(x=0, y=40)

        self.piz_ch_bt_2 = IntVar()
        piz2 = Checkbutton(tab1, text="Chicken Tikka", variable=self.piz_ch_bt_2, font="Helvetica 12 bold italic",
                           bg="bisque")

        piz2.place(x=0, y=90)
        self.piz_ch_bt_3 = IntVar()
        piz3 = Checkbutton(tab1, text="Cheese Lover", variable=self.piz_ch_bt_3, font="Helvetica 12 bold italic",
                           bg="bisque")
        piz3.place(x=0, y=140)

        self.piz_ch_bt_4 = IntVar()
        piz4 = Checkbutton(tab1, text="Chicken Supreme", variable=self.piz_ch_bt_4, font="Helvetica 12 bold italic",
                           bg="bisque")

        piz4.place(x=0, y=190)

        self.piz_ch_bt_5 = IntVar()
        piz5 = Checkbutton(tab1, text="Spicy Ranch", variable=self.piz_ch_bt_5, font="Helvetica 12 bold italic",
                           bg="bisque")

        piz5.place(x=0, y=240)

        self.piz_ch_bt_6 = IntVar()
        piz6 = Checkbutton(tab1, text="Double Cheese Margherita", variable=self.piz_ch_bt_6,
                           font="Helvetica 12 bold italic", bg="bisque")

        piz6.place(x=0, y=290)

        # optionmenu widget for dropdown of quantity place with pizza in tab1
        global list_menu
        list_menu = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.drop_op_piz_1 = StringVar()
        self.drop_op_piz_1.set(list_menu[0])
        drop1 = OptionMenu(tab1, self.drop_op_piz_1, *list_menu)

        self.drop_op_piz_2 = StringVar()
        self.drop_op_piz_2.set(list_menu[0])
        drop2 = OptionMenu(tab1, self.drop_op_piz_2, *list_menu)

        self.drop_op_piz_3 = StringVar()
        self.drop_op_piz_3.set(list_menu[0])
        drop3 = OptionMenu(tab1, self.drop_op_piz_3, *list_menu)

        self.drop_op_piz_4 = StringVar()
        self.drop_op_piz_4.set(list_menu[0])
        drop4 = OptionMenu(tab1, self.drop_op_piz_4, *list_menu)

        self.drop_op_piz_5 = StringVar()
        self.drop_op_piz_5.set(list_menu[0])
        drop5 = OptionMenu(tab1, self.drop_op_piz_5, *list_menu)

        self.drop_op_piz_6 = StringVar()
        self.drop_op_piz_6.set(list_menu[0])
        drop6 = OptionMenu(tab1, self.drop_op_piz_6, *list_menu)

        drop1.place(x=180, y=40)
        drop2.place(x=180, y=90)
        drop3.place(x=180, y=140)
        drop4.place(x=180, y=190)
        drop5.place(x=180, y=240)
        drop6.place(x=250, y=290)

        # sizes optionmenu in tab1
        self.s1 = StringVar()
        self.s1.set("size")
        list_menu2 = ["small", "medium", "large"]
        size_opt1 = OptionMenu(tab1, self.s1, *list_menu2)
        size_opt1.place(x=270, y=40)
        self.s2 = StringVar()
        self.s2.set("size")
        size_opt2 = OptionMenu(tab1, self.s2, *list_menu2)
        size_opt2.place(x=270, y=90)
        self.s3 = StringVar()
        self.s3.set("size")
        size_opt3 = OptionMenu(tab1, self.s3, *list_menu2)
        size_opt3.place(x=270, y=140)
        self.s4 = StringVar()
        self.s4.set("size")
        size_opt4 = OptionMenu(tab1, self.s4, *list_menu2)
        size_opt4.place(x=270, y=190)
        self.s5 = StringVar()
        self.s5.set("size")
        size_opt5 = OptionMenu(tab1, self.s5, *list_menu2)
        size_opt5.place(x=270, y=240)
        self.s6 = StringVar()
        self.s6.set("size")
        size_opt6 = OptionMenu(tab1, self.s6, *list_menu2)
        size_opt6.place(x=330, y=290)

        # drinks checkbutton in tab2
        label_2 = Label(tab2, text="Drinks", font="Helvetica 15 bold italic", bg="black", fg="white")
        label_2.place(x=0, y=0)
        self.d_ch_bt_1 = IntVar()
        cd1 = Checkbutton(tab2, text="7up", variable=self.d_ch_bt_1, font="Helvetica 12 bold italic", bg="bisque")
        cd1.place(x=0, y=40)
        self.d_ch_bt_2 = IntVar()
        cd2 = Checkbutton(tab2, text="Marinda", variable=self.d_ch_bt_2, font="Helvetica 12 bold italic", bg="bisque")
        cd2.place(x=0, y=90)
        self.d_ch_bt_3 = IntVar()
        cd3 = Checkbutton(tab2, text="Pepsi", variable=self.d_ch_bt_3, font="Helvetica 12 bold italic", bg="bisque")
        cd3.place(x=0, y=140)
        self.d_ch_bt_4 = IntVar()
        cd4 = Checkbutton(tab2, text="Sprite", variable=self.d_ch_bt_4, font="Helvetica 12 bold italic", bg="bisque")
        cd4.place(x=0, y=190)
        self.d_ch_bt_5 = IntVar()
        cd5 = Checkbutton(tab2, text="Coca Cola", variable=self.d_ch_bt_5, font="Helvetica 12 bold italic", bg="bisque")
        cd5.place(x=0, y=240)
        self.d_ch_bt_6 = IntVar()
        cd6 = Checkbutton(tab2, text="Sting", variable=self.d_ch_bt_6, font="Helvetica 12 bold italic", bg="bisque")
        cd6.place(x=0, y=290)

        # option menu widget place alongside with drinks  in tab2
        self.drop_op_d_1 = StringVar()
        self.drop_op_d_1.set(list_menu[0])
        drop1b = OptionMenu(tab2, self.drop_op_d_1, *list_menu)
        self.drop_op_d_2 = StringVar()
        self.drop_op_d_2.set(list_menu[0])
        drop2b = OptionMenu(tab2, self.drop_op_d_2, *list_menu)
        self.drop_op_d_3 = StringVar()
        self.drop_op_d_3.set(list_menu[0])
        drop3b = OptionMenu(tab2, self.drop_op_d_3, *list_menu)
        self.drop_op_d_4 = StringVar()
        self.drop_op_d_4.set(list_menu[0])
        drop4b = OptionMenu(tab2, self.drop_op_d_4, *list_menu)
        self.drop_op_d_5 = StringVar()
        self.drop_op_d_5.set(list_menu[0])
        drop5b = OptionMenu(tab2, self.drop_op_d_5, *list_menu)
        self.drop_op_d_6 = StringVar()
        self.drop_op_d_6.set(list_menu[0])
        drop6b = OptionMenu(tab2, self.drop_op_d_6, *list_menu)

        drop1b.place(x=180, y=40)
        drop2b.place(x=180, y=90)
        drop3b.place(x=180, y=140)
        drop4b.place(x=180, y=190)
        drop5b.place(x=180, y=240)
        drop6b.place(x=180, y=290)

        # checkbutton of salads in tab 3
        label_3 = Label(tab3, text="Salads", font="Helvetica 15 bold italic", bg="black", fg="white")
        label_3.place(x=0, y=0)
        self.s_ch_bt_1 = IntVar()
        sal1 = Checkbutton(tab3, text="chicken minced salad", variable=self.s_ch_bt_1, font="Helvetica 12 bold italic",
                           bg="bisque")
        sal1.place(x=0, y=40)
        self.s_ch_bt_2 = IntVar()
        sal2 = Checkbutton(tab3, text="mixed beans salad", variable=self.s_ch_bt_2, font="Helvetica 12 bold italic",
                           bg="bisque")
        sal2.place(x=0, y=90)
        self.s_ch_bt_3 = IntVar()
        sal3 = Checkbutton(tab3, text="fruit cube salad", variable=self.s_ch_bt_3, font="Helvetica 12 bold italic",
                           bg="bisque")
        sal3.place(x=0, y=140)
        self.s_ch_bt_4 = IntVar()
        sal4 = Checkbutton(tab3, text="olive and peppers salad", variable=self.s_ch_bt_4,
                           font="Helvetica 12 bold italic", bg="bisque")
        sal4.place(x=0, y=190)
        self.s_ch_bt_5 = IntVar()
        sal5 = Checkbutton(tab3, text="super food salad", variable=self.s_ch_bt_5, font="Helvetica 12 bold italic",
                           bg="bisque")
        sal5.place(x=0, y=240)

        # optionmenu of salads in tab3
        global list_menu_s
        list_menu_s = ["0", "1", "2", "3", "4", "5"]
        self.drop_op_s1 = StringVar()
        self.drop_op_s1.set(list_menu_s[0])
        drop1s = OptionMenu(tab3, self.drop_op_s1, *list_menu_s)
        self.drop_op_s2 = StringVar()
        self.drop_op_s2.set(list_menu_s[0])
        drop2s = OptionMenu(tab3, self.drop_op_s2, *list_menu_s)
        self.drop_op_s3 = StringVar()
        self.drop_op_s3.set(list_menu_s[0])
        drop3s = OptionMenu(tab3, self.drop_op_s3, *list_menu_s)
        self.drop_op_s4 = StringVar()
        self.drop_op_s4.set(list_menu_s[0])
        drop4s = OptionMenu(tab3, self.drop_op_s4, *list_menu_s)
        self.drop_op_s5 = StringVar()
        self.drop_op_s5.set(list_menu_s[0])
        drop5s = OptionMenu(tab3, self.drop_op_s5, *list_menu_s)

        drop1s.place(x=220, y=40)
        drop2s.place(x=220, y=90)
        drop3s.place(x=220, y=140)
        drop4s.place(x=220, y=190)
        drop5s.place(x=220, y=240)

        # deals in tab4

        label_4 = Label(tab4, text="Deals", font="Helvetica 18 bold italic", bg="black", fg="white")
        label_4.place(x=240, y=0)
        deal1 = Button(tab4, text="deal1", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal1_b())
        deal2 = Button(tab4, text="deal2", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal2_b())
        deal3 = Button(tab4, text="deal3", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal3_b())
        deal4 = Button(tab4, text="deal4", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal4_b())
        deal5 = Button(tab4, text="deal5", font="Helvetica 15 bold italic", bg="misty rose",
                       command=lambda: self.deal5_b())

        deal1.place(x=240, y=60)
        deal2.place(x=240, y=150)
        deal3.place(x=240, y=240)
        deal4.place(x=240, y=330)
        deal5.place(x=240, y=420)

        self.receipt_made = Text(window, width=73, height=32)
        self.receipt_made.place(x=620, y=135)


        # receipt label in top of text box for reeipt
        title_label2 = Label(window, text="Receipt", font=("Aisha Latin Semibold", 18, "bold"), bg="black", fg="white",
                             pady=20, padx=250)
        title_label2.place(x=620, y=50)
        #  total recipt rest buton in bootom frame
        total = Button(bottom_frame, text="Total", font="Helvetica 12 bold italic", bg="bisque",
                       command=lambda: self.total())
        total.place(x=80, y=30)

        receipt = Button(bottom_frame, text="receipt", font="Helvetica 12 bold italic", bg="bisque",
                         command=lambda: self.print_receipt())
        receipt.place(x=250, y=30)

        reset = Button(bottom_frame, text="reset", font="Helvetica 12 bold italic", bg="bisque",
                       command=lambda: self.reset_sales())
        reset.place(x=420, y=30)
        # total label and entry widget for all total
        total_x = Label(bottom_frame, text="Total:", font="Helvetica 12 bold italic", bg="bisque")
        total_x.place(x=550, y=33)
        self.total_a = StringVar()
        self.total_x_e = Entry(bottom_frame, textvariable=self.total_a)
        self.total_x_e.place(x=600, y=34)

        #  for date label in botom frmae
        now = datetime.now()
        self.dt = now.strftime("%d-%m-%Y")
        self.tym = now.strftime("%H:%M")
        date_str = StringVar()
        date_str.set(str(self.dt))
        lbl_date = Label(bottom_frame, text="Date", font="Helvetica 12 bold italic", bg="bisque")
        lbl_date.place(x=850, y=34)
        lbl_date = Entry(bottom_frame, textvariable=date_str)
        lbl_date.place(x=900, y=34)

        self.total_deals = 0
        self.deal1_p = 0
        self.deal2_p = 0
        self.deal3_p = 0
        self.deal4_p = 0
        self.deal5_p = 0

    global item_quantity_price
    item_quantity_price = []

    def error_handling(self, msg):
        if msg == "error!":
            messagebox.showerror("Error", "No Digits to compute!")
        elif msg == "division by zero!":
            messagebox.showerror("Error", "You can not divide a digit by zero!")
    # back end
    def total(self):
        try:

            # for pizza 1
            if self.piz_ch_bt_1.get() == 1:
                if self.s1.get() == "large":
                    fajita_result = int(self.drop_op_piz_1.get()) * 300
                    p1_t = ("fajita pizza", str(self.drop_op_piz_1.get()), "300")
                elif self.s1.get() == "medium":
                    fajita_result = int(self.drop_op_piz_1.get()) * 200
                    p1_t = ("fajita pizza", str(self.drop_op_piz_1.get()), "200")
                else:
                    fajita_result = int(self.drop_op_piz_1.get()) * 150
                    p1_t = ("fajita pizza", str(self.drop_op_piz_1.get()), "150")
                item_quantity_price.append(p1_t)
            else:
                fajita_result = 0
            #     for pizza 2
            if self.piz_ch_bt_2.get() == 1:
                if self.s2.get() == "large":
                    ch_tikka_result = int(self.drop_op_piz_2.get()) * 300
                    p2_t = ("chicken tikka pizza", str(self.drop_op_piz_2.get()), "300")
                elif self.s2.get() == "medium":
                    ch_tikka_result = int(self.drop_op_piz_2.get()) * 200
                    p2_t = ("chicken tikka pizza", str(self.drop_op_piz_2.get()), "200")
                else:
                    ch_tikka_result = int(self.drop_op_piz_2.get()) * 150
                    p2_t = ("chicken tikka pizza", str(self.drop_op_piz_2.get()), "150")
                item_quantity_price.append(p2_t)
            else:
                ch_tikka_result = 0
            # for pizza 3
            if self.piz_ch_bt_3.get() == 1:
                if self.s3.get() == "large":
                    chs_lover_result = int(self.drop_op_piz_3.get()) * 300
                    p3_t = ("cheese lover pizza", str(self.drop_op_piz_3.get()), "300")
                elif self.s3.get() == "medium":
                    chs_lover_result = int(self.drop_op_piz_3.get()) * 200
                    p3_t = ("chesse lover pizza", str(self.drop_op_piz_3.get()), "200")
                else:
                    chs_lover_result = int(self.drop_op_piz_3.get()) * 150
                    p3_t = ("chesse lover pizza", str(self.drop_op_piz_3.get()), "150")
                item_quantity_price.append(p3_t)
            else:
                chs_lover_result = 0
            #     for pizza 4
            if self.piz_ch_bt_4.get() == 1:
                if self.s4.get() == "large":
                    ch_supreme_result = int(self.drop_op_piz_4.get()) * 300
                    p4_t = ("chicken supreme pizza", str(self.drop_op_piz_1.get()), "300")
                elif self.s4.get() == "medium":
                    ch_supreme_result = int(self.drop_op_piz_4.get()) * 200
                    p4_t = ("chicken supreme pizza", str(self.drop_op_piz_4.get()), "200")
                else:
                    ch_supreme_result = int(self.drop_op_piz_4.get()) * 150
                    p4_t = ("chicken supreme pizza", str(self.drop_op_piz_4.get()), "150")
                item_quantity_price.append(p4_t)
            else:
                ch_supreme_result = 0
            #     for pizza 5
            if self.piz_ch_bt_5.get() == 1:
                if self.s5.get() == "large":
                    sp_ranch_result = int(self.drop_op_piz_5.get()) * 300
                    p5_t = ("spsicy ranch pizza", str(self.drop_op_piz_5.get()), "300")
                elif self.s5.get() == "medium":
                    sp_ranch_result = int(self.drop_op_piz_5.get()) * 200
                    p5_t = ("spicy ranch pizza", str(self.drop_op_piz_5.get()), "200")
                else:
                    sp_ranch_result = int(self.drop_op_piz_5.get()) * 150
                    p5_t = ("spicy ranch pizza", str(self.drop_op_piz_5.get()), "150")
                item_quantity_price.append(p5_t)
            else:
                sp_ranch_result = 0
            # for pizza 6
            if self.piz_ch_bt_6.get() == 1:
                if self.s6.get() == "large":
                    db_chs_marg_result = int(self.drop_op_piz_6.get()) * 300
                    p6_t = ("double cheese margerita pizza", str(self.drop_op_piz_6.get()), "300")
                elif self.s6.get() == "medium":
                    db_chs_marg_result = int(self.drop_op_piz_6.get()) * 200
                    p6_t = ("double cheese margerita pizza", str(self.drop_op_piz_6.get()), "200")
                else:
                    db_chs_marg_result = int(self.drop_op_piz_6.get()) * 150
                    p6_t = ("double cheese margherita pizza", str(self.drop_op_piz_6.get()), "150")
                item_quantity_price.append(p6_t)
            else:
                db_chs_marg_result = 0

            global total_all_pizzas
            self.total_all_pizzas = (
                        fajita_result + ch_tikka_result + chs_lover_result + sp_ranch_result + db_chs_marg_result + ch_supreme_result)
            # for drinks
            # drink1
            if self.d_ch_bt_1.get() == 1:
                d1r = int(self.drop_op_d_1.get()) * 30
                d1_t = ("7up", str(self.drop_op_d_1.get()), "30")
                item_quantity_price.append(d1_t)
            else:
                d1r = 0
            if self.d_ch_bt_2.get() == 1:
                d2r = int(self.drop_op_d_2.get()) * 30
                d2_t = ("marinda", str(self.drop_op_d_2.get()), "30")
                item_quantity_price.append(d2_t)
            else:
                d2r = 0
            if self.d_ch_bt_3.get() == 1:
                d3r = int(self.drop_op_d_3.get()) * 30
                d3_t = ("pepsi", str(self.drop_op_d_3.get()), "30")
                item_quantity_price.append(d3_t)
            else:
                d3r = 0
            if self.d_ch_bt_4.get() == 1:
                d4r = int(self.drop_op_d_1.get()) * 30
                d4_t = ("sprite", str(self.drop_op_d_4.get()), "30")
                item_quantity_price.append(d4_t)
            else:
                d4r = 0
            if self.d_ch_bt_5.get() == 1:
                d5r = int(self.drop_op_d_5.get()) * 30
                d5_t = ("coca cola", str(self.drop_op_d_5.get()), "30")
                item_quantity_price.append(d5_t)
            else:
                d5r = 0
            if self.d_ch_bt_6.get() == 1:
                d6r = int(self.drop_op_d_6.get()) * 35
                d6_t = ("sting", str(self.drop_op_d_6.get()), "35")
                item_quantity_price.append(d6_t)
            else:
                d6r = 0

            global t_drink
            self.t_drink = (d1r + d2r + d3r + d4r + d5r + d6r)
            #         for salads
            if self.s_ch_bt_1.get() == 1:
                s1r = int(self.drop_op_s1.get()) * 70
                s1_t = ("chicken minced salad", str(self.drop_op_s1.get()), "70")
                item_quantity_price.append(s1_t)
            else:
                s1r = 0

            if self.s_ch_bt_2.get() == 1:
                s2r = int(self.drop_op_s2.get()) * 70
                s2_t = ("mixed beeen salad", str(self.drop_op_s2.get()), "70")
                item_quantity_price.append(s2_t)
            else:
                s2r = 0
            if self.s_ch_bt_3.get() == 1:
                s3r = int(self.drop_op_s3.get()) * 70
                s3_t = ("fruit cube salad", str(self.drop_op_s3.get()), "70")
                item_quantity_price.append(s3_t)
            else:
                s3r = 0
            if self.s_ch_bt_4.get() == 1:
                s4r = int(self.drop_op_s4.get()) * 70
                s1_4 = ("olive and peppers salad", str(self.drop_op_s4.get()), "70")
                item_quantity_price.append(s1_4)
            else:
                s4r = 0
            if self.s_ch_bt_5.get() == 1:
                s5r = int(self.drop_op_s5.get()) * 70
                s5_t = ("super food salad", str(self.drop_op_s5.get()), "70")
                item_quantity_price.append(s5_t)
            else:
                s5r = 0

            global t_salad
            self.t_salad = (s1r + s2r + s3r + s4r + s5r)
            global total_all

            self.total_all = (self.total_deals + self.t_salad + self.total_all_pizzas + self.t_drink)
            global sub_total

            global tax
            global service_charge

            self.tax = self.total_all * 0.17
            self.service_charge = self.total_all * 0.05
            self.sub_total = self.tax + self.service_charge + self.total_all
            # total_entry.delete(0, END)
            # total_entry.insert(0, "KES. " + str(total_cost_of_juice + total_cost_of_fruits + tax_on_all_items))
            if self.sub_total == 0:
                pass
            else:
                self.total_x_e.insert(0, str(self.sub_total))
            # self.total_x_e.delete(0, END)

        except NameError:
            self.error_handling("error!")

    def print_receipt(self):
        x = randint(390000, 500000)
        try:
            self.receipt_made.delete("1.0", END)
            self.receipt_made.insert(END, "\t\t\t   California Pizza." + "\n")
            self.receipt_made.insert(END, "\t\t\t     Sale Receipt." + "\n")
            self.receipt_made.insert(END, " " + "\n")
            self.receipt_made.insert(END, "Invoice# " + str(x) + "\n\n")

            self.receipt_made.insert(END, "Operator name:Mr Abc\n\n")
            self.receipt_made.insert(END, "Date:{}\t\t\tTime:{}\n".format(self.dt, self.tym))

            x = 0
            y = 1
            while True:
                self.receipt_made.insert(END, "Item{}:{} \nquantity:{:.2} each @:{:.5}\n\n".format(y,
                                                                                                   item_quantity_price[
                                                                                                       x][0],
                                                                                                   item_quantity_price[
                                                                                                       x][1],
                                                                                                   item_quantity_price[
                                                                                                       x][2]))
                # receipt_made.insert(END,item_quantity_price[x][0] + " :   " + item_quantity_price[x][1] + " each @ " +
                #                      item_quantity_price[x][2] + "\n")
                # receipt_made.insert(END, "deal:" + deal_list[x][0] +":"+ deal_list[x][1] + "each @" +
                #                     deal_list[x][2] + "\n")

                x += 1
                y += 1

                if x < len(item_quantity_price):
                    continue
                else:
                    break

            self.receipt_made.insert(END, " " + "\n")
            if self.total_all_pizzas == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Total of pizzas: " + str(self.total_all_pizzas) + "\n")
            if self.t_drink == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Total of drink: " + str(self.t_drink) + "\n")
            if self.t_salad == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Total of salads: " + str(self.t_salad) + "\n")
            if self.total_deals == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Total of deals: " + str(self.total_deals) + "\n")
            if self.total_all == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Total(gst+service charge not included): " + str(self.total_all) + "\n")
            if self.tax == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Tax(GST):{:.2f}".format(self.tax) + "\n")
            if self.service_charge == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "service charges:{:.2f}".format(self.service_charge) + "\n")
            if self.sub_total == 0:
                self.receipt_made.insert(END, "")
            else:
                self.receipt_made.insert(END, "Total:{}".format(self.sub_total) + "\n")

            # receipt_made.insert(END, "Cost of juice: " + entry_cost_juice_var.get() + "\n")
            # receipt_made.insert(END, "Total cost:  " + entry_total_cost_var.get() + "\n")
            self.receipt_made.insert(END, " " + "\n")
            self.receipt_made.insert(END, "\t\t\t***** THANK YOU *****" + "\n")
        except IndexError:
            messagebox.showerror("Error!", "select items first! Thank you!")
        except NameError:
            messagebox.showerror("Error!", "select items first! Thank you!")

    def deal1_b(self):
        global total_deals
        global deal1_p
        # deal1="1 Large pizza + 1 (1.5ltr) Drink + 6 chicken nuggets)"
        deal1_p = 999
        tup_d1 = ("1 Large pizza + 1.5 ltr drink + 6 chicken nuggets", "1", "999")
        item_quantity_price.append(tup_d1)
        # receipt_made.insert(END,"deal1")
        self.total_deals += deal1_p

    def deal2_b(self):
        global total_deals
        global deal2_p
        # deal2="1 medium pizza + 1 (1 ltr) Drink + 6 chicken nuggets)"
        deal2_p = 790
        tup_d2 = ("1 medium pizza + 1 (1 ltr) Drink + 6 chicken nuggets", "1", "790")
        item_quantity_price.append(tup_d2)
        self.total_deals += deal2_p

    def deal3_b(self):
        global total_deals
        global deal3_p
        # deal3="1 small pizza + 6 chicken nuggets)"
        deal3_p = 650
        tup_d3 = ("1 small pizza + 6 chicken nuggets", "1", "650")
        item_quantity_price.append(tup_d3)
        self.total_deals += deal3_p

    def deal4_b(self):
        global total_deals
        global deal4_p
        # deal3="1 small pizza + 6 chicken nuggets)"
        deal4_p = 450
        tup_d4 = ("3 small pizza", "1", "450")
        item_quantity_price.append(tup_d4)
        self.total_deals += deal4_p

    def deal5_b(self):
        global total_deals
        global deal5_p
        # deal3="1 small pizza + 6 chicken nuggets)"
        deal5_p = 650
        tup_d4 = ("2 medium pizza + salad + 1 jumbo 2.5ltr drink", "1", "650")
        item_quantity_price.append(tup_d4)
        self.total_deals += deal5_p

    def reset_sales(self):

        try:
            self.piz_ch_bt_1.set(0)
            self.piz_ch_bt_2.set(0)
            self.piz_ch_bt_3.set(0)
            self.piz_ch_bt_4.set(0)
            self.piz_ch_bt_5.set(0)
            self.piz_ch_bt_6.set(0)

            self.drop_op_piz_1.set(list_menu[0])
            self.drop_op_piz_2.set(list_menu[0])
            self.drop_op_piz_3.set(list_menu[0])
            self.drop_op_piz_4.set(list_menu[0])
            self.drop_op_piz_5.set(list_menu[0])
            self.drop_op_piz_6.set(list_menu[0])

            self.s1.set("size")
            self.s2.set("size")
            self.s3.set("size")
            self.s4.set("size")
            self.s5.set("size")
            self.s6.set("size")

            self.d_ch_bt_1.set(0)
            self.d_ch_bt_2.set(0)
            self.d_ch_bt_3.set(0)
            self.d_ch_bt_4.set(0)
            self.d_ch_bt_5.set(0)
            self.d_ch_bt_6.set(0)

            self.drop_op_d_1.set(list_menu[0])
            self.drop_op_d_2.set(list_menu[0])
            self.drop_op_d_3.set(list_menu[0])
            self.drop_op_d_4.set(list_menu[0])
            self.drop_op_d_5.set(list_menu[0])
            self.drop_op_d_6.set(list_menu[0])

            self.s_ch_bt_1.set(0)
            self.s_ch_bt_2.set(0)
            self.s_ch_bt_3.set(0)
            self.s_ch_bt_4.set(0)
            self.s_ch_bt_5.set(0)

            self.drop_op_s1.set(list_menu_s[0])
            self.drop_op_s2.set(list_menu_s[0])
            self.drop_op_s3.set(list_menu_s[0])
            self.drop_op_s4.set(list_menu_s[0])
            self.drop_op_s5.set(list_menu_s[0])
            global total_deals
            global deal1_p, deal2_p, deal3_p, deal4_p, deal5_p
            # total_deals=0
            # self.deal1_p=0
            # self.deal2_p=0
            # self.deal3_p=0
            # self.deal4_p=0
            # self.deal5_p=0
            global total_all_pizzas, t_drink, t_salad
            self.total_all_pizzas = 0
            self.t_drink = 0
            self.t_salad = 0
            global item_quantity_price
            item_quantity_price.clear()
            self.total_x_e.delete(0, END)

            self.receipt_made.delete("1.0", END)
            messagebox.showinfo("Next Customer!", "Serve the next customer please!")
        except NameError:
            messagebox.showerror("error nothing to clear")


window = Tk()
ob = Pos(window)

window.mainloop()

