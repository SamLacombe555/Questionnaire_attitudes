import random

def bienvenu():
    print("Bienvenu! Vous devez essayer de deviner un joueur grâce à mes indices.")
    print("Un joueur c'est fait sélectionner par hasard. Bonne chance!")

def selection_de_joueur(joueurs):
    return random.choice(joueurs)

def selection_indice(liste_indice):
    return random.choice(liste_indice)

def remove_indice(liste_indice, indice):
    return liste_indice.remove(indice)

def trouver_valeur(joueur, indice):
    return joueur[indice]

def donne_indice(round, indice, indice_valeur):
    print(f"L'indice n.{round} est ceci:")
    print(f"Son/sa {indice} est {indice_valeur}")
    return str(input("Quelle est le nom du joueur?"))

def verifie(devinette, joueur):
    return devinette.title() == joueur["Nom"]

def win(joueur):
    print(f"Félicitation! Le joueur était {joueur["Nom"]}")

def lose(joueur):
    print(f"Mauvaise réponse. Oops! Il ne reste plus d'indice. Le joueur était {joueur["Nom"]}")

def mauvaise_reponse():
    print("Mauvaise réponse. Veuillez réessayer")

def round_count(round):
    return round - 1


joueurs = [
    {
        "Nom": "Sidney Crosby",
        "Équipe": "Penguins de Pittsburgh",
        "Position": "Centre",
        "Province": "Nouvelle-Écosse",
        "Numéro": 87
    },
    {
        "Nom": "Connor McDavid",
        "Équipe": "Oilers d’Edmonton",
        "Position": "Centre",
        "Province": "Ontario",
        "Numéro": 97
    },
    {
        "Nom": "Carey Price",
        "Équipe": "Canadiens de Montréal",
        "Position": "Gardien",
        "Province": "Colombie-Britannique",
        "Numéro": 31
    },
    {
        "Nom": "Nathan MacKinnon",
        "Équipe": "Avalanche du Colorado",
        "Position": "Centre",
        "Province": "Nouvelle-Écosse",
        "Numéro": 29
    },
    {
        "Nom": "Cale Makar",
        "Équipe": "Avalanche du Colorado",
        "Position": "Défenseur",
        "Province": "Alberta",
        "Numéro": 8
    },
    {
        "Nom": "Marie-Philip Poulin",
        "Équipe": "Équipe Canada Féminine",
        "Position": "Avant",
        "Province": "Québec",
        "Numéro": 29
    },
    {
        "Nom": "Sarah Nurse",
        "Équipe": "Équipe Canada Féminine",
        "Position": "Avant",
        "Province": "Ontario",
        "Numéro": 20
    }
]

round = 1

liste_indice = ["Équipe", "Position", "Province", "Numéro"]


# Début
bienvenu()
joueur = selection_de_joueur(joueurs)
while True:
    indice = selection_indice(liste_indice)
    liste_indice = remove_indice(liste_indice, indice)
    indice_valeur = trouver_valeur(joueur, indice)
    devinette = donne_indice(round, indice, indice_valeur)
    if verifie(devinette, joueur):
        win(joueur)
    else:
        round = round_count(round)
        if round == 4

