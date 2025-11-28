import random

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

liste_indice = ["Équipe", "Position", "Province", "Numéro"]

# bienvenu
# un joeur aléatoire a été choisi
# random choice joueur = solution
# while True:
    # indice = random choice liste indice
    # le [n.] indice est que son [clé] est [valeurs]
    # essai == input (c'est quoi le nom du joueur?)
    # if essai == joueur[solution]["Nom"]
        # break
    # else:
        # Mauvaise réponse. Veuillez réessayer
        # list indice.supprime indice



solution = random.choice(joueurs)
round = 1
while True:
    indice_random = random.choice(liste_indice)
    liste_indice.remove(indice_random)
    devinette = input(f"Ton indice n.{round} est que le/la {indice_random} du joueur(se) est {solution[indice_random]}.\n Quelle est le nom du joueur(se)?")
    solution_nom = solution["Nom"]
    devinette_cap = devinette.title()
    if devinette_cap == solution["Nom"]:
        print(f"Bravo! La réponse était {solution_nom}!")
        break
    elif liste_indice == []:
        print(f"Mauvaise réponse. Oops! Il ne reste plus d'indice.\nLa réponse était {solution_nom}!")
        break
    else:
        round += 1
        print("Mauvaise réponse. Veuillez-réessayer")

print(f"Bravo! La réponse était {solution_nom}!")