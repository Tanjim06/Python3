class Employee:
    company = 'Google'


tanjim = Employee()
tanjim.salary = "30k"
tanvir = Employee()
tanvir.salary = "300k"
print(tanjim.company)
print(tanvir.company)

Employee.company = 'YouTube'    #this will change the company name

print(tanjim.company)
print(tanvir.company)



