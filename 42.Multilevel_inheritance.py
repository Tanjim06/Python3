class Person:
    country = 'Bangladesh'
    def takeWalk(self):
        print('I am walking')

class Employee(Person):
    copmpany = 'Google'
    def getSalary(self):
        print(f'The salary is {self.salary}')    
    def takeWalk(self):
        print('I am a employee and I am walking')        

class Programmer(Employee):
    company = 'Activision'
    language = 'Python'
    def getSalary(self):
        print('No money here')

p = Person()
p.takeWalk()
e = Employee()
e.takeWalk()
pr = Programmer()       
pr.takeWalk()
print(pr.company)
print(p.company)