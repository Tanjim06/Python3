#def keyword is use to create a function

def percentage(marks):
    res = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return res

marks = [45,98,50,66]
percent = percentage(marks)
print(percent)

marks = [68,86,81,78]
percent = percentage(marks)
print(percent)


#quick quize: print "good day with a function"

def greet(name):
    print('Good Day '+ name)

greet('Tanjim')



def sumX(sum1 ,sum2):
    return sum1 + sum2

print(sumX(5,6))