def generer_adresses_courriel(prenoms:list, noms:list, domaine:str):
    """
    Génère des adresses courriel au format [prenom].[nom]@[domaine].
    :param prenoms: Une liste contenant les prénoms.
    :param noms: Une liste contenant les noms.
    :param domaine: Le nom de domaine à utiliser pour les adresses courriel.
    :return: Une liste contenant les adresses courriel générées.
    """

    adresses_courriel = []

    for i in range(len(prenoms)):
        prenom = prenoms[i]
        nom = noms[i]

        email = f"{prenom.lower()}.{nom.lower()}@{domaine}"  # Minuscule et suppression des espaces
        adresses_courriel.append(email)

    return adresses_courriel


if __name__ == "__main__":

    prenoms = []
    noms = []

    for i in range(3):
        prenom = input(f"Entrez le prénom de la personne {i + 1}: ")
        nom = input(f"Entrez le nom de la personne {i + 1}: ")

        # Utilisation de strip() pour enlever les espaces superflus
        noms.append(nom.strip())
        prenoms.append(prenom.strip())

    nom_domaine = input(f"Quel est le nom de domaine à utiliser ? ")

    adresses_courriel = generer_adresses_courriel(prenoms, noms, nom_domaine)

    print("\nAdresses courriel générées :")
    for adresse in adresses_courriel:
        print(adresse)