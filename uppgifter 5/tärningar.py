import random

def kasta_tarning():
    return random.randint(1, 6)

antal_kast = int(input("Ange antal kast att simulera: "))

print("Resultat av kast med tva tarningar:")
for i in range(antal_kast):
    tarning1 = kasta_tarning()
    tarning2 = kasta_tarning()
    print("Tarning 1:", tarning1, " Tarning 2:", tarning2)


# Planeringen av programmeringsuppgiften
# 1. Förstå uppgiften: Förstå kraven och målen med uppgiften, vilket i detta fall är att skapa ett program som simulerar kast med två tärningar.
# 2. Definiera funktionalitet: Bestäm vilka funktioner som behövs för att uppnå målet, t.ex. en funktion för att simulera kast med en tärning och en annan för att simulera kast med två tärningar.
# 3. Strukturera koden: Dela upp koden i lämpliga funktioner för att göra den lättare att förstå och underhålla.
# 4. Planera input och output: Definiera hur användarens input kommer att hanteras och hur resultatet kommer att presenteras för användaren.

# Felsökning av enkla syntaxfel
# 1. Kontrollera stavning: Se till att alla nyckelord och variabelnamn är korrekt stavade.
# 2. Kontrollera parenteser och citattecken: Se till att alla parenteser och citattecken är ordentligt matchade och att inga syntaxfel förekommer.
# 3. Använd kommentarer: Använd kommentarer för att förklara koden och identifiera eventuella fel.
# 4. Testa stegvis: Testa varje del av koden stegvis för att identifiera och korrigera eventuella fel.

# Utvärdering av programmet
# Programmet lyckas med att uppnå sitt mål att simulera kast med två tärningar. Det använder en tydlig och lättförståelig kodstruktur med användning av funktioner för att separera olika delar av funktionaliteten. Programmet ger användaren möjlighet att ange antalet kast att simulera och presenterar resultaten på ett tydligt sätt. Detta gör programmet lättanvänt och lämpar sig väl för sitt syfte.