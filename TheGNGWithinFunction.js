function guessGame (){
    var nombre = 24
    var couleur = "vert"
    var nombreQuestion = window.prompt("Devinez le nombre magique : ");
    var couleurQuestion = window.prompt("Découvrez la couleur magique : ");

    if (nombre == Number(nombreQuestion) && couleur == couleurQuestion){
        console.log("Bravo, vous avez trouvé le nombre et la couleur magiques !");
    }
    else if (nombre == Number(nombreQuestion) || couleur == couleurQuestion){
        console.log("Bravo, vous avez trouvé un des deux mystères !");
    }
    else{
        console.log("Vous n'avez trouvé aucun des deux mystères");
        console.log("Bonne chance pour la prochaine !");
    }
        
    console.log("Essayez à nouveau");
}

guessGame();

//it works !!! youhrrraaaa !
//si je pose les deux variables dans les paramètres de la fonction, et que je les pose lorsque j'appelle
//la fonction, ça joue également, toutefois j'ai une ligne "undiefined" en grisé en plus en dessous des outputs
