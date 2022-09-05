from user_info import User_info
from Readfile import Readfile
class Register(Readfile):


    # register the user with name, username and password
    def register(self,User_info):
        reg.set_name(input("enter the name"))
        reg.set_username(input("enter the username"))
        reg.set_password(input("enter the password"))
        print("Register Successfully!!!")

    #login with above credentials
    def login(self,reg):
        l1 = input("enter the username")
        l2 = input("Enter the password")
        if(l2 == reg.get_password()):
            print("LOGIN SUCCESSFULLY!!! welcome", reg.get_name())
            self.read_file()
        else:
            print("enter valid details")




reg = User_info()


regis = Register()
regis.register(reg)
regis.login(reg)



