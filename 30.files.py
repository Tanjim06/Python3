#use open function to read the content of a file
#open is a function which takes two arguement file name and mode(read mode,write mode)

# f = open('test.txt','r')
f = open('test.txt')    #by default the mode is r
# text = f.read()
text = f.read(6)    #reads first six characters
print(text)
f.close()




