#FUNCTIONAL PROGRAMMING
# MAP, FILTER, ZIP, REDUCE
from functools import reduce
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 15)
    return new_list
print(multiply_by2([1,2,3,4,5,6,7,8,9,10]))
#MAP
def multiply_by3(item):
    return item * 3
arr = [1,2,3,4,5,6,7,8,9,10]
your_list = [2,5,3,2,6,7,1,2,3,4,5,6,7,3,4]
we_list = [1,2,3,4,5,6,7,8,9,10]
print(list(map(multiply_by3, arr)))
#FILTER
def filtered_items(item):
    return item % 2 != 0
print(list(filter(filtered_items, arr)))
#ZIP
print(list(zip(arr, your_list, we_list)))
#REDUCE
def accumulator(acc, item):
    return acc + item
print(reduce(accumulator, your_list, 0))
#LAMBDA
print(list(map(lambda item: item * 2314, your_list)))
print(reduce(lambda acc, item: acc * item, your_list))
print('==============LAMBDA LEARN================')
lambda_list = [11,12,13,14,15,16,17,18,19,20]
new_lambda_list = list(map(lambda num: num ** 2, lambda_list))
print(new_lambda_list)
#List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key = lambda x: x[0])
print(a)
#LIST COMPRENENSIONS
#list, set, dictionary
array = [char for char in "hello"]
array2 = [num for num in range(0, 50)]
array3 = [num * 3 for num in range(0, 50)]
array4 = [num ** 3 for num in range(0, 50)]
array5 = [num * 3 for num in range(0, 50) if num % 5 == 0]
print(array)
print(array2)
print(array3)
print(array4)
print(array5)

#DICTIONARY
simple_dict = {
    'a': 1,
    'b': 2
}
my_dictionary = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dictionary)
some_list = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

some_list2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
duplicates2 = set([x for x in some_list2 if some_list2.count(x) > 1])
print(duplicates2)