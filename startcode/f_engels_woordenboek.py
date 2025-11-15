woorden = {
    'aap': 'monkey',
    'banaan': 'banana',
    'aansprakelijkheidswaardevaststellingsveranderingen': 'liability valuation changes',

}

woorden_vertaler = input("Geef een te vertalen woord in dat nederlands is: ")

if woorden_vertaler in woorden:
	print(f"\nDe vertaling van {woorden_vertaler} is {woorden[woorden_vertaler]}.")
else:
	print("Dat woord is nog niet in onze database toegevoegt.\nHet spijt ons.")

print("Bedankt om gebruik te maken van onze service.")