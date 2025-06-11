class Employee:
    company = 'Google'
    id = 12

class Freelancer:
    company = 'Fiverr'
    level = 0
    def UpgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):  
    language = 'Python'    

p = Programmer()
print(p.company)
print(p.company)
print(p.language)
p.UpgradeLevel()
print(p.level)
print(p.company)