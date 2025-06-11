'''__init__() is a special method which create automaticly when a object created.It is 
also known as constructor'''
class Employee:
    company = 'Google'

    def __init__(self, name ,salary):
        self.name = name
        self.salary = salary
        print('The object is created')

    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the name of the company is {self.company}")
        print(f"the salary is {self.salary}") 

tanjim = Employee('Tanjim','30k')     
tanjim.getDetails()   