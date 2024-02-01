def arPrimTal(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

try:
    primtal = int(input("Ange primtal..."))
    print("Ditt primtal mellan 1 och", primtal, ":")
    for num in range(2, primtal + 1):
        if arPrimTal(num):
            print(num, end = " ")
except ValueError:
    print("Du maste ange ett heltal.")