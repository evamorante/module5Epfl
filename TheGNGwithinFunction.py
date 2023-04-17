#exercice 32./part 2 module 5 - if/else cond. within a function
#nombre = 24
#couleur = "vert"

def guess_number(nombre, couleur):

    nombre_question = input("Devinez le nombre magique : ")
    couleur_question = input("Découvrez la couleur magique : ")
    if nombre == int(nombre_question) and couleur == couleur_question:
        print("Bravo, vous avez trouvé le nombre et la couleur magiques !")
    elif nombre == int(nombre_question) or couleur == couleur_question:
        print("Bravo, vous avez trouvé un des deux mystères !")
    else:
        print("Vous n'avez trouvé aucun des deux mystères")
        print("Bonne chance pour la prochaine !")

    print("Essayez à nouveau")

guess_number(24, "vert")