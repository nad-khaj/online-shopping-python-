import sys
import tkinter
from tkinter import *
from tkinter import ttk
import userclass as u
import productclass as p
import database as db
from tkinter import messagebox


# ---------------------------------- Save User Information -----------------------
# def onclickSave(scr2, seller):
#     u1 = u.Usr()
#     name = namtxt.get()
#     family = famtxt.get()
#     usrnam = usrtxt.get()
#     passwrd = passtxt.get()
#     mellicode = mcodetxt.get()
#     if name == "" or family == "" or usrnam == "" or passwrd == "" or mellicode == "":
#         messagebox.showwarning("توجه", "فیلدهای خالی را تکمیل کنید ")
#     else:
#         u1.set_usr_all(name, family, usrnam, passwrd, seller, mellicode, 0)
#         command = db.DB1()
#         if command.find_usernam(u1):
#             messagebox.showwarning(" توجه:", f"**   کد کاربری تکراری است .{usrnam}**   ")
#         elif command.find_mellicode(u1):
#             messagebox.showwarning(" توجه:", f"**   کد ملی تکراری است .{mellicode}**   ")
#         else:
#             messagebox.showinfo(f"{name}  {family} ",
#                                 " ثبت نام انجام شد . جهت ورود کد کاربری و رمز خود را وارد کنید :)")
#             command.save_user(u1)
#             scr2.destroy()
#
#
# # --------------------------------User register------------------------------
# def register(scr1):
#     # global  scr1
#     scr2 = tkinter.Toplevel(scr1)
#     scr2.geometry("%dx%d+%d+%d" % (350, 500, 400, 250))
#     scr2.configure(bg="blue")
#     scr2.title("ثبت نام در سامانه ")
#     scr2.iconbitmap("images/shopping.ico")
#     scr2.resizable(False, False)
#     # -----------------labels ------------------------
#     global namtxt, famtxt, usrtxt, passtxt, seller, mcodetxt
#     Name = StringVar()
#     Family = StringVar()
#     Usrnam = StringVar()
#     Passwrd = StringVar()
#     seller = BooleanVar()
#     Mellicode = StringVar()
#     lbl1 = Label(scr2, text=":نام ", fg="white", bg="blue")
#     lbl1.place(x=270, y=50)
#     lbl2 = Label(scr2, text=":نام خانوادگی ", fg="white", bg="blue")
#     lbl2.place(x=270, y=120)
#     lbl3 = Label(scr2, text=":کد ملی ", fg="white", bg="blue")
#     lbl3.place(x=270, y=190)
#     lbl4 = Label(scr2, text=":کد کاربری ", fg="white", bg="blue")
#     lbl4.place(x=270, y=260)
#     lbl5 = Label(scr2, text=":رمز عبور ", fg="white", bg="blue")
#     lbl5.place(x=270, y=330)
#
#     namtxt = Entry(scr2, textvariable=Name, font="nazanin 12 bold", bg="white", fg="blue", justify="right",
#                    width=20)
#     namtxt.place(x=120, y=50)
#
#     famtxt = Entry(scr2, textvariable=Family, font="nazanin 12 bold", bg="white", fg="blue", justify="right",
#                    width=25)
#     famtxt.place(x=90, y=120)
#     mcodetxt = Entry(scr2, textvariable=Mellicode, font="nazanin 12 bold", bg="white", fg="blue", justify="right",
#                      width=20)
#     mcodetxt.place(x=120, y=190)
#
#     usrtxt = Entry(scr2, textvariable=Usrnam, font="nazanin 12 bold", bg="white", fg="blue", justify="right",
#                    width=20)
#     usrtxt.place(x=120, y=260)
#     usrtxt.focus()
#     passtxt = Entry(scr2, textvariable=Passwrd, font="nazanin 12 bold", bg="white", fg="blue", justify="right",
#                     width=20
#                     , show="*")
#     passtxt.place(x=120, y=330)
#     radioseller = Radiobutton(scr2, text="فروشنده", variable=seller, value=1, bg="blue")
#     radioseller.place(x=100, y=380)
#     radioseller = Radiobutton(scr2, text=" مشتری", variable=seller, value=0, bg="blue")
#     radioseller.place(x=220, y=380)
#     reg = Button(scr2, text="ثبت", bg="green", width=10, font="nazanin 12 bold", fg="white",
#                  command=lambda: onclickSave(scr2, seller.get()))
#     # reg.bind("<Button-1>", onclickSave)
#     reg.place(x=120, y=430)
#     scr2.mainloop()
#
#
# # ------------------------------------User  Login -------------------------------
# def login1(scr1):
#     global usrtxt1, passtxt1, curr_user
#     global curr_user
#     command = db.DB1()
#     usrnam = usrtxt1.get()
#     passwrd = passtxt1.get()
#
#     curr_user = command.valid_user(usrnam, passwrd)
#     if curr_user:
#         messagebox.showinfo("ورود به سامانه", f"   خوش آمدید{usrnam}  کاربر ")
#         scr1.destroy()
#     else:
#         messagebox.showwarning("توجه :", "  کد کاربری / رمز عبور صحیح نیست !! ")
#
#
# # ------------------------------- sign up / Register  ------------------------------
# def begin():
#     global usrtxt1, passtxt1, curr_user
#     scr1 = Tk()
#     scr2 = ""
#     scr1.geometry("%dx%d+%d+%d" % (300, 250, 600, 200))
#     scr1.configure(bg="dark blue")
#     scr1.title("ورود به سامانه ")
#     scr1.iconbitmap("images/shopping.ico")
#     scr1.resizable(False, False)
#     lbl1 = Label(scr1, text=":کد کاربری ", fg="white", bg="dark blue")
#     lbl1.place(x=200, y=50)
#     Usrnam = StringVar()
#     Passwrd = StringVar()
#     usrtxt1 = Entry(scr1, textvariable=Usrnam, font="nazanin 12 bold", bg="white", fg="dark blue", justify="right",
#                     width=20)
#     usrtxt1.place(x=50, y=50)
#     usrtxt1.focus()
#     passtxt1 = Entry(scr1, textvariable=Passwrd, font="nazanin 12 bold", bg="white", fg="dark blue", justify="right",
#                      width=20
#                      , show="*")
#     passtxt1.place(x=50, y=120)
#     lbl2 = Label(scr1, text=":رمز عبور ", fg="white", bg="dark blue")
#     lbl2.place(x=200, y=120)
#     sub = Button(scr1, text="ورود", bg="green", width=5, font="nazanin 12 bold", fg="white",
#                  command=lambda: login1(scr1))
#     # sub.bind("<Button-1>", login1)
#     sub.place(x=20, y=200)
#     reg1 = Button(scr1, text="ثبت نام", bg="dark blue", width=5, font="nazanin 12 bold", fg="yellow",
#                   command=lambda: register(scr1))
#     reg1.place(x=220, y=200)
#     scr1.mainloop()
#

def chargeWallet(e):
    global lblw, scr3, wallet
    wallet = wlttxt.get()
    try:
        wallet = int(wallet) + curr_user.get_wallet()
    except:
        messagebox.showerror("خطا", wallet + "مقدار وارد شده نامعتبر است .")
    else:
        curr_user.set_wallet(wallet)
        command = db.DB1()
        command.updateWallet(curr_user, wallet)
        lblw.config(text="  اعتبار : " + str(wallet) + " ریال ")
        Wallet.set("")


def onclickSaveGoods(e):
    global p1
    p1 = p.Product()
    pname = pnametxt.get()
    pcolor = pcolortxt.get()
    pprice = ppricetxt.get()
    pdiscount = pdiscounttxt.get()
    pcount = pcounttxt.get()
    pseller = usrnam
    pfprice = int(pprice) - int(pprice) * int(pdiscount) / 100
    if pname == "" or pcolor == "" or pprice == "":
        messagebox.showwarning("توجه", "فیلدهای  ضروری را تکمیل کنید ")
        return
    p1.set_all_product(pname, pcolor, pseller, pprice, pcount, pdiscount)
    messagebox.showinfo("  توجه ",
                        f" ,  {pname} {pcolor}  ثبت شد ")
    command = db.DB1()
    command.save_product(p1)
    table1.insert('', 'end', text="1", values=[pseller, pcount, int(pfprice), pdiscount, pprice, pcolor, pname])
    clearSeller()


def onclickCancel(e):
    clearSeller()


def clearSeller():
    Pname.set("")
    Pcolor.set("")
    Pprice.set("")
    Pfprice.set("")
    Pcount.set("")
    Pdiscount.set("")
    if isSeller:
        returnbtn.place_forget()
        savebtn.place(x=820, y=440)
    else:
        buybtn.place(x=820, y=400)
        deletebtn.place_forget()
    cancelbtn.place_forget()


def onclickDeleteTable1(e):
    global p1
    table1.delete(selected_row)
    clearSeller()
    db1 = db.DB1()
    db1.delete_products(p1)
    messagebox.showinfo("توجه", " کالای مورد نظر از لیست  کالاهای قابل فروش خارج  شد ")


def onclickDeleteTable2(e):
    global p1, amount
    amount = int(amount - table2.item(selected_row)["values"][0])
    lbla.config(text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ")
    if int(amount) == 0:
        paybtn.place_forget()
    table2.delete(selected_row)
    clearSeller()
    db1 = db.DB1()
    db1.delete_products(p1)
    messagebox.showinfo("توجه", " کالای مورد نظر از سبد خرید خارج  شد ")


def onclickBuy(e):
    global table2, pcounttxt, amount, lbla
    if int(pcounttxt.get()) > int(p1.get_pcount()):
        messagebox.showwarning("خطا", "موجودی کالا کافی نیست ")
    else:
        pfprice = int(p1.get_pprice()) - int(p1.get_pprice()) * int(p1.get_pdiscount()) / 100
        count = pcounttxt.get()
        total = int(pfprice * int(count))
        amount = int(amount + pfprice * int(count))
        lbla.config(text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ")
        if int(amount) == 0:
            paybtn.place_forget()
        else:
            paybtn.place(x=950, y=550)
        table2.insert('', 'end', text="1", values=[total, count, int(pfprice), p1.get_pdiscount()
            , p1.get_pprice(), p1.get_pcolor(), p1.get_pname(), p1.get_pseller()])
        clearSeller()


# --------------------------------------------------------------------
def onclickSearch(e):
    updateTable1()


# ---------------------------------- Update table1 (Store) -----------------------------
def updateTable1():
    query = srchtxt.get()
    db1 = db.DB1()
    for item in table1.get_children():
        table1.delete(item)
    result = db1.searchProduct(isSeller, curr_user, query)
    for item in result:
        finalPrice = item[4] - (item[3] * item[4] / 100)
        table1.insert('', 'end', text="1",
                      values=[item[2], item[5], finalPrice, item[3], item[4], item[1], item[0]])


def removeBasket():
    basketList = []
    for item in table2.get_children():
        values = table2.item(item, "values")
        basketList.append(values)
        table2.delete(item)
    db1 = db.DB1()
    db1.updateCount(basketList)


def onclickPay(e):
    global table2, amount, wallet, curr_user
    if int(amount) > int(wallet):
        messagebox.showwarning("خطا", "اعتبار مالی شما کافی نیست ")
    else:
        wallet = (int(wallet) - int(amount))
        curr_user.set_wallet(wallet)
        command = db.DB1()
        command.updateWallet(curr_user, wallet)
        lblw.config(text="  اعتبار : " + str(wallet) + " ریال ")
        # Wallet.set("")

        messagebox.showinfo("پیغام", " خرید با موفقیت انجام شد ")
        amount = 0
        lbla.config(text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ")
        removeBasket()
        updateTable1()
        paybtn.place_forget()


def onclickExit(scr3):
    scr3.destroy()


# ------------------------------------- main ----------------------------
global namtxt, famtxt, usrtxt1, passtxt1, seller, mcodetxt, curr_user, \
    table1, table2, isSeller, p1, amount
curr_user = ""
begin()
if not curr_user:
    sys.exit("----  Exit  ----")
scr3 = Tk()
scr3.geometry("%dx%d+%d+%d" % (1500, 750, 10, 10))
scr3.configure(bg="#36C9F4")
title = "به سامانه خرید اینترنتی آنلاین شاپ خوش آمدید" + (" " * 180) + " آنلاین شاپ "
scr3.title(title)
scr3.iconbitmap("images/shopping.ico")
scr3.resizable(False, False)

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
# --------------------------------- User Profile  ------------------------------------
canvas = Canvas(scr3, width=400, height=300)
canvas.place(x=1240, y=50)
rect = canvas.create_rectangle(5, 5, 258, 300, outline="dark blue")
user_img = PhotoImage(file="images/user1.png")
lbl1 = Label(scr3, image=user_img)
lbl1.place(x=1350, y=70)
lbl2 = Label(scr3, text=usrnam + " : کد کاربری", bg="#36C9F4", fg="black", font="nazanin 15", width=20)
lbl2.place(x=1250, y=130)
lbl3 = Label(scr3, text=name + " " + family, bg="#36C9F4", fg="black", font="nazanin 15", width=20)
lbl3.place(x=1250, y=180)
lbl4 = Label(scr3, text=seller, bg="#36C9F4", fg="black", font="nazanin 15", width=20)
lbl4.place(x=1250, y=230)
lblw = Label(scr3, text="  اعتبار : " + str(wallet) + " ریال ", bg="#36C9F4", fg="black", font="nazanin 15", width=20)
lblw.place(x=1250, y=280)
exit_image = PhotoImage(file="images/exit.png")
exitbtn = Button(scr3, image=exit_image, command=lambda: onclickExit(scr3))
# exitbtn.bind("<Button-1>", )
exitbtn.place(x=1250, y=60)
# ---------------------------------  Charge Wallet ------------------------------------
canvas = Canvas(scr3, width=400, height=300)
canvas.place(x=1240, y=400)
wallet_img = PhotoImage(file="images/wallet.png")
lbl1 = Label(scr3, image=wallet_img)
lbl1.place(x=1350, y=450)
rectang = canvas.create_rectangle(5, 5, 258, 300, outline="dark blue")
lbl1 = Label(scr3, text="افزایش اعتبار", fg="dark red", font="nazanin 18 bold")
lbl1.place(x=1320, y=410)
lbl2 = Label(scr3, text=": مبلغ افزایش ", fg="dark blue", font="nazanin 14 bold")
lbl2.place(x=1395, y=520)
Wallet = StringVar()
wlttxt = Entry(scr3, textvariable=Wallet, font="nazanin 12 bold", bg="#36C9F4", fg="black", justify="right",
               width=20)
wlttxt.place(x=1275, y=520)
wlttxt.focus()
lbl3 = Label(scr3, text="ریال", fg="dark blue", font="nazanin 12 bold")
lbl3.place(x=1250, y=520)
sub = Button(scr3, text="افزایش اعتبار", bg="green", width=10, font="nazanin 12 bold", fg="white")
sub.bind("<Button-1>", chargeWallet)
sub.place(x=1300, y=600)
if isSeller:
    sub.place_forget()
# -----------------------------------Selling  -----------------------------------
# def selling(scr3):
if isSeller:
    Pname = StringVar()
    Pcolor = StringVar()
    Pprice = StringVar()
    Pfprice = StringVar()
    Pcount = StringVar()
    Pdiscount = StringVar()
    canvas = Canvas(scr3, width=400, height=655)
    canvas.place(x=800, y=50)
    sell_img = PhotoImage(file="images/selling.png")
    search_img = PhotoImage(file="images/searching1.png")
    lbl1 = Label(scr3, text="فروش کالا", fg="dark red", font="nazanin 18 bold")
    lbl1.place(x=950, y=60)
    lbls = Label(scr3, image=sell_img)
    lbls.place(x=980, y=130)
    rectang = canvas.create_rectangle(5, 5, 395, 650, outline="dark blue")
    pnametxt = Entry(scr3, textvariable=Pname, font="nazanin 12 bold", bg="#36C9F4", fg="black", justify="right",
                     width=40)
    pnametxt.place(x=850, y=200)
    lbl2 = Label(text=":نام کالا", fg="dark blue", font="nazanin 15 bold")
    lbl2.place(x=1100, y=200)
    pcolortxt = Entry(scr3, textvariable=Pcolor, font="nazanin 15 bold", bg="#36C9F4", fg="black", justify="right",
                      width=20)
    pcolortxt.place(x=950, y=260)
    lbl3 = Label(text=": رنگ", fg="dark blue", font="nazanin 15 bold")
    lbl3.place(x=1100, y=260)
    ppricetxt = Entry(scr3, textvariable=Pprice, font="nazanin 15 bold", bg="#36C9F4", fg="black", justify="right",
                      width=15)
    ppricetxt.place(x=985, y=320)
    lbl4 = Label(text=":قیمت ", fg="dark blue", font="nazanin 15 bold")
    lbl4.place(x=1100, y=320)
    pdiscounttxt = Entry(scr3, textvariable=Pdiscount, font="nazanin 15 bold", bg="#36C9F4", fg="black",
                         justify="right",
                         width=5)
    pdiscounttxt.place(x=850, y=320)
    lbl5 = Label(text=": تخفیف", fg="dark blue", font="nazanin 15 bold")
    lbl5.place(x=900, y=320)
    print(pdiscounttxt.get())
    pcounttxt = Entry(scr3, textvariable=Pcount, font="nazanin 15 bold", bg="#36C9F4", fg="black", justify="right",
                      width=5)
    pcounttxt.place(x=1055, y=380)
    lbl6 = Label(text=":تعداد ", fg="dark blue", font="nazanin 15 bold")
    lbl6.place(x=1100, y=380)
    savebtn = Button(scr3, text="ثبت", bg="green", width=5, font="nazanin 15 bold", fg="white")
    savebtn.bind("<Button-1>", onclickSaveGoods)
    savebtn.place(x=820, y=400)
    returnbtn = Button(scr3, text="برگشت", bg="#ec1f26", width=5, font="nazanin 12 bold", fg="white")
    returnbtn.bind("<Button-1>", onclickDeleteTable1)
    returnbtn.place(x=820, y=400)
    returnbtn.place_forget()
    cancelbtn = Button(scr3, text="انصراف", bg="#0072c6", width=5, font="nazanin 12 bold", fg="white")
    cancelbtn.bind("<Button-1>", onclickCancel)
    cancelbtn.place(x=1020, y=400)
    cancelbtn.place_forget()
    lbls = Label(scr3, image=search_img)
    lbls.place(x=1120, y=600)
    Search = StringVar()
    srchtxt = Entry(scr3, textvariable=Search, font="nazanin 14 bold", bg="#36C9F4", fg="black", justify="right",
                    width=25)
    srchtxt.place(x=910, y=605)
    srchbtn = Button(scr3, text="جستجو", bg="green", width=5, font="nazanin 12 bold", fg="white")
    srchbtn.bind("<Button-1>", onclickSearch)
    srchbtn.place(x=820, y=600)
else:
    # --------------------------------------Buy Goods ------------------------------------------
    global amount
    amount = 0
    Pname = StringVar()
    Pcolor = StringVar()
    Pprice = StringVar()
    Pfprice = StringVar()
    Pcount = StringVar()
    Pdiscount = StringVar()
    canvas = Canvas(scr3, width=400, height=655)
    canvas.place(x=800, y=50)
    buy_img = PhotoImage(file="images/buying.png")
    search_img = PhotoImage(file="images/searching1.png")
    lbl1 = Label(scr3, text="خرید کالا", fg="dark red", font="nazanin 18 bold")
    lbl1.place(x=950, y=60)
    lbls = Label(scr3, image=buy_img)
    lbls.place(x=980, y=130)
    rectang = canvas.create_rectangle(5, 5, 395, 650, outline="dark blue")
    pnametxt = Label(scr3, textvariable=Pname, font="nazanin 12 bold", bg="#36C9F4", fg="black", anchor=E,
                     width=22)
    pnametxt.place(x=850, y=200)
    lbl2 = Label(text=":نام کالا", fg="dark blue", font="nazanin 15 bold")
    lbl2.place(x=1100, y=200)
    pcolortxt = Label(scr3, textvariable=Pcolor, font="nazanin 15 bold", bg="#36C9F4", fg="black", anchor=E,
                      width=12)
    pcolortxt.place(x=940, y=260)
    lbl3 = Label(text=": رنگ", fg="dark blue", font="nazanin 15 bold")
    lbl3.place(x=1100, y=260)
    ppricetxt = Label(scr3, textvariable=Pprice, font="nazanin 15 bold", bg="#36C9F4", fg="black", anchor=E,
                      width=10)
    ppricetxt.place(x=980, y=320)
    lbl4 = Label(text=":قیمت ", fg="dark blue", font="nazanin 15 bold")
    lbl4.place(x=1100, y=320)
    pdiscounttxt = Label(scr3, textvariable=Pdiscount, font="nazanin 15 bold", bg="#36C9F4", fg="black",
                         justify="right",
                         width=5)
    pdiscounttxt.place(x=850, y=320)
    lbl5 = Label(text=": تخفیف", fg="dark blue", font="nazanin 15 bold")
    lbl5.place(x=900, y=320)
    pcounttxt = Entry(scr3, textvariable=Pcount, font="nazanin 15 bold", bg="#36C9F4", fg="black", justify="right",
                      width=5)
    pcounttxt.place(x=1055, y=380)
    lbl6 = Label(text=":تعداد ", fg="dark blue", font="nazanin 15 bold")
    lbl6.place(x=1100, y=380)
    buybtn = Button(scr3, text="افزودن به سبد", bg="green", width=8, font="nazanin 12 bold", fg="white")
    buybtn.bind("<Button-1>", onclickBuy)
    # if isSeller:
    buybtn.place(x=820, y=400)
    # else:
    #     savebtn.place_forget()
    deletebtn = Button(scr3, text="حذف از سبد", bg="#ec1f26", width=8, font="nazanin 12 bold", fg="white")
    deletebtn.bind("<Button-1>", onclickDeleteTable2)
    deletebtn.place(x=820, y=400)
    deletebtn.place_forget()
    cancelbtn = Button(scr3, text="انصراف", bg="#0072c6", width=5, font="nazanin 12 bold", fg="white")
    cancelbtn.bind("<Button-1>", onclickCancel)
    cancelbtn.place(x=1020, y=400)
    cancelbtn.place_forget()
    lbla = Label(scr3, text="  مبلغ قابل پرداخت : " + str(amount) + " ریال ", bg="#36C9F4", fg="black",
                 font="nazanin 15",
                 width=31)
    lbla.place(x=810, y=460)
    paybtn = Button(scr3, text="پرداخت", bg="green", width=5, font="nazanin 12 bold", fg="white")
    paybtn.bind("<Button-1>", onclickPay)
    paybtn.place(x=950, y=550)
    paybtn.place_forget()
    lbls = Label(scr3, image=search_img)
    lbls.place(x=1120, y=630)
    Search = StringVar()
    srchtxt = Entry(scr3, textvariable=Search, font="nazanin 14 bold", bg="#36C9F4", fg="black", justify="right",
                    width=25)
    srchtxt.place(x=910, y=635)
    srchbtn = Button(scr3, text="جستجو", bg="green", width=5, font="nazanin 12 bold", fg="white")
    srchbtn.bind("<Button-1>", onclickSearch)
    srchbtn.place(x=820, y=630)
# ----------------------------------------  Goods  Table -----------------------------------------
canvas = Canvas(scr3, width=760, height=300)
canvas.place(x=10, y=50)
rectang = canvas.create_rectangle(5, 5, 755, 300, outline="dark blue")


def ttable1(scr3):
    global table1, table2
    canvas = Canvas(scr3, width=760, height=300)
    canvas.place(x=10, y=400)
    rectang = canvas.create_rectangle(5, 5, 755, 300, outline="dark blue")
    store_img = PhotoImage(file="images/store.png")
    lbl1 = Label(scr3, image=store_img)
    lbl1.place(x=400, y=70)
    # ------------------------------ Draw table1-----------------------------------
    cols = ("c1", "c2", "c3", "c4", "c5", "c6", "c7")
    table1 = (tkinter.ttk.Treeview(scr3, columns=cols, height=13, show="headings"))
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
    table1.bind("<Button-1>", fillFields1)


# -----------------------------Fill fields for return goods from store---------------------------
def fillFields1(e):
    global selected_row, p1
    selected_row = table1.selection()
    if selected_row:
        p1 = p.Product()
        p1.set_all_product(table1.item(selected_row)["values"][6], table1.item(selected_row)["values"][5],
                           table1.item(selected_row)["values"][0], table1.item(selected_row)["values"][4],
                           table1.item(selected_row)["values"][1], table1.item(selected_row)["values"][3])
        Pname.set(p1.get_pname())
        Pcolor.set(p1.get_pcolor())
        Pprice.set(p1.get_pprice())
        Pfprice.set(table1.item(selected_row)["values"][2])
        Pdiscount.set(p1.get_pdiscount())
        if isSeller:
            Pcount.set(p1.get_pcount())
            returnbtn.place(x=820, y=440)
            cancelbtn.place(x=1020, y=440)
            savebtn.place_forget()
        else:
            buybtn.place(x=820, y=400)
            deletebtn.place_forget()


# ------------------------ Fill Fields  for delete goods from  shopping basket---------------------------
def fillFields2(e):
    global selected_row, p1, amount
    selected_row = table2.selection()
    if selected_row:
        p1 = p.Product()
        p1.set_all_product(table2.item(selected_row)["values"][6], table2.item(selected_row)["values"][5],
                           table2.item(selected_row)["values"][0], table2.item(selected_row)["values"][4],
                           table2.item(selected_row)["values"][1], table2.item(selected_row)["values"][3])
        Pname.set(p1.get_pname())
        Pcolor.set(p1.get_pcolor())
        Pprice.set(p1.get_pprice())
        Pfprice.set(table2.item(selected_row)["values"][2])
        Pdiscount.set(p1.get_pdiscount())
        buybtn.place_forget()
        Pcount.set(p1.get_pcount())
        deletebtn.place(x=820, y=400)
        cancelbtn.place(x=980, y=400)


# ---------------------------------------------------------------------------------
ttable1(scr3)
store_img = PhotoImage(file="images/store.png")
lbl1 = Label(scr3, image=store_img)
lbl1.place(x=350, y=15)


# -------------------------------Draw Table2 --------------------------------------
def ttable2(scr3):
    global table2
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
    table2.bind("<Button-1>", fillFields2)


# -------------------------------Draw Table1 --------------------------------
ttable2(scr3)
basket_img = PhotoImage(file="images/buying1.png")
lbl1 = Label(scr3, image=basket_img)
lbl1.place(x=350, y=360)


# -------------------------------fill Table1 --------------------------------
def fillTable1():
    db1 = db.DB1()
    result = db1.read_products(isSeller, curr_user)
    for item in result:
        finalPrice = item[4] - (item[3] * item[4] / 100)
        table1.insert('', 'end', text="1", values=[item[2], item[5], finalPrice, item[3], item[4], item[1], item[0]])


fillTable1()
scr3.mainloop()
