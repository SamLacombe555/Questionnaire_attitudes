
def proposition_valide(proposition_maths:str) -> bool:
    """
    Vérifie si l'expression entrée est une proposition valide.
    :param proposition_math: L'expression à valider.
    :return: True si l'expression est bien une proposition valide, False sinon.
    """
    caracteres_proposition = ['.', '+', '|', '(', ')', 'p', 'q']

    # TODO: Compléter cette fonction de façon à vérifier qu'une proposition est valide.
    #       Prendre en considération les contraintes sur les variables utilisées.
    #       Indice : Il est possible de parcourir les caractères d'un string exactement comme une liste.


def conversion_proposition_math_prog(proposition_math:str)-> str:
    """
    Cette fonction permet de convertir une proposition de
    mathématiques en une expression en programmation (Python).

    :param proposition_math: La proposition en logique booléenne à convertir.
    :return: L'expression logique équivalente en Python.
    """

    # TODO: Compléter la conversion proposition (maths) --> expression prog (str). Voir tableau énoncé.
    pass

def construire_table_verite(expression_logique:str, afficher_table_verite:bool=False):
    if afficher_table_verite:
        print(f"\nTable de vérité de la proposition {expression_logique} :")
        print("p | q | Résultat")

    eval_combinaisons = []

    # TODO: On évalue l'expression pour toutes les combinaisons de p et q qui prenent des valeurs dans (0, 1)
    #       Une table de vérité sera affichée uniquement si afficher_table_verite est à True.

    return eval_combinaisons

def evaluation(proposition:str, table_verite:bool=False):
    """
    Cette fonction vérifie si la proposition est valide,
    et retourne le résultat de son évaluation.
    :param proposition: la proposition d'Algèbre de Boole à évaluer.
    :param table_verite: On le met à True si on veut afficher la table de vérité.
    :return: retourne le résultat d'évaluation de la proposition.
    """
    prop_est_valide = proposition_valide(proposition)
    if prop_est_valide:
        # TODO: appeler fonction pour convertir la proposition en expression booléenne prog
        # TODO: appeler fonction qui donne le résultat de l'évaluation de l'expression booléenne.
        pass


if __name__ == "__main__":

    # TODO: inclure des dictionnaires.

    proposition1 = input("Veuillez entrer une proposition (ex. p+|(p.q) : ")
    proposition2 = input("Veuillez entrer une proposition (ex. p+|(p.q) : ")

    evaluation(proposition1, table_verite=True)
