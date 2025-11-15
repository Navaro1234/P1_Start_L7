prijzenkast = ("knuffelbeer", "gameconsole", "fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!\n")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3\n")


gekozen_doos = int(input("Welke doos wil je? \n"))
if gekozen_doos in (1, 2, 3):
    gewonnen_doos = prijzenkast[gekozen_doos - 1]
    print("Gefeliciteerd je hebt een " + gewonnen_doos + " gewonnen. \n")
else:
    print("ongeldig nummer\n")

