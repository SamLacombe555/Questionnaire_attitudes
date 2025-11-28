import random

# Les provinces associées à leur capitale.
provinces = {
"Yukon"                : "Whitehorse",
"TNO"                  : "Yellowknife",
"Nunavut"              : "Iqaluit",
"Terre-Neuve"          : "St-John's",
"IPE"                  : "Charlottetown",
"Nouvelle-Écosse"      : "Halifax",
"Nouveau-Brunswick"    : "Fredericton",
"Québec"               : "Québec",
"Ontario"              : "Ottawa",
"Manitoba"             : "Winnipeg",
"Saskatchewan"         : "Regina",
"Alberta"              : "Edmonton",
"Colombie-Britannique" : "Victoria"
}

list_p_c = ["province","capitale"]
pointage = 0
essai = 0

def resultat(pointage, essai):
    resultat_pourcentage = (pointage/essai)*100
    return resultat_pourcentage

while True:
    # choisi hasard soit province ou capitale = afficher et l'autre = a_deviner
    affichee = random.choice(list_p_c)
    if affichee == "province":
        cachee = "capitale"
        list_hasard_affichee = list(provinces.keys())
        list_hasard_cachee = list(provinces.values())
    elif affichee == "capitale":
        cachee = "province"
        list_hasard_affichee = list(provinces.values())
        list_hasard_cachee = list(provinces.keys())

    # choisi hasard un des afficher
    affichee_question = random.choice(list_hasard_affichee)

    # demande de deviner a_deviner
    guess = str(input(f"Quelle est la {cachee} de {affichee_question}?"))

    # terminer questionnement
    if guess == "":
        break

    # si devinette = a_deviner
    elif affichee == "province":
        for i in range(len(provinces)):
            if list(provinces.values())[i] == guess:
                bonne_reponse = list(provinces.keys())[i]
                if bonne_reponse == affichee_question:
                    # ajoute 1 point
                    pointage += 1
        # ajoute 1 question
        essai += 1


    # si devinette = a_deviner
    elif affichee == "capitale":  # a deviner province
        if provinces[guess] == affichee_question:
            # ajoute 1 point
            pointage += 1
        # ajoute 1 question
        essai += 1

resultat_pourcentage = resultat(pointage,essai)
print(f"Ton résultat est {resultat_pourcentage}%")

# si entre 80-100
if resultat_pourcentage >= 80:
    print("Super, tu es prêt!")

elif resultat_pourcentage >= 60:
    print("Tu y es presque")

elif resultat_pourcentage >= 50:
    print("Ça s'en vient!")

else:
    print("Continue de pratiquer si tu veux du temps d'écran")



# ajoute 1 point

    # demande enccore
# si devinette != a_deviner
    # ajoute 1 question
    # demande encore
# si devinette = ""
    # arrête de demander
    # calcule résultat
    # si entre 0-50
        # print "Continue de pratiquer si tu veux du temps d'écran"
    # si entre 50-60
        # print "Ça s'en vient!"
    # si entre 60-80
        # print "Tu y es presque"
    # si entre 80-100
        # print "Super, tu es prêt!