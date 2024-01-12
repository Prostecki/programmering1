# Dokumentation för programmet "Momsberäkning"

# Planering:
# Denna kod är en enkel Python-applikation för att beräkna priset inklusive moms.
# Användaren ombeds ange priset utan moms, och programmet beräknar priset inklusive 25% moms.
# Planeringen inkluderade identifiering av nödvändiga variabler, input från användaren och enkel aritmetik för att utföra beräkningen.

# Felsökning av enkla syntaxfel:
# - Kontrollerade att alla variabler är korrekt deklarerade.
# - Använde lämpliga datatyper, som 'float', för att hantera pris med decimaler.
# - Använde undantagshantering för att undvika krascher om användaren anger icke-numeriska värden.

# Kort utvärdering:
# Programmet fungerar korrekt och ger förväntade resultat.
# Det är användarvänligt och enkelt att förstå.
# En eventuell förbättring kan vara att inkludera en loop för att låta användaren ange flera priser utan att behöva starta om programmet varje gång.

# Här är själva programmet:

try:
    # Användaren ombeds ange pris utan moms
    pris_exkl_moms = float(input("Ange pris exkl. moms: "))

    # Beräkna pris inklusive 25% moms
    pris_inkl_moms = pris_exkl_moms * 1.25

    # Skriv ut resultatet
    print(f"Pris inkl. moms: {pris_inkl_moms}")

except ValueError:
    print("Felaktig inmatning. Ange ett numeriskt värde för priset.")