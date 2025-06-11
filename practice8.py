'''write a program to read text from a given file poem.txt and find out 
whether it continues the word twinkle'''

# f = open("poem.txt")
# t = f.read()

# if "twinkle" in t :
#     print("twinkle is present")
# else:
#     print("twinkle is not present")  

# f.close()      




'''The game() function in a program lets a user play a game and refers the score 
as an integer.You need to read a file HI-score.txt which is either blank or
contain the previous  Hi-score. You need to write a program to update the Hi-score 
whenever game() breaks the high score'''


# def game():
#     return 100

# score = game()   #game function will return score and store it into score

# with open("Hi-score.txt") as f:
#     Hi_scoreStr = f.read()



# if Hi_scoreStr == "":       #if condition is true then it will update
     
#      with open("Hi-score.txt", "w") as f:
#         f.write(str(score))


# elif int(Hi_scoreStr)<score:  #if condition is true then it will update

#     with open("Hi-score.txt", "w") as f:
#         f.write(str(score))


'''write a program to generate multiplication tables for 2 to 20 and write it to 
the deffered files. Place this files into folder'''

# for i in range(2,21):
#     with open(f"tables/Multiplication_of_{i}".txt, "w") as f:
#         for j in range(1,11):
#             f.write(f"{i} X {j} = {i*j}\n")


'''a file contains a word donkey multiple times. You need to write a 
program which replaces the word with ##### by updating the same file'''

# with open("donkey.txt") as f:
#     content = f.read()

# content = content.replace("donkey","%$#@&")

# with open("donkey.txt", "w") as f:
#     f.write(content)



'''repeat the previous problem for a list of such words to be censored'''

# with open("donkey.txt") as f:
#     content = f.read()

# words = ["donkey","motherfucker","fucking"]
# for word in words:

#     content = content.replace(word,"%$#@&")

#     with open("donkey.txt", "w") as f:
#         f.write(content)



'''write a program to mine a log file and find out whether it contains python'''
# with open("log.txt") as f:
#     content = f.read()

# if "python" in content:
#     print("Yes!!!Python is present on the log file")
# else:
#     print("Python is not present")    



'''write a program to find out the line number where pytjon is present from 
the previous question'''

# content = True
# i=1
# with open("log.txt") as f :
#     while content:
#         content = f.readline()

#         if "python" in content:
#             print(content)
#             print(f"Python is present on line {i}")
#         i+=1    



'''write a program to make a copy of a text file this.txt'''

# with open("this.txt") as f:
#     content = f.read()

# with open("copy.txt", "w") as f:
#     f.write(content)

'''write a program to find out whether a file is identical 
and matches the content of another file'''

# file1='copy.txt'
# file2='this.txt'

# with open(file1) as f:
#     f1 = f.read()

# with open(file2) as f:
#     f2 = f.read()

# if f1==f2:
#     print('The files are identical')
# else:
#     print('The files are not identical')        

'''write a program to wipe out the contents of a file using python'''

# filename = "wipe.txt"

# with open(filename, "w") as f:
#     f.write("")


'''write program to rename a file'''

import os
oldfile = "oldfile.txt"
newfile = "rename_by_python.txt"

with open(oldfile) as f:
    content = f.read()

with open(newfile, "w") as f:
    f.write(content)

os.remove(oldfile)










                 
           








