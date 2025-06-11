t = open('test.txt','r')
#reads the first line
data = t.readline()       
print(data)
#reads the second line
data = t.readline()
print(data)
t.close()
