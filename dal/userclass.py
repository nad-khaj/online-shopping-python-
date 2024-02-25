class Usr:
    def __init__(self):
        self.__usrnam = ""
        self.__passwrd = ""
        self.__name = ""
        self.__family = ""
        self.__seller = False
        self.__mellicode = ""
        self.__wallet = 0

    def  set_usrnam(self,usrnam):
        self.__usrnam = usrnam

    def set_passwrd(self, passwrd):
        self.__passwrd = passwrd

    def  set_name(self,name):
        self.__name = name

    def  set_family(self,family ):
        self.__family = family

    def  set_seller(self,seller):
        self.__seller  =  seller

    def  set_mellicode(self,mellicode):
        self.__mellicode  =  mellicode

    def set_wallet(self, wallet):
        self.__wallet = wallet
    def set_usr_all(self,name,family,usrnam,passwrd,seller,mellicode,wallet=0):
        self.__usrnam = usrnam
        self.__passwrd = passwrd
        self.__name = name
        self.__family = family
        self.__seller = seller
        self.__mellicode = mellicode
        self.__wallet = wallet


    def get_usrnam(self):
        return self.__usrnam


    def get_passwrd(self):
        return self.__passwrd


    def get_name(self):
        return self.__name


    def get_family(self):
        return self.__family


    def get_seller(self):
        return self.__seller

    def get_mellicode(self):
        return self.__mellicode
    def get_wallet(self)->int:
        return self.__wallet