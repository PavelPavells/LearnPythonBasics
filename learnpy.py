# Fundamentals Data Types
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
# Math Functions
print(round(3.1))
print(abs(-4))
print(bin(24))
print('======================================')
# String
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
print(f"hi {name}. You are {age} years old")
print(name[3:5])
print(name[0:len(name)])
print(name.upper())
print('================DATA STRUCTURE======================')
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 2, 3, 'f', True]
#li[0] = 10
# print(li)
# print(li[2:4])
# li.pop(4)
# li.sort()
print(sorted(li))
print('===============DICTIONARY===============')
dictionary = {
    'a': [1, 2, 3, 4, 5],
    'b': True,
    'c': "Hello String",
    1: 123
}
print(dictionary['a'][3])
print(dictionary['b'])
print(dictionary[1])
print(dictionary.get('a'))

dictionary2 = dict(name='Pavel')
print(dictionary2)
print('c' in dictionary.keys())
print(dictionary.update({'ages': 55}))
print(dictionary)
print('=============TUPLES=============')
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(5 in my_tuple)
print('==============SET================')
my_set = {1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7}
my_set.add(100)
print(my_set)
my_set2 = {1, 2, 3, 4, 5}
print(my_set.difference(my_set2))
print('===================BASIC DATA PART 2===================')
is_old = False
is_licensed = True
if is_old or is_licensed:
    print('Yes')
elif is_licensed:
    print('Something!')
else:
    print('No')
user_password = '123'
user_login = 'pavel'
if user_password and user_login:
    print('Welcome!')
elif user_password == "" or user_login == "":
    print('Incorrect Data!')
else:
    print('Hello!')

is_friend = False
can_message = 'Hello!' if is_friend else 'Goodbye!'
print(can_message)
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in items:
    print(item)

people = {
    'name': 'Pavel',
    'age': '24'
}
for items in people.keys():
    print(items)
for items in people.values():
    print(items)
for i, char in enumerate(list(range(10))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')
print('===============FUNCTIONS===============')


def say_hello(name, surname):
    print(f'Hello, {name} {surname}')


say_hello('Pavel', 'Smirnov')
print('===========ARGUMENTS=============')


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(items)
    return max(evens)


print(highest_even([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14]))
class BigObject:
  pass
obj1 = BigObject()
print(type(obj1))
class PlayerCharacter:
  def __init__(self, name, age):
    super().__init__()
    self._name = name
    self._age = age
  def run(self):
    print('run')
  def speak(self):
    print(f'My name is {self._name}, and I am {self._age} years old')
  @classmethod
  def adding_things(cls, num1, num2):
      return cls('Pavel', num1 ** num2)
  @staticmethod
  def stc_method(param1, param2):
      return param1 + param2
player1 = PlayerCharacter('Pavel', 26)
#print(player1.name)
#print(player1.age)
print(player1.speak())
#player3 = PlayerCharacter.adding_things(123, 123)
#print(player1.name)
#print(player1.age)
#print(player1.run())
#print(player3)
print('===============OBJECT ORIENTIED PROGRAMMING================')
class User:
  def sign_in(self):
    print('logged in')
class Wizard(User):
  def __init__(self, name, power):
        super()
        self.name = name
        self.power = power
  def attack(self):
        print(f'attacking with power of {self.power}')
class Archer(User):
  def __init__(self, name, num_arrows):
        super()
        self.name = name
        self.num_arrows = num_arrows
  def attack(self):
        print(f'attacking with power of {self.num_arrows}')
wizard1 = Wizard('Pavel', 24)
print(wizard1.sign_in())