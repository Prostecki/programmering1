try:
    integer = int(input('Ange ett heltal...'))

    print('Multiplikation for', integer, ':')

    for i in range(1, 11):
        print(integer, 'x', i, '=', integer * i)
        
except ValueError:
    print('you need to write an integer')