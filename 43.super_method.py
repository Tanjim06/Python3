class Person:
    def __init__(self):
        print('Person created')
        
    country = 'Bangladesh'
    def takeWalk(self):
        print('I am walking')

class Employee(Person):
    company = 'Google'
    def __init__(self):
        super().__init__()       #run its superclass constructor
        print('Employee created')
        
    def getSalary(self):
        print(f'The salary is {self.salary}')    
    def takeWalk(self):
        super().takeWalk()      #run its superclass takeWalk method
        print('I am a employee and I am walking')        

class Programmer(Employee):
    company = 'Activision'
    language = 'Python'   
    def takeWalk(self):
        super().takeWalk()    #run its superclass takeWalk method
        print('just walking')


p = Person()
p.takeWalk()

e = Employee()
e.takeWalk()

pr = Programmer()     
pr.takeWalk()

