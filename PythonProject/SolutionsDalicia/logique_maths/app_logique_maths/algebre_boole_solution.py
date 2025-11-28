
def proposition_valide(proposition_math:str):
    """
    Vérifie si l'expression entrée est une proposition valide.
    :param proposition_math: L'expression à valider.
    :return: True si l'expression est bein une proposition valide, False sinon.
    """
    caracteres_proposition = ['.', '+', '|', '(', ')', 'p', 'q']

    # Il est possible de parcourir les caractères d'un string exactement comme une liste.
    for caractere in proposition_math:
        if caractere not in caracteres_proposition:
            return False
    else:
        return True


def conversion_proposition_math_prog(proposition_math:str):
    """
    Cette fonction permet de convertir une proposition de
    mathématiques en une expression en programmation (Python).

    :param proposition_math: La proposition en logique booléenne à convertir.
    :return: L'expression logique équivalente en Python.
    """

    proposition_prog = proposition_math.replace(".", " and ")
    proposition_prog = proposition_prog.replace("+", " or ")
    proposition_prog = proposition_prog.replace("|", "not ")

    # print(f"La proposition {proposition_math} en mathématiques est équivalente à {proposition_prog} en programmation")
    return proposition_prog


def construire_table_verite(expression_logique:str, afficher_table_verite:bool=False):
    if afficher_table_verite:
        print(f"\nTable de vérité de la proposition {expression_logique} :")
        print("p | q | Résultat")

    eval_combinaisons = []

    # TODO: utiliser les variables trouvées automatiquement
    for p in (0, 1):
        for q in (0, 1):
            resultat = eval(expression_logique)
            if afficher_table_verite:
                print(f"{p} | {q} | {int(resultat)}")
            eval_combinaisons.append(resultat)

    return eval_combinaisons

def evaluation(proposition:str, table_verite:bool=False):
    prop_est_valide = proposition_valide(proposition)
    if prop_est_valide:
        exp_prog = conversion_proposition_math_prog(proposition)
        resultat_eval_proposition = construire_table_verite(exp_prog, table_verite)

    return resultat_eval_proposition

def est_tautologie(proposition):
    table_verite_proposition = evaluation(proposition)
    est_tautologie = all(table_verite_proposition)

    return est_tautologie


def est_contradiction(proposition):
    table_verite_proposition = evaluation(proposition)
    for i in range(len(table_verite_proposition)):
        if table_verite_proposition[i] == 1:
            return False
    else:
        return True

    return est_contradiction

def implication(proposition1, proposition2):
    table_verite_proposition1 = evaluation(proposition1)
    table_verite_proposition2 = evaluation(proposition2)

    for i in range(len(table_verite_proposition1)):
        if table_verite_proposition1[i] == 0 and table_verite_proposition2[i] == 1:
            return False
    else:
        return True

def equivalence(proposition1, proposition2):
    table_verite_proposition1 = evaluation(proposition1)
    table_verite_proposition2 = evaluation(proposition2)

    for i in range(len(table_verite_proposition1)):
        if table_verite_proposition2[i] != table_verite_proposition1[i]:
            return False
    else:
        return True


if __name__ == "__main__":

    # TODO: inclure des dictionnaires.

    proposition1 = input("Veuillez entrer une proposition (ex. p+|(p.q) : ")
    proposition2 = input("Veuillez entrer une proposition (ex. p+|(p.q) : ")

    evaluation(proposition1, table_verite=True)
    if est_tautologie(proposition1):
        print(f"La proposition {proposition1} est une tautologie")
    else:
        print(f"La proposition {proposition1} n'est pas une tautologie")

    est_contradiction(proposition1)
    if est_contradiction(proposition1):
        print(f"La proposition {proposition1} est une contradiction")
    else:
        print(f"La proposition {proposition1} n'est pas une contradiction")


    evaluation(proposition2, table_verite=True)
    if est_tautologie(proposition2):
        print(f"La proposition {proposition2} est une tautologie")
    else:
        print(f"La proposition {proposition2} n'est pas une tautologie")

    est_contradiction(proposition2)
    if est_contradiction(proposition2):
        print(f"La proposition {proposition2} est une contradiction")
    else:
        print(f"La proposition {proposition2} n'est pas une contradiction")

    if implication(proposition1, proposition2):
        print(f"{proposition1} ==> {proposition2}")
    else:
        print(f"{proposition1} =/=> {proposition2}")

    if equivalence(proposition1, proposition2):
        print(f"{proposition1} <==> {proposition2}")
    else:
        print(f"{proposition1} <=/=> {proposition2}")
