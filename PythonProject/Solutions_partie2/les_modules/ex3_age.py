from datetime import datetime, date
import locale

locale.setlocale(locale.LC_ALL, "fr_CA.utf8")

def demander_date_naissance():
    texte = input("Veuillez entrer une date de naissance au format jj/mm/aaaa : ")
    date_liste = texte.split("/")
    return date(int(date_liste[2]), int(date_liste[1]), int(date_liste[0]))

def age_en_annees(date_naissance):
    aujourd_hui = date.today()
    age = aujourd_hui - date_naissance
    age = age.days//365
    return age

def age_en_jours(date_naissance):
    aujourd_hui = date.today()
    return (aujourd_hui - date_naissance).days

def afficher_date_naissance(date_naissance):
    print("Vous êtes né(e)", date_naissance.strftime("%A le %d %B %Y"))

# Programme principal
dn = demander_date_naissance()
print(f"Vous avez {age_en_annees(dn)} ans")
print(f"Vous êtes vieux de {age_en_jours(dn)} jours")
afficher_date_naissance(dn)
