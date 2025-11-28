import random


def creer_liste_etudiants():
    """Demande à l'utilisateur d'ajouter des étudiants sous forme de liste."""
    etudiants = []
    nb = int(input("Combien d'étudiants voulez-vous entrer ? "))
    for _ in range(nb):
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        groupe = int(input("Groupe : "))
        etudiants.append([nom, prenom, groupe])
    return etudiants


def former_binomes(etudiants):
    """
    Crée des binômes aléatoires dans les mêmes groupes
    en utilisant UNIQUEMENT des listes.
    """
    binomes = []
    # On va créer une liste distincte pour chaque groupe rencontré
    groupes_uniques = []

    # 1. Identifier les groupes existants
    for etu in etudiants:
        if etu[2] not in groupes_uniques:
            groupes_uniques.append(etu[2])

    # 2. Pour chaque groupe, rassembler les étudiants et créer les binômes
    for g in groupes_uniques:
        # créer une liste temporaire des étudiants de ce groupe
        etudiants_groupe = []
        for etu in etudiants:
            if etu[2] == g:
                etudiants_groupe.append(etu)

        # Mélanger pour un ordre aléatoire
        random.shuffle(etudiants_groupe)

        # Former les binômes
        for i in range(0, len(etudiants_groupe) - 1, 2):
            binomes.append([etudiants_groupe[i], etudiants_groupe[i + 1]])

    return binomes


# Programme principal
etudiants = creer_liste_etudiants()
binomes = former_binomes(etudiants)

print("\nBinômes créés :")
for b in binomes:
    print(b)
