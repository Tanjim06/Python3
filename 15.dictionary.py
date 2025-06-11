#use {} to crerate a dictionary

my_dict = {
           "Fast" : "In a quick manner",
           "Tanjim" : "A person",
           "Marks" : [90,85,88],
           "anotherdict" : {'Tanjim':'Programmer'}  #dict inside of dict
           
          }
           
#printing the value of the key 'Fast'
print(my_dict['Fast'])
#printing the value of the key 'Tanjim'
print(my_dict['Tanjim'])
#printing the value of the list 'Matks'
print(my_dict['Marks'])
#printing the Tanjim inside of anotherdict dictionary 
print(my_dict["anotherdict"]['Tanjim'])
#overwritting value to list inside of dictionary
my_dict['Marks'] = [92,86]
print(my_dict['Marks'])

