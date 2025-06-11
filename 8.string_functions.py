par = "Tanjim ahmed is a good boy"


# String functions---->
# 1.len()---->calculates length of string
# print(len("Tanjim ahmed is a good boy"))
print(len(par))  

# 2.endswith()
print(par.endswith("boy"))  #Is the string ends with the word "boy"

# 3.count()
print(par.count("a"))   #how many "a" in the string
print(par.count("good"))   #how many "Tanjim" in the string

# 4.capilaize()
print(par.capitalize())  #Capitalize the first character of string

# 5.find()
print(par.find("good"))  #find the string

# 6.replace()
print(par.replace("good","active")) #replce good to active
