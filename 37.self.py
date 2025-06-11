class Employee:
    company = 'Google'
    def getSalary(self):        
        print(f'The company is {self.company}. Salary is {self.salary}')

tanjim = Employee()  
tanjim.salary = '1000k'
tanjim.getSalary()        # Employee.getSalary(tanjim) #getSalary takes tanjim as self


