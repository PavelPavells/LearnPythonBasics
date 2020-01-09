# File I/O
#my_file = open('test.txt')
#print(my_file.read())
#print(my_file.readlines())
#print(my_file.close())
try:
    with open('test.txt', mode='r+') as my_file:
        print(my_file.read())
        #print(my_file.readlines())
except FileNotFoundError as err:
    print('file does not exist')
    raise err 
except IOError as err:
    print('IO Error')
    raise err 
