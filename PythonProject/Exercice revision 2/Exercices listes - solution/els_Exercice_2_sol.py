def saisir_notes():
    """
    Demande à l'utilisateur de saisir quatre notes d'examen et les stocke dans une liste.

    Returns:
        list: Une liste contenant les quatre notes d'examens en pourcentage.
    """
    notes = []

    for i in range(4):
        try:
            note = float(input(f"Saisir la note {i + 1} (en %): "))
            if 0 <= note <= 100:
                notes.append(note)
            else:
                print("Erreur: La note doit être comprise entre 0 et 100.")

        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide.")

    return notes


def calculer_moyenne_sum_len(notes: list):
    """
    Calcule la moyenne des notes en utilisant les fonctions sum et len.
    :param notes: Liste des notes d'examen.
    :return: La moyenne des notes.
    """

    return sum(notes) / len(notes)


def calculer_moyenne(notes):
    """
    Calcule la moyenne des notes sans utiliser les fonctions sum et len.
    :param notes: Liste des notes d'examen.
    :return: La moyenne des notes.
    """

    total = 0
    compteur = 0

    for note in notes:
        total += note
        compteur += 1

    return total / compteur


def est_superieure_a_60(moyenne):
    """
    Vérifie si la moyenne est supérieure à 60 %.
    :param moyenne: La moyenne des notes.
    :return: True si la moyenne est supérieure à 60, sinon False.
    """

    return moyenne > 60


if __name__ == "__main__":
    notes_examen = saisir_notes()

    moyenne_avec_sum_len = calculer_moyenne_sum_len(notes_examen)
    print(f"Moyenne (avec sum et len): {moyenne_avec_sum_len:.2f}%")

    moyenne_sans_sum_len = calculer_moyenne(notes_examen)
    print(f"Moyenne (sans sum ni len): {moyenne_sans_sum_len:.2f}%")

    resultat = est_superieure_a_60(moyenne_avec_sum_len)
    print(f"Est-ce que l'étudiant a une moyenne supérieure à 60 % ? {resultat}")