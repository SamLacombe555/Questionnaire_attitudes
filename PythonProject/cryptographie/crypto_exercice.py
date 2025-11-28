def crypter_message(message, clef):
    """
    Chiffre un message selon la clé fournie.
    """
    message_crypte = ""
    for lettre in message.lower():
        if lettre in clef:
            message_crypte += clef[lettre]
        else:
            message_crypte += lettre  # garde espaces et ponctuation
    return message_crypte

# === TODO : À TOI DE JOUER ===
# Écris la fonction suivante :
# def decrypter_message(message_crypte, clef_decryptage):
#     """
#     Déchiffre un message codé à l’aide de la clé fournie.
#     """
def decrypter_message(message_crypte, clef_decryptage):
    message_decrypted = ""
    for lettre in message_crypte.lower():
        if lettre in list(clef_espion.values()):
            for i in range(len(clef_espion)):
                if list(clef_espion.values())[i] == lettre:
                    message_decrypted += list(clef_espion)[i]
        else:
            message_decrypted += lettre
    return message_decrypted
# Dictionnaire de cryptage du Club Sandwich (décalage de 10)
clef_espion = {
    'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o', 'f': 'p', 'g': 'q',
    'h': 'r', 'i': 's', 'j': 't', 'k': 'u', 'l': 'v', 'm': 'w', 'n': 'x',
    'o': 'y', 'p': 'z', 'q': 'a', 'r': 'b', 's': 'c', 't': 'd', 'u': 'e',
    'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i', 'z': 'j'
}

# Message intercepté :
message_secret = "uoxk myv dro vkxoc kbo"
print("Message secret   :", message_secret)

# === TODO : À TOI DE JOUER ===
# Utilise ta fonction pour décrypter le message secret
message_decrypte = decrypter_message(message_secret, clef_espion)
print(f"Message décodé: {message_decrypte}")
message_crypte = crypter_message(message_decrypte, clef_espion)
print(f"Message codé : {message_crypte}")
# === TODO : À TOI DE JOUER ===
# Ajoute un fichier de tests unitaires avec au moins 2 tests pour chaque fonction.
