def retrait(solde: float, montant: float) -> float:
    """
    Effectue un retrait sur le solde donné.

    - Si le montant est négatif ou nul, le retrait est refusé.
    - Si le montant est supérieur au solde, on retire seulement le solde restant.
    - Sinon, on retire le montant demandé.

    Retourne le nouveau solde.
    """
    if montant <= 0:
        print("* Retrait refusé (montant invalide)")
        return solde

    if montant > solde:
        print(f"* Solde insuffisant, retrait effectué: {solde} $")
        return 0  # tout le solde est retiré

    solde -= montant
    print(f"* Retrait effectué: {montant} $")
    return solde


if __name__ == "__main__":
    MONTANT_INITIAL = 1000
    solde = MONTANT_INITIAL

    print("*************************")
    print("***      GUICHET      ***")
    print("*************************")
    print(f"Solde initial:  {solde:.2f} $")
    print("*************************")

    ls_retraits = []
    while True:
        choix = input("Voulez-vous faire un retrait? (o/n) ")
        if choix == "o":
            while True:
                try:
                    retrait_1 = float(input(f"Retrait {len(ls_retraits)+1}: Combien voulez-vous retirer? "))
                    if retrait_1 <= 0 or retrait_1 > solde:
                        print(f"Entrez un entier positif inférieur ou égal au solde de {solde}.")
                    else:
                        break
                except ValueError:
                    print("Entrée invalide : entrez un entier (ex. 2).")
            solde = retrait(solde, retrait_1)
            ls_retraits.append(retrait_1)
        elif choix == "n":
            break
        else:
            print("Choix non valide, entrez la lettre o pour oui ou n pour non.")

    print("*********************")
    print(f"Solde initial: {MONTANT_INITIAL:.2f} $")

    for i in range(len(ls_retraits)):
        print(f"Retrait {i+1}:     {ls_retraits[i]:.2f} $")

    print(f"Solde final:   {solde:.2f} $")
    print("*********************")
