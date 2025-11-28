def verifie(a_verifie:float, seuil_inferieur:float, seuil_superieur:float):
    if a_verifie > seuil_superieur:
        return "La valeur est au-dessus du seuil supérieur"
    elif a_verifie == seuil_superieur:
        return "La veleur est égal au seuil supérieur"
    elif (seuil_inferieur < a_verifie) and (a_verifie < seuil_superieur):
        return "La valeur est entre le seuil inférieur et supérieur"
    elif a_verifie == seuil_inferieur:
        return "La valeur est égal au seuil inférieur"
    elif a_verifie < seuil_inferieur:
        return "La valeur est au-dessous du seuil inférieur"

a_verifie = float(input("Quelle est la valeur à vérifier?"))
seuil_inferieur = float(input("Quelle est le seuil inférieur?"))
seuil_superieur = float(input("Quelle est le seuil supérieur?"))


print(f"{verifie(a_verifie,seuil_inferieur,seuil_superieur)}")
