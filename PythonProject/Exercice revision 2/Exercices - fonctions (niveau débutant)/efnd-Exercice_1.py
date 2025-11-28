def adress(prenom:str, nom:str, domaine:str):
    nouv_adress = str(f"{nom}.{prenom}@{domaine}")
    return nouv_adress

domaine = str("cegepoutaouais.qc.ca")
prenom = str(input("Quelle est votre prénom?"))
nom = str(input("Quelle est votre nom?"))

print(f"Votre nouvelle address courriel est {adress(prenom,nom,domaine)}")
