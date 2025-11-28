import random


def donner_indice(ile: str, lt: int, ct: int, ls_iles: list[list[str]]) -> str:
    """
    Fonction pour donner un indice : si c'est plus au n, s, e ou o...
    :param ile: île choisie par le joueur
    :param lt: ligne de l'île où est le trésor
    :param ct: colonne de l'île où est le trésor
    :param ls_iles: liste des îles possitionnées
    :return: un indice, exemple "Plus au S" ou "Plus au NE"
    """
    # TODO : vérifier que l'ile choisie existe, sionon retourner un message d'erreur
    trouve = False
    for ligne in ls_iles:
        if ile in ligne:
            trouve = True
    if not trouve:
        return "L'île n'est pas dans la liste"

    # trouver les indices dans la list de l'ile choisie  lj, cj
    for i in range(len(ls_iles)):
        if ile in ls_iles[i]:
            lj = i
    # trouver la colonne de l'île choisie par le joueur : cj
    for c in range(len(ls_iles[lj])):
        if ile == ls_iles[lj][c]:
            cj = c
    print(f"Coordonnées joueur {lj}, {cj}")
    indice = "Plus "
    # si lj < lt : S
    if lj < lt:
        indice += "au S"  # += entre 2 str : ralonge le texte
    # si cj < ct : E
    # TODO : compléter les indices avec les autres conditions
    elif lj > lt:
        indice += "au N"
    else:
        indice += "à l'"
    if cj < ct:
        indice += "E"
    if cj > ct:
        indice += "O"

    return indice


ls_iles = [  # N
    ["macargo", "monkey", "alolah", "hoen", "kalos"],
    ["Guadeloupe", "Martinique", "La Réunion", "Mayotte", "Corse"],
    ["Sicile", "Sardaigne", "Crète", "Chypre", "Malte"],  # E
    ["Cuba", "Jamaïque", "Porto Rico", "Barbade", "Dominique"],
    ["Bornéo", "Sumatra", "Java", "Bali", "Philippines"],
    ["Madagascar", "Sri Lanka", "Groenland", "Islande", "Hawaï"]
    # S
]
# Afficher les îles
for l in ls_iles:
    print(l)
print("Nb de lignes :", len(ls_iles))  # nb de lignes
print("Nb de colonnes :", len(ls_iles[0]))  # nb de colonnes
# choisir une île au hasard
ligne_tresor = random.randint(0, len(ls_iles) - 1)  # ligne aléatoire
colonne_tresor = random.randint(0, len(ls_iles[ligne_tresor]) - 1)  # colonne aléatoire
print(f"Coordonnées du trésor: {ligne_tresor}, {colonne_tresor}")
tresor = ls_iles[ligne_tresor][colonne_tresor]
print("Île au trésor :", tresor)

while True:
    # demander une île au joueur
    ile = input("Choisir un île: ")
    # si il a bien deviner terminer le jeu
    if ile == tresor:
        break
    # sinon donner un indice : si c'est plus au n, s, e ou o...
    else:
        indince = donner_indice(ile, ligne_tresor, colonne_tresor, ls_iles)
        print(indince)
print("Bravo c'était bien", tresor)