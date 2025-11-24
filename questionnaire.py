from questionnaires_fonctions import *
#pseudocode
#entrées :
    #tous les inputs (24) des questions
#sorties :
    #résultat des attitudes (int)

"""
list_reussite = []
list_dependance = []
list_autocontrole = []

list_attitudes = [list_reussite, list_dependance, list_autocontrole]
"""
list_attitudes = [
    [],
    [],
    []
]

dict_questions = {
    "Si j'échoue en partie, c'est aussi pire que d'échouer complètement.":0,
    "Si tu déplais aux autres, tu ne peux être heureux(se).":0,
    "Je devrais être heureux(se) tout le temps.":0,
    "Les gens auront probablement une moins bonne opinion de moi si je fais une erreur.":0,
    "Mon bonheur dépend plus des autres que de moi.":0,
    "Je devrais toujours contrôler totalement mes émotions.":0,
    "Ma vie est gâchée si je n’ai pas de succès.":0,
    "Ce que les gens pensent de moi est très important.":0,
    "Je devrais être capable de résoudre mes problèmes rapidement et sans gros effort.":0,
    "Si je ne me fixe pas les buts les plus élevés, je risque de devenir un(e) raté(e).":0,
    "Je ne suis rien si une personne que j’aime ne m’aime pas.":0,
    "Une personne devrait être capable de contrôler ce qui lui arrive.":0,
    "Pour avoir une valeur, je dois être le(la) meilleur(e) dans au moins un domaine.":0,
    "Si tu n’as personne surqui compter, tu seras sans doute triste.":0,
    "Je peux me sentir bien, même si j’ai été chicané(e).":0,
    "Ma vie n’a pas de but, si je ne suis pas une personne utile et productive.":0,
    "Je peux être heureux(se) même s’il y a quelqu’un qui ne m’aime pas.":0,
    "Une personne devrait bien faire tout ce qu’elle entreprend.":0,
    "Si je ne réussis pas tout le temps, les gens ne me respecteront pas.":0,
    "Je n’ai pas besoin de l’accord des autres pour être heureux(se).":0,
    "Si j’essaie vraiment fort, je devrais être le(la) meilleur(e) dans tout ce que j’entreprends.":0,
    "Les gens qui ont de bonnes idées ont plus de valeur que ceux qui n’en n’ont pas.":0,
    "Une personne n’a pas besoin d’être aimée par beaucoup de personnes pour être heureuse.":0,
    "Chaque fois que je prends un risque, je ne fais que me causer des ennuis.":0
}



attitudes_indice = 0


if __name__ == "__main__":
    consignes()
    input("Appuyez sur ENTRÉE pour débuter.")
    for question, réponse in dict_questions.items():
        probleme = True
        while probleme == True:
            reponses_possibles()
            reponse = int(input(question))
            if (reponse >= 8) or (reponse <= 0):
                probleme = True
            else:
                if list(dict_questions).index(question) ==( 16 or 19 or 20):
                    reponse = inversement(reponse)
                list_attitudes[attitudes_indice].append(reponse)
                attitudes_indice += 1
                if attitudes_indice >= 3:
                    attitudes_indice = 0
                probleme = False

    valeur_reussite = sum(list_attitudes[0])
    valeur_dependance = sum(list_attitudes[1])
    valeur_autocontrole = sum(list_attitudes[2])

    age = int(input("Êtes-vous un étudiant âgé entre 18 et 25 ans?\n1- Oui\n0- Non"))
    if age == 1:
        genre = int(input("Quelle est votre genre?\n2- Garçon\n1- Fille\n0- Autres/Préfère ne pas dire"))
        if genre != (1 or 2):
            genre = 0
    else:
        genre = 0
    for question, reponse in dict_questions.items():
        print(f"{question} = {reponse}")


    print(f"\nTotal Réussite = {valeur_reussite} \nTotal Dépendance = {valeur_dependance} \nTotal Autocontrôle = {valeur_autocontrole}")

    if genre != 0:
        if genre == 1:
            if genre =
