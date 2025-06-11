'''1.create a class c-2d vector and use tocreate another class representing a 3-d vector'''
# class c2dvector:
#     def __init__(self,i,j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"
            
        
# class c3dvector(c2dvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k "    
        

# v2d = c2dvector(1,5)
# v3d = c3dvector(1,5,9)
# print(v2d)
# print(v3d)

'''2.create a class pets from a class animals and further create class dog from pets. 
Add a method bark to class dog'''

# class Animal:
#     type = "mammals"

# class pet(Animal):
#     color = "white"

# class dog(pet):
#     @staticmethod
#     def bark():
#         print("Bark Bark")        

# d = dog()
# print(d.type)    
# print(d.color)   
# d.bark()     


'''3.create a class employee and add salary and increament properties to it. 
Write a method SalaryAfterIncreament method with a @property decorator with a setter 
which changes the value of increament based on salary'''

# class Employee:
#     salary = 1000
#     increament = 2

#     @property 
#     def salaryAfterIncreament(self):
#         return self.salary*self.increament
    
#     @salaryAfterIncreament.setter
#     def salaryAfterIncreament(self,salaryAfterInc):
#         self.increament = salaryAfterInc/self.salary

# e = Employee()
# print(e.salaryAfterIncreament)
# print(e.increament)
# e.salaryAfterIncreament = 10000
# print(e.increament)


'''4.write a class complex to represent complex numbers along with overloaded operators
 + and * which adds and multiplies them'''

# class Complex:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i

#     def __add__(self,c):
#         return complex(self.real+c.real,self.imaginary+c.imaginary)    
    

#     def __mul__(self,c):
#         mulReal = self.real*c.real-self.imaginary*c.imaginary
#         mulImg = self.real*c.imaginary+self.imaginary*c.real
#         return complex(mulReal,mulImg)    
    
#     def __str__(self):
#         return f"{self.real}+{self.imaginary}"  
    
# c1 = complex(1,5)
# c2 = complex(2,17)  
# print(c1+c2)  
# print(c1*c2)


'''5.write a class vector representing a vector of n dimensions.
Overload the + and * operator which calculates the sum and the dot product of them'''

# class Vector:
#     def __init__(self,vec):
#         self.vector = vec

#     def __str__(self):

#         index = 0
#         str1 =""
#         for i in self.vector:
#             str1 += f"{i}a{index} +"     
#             index += 1
#         return str1[:-1]
    
#     def __add__(self,vector2):

#         newList=[]
#         for i in range(len(self.vector)):           
#             newList.append(self.vector[i]+vector2.vector[i])
#         return Vector(newList)    
 
    
#     def __mul__(self,vector2):
#         sum = 1
#         for i in range(len(self.vector)):           
#             sum += (self.vector[i]*vector2.vector[i])
#         return sum

# v1 = Vector([1,2,3])
# v2 = Vector([5,8,13])
# print(v2)
# print(v1+v2)
# print(v1*v2)


'''6.write __str__() method to print the vector as follows:

        7i + 8j + 10k

Assume vector of dimension 3 for this problem'''

# class Vector:
#     def __init__(self,vec):
#         self.vector = vec

#     def __str__(self):
#         return f"{self.vector[0]}i + {self.vector[1]}j + {self.vector[2]}k"

# v1 = Vector([1,3,5])
# v2 = Vector([2,6,7])
# print(v1)
# print(v2)


'''Override the __len()__ method on vector of problem 5 to display the dimension of the vector'''

class Vector:
    def __init__(self,vec):
        self.vector = vec

    def __str__(self):

        index = 0
        str1 =""
        for i in self.vector:
            str1 += f"{i}a{index} +"     
            index += 1
        return str1[:-1]
    
    def __add__(self,vector2):

        newList=[]
        for i in range(len(self.vector)):           
            newList.append(self.vector[i]+vector2.vector[i])
        return Vector(newList)    
 
    
    def __mul__(self,vector2):
        sum = 1
        for i in range(len(self.vector)):           
            sum += (self.vector[i]*vector2.vector[i])
        return sum
    
    def __len__(self):
        return len(self.vector)


v1 = Vector([1,2,3])
v2 = Vector([5,8,13])
print(v2)
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))