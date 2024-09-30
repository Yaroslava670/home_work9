my_dict = {'Sasha': 14.09, 'Alex': 15.05}
print(my_dict['Sasha'])
print(my_dict.get('Bob'))
my_dict.update({'Den': 21.07, 'Sveta': 24.04})
a = my_dict.pop('Sasha')
print(a)
print(my_dict)
my_set = {1, 1, 2, 5, 5, 5, 8, 'string'}
print(my_set)
print(my_set.add(9))
print(my_set.add(4))
print(my_set)
print(my_set.discard(4))
print(my_set)
