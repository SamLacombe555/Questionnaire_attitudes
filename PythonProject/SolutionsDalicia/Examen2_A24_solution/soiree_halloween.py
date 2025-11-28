import random


def creer_rue_frisson(nombre_maisons):
    """
    Génère une rue sous forme de liste composée de maisons offrant des bonbons,
    sans bonbons ou hantées.
    Sur la rue du Frisson, chaque maison est représentée par un caractère :
    - 'B' : Une maison où l'on offre des bonbons.
    - 'A' : Une maison où l'on n'offre pas de bonbons.
    - 'F' : Une maison hantée.

    La fonction sélectionne aléatoirement l'un de ces trois types de maisons pour chaque emplacement
    sur la rue, puis retourne une liste des caractères représentant les maisons.

    :param nombre_maisons: nombre de maisons sur la rue du frisson.

    :return: Une liste de caractères où chaque caractère représente un type de maison sur
    la rue du Frisson ('B', 'A', ou 'F').
    """

    types_maisons = ['F', 'A', 'B']
    rue_frisson = []

    for i in range(nombre_maisons):
        type_maison = random.choice(types_maisons)
        rue_frisson.append(type_maison)

    return rue_frisson

def choisir_maisons_a_visiter(nombre_visites, nombre_maisons):
    """
    La fonction invite l'utilisateur à choisir les numéros des maisons à visiter
    sur la rue du frisson. Le choix des maisons se fait en entrant les numéros de
    maison dans une plage allant de 0 à nb_maisons - 1.

    :param nombre_visites: Nombre de maisons que l'on peut visiter (par exemple, 4).
    :param nombre_maisons: Nombre total de maisons disponibles dans la rue.

    :return: Une liste contenant les numéros des maisons sélectionnées pour la visite.
    """
    numeros_maisons = []
    for i in range(nombre_visites):
        try:
            num_maison = int(input(f"Veuillez choisir un numéro de maison de {0} à {nombre_maisons - 1} ({i + 1}/{nombre_visites}) : "))
            numeros_maisons.append(num_maison)

        except ValueError:
            print("La valeur entrée n'est pas un entier. Elle est ignorée. ")

    return numeros_maisons

def choisir_costume(partie_superieur, partie_inferieur, nb_chances = 3):
    """

    :param partie_superieur:
    :param partie_inferieur:
    :param nb_chances:
    :return:
    """
    costume_valide = "non"
    nb_iter = 1

    while costume_valide != "oui":

        try:
            choix_haut = int(input(f"Choisissez un numéro de {0} à {len(partie_superieur) - 1} pour la partie supérieure du costume : "))
            choix_bas = int(input(f"Choisissez un numéro de {0} à {len(partie_inferieur) - 1} pour la partie inférieure du costume : "))

            costume = partie_superieur[choix_haut] + " avec " + partie_inferieur[choix_bas]

        except ValueError:
            print(f"Les caractères alphabétiques ne sont pas acceptés.")
        except IndexError:
            print(f"Le numéro de costume choisi n'exite pas, veuillez choisir un numéro de {0} à {len(partie_superieur) - 1}")

        nb_iter += 1

        try:
            if nb_iter > nb_chances:
                print(f"C'était votre dernière chance de choix de costume, vous serez déguisée en {costume}")
                break

            costume_valide = input(f"Le costume choisi est {costume}.\nÊtes-vous satisfait(e) de votre choix de costume (chance {nb_iter}/{nb_chances}) ? (oui/non) : ").strip().lower()

        except UnboundLocalError:
            if nb_iter > nb_chances:
                print(f"C'était votre dernière chance de choix de costume. Aucun costume n'a été choisi.")
                break

    try:
        return costume
    except UnboundLocalError:
        return None


def collecte_bonbons(maisons_rue_frisson:list, numeros_maisons:list):
    """

    :param maisons_rue_frisson: liste des maisons de la rue à visiter ("B", "A" ou "F").
    :param nums_choix_maison: les numéros de maisons à visiter.
    :return:
    """
    nb_bonbons = 0
    for num in numeros_maisons:

        try:
            if maisons_rue_frisson[num] == "B":
                nb_bonbons += 10
            elif maisons_rue_frisson[num] == "F":
                nb_bonbons = -1
                break
        except IndexError:
            print(f"Un des numéros de maisons choisis n'existent pas sur la rue du frisson.")

    return nb_bonbons

if __name__ == "__main__":
    print("╔🎃✨══════════════════════════════════════════════════════════════════════════════════✨🎃╗")
    print(f"\tAllô Morbleue! Le soir d'halloween est venu, tu dois choisir ton costume.\n"
          f"\tTon costume sera une combinaison de deux parties (inférieure et supérieure),\n"
          f"\tque tu dois choisir séparément.\n\tTu as 3 essais au maximum. Le dernier sera pris si tu refuses les 2 premiers.")
    print("╚🎃✨══════════════════════════════════════════════════════════════════════════════════✨🎃╝")

    partie_superieure = ["tête de citrouille", "masque de vampire", "chapeau de sorcière", "masque de démon"]
    partie_inferieure = ["jupe de sorcière", "cape de vampire", "robe de fantôme", "robe de zombie"]


    costume_choisi = choisir_costume(partie_superieure, partie_inferieure)

    # Pas obligatoire
    if costume_choisi == None:
        costume_choisi = "Aucun"

    print("╔🎃✨═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════✨🎃╗")
    print(f"\tMorbleue, vêtue de son beau déguisement - {costume_choisi} -, part collecter des bonbons sur la rue du Frisson... ")
    print("╠🎃✨════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════✨🎃═╣")
    print(f"\tÀ présent Morbleue, tu dois choisir les numéros des 4 maisons que tu vas visiter.")
    print("╚🎃✨═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════✨🎃╝")

    maisons_rue_frissons = creer_rue_frisson(nombre_maisons=10)

    print(f"Une rue du frisson serait : {maisons_rue_frissons}")

    nombre_maisons = len(maisons_rue_frissons)
    nums_maisons_a_visiter = choisir_maisons_a_visiter(nombre_visites=4, nombre_maisons=nombre_maisons)

    print("╔🎃✨══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════✨🎃╗")
    print(f"\tTes choix de maisons sont faits, il est temps d'aller à ta collecte de bonbons sur la rue du Frisson. Bonne chance! ")
    print("╚🎃✨══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════✨🎃╝")

    nb_bonbons_collectes = collecte_bonbons(maisons_rue_frissons, nums_maisons_a_visiter)

    # Il est également possible de mettre les lignes de code suivantes dans la fonction collecte_bonbons et ne rien retourner.
    if nb_bonbons_collectes > 0:
        print(f"Félicitations Morbleue ! Tu as collecté {nb_bonbons_collectes} bonbons. Bravo pour ton courage et ta chance !")
    elif nb_bonbons_collectes == 0 :
        print("Pas de bonbons cette fois, Morbleue ! Bravo pour ton courage et contente que tu sois saine et sauve!")
    else:
        print("Oh non, Morbleue a été capturée par un fantôme... Quelle frayeur !")
