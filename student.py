#from random import choice
#books = [' ya robot', 'lunnaya pil', 'tainstvenniy ostrov']

#for i in books:
#    print(i)

#class Students:

#def __init__(self, name, birthdate, adress):
#    self.name = name
 #   self.birthdate = "20.01.2002"
   # self.adress = "bluxera 10"

#    def start(self):
#        print("Студент 33 группы")

class Students:

    def __init__(self, name, date_brithday, address):
        self.name = name
        self.date_brithday = date_brithday
        self.address = address

    def display_info(self):
        print('Студентs: ', self.name)


class group:

    def __init__(self, name):
        self.name = name
        self.student = Student