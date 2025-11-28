# Liste fournie (ne pas modifier)
tables = [
    [0, 4, True],
    [1, 2, False],
    [2, 4, True],
    [3, 10, True],
    [4, 6, True]
]

def trouver_table(nb_personnes, tables):
    """Retourne le numéro de la première table assez grande ET disponible."""
    for table in tables:
        numero = table[0]
        capacite = table[1]
        disponible = table[2]
        if disponible and capacite >= nb_personnes:
            # Marquer la table comme occupée
            table[2] = False
            return numero
    return None


def afficher_tables(tables):
    """Affiche toutes les tables dans un format lisible."""
    print("Tables du restaurant :")
    for table in tables:
        numero, capacite, dispo = table
        etat = "Disponible" if dispo else "Occupée"
        print(f"Table {numero} - Capacité : {capacite} - État : {etat}")


def programme_tables():
    try:
        nb = int(input("Entrez le nombre de personnes du groupe à installer : "))
        if nb <= 0:
            print("Le nombre doit être positif.")
            return

        resultat = trouver_table(nb, tables)

        if resultat is not None:
            print(f"Une table disponible a été trouvée : Table {resultat}")
        else:
            print("Aucune table disponible ne peut accueillir ce groupe.")

        afficher_tables(tables)

    except ValueError:
        print("Erreur. Veuillez entrer un nombre entier.")


# Lancer la partie 2
if __name__ == "__main__":
    programme_tables()
