class Employee():
    company = 'Google'
    city = 'Dhaka'
    salary = '100'

    # def changeSalary(self,sal):
        # self.salary = sal        #it will change the instance attribute

    # def changeSalary(self,sal):    
    #     self.__class__.salary = sal    #it will change the class attribute

    @classmethod              #accessing the class and changing class attributes 
    def changeSalary(cls,sal,com):
        cls.salary = sal           #Employee(cls) = sal---->cls means Employee
        cls.company = com

tanjim = Employee()
print(tanjim.salary)
print(Employee.salary)
tanjim.changeSalary(500,'YouTube')
print(Employee.salary)
print(tanjim.salary)
print(tanjim.company)