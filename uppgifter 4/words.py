# Planeringen av programmeringsuppgiften:
# Syftet med detta program är att ta emot en mening från användaren, dela upp den i ord och sedan ge användaren information om antalet ord samt det första och sista ordet i meningen.

# Läs in en mening från användaren
mening = input("Ange en mening bestående av minst två ord: ")

# Dela upp meningen i ord
antal_ord = mening.split()

# Kontrollera om det finns minst två ord
if len(antal_ord) >= 2:
    # Skriv ut antalet ord och det första och sista ordet
    print(f'Du skrev {len(antal_ord)} ord')
    print(f'Det första ordet är: {antal_ord[0]}')
    print(f'Det sista ordet är: {antal_ord[-1]}')
else:
    print('Du måste ange minst två ord för att programmet ska fungera.')

# Felsökning av enkla syntaxfel:
# Om du får syntaxfel kan det vara på grund av felaktig användning av citattecken, parenteser eller kolon. Kontrollera noga dessa.

# Kort utvärdering av programmet:
# Programmet uppfyller sitt syfte genom att informera användaren om antalet ord samt det första och sista ordet i den angivna meningen. Det innehåller en enkel felkontroll för att säkerställa att det finns minst två ord.

# Möjligheter och begränsningar:
# - Möjligheter: Programmet kan enkelt utökas för att inkludera fler statistik- eller analysfunktioner för den angivna meningen.
# - Begränsningar: Programmet antar att användaren anger minst två ord. Det innehåller inte avancerade felkontroller eller hantering av specialfall, såsom när användaren inte anger någon mening alls.
