# fonction qui calcule et retourne division entre 2 nombre entiers input

def division(nbr1:int, nbr2:int) -> float:
    try:
        resultat = round(nbr1 / nbr2)
        return resultat

    except:
        print("Erreur")

try:
    nbr1 = int(input("Premier nombre"))
    nbr2 = int(input("Deuxième nombre"))

    print(division(nbr1,nbr2))

except ValueError:
    print("Doivent être entiers")