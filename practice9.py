'''1.create a class programmer for storing information of few programmers working at microsoft'''
# class Programmer:
#     company = 'Microsoft'

#     def __init__(self,name,product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"The name of the programmer is {self.name} and the product is {self.product}")


# p1 = Programmer("Tanjim","Gmail")
# p2 = Programmer("Farhan","Skype")

# p1.getInfo()
# p2.getInfo()


'''2.write a calculator capable of finding square,squareroot and cube'''
# class Calculator:
#     def __init__(self,num):
#         self.number = num

#     def square(self):
#         print(f"The square of {self.number} is {self.number**2}")

#     def cube(self):
#         print(f"The cube of {self.number} is {self.number**3}")

#     def sqrt(self):
#         print(f"The square of {self.number} is {self.number**0.5}")       

# a = Calculator(3)
# a.cube()
# a.square()
# a.sqrt()


'''3.create a class with a class attrbiute a; create an object form it and set a directly using a=0.
Does this change the class attribute??'''

# class Sample:
#     a = "Tanjim"

# obj1 = Sample()
# obj1.a = "Ahmed"

# print(Sample.a) #it will not change. You cant change a class attribute with an instance attribute

'''4.add a static method in problem 2 to greet the user with hello'''
# class Calculator:
#     def __init__(self,num):
#         self.number = num

#     def square(self):
#         print(f"The square of {self.number} is {self.number**2}")

#     def cube(self):
#         print(f"The cube of {self.number} is {self.number**3}")

#     def sqrt(self):
#         print(f"The square of {self.number} is {self.number**0.5}")    

#     @staticmethod
#     def greet():
#         print("*************HELLO!!!Welcome to the calculator****************")



# a = Calculator(3)
# a.greet()
# a.cube()
# a.square()
# a.sqrt()

        

        
'''write a class train which has methods to book a ticket, get status(no of seats) and
 get fare information of trains remaining under Bangladesh Railway'''

# class Train:
#     def __init__(self,name,fare,seats):
#         self.trainName = name
#         self.fare = fare
#         self.AvailableSeats = seats

#     def getStatus(self):
#         print(f"The name of the train is {self.trainName}")
#         print(f"The available seats are {self.AvailableSeats}")    
    
#     def getFareInfo(self):
#         print(f"The ticket price is Tk. {self.fare}")

#     def bookTicket(self):
#         if(self.AvailableSeats>0):
#             print(f"Your seat number is {self.AvailableSeats}")    
#             self.AvailableSeats = self.AvailableSeats - 1
#         else:
#             print("SORRY!!!The train is booked")

    
# InterCity = Train("Intercity",100,50)
# InterCity.getStatus()
# InterCity.getFareInfo()
# InterCity.bookTicket()
# InterCity.getStatus()



'''can you change the self parameter inside a class to something else (say 'Tanjim').
Try changing self to slf or Tanjim and see the effects '''

# class Sample:
#     def __init__(slf,name):
#         slf.name = name

# obj = Sample("Tanjim")
# print(obj.name)        