'''write a python program to display a user entered name followed by 
good afternoon using input function'''

# name = input("What is your name??")
# print("Good afternoon, "+name)

'''write a program to fill in a letter template given below with name date'''
# letter = '''Dear <NAME>
#             YOU ARE SELECTED!
#              <DATE> '''

# name = input("What is your name??")
# date = input("date : ")
# letter=letter.replace("<NAME>",name)
# letter=letter.replace("<DATE>",date)
# print(letter)


#write a program to detect double spaces in string
# a = input("What is your  full name??")
# doubleSpaces =a.find(" ")
# print(doubleSpaces)

#replace the double spaces with single spaces
# a = "my  name is tanjim  ahmed"
# a = a.replace("  "," ")
# print(a)

#write a program to format the following letter using escape sequence character 

letter = "Hello Tanjim,Welcome to python community"
formated_letter = "Hello Tanjim,\nWelcome to python community\nThanks!!!"
print(formated_letter)