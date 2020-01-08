#GENERATORS

range(100)
list(range(100))

def generator_function(num):
    for i in range(num):
        yield i * 2 
g = generator_function(10000)
next(g)
next(g)
print(next(g))
print(next(g))
# for item in generator_function(10000):
#     print(item)
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result
# my_list = make_list(100)
# print(list(range(100000)))

#FIBONACCI
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
for x in fib(20):
    print(x)