def adress(prenom:str, nom:str, domaine:str):
    nouv_adress = str(f"{nom}.{prenom}@{domaine}")
    return nouv_adress

while True:
    domaine = str("cegepoutaouais.qc.ca")
    nom = str(input("Quelle est votre nom?"))
    prenom = str(input("Quelle est votre prénom?"))

    nom1=nom.replace(" ","")
    prenom1=prenom.replace(" ","")

    if (nom1.isalpha() and prenom1.isalpha()) == False:
        print("Le nom et prénom ne doivent contenir aucune valeur numérique")
    else:
        break

nouv_adress = adress(prenom,nom,domaine).lower()
nouv_adress_final = nouv_adress.replace(" ","-")


print(f"Votre nouvelle address courriel est {nouv_adress_final}")
