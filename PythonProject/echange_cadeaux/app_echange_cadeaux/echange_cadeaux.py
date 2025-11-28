from datetime import *


# TODO: Ce programme doit être complété selon les exigences de l'énoncé (ajout et complétion de fonctions,
#       complétion du programme principal).

def afficher_details_participations(participations_cadeaux:list[list]):
    """
    Cette fonction permet d'afficher les détails des participations
    incluant, le nom du participant, les cadeaux qu'il offre
    ainsi que la date de déballage permise des cadeaux.

    Exemple d'affichage pour 2 participants :

    Participant : Franck
        Cadeaux : certificat, casquette
        Date de déballage : sam. 23 déc. 2023 à partir de 11:30
    Participant : Camilla
        Cadeaux : chocolats, orange, charbon
        Date de déballage : jeu. 23 nov. 2023 à partir de 10:45

    :param participations_cadeaux: Liste des participations à l'échange de cadeaux.
    :return: aucun
    """
    print("Voici la liste des participations : ")
    for participation in participations_cadeaux:
        nom_participant = participation[0]
        if len(participation) > 2:
            cadeaux = participation[1:-1]
        date_deballage_obj = participation[-1]

        liste_mois = ["janv.","fév.", "mars", "avril", "may", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
        mois_choisi = liste_mois[int(date_deballage_obj.month)-1]

        journee_semaine = ["lun.", "mar.", "mer.", "jeu.", "ven.", "sam.", "dim."]
        semaine_now = journee_semaine[date_deballage_obj.weekday()]

        temps_allowed = date_deballage_obj.strftime("%H:%M")

        print(f"Participant : {nom_participant}")
        print(f"Cadeaux : {cadeaux}")
        print(f"Date de déballage: {semaine_now} {date_deballage_obj.day} {mois_choisi} {date_deballage_obj.year} à partir de {temps_allowed}")

        # TODO : À compléter. Voir l'exemple d'affichage souhaité dans le docstring.
        #        Notez bien le format souhaité pour la date. Ex: jeu. 23 nov. 2023 à partir de 10:45


def obtenir_prenoms_participants(participations_cadeaux: list[list]) -> list:
    """
    Cette fonction permet d'obtenir la liste des prénoms des participants
    à partir de la liste des participations à l'échange de cadeaux.
    :param participations_cadeaux: Liste des participations à l'échange de cadeaux.
    :return: Liste des prénoms des participants.
    """

    # TODO: Créez les tests unitaires pour cette fonction.
    #       Corrigez/gérez les erreurs qui ressortent de vos tests unitaires.
    #       Voir l'énoncé pour plus de détails.

    participants = []
    for participation in participations_cadeaux:
        if not isinstance(participation, list):
            print(f"Attention, la liste des participations de l'échange de cadeaux n'est pas au bon format!")
            return None

        participants.append(participation[0])

    return participants

def ajout_participant() -> list:
    list_du_participant = []
    print(f"Ajout du participant {participant+1}/{nbr_nouveaux_participants}")
    nom_participant = str(input("Veuillez entrer le prénom du participant :"))
    list_du_participant.append(nom_participant)
    print(
        "Entrez les cadeaux que le participant souhaite offrir.\nSi vous voulez arrêter l'ajout de cadeaux, appuyez sur 'Entrée' sans rien écrire.")
    ajout_cadeaux = True
    while ajout_cadeaux == True:
        cadeaux_a_ajoutee = str(input("Veuillez entrer un cadeau à offrir :"))
        if cadeaux_a_ajoutee == "":
            ajout_cadeaux = False
        else:
            list_du_participant.append(cadeaux_a_ajoutee)
    date_quil_donne = str(input("Veuillez entrer la date à laquelle les cadeaux peuvent être déallés (format JJ-MM-AA HH:MM) :"))
    bonne_date = datetime.strptime(date_quil_donne, "%d-%m-%20Y %H:%M")
    list_du_participant.append(bonne_date)
    return list_du_participant



if __name__ == "__main__":

    participations_cadeaux = [["Rabia", "bas", "tasse", "livre", datetime(2023, 11, 20, 21, 0)],
                              ["Franck", "certificat", "casquette", datetime(2023, 12, 23, 11, 30)],
                              ["Camilla", "chocolats", "orange", "charbon", datetime(2023, 11, 23, 10, 45)]]

    print("Bienvenue dans l'application de gestion d'échange de cadeaux!")
    nbr_nouveaux_participants = int(input("Combien de participations voulez-vous ajouter à l'échange de cadeaux ?"))
    for participant in range(nbr_nouveaux_participants):
        participations_cadeaux.append(ajout_participant())
    afficher_details_participations(participations_cadeaux)