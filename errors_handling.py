##ERRORS HANDLING
#print(1 + 'hello!')

while True:
    try:
        age = 2
        10 / age
    except ValueError:
        print('please enter a number.')
        continue
    except ZeroDivisionError:
        print('Enter age higher than 0')
        break
    else:
        print('thanks')
        break
    finally:
        print('ok, i am finally done.')
    print('Can you hear me?')