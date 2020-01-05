#Fundamentals Data Types
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 5))
print(type(9 + 9.0))
print('======================================')
print(2 * 1024)
print(23 // 6)
print(23 % 6)
print('======================================')
#Math Functions
print(round(3.1))
print(abs(-4))
print(bin(24))
print('======================================')
#String
print(type('Hello'))
username = 'pavel '
password = '12345'
hello = '''
H
E
L
L
O
'''
print(username + password + hello)
name = 'Pavel'
age = 24
print(f'hi {name}. You are {age} years old')
print(name[3:5])
print(name[0:len(name)])
print(name.upper())
print('================DATA STRUCTURE======================')
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 2, 3, 'f', True]
#li[0] = 10
#print(li)
#print(li[2:4])
#li.pop(4)
#li.sort()
print(sorted(li))
print('===============DICTIONARY===============')
dictionary = {
  'a': [1,2,3,4,5],
  'b': True,
  'c': "Hello String",
  1: 123
}
print(dictionary['a'][3])
print(dictionary['b'])
print(dictionary[1])
print(dictionary.get('a'))

dictionary2 = dict(name = 'Pavel')
print(dictionary2)
print('c' in dictionary.keys())
print(dictionary.update({'ages': 55}))
print(dictionary)
print('=============TUPLES=============')
my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(5 in my_tuple)
print('==============SET================')
my_set = {1,2,3,4,5,5,5,5,6,6,7}
my_set.add(100)
print(my_set)
