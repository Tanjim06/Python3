#Inheritance is a way to create a class from an existing class

class Employee:
    company = 'Google'

    def printDetails(self):
        print('This is employee')

class Programmer(Employee):    #the child class programmer is inherit from employee
    language = 'Python'

    def printLang(self):
        print(f'The language is {self.language}')

e = Employee()
e.printDetails()
p = Programmer()
p.printLang()
print(p.company)