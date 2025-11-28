def supprimer_ingredients(ingredients):
    """
    Cette fonction supprime les ingrédients qui ne sont plus disponibles dans la cuisine de Techwitch.
    Si l'utilisateur répond "non", l'ingrédient est supprimé de la liste.
    Si l'utilisateur répond "oui", l'ingrédient est conservé.

    :param ingredients: Liste des ingrédients à mettre à jour.
    :return: La liste des ingrédients mise à jour après vérification.
    """

    index = 0
    while index < len(ingredients):
        ingr = ingredients[index]
        reponse = input(f"Avez-vous {ingr} ? (oui/non) : ").strip().lower()

        if reponse == 'non':
            ingredients.remove(ingr)
            print(f"{ingr} a été supprimé de la liste des ingrédients.")
        elif reponse == "oui":
            index += 1
        else:
            print("Veuillez répondre par oui ou non.")

    return ingredients

def afficher_ingredients(ingredients):
    print("╔═══════════════════════════════════════════╗")
    print(" Voici les ingrédients disponibles :")

    for i in range(len(ingredients)):
        print(f"\t- {ingredients[i]}")
    print("╚═══════════════════════════════════════════╝")

def creer_recettes_potions(ingredients_disponibles):

    recettes_potions = []
    nouvelle_potion = "oui"

    while nouvelle_potion == "oui":

        afficher_ingredients(ingredients_disponibles)

        liste_ingredients_str = input("Copiez les ingredients souhaités dans votre potion parmi la liste d'ingrédients ci-dessus, en les séparant par des virgules : ")

        liste_ingredients = liste_ingredients_str.split(',')

        if len(liste_ingredients) != 0:
            nom_potion = input("Entrez le nom de la potion : ")

            recette_potion = (f"La potion {nom_potion}: Dans un chaudron, mélangez à l'aide "
                              f"d'une patte d'autruche ") + ", ".join(liste_ingredients) + "."

            recettes_potions.append(recette_potion)

        nouvelle_potion = input("Voulez-vous créer une autre recette ? (oui/non) : ").strip().lower()

    return recettes_potions

def devoiler_recettes_potions(recettes):
    print("╔🍲═════════════════════════════════════════════════════════════════════════════════")
    if recettes:
        print(" Recettes de potions créées par Techwitch :")
        for recette in recettes:
            print(f" {recette}")
    else:
        print("Aucune recette n'a été créée.")
    print("╚🍲═════════════════════════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    ingredients = ["de la poudre de dragon", "des yeux de grenouille", "des plumes de corbeau", "des gouttes de feu liquide", "des fleurs de souci"]

    print("╔══════════════════════════════════════════════════════╗")
    print("\tOn commence par le tri des ingrédients : ")
    print("╚══════════════════════════════════════════════════════╝")

    ingredients_restants = supprimer_ingredients(ingredients)

    print(f"🧙‍On peut commencer à concoter les recettes avec les ingrédients ci-dessus. Suivez les instructions suivantes : ")
    recettes_potion = creer_recettes_potions(ingredients_restants)
    devoiler_recettes_potions(recettes_potion)
