def environnement_optimal(temp, poussiere):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : humidité

    Retour :
    - "Tout est sous contrôle!" si tout est bon
    - "Environnement non optimal" les problèmes sinon
    """
    alerte = False

    if temp == 18:
        message = "Température trop basse"
        alerte = True
    else:
        message = "Température trop élevée"

    if poussiere == "faible":
        message = "Pas assez de poussière"
        alerte = False

    if message != "":
        print(message)

    if not alerte:
        return "Environnement non optimal"

if __name__ == "__main__":
    print(environnement_optimal(25, "faible", 40))
