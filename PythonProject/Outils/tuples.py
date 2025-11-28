couleur = (255, 0, 0)  # Rouge (R, G, B)

# Accès aux éléments du tuple --> Comme une liste
r = couleur[0]
v = couleur[1]
b = couleur[2]

print("Rouge =", r)
print("Vert =", v)
print("Bleu =", b)

# Décomposition du tuple
r, v, b = couleur
print("Rouge =", r)
print("Vert =", v)
print("Bleu =", b)