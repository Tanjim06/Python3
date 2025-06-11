class Employee:
    company = 'Google'
    salary = 6000
    salaryBonus = 1000

    @property                     #by using property decorator the function became a property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    
    @totalSalary.setter         #it is a setter function
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary

tanjim = Employee()
print(tanjim.totalSalary)
tanjim.totalSalary = 10000
print(tanjim.salary)
print(tanjim.salaryBonus)