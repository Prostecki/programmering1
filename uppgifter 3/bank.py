# Bankprogram för att beräkna kapitaltillväxt över tid med ränta

# Initiala kapitalet på bankkontot
pengar = 100000

# Antal år pengarna kommer att stå inne
antal_år = 5

# Fråga användaren efter räntesatsen (i procent)
ränta = float(input("Ange räntesatsen i procent: "))

# Beräkna det totala kapitalet efter angivet antal år
totalt_kapital = pengar * (1 + ränta / 100) ** antal_år

# Skriv ut det totala kapitalet
print(f"\nTotalt kapital efter {antal_år} år: {totalt_kapital:.2f}")

# Dokumentation:
# - Planeringen av programmeringsuppgiften:
#   Programmet är utformat för att låta användaren ange räntesatsen och beräkna det totala kapitalet
#   efter ett antal år med hjälp av en enkel ränta på kapitalformel.
# - Felsökning av enkla syntaxfel:
#   Koden är relativt enkel och det finns inga uppenbara syntaxfel. Användningen av float(input()) 
#   används för att hantera användarinmatning av decimaltal för räntesatsen.
# - Utvärdering av programmet:
#   Programmet fungerar som avsett och ger användaren möjlighet att ange räntesatsen och få en uppskattning
#   av det totala kapitalet på bankkontot efter det angivna antalet år. Dock skulle ytterligare
#   användarfeedback och felhantering kunna läggas till för att göra programmet robustare och mer användarvänligt.
