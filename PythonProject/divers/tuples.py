def afficher_pixel(r, g, b):
    """
    Permet d'afficher un pixel (carré) avec la couleur RGB envoyée en paramètre.
    :param r: niveau de rouge
    :param g: niveau de vert
    :param b: niveau de bleu
    :return: None
    """
    # \033[48;2;R;G;Bm → définit la couleur d’arrière-plan (background)
    #     \033[ : indique le début d’une séquence d’échappement ANSI.
    #     48;2;R;G;B : définit une couleur d’arrière-plan RGB (24 bits).
    #     m : termine la séquence.
    #     \033[0m : réinitialise les couleurs après affichage.
    #     end="" : évite le saut de ligne entre les “pixels”.
    #     " " : deux espaces pour former un carré visuellement.
    print(f"\033[48;2;{r};{g};{b}m  \033[0m", end="")