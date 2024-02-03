# Skapa en tom lista för att lagra information om personer
personer = []

# Loopa för att låta användaren mata in information om varje person
while True:
    kön = input("Ange kön på person (man/kvinna) eller 'avsluta' för att avsluta: ")
    
    # Om användaren skriver 'avsluta', avsluta loopen
    if kön == 'avsluta':
        break
    
    # Annars, låt användaren mata in åldern för personen
    ålder = int(input("Ange ålder på person: "))
    
    # Skapa en tupel med kön och ålder för personen och lägg till den i listan över personer
    person = (kön, ålder)
    personer.append(person)

# Beräkna genomsnittsåldern för varje kön i gruppen
total_ålder_man = 0
antal_man = 0
total_ålder_kvinna = 0
antal_kvinna = 0

# Loopa genom varje person i listan över personer
for person in personer:
    kön, ålder = person
    
    # Om kön är 'man', lägg till åldern i total_ålder_man och öka antal_man med 1
    if kön == 'man':
        total_ålder_man += ålder
        antal_man += 1
    
    # Om kön är 'kvinna', lägg till åldern i total_ålder_kvinna och öka antal_kvinna med 1
    elif kön == 'kvinna':
        total_ålder_kvinna += ålder
        antal_kvinna += 1

# Beräkna genomsnittsåldern för män och kvinnor i gruppen
genomsnittsålder_man = total_ålder_man / antal_man if antal_man > 0 else 0
genomsnittsålder_kvinna = total_ålder_kvinna / antal_kvinna if antal_kvinna > 0 else 0

# Skriv ut genomsnittsåldern för män och kvinnor i gruppen
print("Genomsnittsåldern för män i gruppen är:", genomsnittsålder_man)
print("Genomsnittsåldern för kvinnor i gruppen är:", genomsnittsålder_kvinna)

# Planeringen av programmeringsuppgiften:
# 1. Programmet börjar med att skapa en tom lista för att lagra information om personer.
# 2. Sedan låter det användaren mata in kön och ålder för varje person tills de väljer att avsluta.
# 3. Efter att alla uppgifter har samlats in, beräknar programmet genomsnittsåldern för män och kvinnor i gruppen.
# 4. Till sist skriver programmet ut genomsnittsåldern för män och kvinnor.

# Felsökning av enkla syntaxfel:
# 1. Koden är relativt enkel och innehåller inte många komplexa strukturer, vilket minskar risken för syntaxfel.
# 2. Dock finns det en kontroll för att se till att åldern som matas in är ett heltal. Om användaren anger något annat än ett heltal kommer programmet att kasta ett `ValueError`.

# Utvärdering av programmet:
# 1. Programmet uppfyller syftet att beräkna genomsnittsåldern för män och kvinnor baserat på användarens input.
# 2. Det är användarvänligt och har en enkel gränssnitt för inmatning och resultatutskrift.
# 3. En begränsning är att det inte finns någon hantering för ogiltig inmatning av ålder (t.ex. negativa tal eller bokstäver). Detta kan orsaka fel eller ge oväntade resultat om användaren ger ogiltig inmatning.
# 4. Ytterligare förbättringar kan göras för att hantera ogiltig inmatning och göra programmet mer robust.