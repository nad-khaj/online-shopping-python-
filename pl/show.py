import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import dal.database as db
import dal.productclass as p
import dal.userclass as u
from tkinter import messagebox


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.master = screen
        self.createWidget()

    def createWidget(self):
        self.layer_1 = Frame(self.master, bg="blue", width=300, height=300)
        self.layer_1.place(x=0, y=0)
        self.layer_2 = Frame(self.master, bg="cyan", width=300, height=300)
        self.layer_2.place(x=0, y=0)
        self.layer_3 = Frame(self.master, bg="yellow", width=300, height=300)
        self.layer_3.place(x=0, y=0)


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')
        self.resizable(None, None)

        ttk.Button(self,
                   text='Close',
                   command=self.destroy).pack(expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.scr2 = None
        self.geometry("%dx%d+%d+%d" % (400, 280, 500, 200))
        self.title("فروشگاه آنلاین(ورود به سامانه)")
        self.iconbitmap("./images/shopping.ico")
        self.configure(bg="dark Blue")
        self.resizable(False, False)
        self.begin()

    def begin(self):
        global usrtxt1, passtxt1, curr_user
        self.lbl1 = Label(self.master, text=":کد کاربری ", fg="white", bg="dark blue")
        self.lbl1.place(x=270, y=50)
        self.Usrnam = StringVar()
        self.Passwrd = StringVar()
        self.usrtxt1 = Entry(self.master, textvariable=self.Usrnam, font="nazanin 12 bold", bg="white", fg="dark blue",
                             justify="right",
                             width=20)
        self.usrtxt1.place(x=70, y=50)
        self.usrtxt1.focus()
        self.passtxt1 = Entry(self.master, textvariable=self.Passwrd, font="nazanin 12 bold", bg="white",
                              fg="dark blue",
                              justify="right",
                              width=20
                              , show="*")
        self.passtxt1.place(x=70, y=120)
        lbl2 = Label(self.master, text=":رمز عبور ", fg="white", bg="dark blue")
        lbl2.place(x=270, y=120)
        self.sub = Button(self.master, text="ورود", bg="green", width=5, font="nazanin 12 bold", fg="white")
        # command=lambda: self.login1
        self.sub.bind("<Button-1>", self.login1)
        self.sub.place(x=70, y=200)
        self.reg = Button(self.master, text="ثبت نام", bg="blue", width=5, font="nazanin 12 bold", fg="yellow",
                          command=lambda: self.register(self.master))
        self.reg.place(x=250, y=200)

    # ------------------------------------User  Login -------------------------------
    def login1(self, evt):
        global usrtxt1, passtxt1, curr_user
        global curr_user
        self.command = db.DB1()
        self.usrnam = self.usrtxt1.get()
        self.passwrd = self.passtxt1.get()

        curr_user = self.command.valid_user(self.usrnam, self.passwrd)
        if curr_user:
            messagebox.showinfo("ورود به سامانه", f"   خوش آمدید{self.usrnam}  کاربر ")
            self.destroy()
            self.mainPart()

        else:
            messagebox.showwarning("توجه :", "  کد کاربری / رمز عبور صحیح نیست !! ")

    # --------------------------------User register------------------------------
    def register(self, scr1):
        # global  scr1
        self.scr2 = tk.Toplevel(scr1)
        self.scr2.geometry("%dx%d+%d+%d" % (350, 500, 400, 250))
        self.scr2.configure(bg="blue")
        self.scr2.title("ثبت نام در سامانه ")
        self.scr2.iconbitmap("images/shopping.ico")
        self.scr2.resizable(False, False)
        # -----------------labels ------------------------
        global namtxt, famtxt, usrtxt, passtxt, seller, mcodetxt
        self.Name = StringVar()
        self.Family = StringVar()
        self.Usrnam = StringVar()
        self.Passwrd = StringVar()
        self.seller = BooleanVar()
        self.Mellicode = StringVar()
        self.lbl1 = Label(self.scr2, text=":نام ", fg="white", bg="blue")
        self.lbl1.place(x=270, y=50)
        self.lbl2 = Label(self.scr2, text=":نام خانوادگی ", fg="white", bg="blue")
        self.lbl2.place(x=270, y=120)
        self.lbl3 = Label(self.scr2, text=":کد ملی ", fg="white", bg="blue")
        self.lbl3.place(x=270, y=190)
        self.lbl4 = Label(self.scr2, text=":کد کاربری ", fg="white", bg="blue")
        self.lbl4.place(x=270, y=260)
        self.lbl5 = Label(self.scr2, text=":رمز عبور ", fg="white", bg="blue")
        self.lbl5.place(x=270, y=330)

        namtxt = Entry(self.scr2, textvariable=self.Name, font="nazanin 12 bold", bg="white", fg="blue",
                       justify="right",
                       width=20)
        namtxt.place(x=70, y=50)

        famtxt = Entry(self.scr2, textvariable=self.Family, font="nazanin 12 bold", bg="white", fg="blue",
                       justify="right",
                       width=25)
        famtxt.place(x=25, y=120)
        mcodetxt = Entry(self.scr2, textvariable=self.Mellicode, font="nazanin 12 bold", bg="white", fg="blue",
                         justify="right",
                         width=20)
        mcodetxt.place(x=70, y=190)

        usrtxt = Entry(self.scr2, textvariable=self.Usrnam, font="nazanin 12 bold", bg="white", fg="blue",
                       justify="right",
                       width=20)
        usrtxt.place(x=70, y=260)
        usrtxt.focus()
        passtxt = Entry(self.scr2, textvariable=self.Passwrd, font="nazanin 12 bold", bg="white", fg="blue",
                        justify="right",
                        width=20
                        , show="*")
        passtxt.place(x=70, y=330)
        radioseller = Radiobutton(self.scr2, text="فروشنده", variable=self.seller, value=1, bg="blue")
        radioseller.place(x=100, y=380)
        radioseller = Radiobutton(self.scr2, text=" مشتری", variable=self.seller, value=0, bg="blue")
        radioseller.place(x=220, y=380)
        self.reg = Button(self.scr2, text="ثبت", bg="green", width=10, font="nazanin 12 bold", fg="white",
                          command=lambda: self.onclickSave(self.seller.get()))
        # reg.bind("<Button-1>", onclickSave)
        namtxt.focus()
        self.reg.place(x=120, y=430)
        self.scr2.mainloop()

    def onclickSave(self, seller1):
        u1 = u.Usr()
        name = namtxt.get()
        family = famtxt.get()
        usrnam = usrtxt.get()
        passwrd = passtxt.get()
        mellicode = mcodetxt.get()
        if name == "" or family == "" or usrnam == "" or passwrd == "" or mellicode == "":
            messagebox.showwarning("توجه", "فیلدهای خالی را تکمیل کنید ")
        else:
            u1.set_usr_all(name, family, usrnam, passwrd, seller1, mellicode, 0)
            self.command = db.DB1()
            if self.command.find_usernam(u1):
                messagebox.showwarning(" توجه:", f"**   کد کاربری تکراری است .{usrnam}**   ")
            elif self.command.find_mellicode(u1):
                messagebox.showwarning(" توجه:", f"**   کد ملی تکراری است .{mellicode}**   ")
            else:
                messagebox.showinfo(f"{name}  {family} ",
                                    " ثبت نام انجام شد . جهت ورود کد کاربری و رمز خود را وارد کنید :)")
                self.command.save_user(u1)
                self.scr2.destroy()
            self.scr2.mainloop()

    def clearSeller(self):
        self.Pname.set("")
        self.Pcolor.set("")
        self.Pprice.set("")
        self.Pfprice.set("")
        self.Pcount.set("")
        self.Pdiscount.set("")
        if isSeller:
            self.returnbtn.place_forget()
            self.savebtn.place(x=820, y=440)
        else:
            self.buybtn.place(x=820, y=400)
            self.deletebtn.place_forget()
        self.cancelbtn.place_forget()

    def onclickDeleteTable1(self,e):
        global p1
        table1.delete(selected_row)
        self.clearSeller()
        self.db1 = db.DB1()
        self.db1.delete_products(p1)
        messagebox.showinfo("توجه", " کالای مورد نظر از لیست  کالاهای قابل فروش خارج  شد ")

    def onclickDeleteTable2(self,e):
        global p1, amount
        amount = int(amount - table2.item(selected_row2)["values"][0])
        self.lbla.config(text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ")
        if int(amount) == 0:
            self.paybtn.place_forget()
        table2.delete(selected_row2)
        self.clearSeller()
        db1 = db.DB1()
        db1.delete_products(p1)
        messagebox.showinfo("توجه", " کالای مورد نظر از سبد خرید خارج  شد ")

    def onclickBuy(self,e):
        global table2, pcounttxt, amount, lbla
        if int(self.pcounttxt.get()) > int(p1.get_pcount()):
            messagebox.showwarning("خطا", "موجودی کالا کافی نیست ")
        else:
            self.pfprice = int(p1.get_pprice()) - int(p1.get_pprice()) * int(p1.get_pdiscount()) / 100
            self.count = self.pcounttxt.get()
            total = int(self.pfprice * int(self.count))
            amount = int(amount + self.pfprice * int(self.count))
            self.lbla.config(text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ")
            if int(amount) == 0:
                self.paybtn.place_forget()
            else:
                self.paybtn.place(x=950, y=550)
            table2.insert('', 'end', text="1", values=[total, self.count, int(self.pfprice), p1.get_pdiscount()
                , p1.get_pprice(), p1.get_pcolor(), p1.get_pname(), p1.get_pseller()])
            self.clearSeller()

    # --------------------------------------------------------------------
    def onclickSearch(self,e):
        self.updateTable1()

    # ---------------------------------- Update table1 (Store) -----------------------------
    def updateTable1(self):
        query = self.srchtxt.get()
        db1 = db.DB1()
        for item in table1.get_children():
            table1.delete(item)
        self.result = db1.searchProduct(isSeller, curr_user, query)
        for item in self.result:
            self.finalPrice = item[4] - (item[3] * item[4] / 100)
            table1.insert('', 'end', text="1",
                          values=[item[2], item[5], self.finalPrice, item[3], item[4], item[1], item[0]])

    def removeBasket(self):
        self.basketList = []
        for item in table2.get_children():
            values = table2.item(item, "values")
            self.basketList.append(values)
            table2.delete(item)
        db1 = db.DB1()
        db1.updateCount(self.basketList)

    def onclickPay(self,e):
        global table2, amount, wallet, curr_user
        if int(amount) > int(wallet):
            messagebox.showwarning("خطا", "اعتبار مالی شما کافی نیست ")
        else:
            wallet = (int(wallet) - int(amount))
            curr_user.set_wallet(wallet)
            self.command = db.DB1()
            self.command.updateWallet(curr_user, wallet)
            self.lblw.config(text="  اعتبار : " + str(wallet) + " ریال ")
            # Wallet.set("")

            messagebox.showinfo("پیغام", " خرید با موفقیت انجام شد ")
            amount = 0
            self.lbla.config(text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ")
            self.removeBasket()
            self.updateTable1()
            self.paybtn.place_forget()

    def onclickExit(self,scr3):
        scr3.destroy()

    def onclickCancel(self,e):
        self.clearSeller()

    # =================================== main part ===============================================
    def mainPart(self):
        global namtxt, famtxt, usrtxt1, passtxt1, seller, mcodetxt, curr_user, \
            table1, table2, isSeller, p1, amount, name, family, seller, wallet
        # curr_user = ""
        # begin()
        # if not curr_user:
        #     sys.exit("----  Exit  ----")
        self.scr3 = Tk()
        self.scr3.geometry("%dx%d+%d+%d" % (1500, 750, 10, 10))
        self.scr3.configure(bg="#36C9F4")
        self.title = "به سامانه خرید اینترنتی آنلاین شاپ خوش آمدید" + (" " * 180) + " آنلاین شاپ "
        self.scr3.title(self.title)
        self.scr3.iconbitmap("images/shopping.ico")
        self.scr3.resizable(False, False)

        usrnam = curr_user.get_usrnam()
        name = curr_user.get_name()
        family = curr_user.get_family()
        if curr_user.get_seller():
            seller = "فروشنده"
            isSeller = True
        else:
            seller = "مشتری"
            isSeller = False
        wallet = curr_user.get_wallet()
        self.fillUserProfile(self.scr3)
        self.showWallet(self.scr3)
        if isSeller:
            self.selling(self.scr3)
        else:
            self.buying(self.scr3)
        self.ttable1(self.scr3)

        self.fillTable1()
        self.ttable2(self.scr3)

        self.scr3.mainloop()

    # --------------------------------- User Profile  ------------------------------------
    def fillUserProfile(self, scr3):
        canvas = Canvas(scr3, width=400, height=300)
        canvas.place(x=1240, y=50)
        rect = canvas.create_rectangle(5, 5, 258, 300, outline="dark blue")
        self.user_img = PhotoImage(file="images/user1.png")
        self.lbl1 = Label(scr3, image=self.user_img)
        self.lbl1.place(x=1350, y=70)
        self.lbl2 = Label(scr3, text=self.usrnam + " : کد کاربری", bg="#36C9F4", fg="black", font="nazanin 15",
                          width=22)
        self.lbl2.place(x=1250, y=130)
        self.lbl3 = Label(scr3, text=name + " " + family, bg="#36C9F4", fg="black", font="nazanin 15", width=22)
        self.lbl3.place(x=1250, y=180)
        self.lbl4 = Label(scr3, text=seller, bg="#36C9F4", fg="black", font="nazanin 15", width=22)
        self.lbl4.place(x=1250, y=230)
        self.lblw = Label(scr3, text="  اعتبار : " + str(wallet) + " ریال ", bg="#36C9F4", fg="black",
                          font="nazanin 15",
                          width=22)
        self.lblw.place(x=1250, y=280)
        self.exit_image = PhotoImage(file="images/exit.png")
        self.exitbtn = Button(scr3, image=self.exit_image, command=lambda: self.onclickExit(scr3))
        self.exitbtn.bind("<Button-1>", )
        self.exitbtn.place(x=1250, y=60)

    def showWallet(self, scr3):
        # ---------------------------------  Charge Wallet ------------------------------------
        canvas = Canvas(scr3, width=400, height=300)
        canvas.place(x=1240, y=400)
        self.wallet_img = PhotoImage(file="images/wallet.png")
        self.lbl1 = Label(scr3, image=self.wallet_img)
        self.lbl1.place(x=1350, y=450)
        rectang = canvas.create_rectangle(5, 5, 258, 300, outline="dark blue")
        self.lbl1 = Label(scr3, text="افزایش اعتبار", fg="dark red", font="nazanin 18 bold")
        self.lbl1.place(x=1320, y=410)
        self.lbl2 = Label(scr3, text=": مبلغ افزایش ", fg="dark blue", font="nazanin 14 bold")
        self.lbl2.place(x=1395, y=520)
        self.Wallet = StringVar()
        self.wlttxt = Entry(scr3, textvariable=self.Wallet, font="nazanin 12 bold", bg="#36C9F4", fg="black",
                            justify="right",
                            width=12)
        self.wlttxt.place(x=1275, y=520)
        self.wlttxt.focus()
        self.lbl3 = Label(scr3, text="ریال", fg="dark blue", font="nazanin 12 bold")
        self.lbl3.place(x=1250, y=520)
        self.sub = Button(scr3, text="افزایش اعتبار", bg="green", width=10, font="nazanin 12 bold", fg="white")
        self.sub.bind("<Button-1>", self.chargeWallet)
        self.sub.place(x=1300, y=600)
        if isSeller:
            self.sub.place_forget()

    def chargeWallet(self, e):
        global lblw, scr3, wallet
        wallet = self.wlttxt.get()
        try:
            wallet = int(wallet) + curr_user.get_wallet()
        except:
            messagebox.showerror("خطا", wallet + "مقدار وارد شده نامعتبر است .")
        else:
            curr_user.set_wallet(wallet)
            self.command = db.DB1()
            self.command.updateWallet(curr_user, wallet)
            self.lblw.config(text="  اعتبار : " + str(wallet) + " ریال ")
            self.Wallet.set("")

    def onclickSaveGoods(self, evt):
        global p1
        p1 = p.Product()
        self.pname = self.pnametxt.get()
        self.pcolor = self.pcolortxt.get()
        self.pprice = self.ppricetxt.get()
        self.pdiscount = self.pdiscounttxt.get()
        self.pcount = self.pcounttxt.get()
        self.pseller = self.usrnam
        self.pfprice = int(self.pprice) - int(self.pprice) * int(self.pdiscount) / 100
        if self.pname == "" or self.pcolor == "" or self.pprice == "":
            messagebox.showwarning("توجه", "فیلدهای  ضروری را تکمیل کنید ")
            return
        p1.set_all_product(self.pname, self.pcolor, self.pseller, self.pprice, self.pcount, self.pdiscount)
        messagebox.showinfo("  توجه ",
                            f" ,  {self.pname} {self.pcolor}  ثبت شد ")
        command = db.DB1()
        command.save_product(p1)
        table1.insert('', 'end', text="1",
                           values=[self.pseller, self.pcount, int(self.pfprice), self.pdiscount, self.pprice, self.pcolor, self.pname])
        self.clearSeller()

    # -----------------------------------Selling  -----------------------------------
    def selling(self, scr3):
        self.Pname = StringVar()
        self.Pcolor = StringVar()
        self.Pprice = StringVar()
        self.Pfprice = StringVar()
        self.Pcount = StringVar()
        self.Pdiscount = StringVar()
        canvas = Canvas(scr3, width=400, height=655)
        canvas.place(x=800, y=50)
        self.sell_img = PhotoImage(file="images/selling.png")
        self.search_img = PhotoImage(file="images/searching1.png")
        self.lbl1 = Label(scr3, text="فروش کالا", fg="dark red", font="nazanin 18 bold")
        self.lbl1.place(x=950, y=60)
        self.lbls = Label(scr3, image=self.sell_img)
        self.lbls.place(x=980, y=130)
        self.rectang = canvas.create_rectangle(5, 5, 395, 650, outline="dark blue")
        self.pnametxt = Entry(scr3, textvariable=self.Pname, font="nazanin 10 bold", bg="#36C9F4", fg="black", justify="right",
                         width=35)
        self.pnametxt.place(x=850, y=200)
        self.lbl2 = Label(text=":نام کالا", fg="dark blue", font="nazanin 12 bold")
        self.lbl2.place(x=1100, y=200)
        self.pcolortxt = Entry(scr3, textvariable=self.Pcolor, font="nazanin 12 bold", bg="#36C9F4", fg="black", justify="right",
                          width=16)
        self.pcolortxt.place(x=950, y=260)
        self.lbl3 = Label(text=": رنگ", fg="dark blue", font="nazanin 12 bold")
        self.lbl3.place(x=1100, y=260)
        self.ppricetxt = Entry(scr3, textvariable=self.Pprice, font="nazanin 12 bold", bg="#36C9F4", fg="black", justify="right",
                          width=12)
        self.ppricetxt.place(x=985, y=320)
        self.lbl4 = Label(text=":قیمت ", fg="dark blue", font="nazanin 12 bold")
        self.lbl4.place(x=1100, y=320)
        self.pdiscounttxt = Entry(scr3, textvariable=self.Pdiscount, font="nazanin 12 bold", bg="#36C9F4", fg="black",
                             justify="right",
                             width=5)
        self.pdiscounttxt.place(x=850, y=320)
        self.lbl5 = Label(text=": تخفیف", fg="dark blue", font="nazanin 12 bold")
        self.lbl5.place(x=900, y=320)
        self.pcounttxt = Entry(scr3, textvariable=self.Pcount, font="nazanin 12 bold", bg="#36C9F4", fg="black", justify="right",
                          width=5)
        self.pcounttxt.place(x=1055, y=380)
        self.lbl6 = Label(text=":تعداد ", fg="dark blue", font="nazanin 12 bold")
        self.lbl6.place(x=1100, y=380)
        self.savebtn = Button(scr3, text="ثبت", bg="green", width=5, font="nazanin 15 bold", fg="white")
        self.savebtn.bind("<Button-1>", self.onclickSaveGoods)
        self.savebtn.place(x=820, y=400)
        self.returnbtn = Button(scr3, text="برگشت", bg="#ec1f26", width=5, font="nazanin 15 bold", fg="white")
        self.returnbtn.bind("<Button-1>", self.onclickDeleteTable1)
        self.returnbtn.place(x=820, y=400)
        self.returnbtn.place_forget()
        self.cancelbtn = Button(scr3, text="انصراف", bg="#0072c6", width=5, font="nazanin 15 bold", fg="white")
        self.cancelbtn.bind("<Button-1>", self.onclickCancel)
        self.cancelbtn.place(x=1020, y=400)
        self.cancelbtn.place_forget()
        self.lbls = Label(scr3, image=self.search_img)
        self.lbls.place(x=1120, y=600)
        self.Search = StringVar()
        self.srchtxt = Entry(scr3, textvariable=self.Search, font="nazanin 14 bold", bg="#36C9F4", fg="black", justify="right",
                        width=18)
        self.srchtxt.place(x=910, y=605)
        self.srchbtn = Button(scr3, text="جستجو", bg="green", width=5, font="nazanin 12 bold", fg="white")
        self.srchbtn.bind("<Button-1>", self.onclickSearch)
        self.srchbtn.place(x=820, y=600)
        # --------------------------------------Buy Goods ------------------------------------------

    def buying(self, scr3):
        global amount
        amount = 0
        self.Pname = StringVar()
        self.Pcolor = StringVar()
        self.Pprice = StringVar()
        self.Pfprice = StringVar()
        self.Pcount = StringVar()
        self.Pdiscount = StringVar()
        canvas = Canvas(scr3, width=400, height=655)
        canvas.place(x=800, y=50)
        self.buy_img = PhotoImage(file="images/buying.png")
        self.search_img = PhotoImage(file="images/searching1.png")
        self.lbl1 = Label(scr3, text="خرید کالا" ,fg="dark red", font="nazanin 18 bold")
        self.lbl1.place(x=950, y=60)
        self.lbls = Label(scr3, image=self.buy_img)
        self.lbls.place(x=980, y=130)
        self.rectang = canvas.create_rectangle(5, 5, 395, 650, outline="dark blue")
        self.pnametxt = Label(scr3, textvariable=self.Pname, font="nazanin 10 bold", bg="#36C9F4", fg="black", anchor=E,
                         width=30)
        self.pnametxt.place(x=850, y=200)
        self.lbl2 = Label(text=":نام کالا ", fg="dark blue", font="nazanin 15 bold")
        self.lbl2.place(x=1100, y=200)
        self.pcolortxt = Label(scr3, textvariable=self.Pcolor, font="nazanin 13 bold", bg="#36C9F4", fg="black", anchor=E,
                          width=15)
        self.pcolortxt.place(x=940, y=260)
        self.lbl3 = Label(text=": رنگ", fg="dark blue", font="nazanin 12 bold")
        self.lbl3.place(x=1100, y=260)
        self.ppricetxt = Label(scr3, textvariable=self.Pprice, font="nazanin 12 bold", bg="#36C9F4", fg="black", anchor=E,
                          width=11)
        self.ppricetxt.place(x=980, y=320)
        self.lbl4 = Label(text=":قیمت ", fg="dark blue", font="nazanin 15 bold")
        self.lbl4.place(x=1100, y=320)
        self.pdiscounttxt = Label(scr3, textvariable=self.Pdiscount, font="nazanin 14 bold", bg="#36C9F4", fg="black",
                             justify="right",
                             width=5)
        self.pdiscounttxt.place(x=850, y=320)
        self.lbl5 = Label(text=": تخفیف", fg="dark blue", font="nazanin 15 bold")
        self.lbl5.place(x=900, y=320)
        self.pcounttxt = Entry(scr3, textvariable=self.Pcount, font="nazanin 12", bg="#36C9F4", fg="black", justify="right",
                          width=5)
        self.pcounttxt.place(x=1050, y=380)
        self.pcounttxt.focus()
        self.lbl6 = Label(text=":تعداد ", fg="dark blue", font="nazanin 15 bold")
        self.lbl6.place(x=1100, y=380)
        self.buybtn = Button(scr3, text="افزودن به سبد", bg="green", width=8, font="nazanin 12 bold", fg="white")
        self.buybtn.bind("<Button-1>", self.onclickBuy)
        # if isSeller:
        self.buybtn.place(x=820, y=400)
        # else:
        #     savebtn.place_forget()
        self.deletebtn = Button(scr3, text="حذف از سبد", bg="#ec1f26", width=8, font="nazanin 12 bold", fg="white")
        self.deletebtn.bind("<Button-1>", self.onclickDeleteTable2)
        self.deletebtn.place(x=820, y=400)
        self.deletebtn.place_forget()
        self.cancelbtn = Button(scr3, text="انصراف", bg="#0072c6", width=5, font="nazanin 12 bold", fg="white")
        self.cancelbtn.bind("<Button-1>", self.onclickCancel)
        self.cancelbtn.place(x=1020, y=400)
        self.cancelbtn.place_forget()
        self.lbla = Label(scr3, text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ", bg="#36C9F4", fg="black",
                     font="nazanin 15",
                     width=34)
        self.lbla.place(x=810, y=460)
        self.paybtn = Button(scr3, text="پرداخت", bg="green", width=5, font="nazanin 12 bold", fg="white")
        self.paybtn.bind("<Button-1>", self.onclickPay)
        self.paybtn.place(x=950, y=550)
        self.paybtn.place_forget()
        self.lbls = Label(scr3, image=self.search_img)
        self.lbls.place(x=1120, y=630)
        self.Search = StringVar()
        self.srchtxt = Entry(scr3, textvariable=self.Search, font="nazanin 14 bold", bg="#36C9F4", fg="black", justify="right",
                        width=18)
        self.srchtxt.place(x=910, y=635)
        self.srchbtn = Button(scr3, text="جستجو", bg="green", width=5, font="nazanin 12 bold", fg="white")
        self.srchbtn.bind("<Button-1>", self.onclickSearch)
        self.srchbtn.place(x=820, y=630)

    # ----------------------------------------  Goods  Table -----------------------------------------

    def ttable1(self,scr3):
        global table1, table2
        canvas = Canvas(scr3, width=760, height=300)
        canvas.place(x=10, y=50)
        rectang = canvas.create_rectangle(5, 5, 755, 300, outline="dark blue")
        self.store_img = PhotoImage(file="images/store.png")
        self.lbl1 = Label(self.scr3, image=self.store_img)
        self.lbl1.place(x=350, y=2)
        # ------------------------------ Draw table1-----------------------------------
        self.cols = ("c1", "c2", "c3", "c4", "c5", "c6", "c7")
        table1 = (tkinter.ttk.Treeview(scr3, columns=self.cols, height=13, show="headings"))
        table1.place(x=20, y=60)
        table1.heading("#7", text="نام کالا")
        table1.column("#7", width=180, anchor=E)
        table1.heading("#6", text=" رنگ ")
        table1.column("#6", width=120, anchor=E)
        table1.heading("#5", text="قیمت")
        table1.column("#5", width=100, anchor=E)
        table1.heading("#4", text="تخفیف")
        table1.column("#4", width=50, anchor=E)
        table1.heading("#3", text="قیمت نهایی")
        table1.column("#3", width=100, anchor=E)
        table1.heading("#2", text="موجودی")
        table1.column("#2", width=90, anchor=E)
        table1.column("#1", width=100, anchor=E)
        table1.heading("#1", text="فروشنده")
        table1.bind("<Button-1>", self.fillFields1)

    # -----------------------------Fill fields for return goods from store---------------------------
    def fillFields1(self,e):
        global selected_row, p1
        selected_row = table1.selection()
        if selected_row:
            p1 = p.Product()
            p1.set_all_product(table1.item(selected_row)["values"][6], table1.item(selected_row)["values"][5],
                               table1.item(selected_row)["values"][0], table1.item(selected_row)["values"][4],
                               table1.item(selected_row)["values"][1], table1.item(selected_row)["values"][3])
            self.Pname.set(p1.get_pname())
            self.Pcolor.set(p1.get_pcolor())
            self.Pprice.set(p1.get_pprice())
            self.Pfprice.set(table1.item(selected_row)["values"][2])
            self.Pdiscount.set(p1.get_pdiscount())
            if isSeller:
                self.Pcount.set(p1.get_pcount())
                self.returnbtn.place(x=820, y=440)
                self.cancelbtn.place(x=1020, y=440)
                self.savebtn.place_forget()
            else:
                self.buybtn.place(x=820, y=400)
                self.deletebtn.place_forget()

    # ------------------------ Fill Fields  for delete goods from  shopping basket---------------------------
    def fillFields2(self,e):
        global selected_row2, p1, amount
        selected_row2 = table2.selection()
        if selected_row2:
            p1 = p.Product()
            p1.set_all_product(table2.item(selected_row2)["values"][6], table2.item(selected_row2)["values"][5],
                               table2.item(selected_row2)["values"][0], table2.item(selected_row2)["values"][4],
                               table2.item(selected_row2)["values"][1], table2.item(selected_row2)["values"][3])
            self.Pname.set(p1.get_pname())
            self.Pcolor.set(p1.get_pcolor())
            self.Pprice.set(p1.get_pprice())
            self.Pfprice.set(table2.item(selected_row2)["values"][2])
            self.Pdiscount.set(p1.get_pdiscount())
            self.buybtn.place_forget()
            self.Pcount.set(p1.get_pcount())
            self.deletebtn.place(x=820, y=400)
            self.cancelbtn.place(x=980, y=400)

    # ---------------------------------------------------------------------------------
    #     print(self.scr3)
    #     self.ttable1(self.scr3)
        self.store_img = PhotoImage(file="images/store.png")
        self.lbl1 = Label(self.scr3, image=self.store_img)
        self.lbl1.place(x=350, y=2)

    # -------------------------------Draw Table2 --------------------------------------
    def ttable2(self,scr3):
        global table2
        canvas = Canvas(scr3, width=760, height=300)
        canvas.place(x=10, y=400)
        rectang = canvas.create_rectangle(5, 5, 755, 300, outline="dark blue")
        self.basket_img = PhotoImage(file="images/buying1.png")
        self.lbl1 = Label(self.scr3, image=self.basket_img)
        self.lbl1.place(x=350, y=351)

        cols = ("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8")
        table2 = (tkinter.ttk.Treeview(scr3, columns=cols, height=13, show="headings"))
        table2.place(x=20, y=410)
        table2.heading("#7", text="نام کالا")
        table2.column("#7", width=180, anchor=E)
        table2.heading("#6", text=" رنگ ")
        table2.column("#6", width=100, anchor=E)
        table2.heading("#5", text="قیمت")
        table2.column("#5", width=100, anchor=E)
        table2.heading("#4", text="تخفیف")
        table2.column("#4", width=50, anchor=E)
        table2.heading("#3", text="قیمت نهایی")
        table2.column("#3", width=100, anchor=E)
        table2.heading("#2", text="تعداد")
        table2.column("#2", width=50, anchor=E)
        table2.column("#1", width=100, anchor=E)
        table2.heading("#1", text="مبلغ کل")
        table2.column("#8", width=60, anchor=E)
        table2.heading("#8", text="فروشنده")
        table2.bind("<Button-1>", self.fillFields2)

    # -------------------------------Draw Table1 --------------------------------
    #     self.ttable2(scr3)
    #     self.basket_img = PhotoImage(file="images/buying1.png")
    #     self.lbl1 = Label(scr3, image=self.basket_img)
    #     self.lbl1.place(x=350, y=360)

    # -------------------------------fill Table1 --------------------------------
    def fillTable1(self):
        db1 = db.DB1()
        self.result = db1.read_products(isSeller, curr_user)
        for item in self.result:
            finalPrice = item[4] - (item[3] * item[4] / 100)
            table1.insert('', 'end', text="1",
                          values=[item[2], item[5], finalPrice, item[3], item[4], item[1], item[0]])

    def open_window(self):
        window = Window(self)
        window.grab_set()
