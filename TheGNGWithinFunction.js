function guess_number(nombre, couleur){
    
    nombreQuestion = windows.prompt("Devinez le nombre magique : ");
    couleurQuestion = windows.prompt("Découvrez la couleur magique : ");

    if (nombre == Number(nombreQuestion) && couleur == couleurQuestion){
        console.log("Bravo, vous avez trouvé le nombre et la couleur magiques !");
    }
    else if (nombre == Number(nombre_question) || couleur == couleur_question){
        console.log("Bravo, vous avez trouvé un des deux mystères !");
    }
    else{
        print("Vous n'avez trouvé aucun des deux mystères");
        print("Bonne chance pour la prochaine !");
    }
        
    console.log("Essayez à nouveau");
}

    
console.log(guess_number(24, "vert"));