class Number:
    def __init__(self,num):
        self.num = num

    def __str__(self):
        return f'the number is : {self.num}'    
    
    def __len__(self):
        return 1
    

n1 = Number(5)
print(n1)    
print(len(n1))