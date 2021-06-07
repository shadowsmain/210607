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

class Student:

    def __init__(self, name, birth_date, address):
        self.name = name
        self.birth_date = birth_date
        self.address = address



class Group:

    def __init__(self, name):
        self.name = name
        self.students = []


student_1 = Student('Владислав', '18.04.2002', 'г.Курган, центр')
group_1 = ('ИСиП-33')
