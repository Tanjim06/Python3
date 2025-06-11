class Employee:
    company = 'Google'
    
    @staticmethod             #by using static method we dont need to pass self
    def greet():
        print('good morning tanjim')

tanjim = Employee()
tanjim.greet()         