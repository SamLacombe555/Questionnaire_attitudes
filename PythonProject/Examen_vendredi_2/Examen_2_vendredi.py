#PSEUDOCODE#
#horaire: liste des temps de la journées que l'autobus passe
#horaire_heures: liste des valeurs des heures (h) que l'autobus passe
#horaire_minutes: liste des valeurs des minutes (min) que l'autobus passe
#ls_heure_rn: liste des chiffres des valeurs d'heures (h) du temps présent
#print "Horaire :"
#print ligne avec tiret
#print liste de l'horaire
#ligne avec tiret

#Demande quelle est l'heure présentement
#Ajoute l'heure présent dans la liste de l'horraire
#Réarrange la liste d'horraire en ordre croissant

#Trouve l'heure que le prochain autobus arrivera
#Enlève l'heure présent de la liste d'horraire
#Annonce l'heure que le prochain autobus arrivera

#Calcule le temps qui reste avant que le prochain autobus arrive
#Annonce le temps qui reste avant que le prochain autobus arrive

def prochain_arret(horaire,heure_rn):
    """
    Fonction qui détermine la prochaine heure où l'autobus passe
    :param horaire: liste des heures que l'autobus passe
    :param heure_rn: heure présentement
    :return: la prochaine heure où l'autobus passe
    """
    try:
        index_heure_rn = horaire.index(heure_rn)
        heure_prochain = horaire[index_heure_rn+1]
        return heure_prochain
    except IndexError:
        return None

def calcule(horaire,horaire_heures,horaire_minutes,ls_heure_rn,heure_rn,arret_prochain):
    """
    Fonction qui calcule le temps restant avant l'arrivé du prochain autobus
    :param horaire: liste des temps de la journées que l'autobus passe
    :param horaire_heures: liste des valeurs des heures (h) que l'autobus passe
    :param horaire_minutes: liste des valeurs des minutes (min) que l'autobus passe
    :param ls_heure_rn: liste des chiffres des valeurs d'heures (h) du temps présent
    :param heure_rn: liste des chiffres des valeurs des minutes (m) du temps présents
    :param arret_prochain: temps en minutes qui reste avant l'arrivée du prochain autobus
    :return: arret_prochain: temps en minutes qui reste avant l'arrivée du prochain autobus
    """
    try:
        for digit in heure_rn:
            if digit.isdigit():
                ls_heure_rn.append(digit)

        h_rn = int(str(ls_heure_rn[0])+str(ls_heure_rn[1]))
        minute_rn = int(str(ls_heure_rn[2])+str(ls_heure_rn[3]))


        index_arret_prochain = horaire.index(arret_prochain)
        heure_prochain = horaire_heures[index_arret_prochain]
        minute_prochain = horaire_minutes[index_arret_prochain]

        minute_total_prochain = heure_prochain*60 + minute_prochain
        minute_total_rn = h_rn*60 + minute_rn

        minute_restant = minute_total_prochain-minute_total_rn
        return minute_restant
    except IndexError:
        return None

#horaire: liste des temps de la journées que l'autobus passe
horaire = ["06h14", "07h44", "09h14", "10h44", "12h14", "13h44", "15h14", "16h44", "18h14", "19h44", "21h14"]
#horaire_heures: liste des valeurs des heures (h) que l'autobus passe
horaire_heures = [6,7,9,10,12,13,15,16,18,19,21]
#horaire_minutes: liste des valeurs des minutes (min) que l'autobus passe
horaire_minutes = [14,44,14,44,14,44,14,44,14,44,14]
#ls_heure_rn: liste des chiffres des valeurs d'heures (h) du temps présent
ls_heure_rn = []

#print "Horaire :"
print("Horaire :")
#print ligne avec tiret
print("-"*10)
#print liste de l'horaire
for heure in horaire:
    print(heure)
#ligne avec tiret
print("-"*10)

#Demande quelle est l'heure présentement
heure_rn = str(input("Entrez l'heure (ex. 15h30) :")).strip()
#Ajoute l'heure présent dans la liste de l'horraire
horaire.append(heure_rn)
#Réarrange la liste d'horraire en ordre croissant
horaire.sort()

#Trouve l'heure que le prochain autobus arrivera
arret_prochain = prochain_arret(horaire,heure_rn)
if arret_prochain == None:
    pass
else:
    #Enlève l'heure présent de la liste d'horraire
    horaire.remove(heure_rn)
    #Annonce l'heure que le prochain autobus arrivera
    print(f"Le prochain autobus pass à {arret_prochain}.")

#Calcule le temps qui reste avant que le prochain autobus arrive
minute_restant = calcule(horaire,horaire_heures,horaire_minutes,ls_heure_rn,heure_rn,arret_prochain)
if minute_restant == None:
    print("Erreur. Donnée entrée est non-valide.")
else:
    #Annonce le temps qui reste avant que le prochain autobus arrive
    print(f"Temps d'attente : {minute_restant} minutes.")
