personer = []

while True:
    kön = input("Ange kön på person (man/kvinna) eller 'avsluta' för att avsluta: ")
    if kön == 'avsluta':
        break
    ålder = int(input("Ange ålder på person: "))
    person = (kön, ålder)
    personer.append(person)

# beräkna genomsnittsålder för en varje person
total_ålder_man = 0
antal_man = 0
total_ålder_kvinna = 0
antal_kvinna = 0

for person in personer:
    kön, ålder = person
    if kön == 'man':
        total_ålder_man += ålder
        antal_man += 1
    elif kön == 'kvinna':
        total_ålder_kvinna += ålder
        antal_kvinna += 1
        
genomsnittsålder_man = total_ålder_man / antal_man if antal_man > 0 else 0
genomsnittsålder_kvinna = total_ålder_kvinna / antal_kvinna if antal_kvinna > 0 else 0

print("Genomsnittsåldern för män i gruppen är:", genomsnittsålder_man)
print("Genomsnittsåldern för kvinnor i gruppen är:", genomsnittsålder_kvinna)