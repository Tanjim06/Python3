my_dict = {
           "Fast" : "In a quick manner",
           "Tanjim" : "A person",
           "Marks" : [90,85,88],
           "anotherdict" : {'Tanjim':'Programmer'},  #dict inside of dict
           1 : 2
          }

#printing keys
print(my_dict.keys())
# printing values
print(my_dict.values())
# printing key-values pair
print(my_dict.items())
#assign new key-values in dictionary
updateDict = {'Tanvir' : 'Friend'}
print(my_dict.update(updateDict))
print(my_dict)