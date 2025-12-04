import hashlib

from Exercice_analyse_statistiques.analyse_statistiques.gestion_fichiers import sauvegarder_resultats_csv


def hasher_mots(mots: list[str]) -> dict:
    """
    Fonction qui reçoit une liste de mots et qui génère les hash md5, sha256 et sha512 de chaque mot à
    l'aide du module hashlib.
    La fonction génère ainsi un dictionnaire dont les clés sont les mots et les valeurs sont
    une liste des 3 hash calculés auparavant.
    :param mots: La liste des mots à hasher
    :return: Le dictionnaire généré contenant les hash de chaque mot
    """
    hash_dict = {}

    # TODO: Complétez cette fonction pour qu'elle génère un dictionnaire contenant les 3 hash demandés (md5, sha256, sha512)
    #   pour chacun des mots dans la liste des mots non chiffrés fournie dans le programme principal.

    #pseudocode
    #boucle pour chaque mot de la liste
        #hasher le mot 3 fois
        #ajouter le mot et ses hash au dictionnaire

    for mot in mots:
        # Réf. Notes de cours
        # https://projets420.gitbook.io/notes-de-cours/cryptographie/introduction-a-la-cryptographie
        mot_en_bytes = mot.encode()
        hash_md5 = hashlib.md5(mot_en_bytes).hexdigest()

        # Réf. : Doc python de hashlib
        # https://docs.python.org/3/library/hashlib.html#usage
        hash_sha256 = hashlib.sha256(mot_en_bytes).hexdigest()
        hash_sha512 = hashlib.sha512(mot_en_bytes).hexdigest()

        hash_dict[mot] = [hash_md5, hash_sha256, hash_sha512]


    return hash_dict


def chiffrement_cesar(chaine: str, nb_cesar: int) -> str:
    """
    Cette fonction reçoit un mot ainsi que le nombre de rotation pour chiffrer le mot. Elle en fait le chiffrement
    de césar en utilisant le nombre reçu pour transformer le mot.
    :param chaine: Le mot ou chaîne de caractères à chiffrer
    :param nb_cesar: Le nombre de rotations à faire pour le chiffrement.
    :return: La chaine chiffrée résultante
    """
    caracteres_remplacement = "abcdefghijklmnopqrstuvwxyz"
    chaine_chiffree = ""

    # TODO: à l'aide des caractères de remplacement, du nombre de César et de la chaine originale, faire le chiffrement
    #   de césar et retournez la chaîne ainsi générée

    # pseudocode :
    # boucle pour le nb de caractère dans la chaine
        # trouver l'index de la lettre
        # ajouter le décalage à l'index
        # valider l'index, exemple si on dépasse z faut revenir au début
        # prendre la lettre après le décalage, au nouvel index, et l'ajouter dans la chaine chiffrée
    # retourner la chaine chiffrée

    for i in range(len(chaine)):
        index = caracteres_remplacement.index(chaine[i])
        nouvel_index = (index + nb_cesar) #% 26
        if nouvel_index >= len(caracteres_remplacement):
            nouvel_index -= len(caracteres_remplacement[nouvel_index])
        lettre = caracteres_remplacement[nouvel_index]
        chaine_chiffree += lettre
    return chaine_chiffree

#def sauvegarder(dict_mots_passes: dict) -> None:
 #   """
  #  Fonction pour sauvegarder un dictionnaire de mots de passes avec ses hash
   # :param dict_mots_passes: dictionnaire contenant les mots de passes et leur listes de hash
    #"""
    #with open("mots_passes.json", "w", encoding="utf-8")

def sauvergarder_mots_passes():

if __name__ == '__main__':

    mots_aleatoires = [
        "arbre", "bateau", "chat", "drapeau", "elephant", "fleur", "glace", "horizon", "iguane", "jonquille",
        "kangourou", "lumiere", "montagne", "nuage", "porte", "quiche", "requin", "soleil", "tigre",
        "univers", "vague", "wagon", "xylophone", "yeti", "zebre", "abeille", "ballon", "canard", "dejeuner",
        "etoile", "fromage", "girafe", "horloge", "internet", "joie", "karaoke", "livre", "magie", "neige",
        "orange", "parapluie", "quartz", "riz", "sable", "telephone", "uniforme", "velo", "weekend", "xylocope",
        "yaourt", "zeste", "amour", "banane", "cerise", "dent", "enfant", "fete", "guitare", "herisson",
        "idee", "jardin", "koala", "lune", "maison", "nature", "oiseau", "pomme", "quai", "riviere",
        "serpent", "tomate", "ulysse", "vent", "whisky", "xenon", "yeux", "zen", "avion", "boulangerie",
        "cerf", "dromadaire", "epinard", "fusil", "grange", "hameau", "ilot", "jongleur", "kilogramme",
        "lavoir", "muguet", "navire", "ours", "pierre", "quatre", "renard", "scie", "trousseau", "universite"
    ]

    mots_cesar = [
        "ozsxkbn",
        "thecqtqyhu",
        "diozmizo"
    ]

    mots_hash = [
        'dc0add0b9d59afd7f5d38ee814f85c37',
        '3378673b4755b9c5d291a295aade6ed10ab531e77cdb96b92e531e3b4be1aa260e34507681117cd8212341e2a37d31540af25302584bb489b5614f805883e2ff',
        'ceac214f32b3bc28669d0e09487d82a171fbc38f7b48140e50279e7774c079ae',
        'ef0738953fcb9fbfedc6795a7c5e8a7d5894d3534adc346e0f9f1bf0a3017f87a21ef14bac9340b7d1fcdc9579906ae1bde0bd514b9b8c1e2e091d1314abf528'
    ]

    mots_cesar_hash = [
        '95b7aa774ee5d86302c89ef3bc6e3fcd',
        '059f79fbb20a17eb6c7dc12883fb6105eca60071034ac32ae201a57762020e07'
    ]

    # TODO : Déchiffrer tout
    # pseudocode
    # hasher tous les mots aléatoires
    # pour chaque hash dans mot_hash
        # trouver une valeur identique dans le dictionnaire
        # boucle pour le dictionnaire de hash
            # comparer les hash dans les listes avec les hash dans le dictionnaire:
            # si hash in valeur : on a trouvé le mot

    dict_hash_mots_aleatoires = hasher_mots(mots_aleatoires)
    for hash in mots_hash:
        for key, value in dict_hash_mots_aleatoires.items():
            #print(key, value)
            if hash in value:
                print(key)


    # for every mot in mots_aléatoires
        # for every nb_cesar possible ie 26

    # pseudocode :
    # boucle pour le nb de caractère dans la chaine
        # trouver l'index de la lettre
        # ajouter le décalage à l'index
        # valider l'index, exemple si on dépasse z faut revenir au début
        # prendre la lettre après le décalage, au nouvel index, et l'ajouter dans la chaine chiffrée
    # retourner la chaine chiffrée


    dict_cesar_mots_aleatoires = {}
    for mot in mots_aleatoires:
        for j in range(25):
            cesar_j = chiffrement_cesar(mot,j)
            dict_cesar_mots_aleatoires[mot] = [cesar_j]

    for key, value in dict_cesar_mots_aleatoires.items():
        print(key, value)
