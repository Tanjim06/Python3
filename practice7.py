#write a program to find greatest of three numbers using function

# def max(num1,num2,num3):

#     if(num1>num2 and num1>num3):
#        return num1

#     elif(num2>num1 and num2>num3):    
#         return num2

#     else:
#         return num3

# m = max(16,32,100)
# print("The great numeber is : ",m)


#write a program to convert celceus to fahreheit using function
# C = int(input("Enter your tempareture in celceus : "))
# def Convert(c):
#     f = (c*(9/5))+32
#     return f
# res = Convert(C)
# print("The fahreheit tempareture is : ",res)


#prevent a python print() function to print newline at the end
# print("Hello", end="")
# print("How", end="")
# print("Are", end="")
# print("You", end="")
 


#write a recursive function to calculate the sum of first natural numbers
# num = int(input("Enter numeber : "))

# def sum(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return sum(n-1)+n

# s = sum(num)
# print("The sum is ", s)



#write a function which converst inchs to cm
# I = int(input("Enter inchs : "))
# def convert(i):
#     return i*2.54

# c = convert(I)

# print(f"This is {c} cm")


#write a function to remove a given word from a string and strip it at same time
# word = "He is a good boy"
# def remove_split(string,word):
#     newStr = string.replace(word,"")
#     return newStr
# n = remove_split(word,"a")
# print(n)


#write a function to print multiplication table of a given number
num = int(input("Enter number : "))
def multi(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")

multi(num)        