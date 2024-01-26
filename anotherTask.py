numSum = 0
count = 0

while True:
    number = input(f"Ange ett tal..(avsluta med 'X')")
    if number.lower() == 'x':
        break
    numSum += float(number)
    count += 1

if count > 0:
    average = numSum / count
    print(average)
else:
    print("Inga tal har matats in.")

