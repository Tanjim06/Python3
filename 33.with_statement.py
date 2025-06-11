#the best way to open and close a file

with open('test2.txt','r') as f:
    data = f.read()

with open('test2.txt','w') as f:
    data = f.write("I am writting")
    
print(data)