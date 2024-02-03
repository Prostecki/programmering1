# skapa en variabeln för att ange ett heltal
integer = int(input('Ange ett heltal: '))

# räknare
count = 0

while count < integer:
    #division med resten - 0
    if count % 3 == 0:
        # utföra print red
        print('red')
    # else if... med resten - 1
    elif count % 3 == 1:
        print('green')
    # annars white
    else:
        print('white')
    
    # lägga till ett värde
    count += 1