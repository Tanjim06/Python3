#creating an empty set
a = set()
#adding elements to an empty set
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(20)
print(a)
#adding tuples to a set
a.add((9,10,12,13))
print(a)
#prints the length of set
print(len(a))
#removing 5 from set
a.remove(5)
print(a)
#removes random values from set and return it 
print(a.pop())
#clears the set
# a.clear()
# print(a)