'''write a program to create dictionary of bangla words with 
values as their english translation. 
Provide user with on option to look it up'''

# myDict = {
#         "Aam" : "mango",
#         "surjo":"sun",
#         "prithibi":"earth"
#          }

# print("Options are : ", myDict.keys())
# a = input('Enter the name in bangla : ')
# print("The meaning is : ",myDict.get(a))



'''write a program to input eight numbers from the user and 
display all the unique numbers'''

# num1 = int(input("Enter number1 :"))
# num2 = int(input("Enter number2 :"))
# num3 = int(input("Enter number3 :"))
# num4 = int(input("Enter number4 :"))
# num5 = int(input("Enter number5 :"))
# num6 = int(input("Enter number6 :"))
# num7 = int(input("Enter number7 :"))
# num8 = int(input("Enter number8 :"))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)



'''can we have a set with 18(int) and "18"(str) as values in it?? '''

# s = {18,"18"}     #yes we can
# print(s)



'''what will be the length of follwing set??'''

# s = set()
# s.add(20)
# s.add(20.0)       #20.0 == 20
# s.add("20")
# print(s)
# print(len(s)) 



# s ={}, what is the data type of s??
# s = {}
# print(type(s))


''' Qustion--->"X" create an empty dictionary allow 4 friends to 
enter their favorite language as values and use keys as their names .
 Assume that the names are unique'''

# MyDict = {}

# friend1 = input("Enter your language tanvir: ")
# friend2 = input("Enter your language farhan: ")
# friend3 = input("Enter your language siyam: ")
# friend4 = input("Enter your language sabbir: ")

# MyDict["tanvir"] = friend1
# MyDict["farhan"] = friend2
# MyDict["siyam"] = friend3
# MyDict["sabbir"] = friend4

# print(MyDict)

#if name of 2 friends are same then what will happen qustion "x"??

# MyDict = {}

# friend1 = input("Enter your language tanvir: ")
# friend2 = input("Enter your language farhan: ")
# friend3 = input("Enter your language tanvir: ")
# friend4 = input("Enter your language sabbir: ")

# MyDict["tanvir"] = friend1
# MyDict["farhan"] = friend2
# MyDict["tanvir"] = friend3
# MyDict["sabbir"] = friend4

# print(MyDict)




#if name of 2 language are same then what will happen qustion "x"??

# MyDict = {}

# friend1 = input("Enter your language tanvir: ")
# friend2 = input("Enter your language farhan: ")
# friend3 = input("Enter your language siyam: ")
# friend4 = input("Enter your language sabbir: ")

# MyDict["tanvir"] = friend1
# MyDict["farhan"] = friend2
# MyDict["siyam"] = friend3
# MyDict["sabbir"] = friend4

# print(MyDict)


#can you change the values inside a list which contained in set s??

# s={10,"Tanjim",[10,12]}  #you cant store list inside of set
# print(s)

