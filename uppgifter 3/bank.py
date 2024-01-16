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
