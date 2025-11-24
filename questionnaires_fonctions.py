def q_1():
    return int(input("Si j'échoue en partie, c'est aussi pire que d'échouer complètement."))

def q_2():
    return int(input("Si tu déplais aux autres, tu ne peux être heureux(se)."))

def q_3():
    return int(input("Je devrais être heureux(se) tout le temps."))

def q_4():
    return int(input("Les gens auront probablement une moins bonne opinion de moi si je fais une erreur."))

def q_5():
    return int(input("Mon bonheur dépend plus des autres que de moi."))

def q_6():
    return int(input("Je devrais toujours contrôler totalement mes émotions."))

def q_7():
    return int(input("Ma vie est gâchée si je n’ai pas de succès."))

def q_8():
    return int(input("Ce que les gens pensent de moi est très important."))

def q_9():
    return int(input("Je devrais être capable de résoudre mes problèmes rapidement et sans gros effort."))

def q_10():
    return int(input("Si je ne me fixe pas les buts les plus élevés, je risque de devenir un(e) raté(e)."))

def q_11():
    return int(input("Je ne suis rien si une personne que j’aime ne m’aime pas."))

def q_12():
    return int(input("Une personne devrait être capable de contrôler ce qui lui arrive."))

def q_13():
    return int(input("Pour avoir une valeur, je dois être le(la) meilleur(e) dans au moins un domaine."))

def q_14():
    return int(input("Si tu n’as personne surqui compter, tu seras sans doute triste."))

def q_15():
    return int(input("Je peux me sentir bien, même si j’ai été chicané(e)."))

def q_16():
    return int(input(" Ma vie n’a pas de but, si je ne suis pas une personne utile et productive."))

def q_17():
    return int(input("Je peux être heureux(se) même s’il y a quelqu’un qui ne m’aime pas."))

def q_18():
    return int(input("Une personne devrait bien faire tout ce qu’elle entreprend."))

def q_19():
    return int(input("Si je ne réussis pas tout le temps, les gens ne me respecteront pas."))

def q_20():
    return int(input("Je n’ai pas besoin de l’accord des autres pour être heureux(se)."))

def q_21():
    return int(input("Si j’essaie vraiment fort, je devrais être le(la) meilleur(e) dans tout ce que j’entreprends."))

def q_22():
    return int(input("Les gens qui ont de bonnes idées ont plus de valeur que ceux qui n’en n’ont pas."))

def q_23():
    return int(input("Une personne n’a pas besoin d’être aimée par beaucoup de personnes pour être heureuse."))

def q_24():
    return int(input("Chaque fois que je prends un risque, je ne fais que me causer des ennuis."))

def reponses():
    print("7- Complètement d'accord \n6- Très d'accord \n5- Un peu d'accord \n4- Neutre \n3- Un peu en désaccord \n2- Très en désaccord \n1- Complètement en désaccord")

def inversement(valeur : int):
    return 8 - valeur

def consignes():
    print("Ce questionnaire présente la liste de différentes attitudes ou opinions que les gens ont parfois. \nLis attentivement CHAQUE énoncé et décide jusqu’à quel point tu es en accord ou en désaccord avec l’énoncé. \n")
    print("Pour chacune de ces attitudes, indique ta réponse en plaçant un X sous la colonne qui DÉCRIT LE MIEUX CE QUE TU PENSES. \nSois certain(e) de choisir seulement une réponse pour chaque attitude. Puisque les gens sont différents, il n’y a pas de bonnes ou de mauvaises réponses à ces énoncés. \nPour décider si une attitude donnée est typique de ta façon de voir les choses, garde simplement en tête ce que tu es la plupart du temps. ")