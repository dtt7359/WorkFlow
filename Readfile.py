import requests
class Readfile:

    def read_file(self):
        # we get the file path by input or give path
        test_file = open(r"C:\Users\dtt7359\Documents\tech1_java.txt", "r")
        # test_file = open(input("input file"), "r")
        #read the file
        readfile = test_file.read()
        test_url = "http://httpbin.org/post"
        test_response = requests.post(test_url, files = {"form_field_name": test_file})
        #if file response is working print response else give error
        if test_response.ok:
            print("Upload completed successfully!")
            print(test_response.text)
            #if file upload successfully call general_info
            self.general_info()
        else:
            print("Something went wrong!")



    def general_info(self,classification = True):
        section = input('''choose a category: 1). Enviromental science
                                              2). Enviromental technology
                                              3). Natural Resource Management''')
        classification = input('''choose a category: 1). Air pollution management
                                              2). Carbon footprint analysis
                                              3). Conservation biology
                                              4). Disaster and adaption
                                              5). Ecosystem adaption''')
        submit = [section, classification]
        print(submit)
        # if we will get genral_info call to suggest_review
        self.suggest_reviews()

    def suggest_reviews(self,name= True, e_mail= True):
        print("Please Suggest reviews!!!")
        name = input("'Enter your Name'")
        e_mail = input("'Enter your e-mail'")
        reviews = input("Type your review Here")
