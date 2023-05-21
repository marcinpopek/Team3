wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:")
plec = input("Podaj swoją płeć, M - mężczyzna, K - kobieta")

if not plec.isalpha():
	exit("Płeć musi być podana w formacie: M - mężczyzna, K - kobieta")

# Sprawdzamy czy podany wiek jest liczbą
if not wiek.isdigit():
	exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
wiek=int(wiek)
if plec.upper() == "M" or plec.upper() == "K":
	if plec.upper() == "K" and wiek >= 30:
		print("Pierwszy Aperol Spritz masz gratis!")
	if wiek>=18 and wiek<40:
		print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
	elif wiek>=40:
		print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
		print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
	else:
		exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
else:
	exit("Płeć musi być podana w formacie: M - mężczyzna, K - kobieta")