import random

def initialiser_sac():
    """
    Initialise le sac avec les premiers objets déjà trouvés par Zigomar.
    """
    return ["potion scintillante", "clé mystérieuse", "boule brillante", "squelette miniature"]


def ajouter_objets(sac, objets):
    """
    Ajoute les objets dans la liste du sac un par un.
    """
    for obj in objets:
        sac.append(obj)


def verifier_taille_sac(sac):
    """
    Retourne True si le sac contient 15 objets ou plus.
    """
    if len(sac) >= 15:
        return True
    else:
        return False


def contient_chiffre(chaine):
    """
    Vérifie si une chaîne contient un chiffre.
    Retourne True ou False.
    """
    for caractere in chaine:
        if caractere.isdigit():
            return True
    return False


def tri_automatique(sac):
    """
    Retire les objets contenant un chiffre OU la lettre 'b'.
    """
    nouveaux_objets = []
    for objet in sac:
        contient_un_chiffre = contient_chiffre(objet)
        contient_un_b = "b" in objet.lower()

        if contient_un_chiffre == False and contient_un_b == False:
            nouveaux_objets.append(objet)

    # On remplace le contenu du sac par la nouvelle liste filtrée
    sac.clear()
    for objet_filtre in nouveaux_objets:
        sac.append(objet_filtre)

    print("Tri automatique effectué !")


def tri_manuel(sac):
    """
    Demande à l'utilisateur quel objet retirer.
    """
    print("Objets dans le sac :", sac)
    objet = input("Quel objet veux-tu retirer ? ")

    if objet in sac:
        sac.remove(objet)
        print(objet + " a été retiré du sac.")
    else:
        print("Zigomar grogne : cet objet n'est pas dans le sac !")


def mini_quiz(sac):
    """
    Mélange le sac, choisit un objet au hasard
    et demande à l'utilisateur de deviner.
    """
    if len(sac) == 0:
        print("Le sac est vide, le quiz est annulé.")
        return

    random.shuffle(sac)
    objet_choisi = random.choice(sac)
    reponse = input("Devine l'objet choisi au hasard : ")

    if reponse.lower() == objet_choisi.lower():
        print("Zigomar saute de joie !")
    else:
        print("Mauvaise réponse... L'objet était :", objet_choisi)


def tri_final(sac):
    """
    Trie les objets en ordre alphabétique.
    """
    sac.sort()
    print("Tri final effectué !")


def main():
    sac = initialiser_sac()
    print("Zigomar commence avec :", sac)

    # Simule quelques explorations
    for i in range(3):
        print("\n--- Exploration", i + 1, "---")
        texte_saisi = input("Quels objets Zigomar a trouvés (séparés par des virgules) ? ")
        morceaux = texte_saisi.split(",")

        nouveaux_objets = []
        for element in morceaux:
            mot = element.strip()
            if mot != "":
                nouveaux_objets.append(mot)

        ajouter_objets(sac, nouveaux_objets)
        print("Contenu actuel du sac :", sac)

        if verifier_taille_sac(sac):
            print("\nLe sac est plein (15 objets ou plus)!")
            choix = input("Tri automatique (A) ou manuel (M) ? ").lower()
            if choix == "a":
                tri_automatique(sac)
            else:
                tri_manuel(sac)

            print("Contenu du sac après le tri :", sac)

    # Quiz
    print("\n--- Mini-quiz ---")
    mini_quiz(sac)

    # Tri final
    print("\n--- Tri final obligatoire ---")
    tri_final(sac)

    print("\nSac final de Zigomar :", sac)


if __name__ == "__main__":
    main()
