#Ask the user for a number between 1 and 20.
#Ask the user for a color.
#Compare the user inputs with your own secret values. The rule is as follows:

    #If the user guessed both values, display You've found both the secret number and the secret color!
    #If the user guessed only one of the two values, display You found at least one of the secrets!
    #If the user didn't guess any of the two values, display the two following sentences on two separate
    #lines: You didn't find any of the secrets! and Better luck next time!

    #Whatever happens, the program will always display Try again! at the end.

nombre = 24
couleur = "vert"
print(nombre)
print(couleur)

nombre_question = input("Devinez le nombre magique : ")
couleur_question = input("Découvrez la couleur magique : ")

if nombre == int(nombre_question) and couleur == couleur_question:
    print("Bravo, vous avez trouvé le nombre et la couleur magiques !")
elif couleur == int(nombre_question) or couleur == couleur_question:
    print("Bravo, vous avez trouvé un des deux mystères !")
else:
    print("Vous n'avez trouvé aucun des deux mystères")
    print("Bonne chance pour la prochaine !")

print("Essayez à nouveau")
