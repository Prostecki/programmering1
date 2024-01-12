# Dokumentation för programmet "Momsberäkning"

# Planering:
# Denna kod är en enkel Python-applikation för att beräkna medelvärdet av alla tre poängen av provet.
# Användaren ombeds ange poäng för tre olika provet
# Planering innebar att definiera alla tre variablerna från inmatning, medelvärdesberäkning och visning

# - Kontrollerade att alla variabler är korrekt deklarerade.
# - Använde datatyper för heltal som 'int'

# Kort utvärdering:
# Programmet fungerar korrekt och ger förväntade resultat.
# Det är användarvänligt och enkelt att förstå.
# Det kan förbättras med else-satsen, för att göra det interaktivt, som jag gjörde.

# Här är själva programmet:

try:
    # Fråga efter poäng på tre olika prov
    prov1 = int(input('Ange poäng med prov 1: '))
    prov2 = int(input('Ange poäng med prov 2: '))
    prov3 = int(input('Ange poäng med prov 3: '))

    # Beräkna medelvärdet av alla tre poängen
    medelvardet = int((prov1 + prov2 + prov3) / 3)

    # Skriv ut medelvärdet
    print(f"Medelvärdet av poängen är: {medelvardet}")

    # Om medelvärdet är över 90, skriv ut "Bra jobbat"
    if medelvardet > 90:
        print("Bra jobbat!")
    else:
        print("Godkänt")

except ValueError:
    print('Felaktig inmatning. Ombeds ange heltal!')
