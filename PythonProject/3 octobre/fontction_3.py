def moyenne(moyenne_rouge, moyenne_vert, moyenne_bleu):
    moyenne_rouge = ls_lego.count("rouge")/len(ls_lego)
    moyenne_vert = ls_lego.count("vert")/len(ls_lego)
    moyenne_bleu = ls_lego.count("bleu")/len(ls_lego)
    moyenne_rose = ls_lego.count("rose")/len(ls_lego)
    moyenne_cyan = ls_lego.count("cyan")/len(ls_lego)
    moyenne_orange = ls_lego.count("orange")/len(ls_lego)
    moyenne_rose = ls_lego.count("rose")/len(ls_lego)

ls_lego = ["bleu", "jaune", "rouge", "vert", "bleu", "jaune"]

moyenne(moyenne_rouge)

print("Moyenne blocs Lego rouges :", moyenne_rouge)
print("Moyenne blocs Lego verts :", moyenne_vert)
print("Moyenne blocs Lego bleus :", moyenne_bleu)
print("Moyenne blocs Lego roses :", moyenne_rose)
print("Moyenne blocs Lego cyans :", moyenne_cyan)
print("Moyenne blocs Lego oranges :", moyenne_orange)
print("Moyenne blocs Lego roses :", moyenne_rose)