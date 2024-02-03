# Funktion för att kontrollera om ett tal är ett primtal
def arPrimTal(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

try:
    # Användaren uppmanas att ange ett tal
    primtal = int(input("Ange primtal..."))

    # Skriv ut meddelande om primtalen som finns mellan 1 och det angivna talet
    print("Ditt primtal mellan 1 och", primtal, ":")

    # Loopa genom alla tal från 2 till det angivna talet
    for num in range(2, primtal + 1):
        # Om talet är ett primtal, skriv ut det
        if arPrimTal(num):
            print(num, end=" ")

except ValueError:
    # Om användaren anger något annat än ett heltal, skriv ut felmeddelande
    print("Du måste ange ett heltal.")


# Dokumentation:

# Planeringen av programmeringsuppgiften: Programmet är utformat för att låta användaren ange ett tal och sedan skriva ut alla primtal som finns mellan 1 och det angivna talet. Planeringen inkluderar att skapa en funktion arPrimTal för att kontrollera om ett givet tal är ett primtal och sedan använda en loop för att generera och skriva ut primtalen.

# Felsökning av enkla syntaxfel: Programmet är ganska enkelt och innehåller inte mycket kod, vilket minimerar risken för syntaxfel. Men det finns en try-except-block för att hantera felaktig inmatning från användaren, vilket är en vanlig källa till fel.

# Utvärdering av programmet: Programmet gör vad det är avsett att göra, vilket är att skriva ut primtalen mellan 1 och det angivna talet. Det är användarvänligt med en felhantering för att hantera ogiltig inmatning. En begränsning är att det kan vara ineffektivt för stora tal eftersom primtalskontrollen görs för varje tal i intervallet. För stora tal kan prestanda vara långsam.