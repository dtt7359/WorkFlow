class User_info:
    # def __init__(self,name = "abc"):
    #     self.name = name
    #     self.username = ""
    #     self.password = ""

    #get the name and return in private member
    def get_name(self):
        return self.__name

    # we use set for chnaging the info
    def set_name(self,new_name):
        self.__name = new_name

    def get_username(self):
        return self.__username

    def set_username(self,new_username):
        self.__username = new_username

    def get_password(self):
        return self.__password

    def set_password(self, new_pass):
        self.__password = new_pass

ask = User_info()
ask.set_name("xyz")
print(ask.get_name())