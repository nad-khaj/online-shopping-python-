class Product():
    def __init__(self):
        self.__pname = ""
        self.__pcolor = ""
        self.__pseller = ""
        self.__pdiscount = 0
        self.__pprice = 0
        self.__pcount = 0

    def set_pname(self,pname):
        self.__pname = pname

    def set_pcolor(self, pcolor):
        self.__pcolor = pcolor

    def set_pseller(self, pseller):
        self.__pseller = pseller

    def set_pdiscount(self, pdiscount):
        self.__pdiscount = pdiscount

    def set_pprice(self, pprice):
        self.__pprice = pprice

    def set_pcount(self, pcount):
        self.__pcount = pcount

    def set_all_product(self,pname, pcolor, pseller, pprice, pcount, pdiscount):
        self.__pname = pname
        self.__pcolor = pcolor
        self.__pseller = pseller
        self.__pdiscount = pdiscount
        self.__pprice = pprice
        self.__pcount = pcount

    def get_pname(self):
        return self.__pname

    def get_pcolor(self ):
        return self.__pcolor

    def get_pseller(self):
        return self.__pseller

    def get_pdiscount(self):
        return self.__pdiscount

    def get_pprice(self):
        return self.__pprice

    def get_pcount(self):
        return self.__pcount