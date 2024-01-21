def är_primtal(num):
    """Funktion för att avgöra om ett tal är ett primtal."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primtal_mellan_1_och_n(n):
    """Funktion för att hitta och skriva ut primtal mellan 1 och n."""
    primtal_lista = [num for num in range(2, n+1) if är_primtal(num)]
    return primtal_lista

# Läs in ett tal från användaren
inläst_tal = int(input("Ange ett heltal: "))

# Hitta och skriv ut primtal mellan 1 och det inlästa talet
primtal_resultat = primtal_mellan_1_och_n(inläst_tal)
print(f"Primtal mellan 1 och {inläst_tal}:")
print(primtal_resultat)
