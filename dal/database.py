import psycopg2
import  dal.userclass as u
from tkinter import messagebox


class DB1():

    def getConnection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="sang101",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")
        return connection

    def save_user(self, user):
        usrnam = user.get_usrnam()
        passwrd = user.get_passwrd()
        name = user.get_name()
        family = user.get_family()
        seller = user.get_seller()

        mellicode = user.get_mellicode()
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(
            f"insert into users (username ,password, name , family , seller,mellicode , wallet) "
            f"values ('{usrnam}' ,'{passwrd}', '{name}' , '{family}' , {seller} , '{mellicode}' , 0 )")
        con.commit()
        cursor.close()

    def find_usernam(self, user):
        usrnam = user.get_usrnam()
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(f"select * from users where username = '{usrnam}'")
        my_result = cursor.fetchall()
        return (my_result)

    def find_mellicode(self, user):
        mellicode = user.get_mellicode()
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(f"select * from users where mellicode = '{mellicode}'")
        my_result = cursor.fetchall()
        return (my_result)

    def valid_user(self, usrnam, passwrd):
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(f"select * from users where username = '{usrnam}' and password = '{passwrd}'")
        result = cursor.fetchall()
        if result:
            u1 = u.Usr()
            u1.set_usr_all(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5],
                           result[0][6])
            return (u1)
        else:
            return None

    def updateWallet(self, user, wallet):
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(f"update  users set wallet =  {wallet} where  username = '{user.get_usrnam()}'")
        con.commit()
        cursor.close()

    # ----------------------------------Product -------------------------------------------
    def save_product(self, product):
        pname = product.get_pname()
        pcolor = product.get_pcolor()
        pseller = product.get_pseller()
        pprice = product.get_pprice()
        pdiscount = product.get_pdiscount()
        pcount = product.get_pcount()
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(
            f"insert into products (name ,color, seller , discount , price, count ) "
            f"values ('{pname}' ,'{pcolor}', '{pseller}' , {pdiscount} , {pprice} , {pcount})")
        con.commit()
        cursor.close()

    def read_products(self, isSeller, user):
        con = self.getConnection()
        cursor = con.cursor()
        if isSeller:
            cursor.execute(f"select * from products where count <> 0 and seller = '{user.get_usrnam()}'order by name")
        else:
            cursor.execute(f"select * from products where count <> 0 order by name")
        my_result = cursor.fetchall()
        cursor.close()
        return (my_result)

    def delete_products(self, p1):
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(f"delete from products where name ='{p1.get_pname()}' and color = '{p1.get_pcolor()}' "
                       f"and seller = '{p1.get_pseller()}' and price = {p1.get_pprice()} and "
                       f"count = {p1.get_pcount()} and discount = {p1.get_pdiscount()}")
        con.commit()
        cursor.close()

    def updateCount(self, list):
        con = self.getConnection()
        cursor = con.cursor()
        for item in list:
            cursor.execute(
                f"update  products set count =  count - {item[1]} where name = '{item[6]}' and color = '{item[5]}'"
                f" and seller = '{item[7]}' and price = {item[4]} and discount = {item[3]}")
        con.commit()
        cursor.close()

    def searchProduct(self, isSeller, user, query):
        con = self.getConnection()
        cursor = con.cursor()
        if isSeller:
            cursor.execute(f"select * from products where (count > 0 and seller = '{user.get_usrnam()}')"
                           f" and  (name like'%{query}%' or color like '%{query}%') order by name")
        else:
            cursor.execute(f"select * from products where count > 0 and (seller like '%{query}%' or name like'%{query}%' or "
              f" color like '%{query}%') order by name")
        my_result = cursor.fetchall()
        cursor.close()
        return (my_result)
