// exercise 26. in javascript

/**Look at the following program written in plain English:

If it is raining and if it is cold, take an umbrella and a warm jacket.
If it is raining and if it is warm, take an umbrella and a t-shirt.
If it is sunny and if it is cold, take sunglasses and a warm jacket.
If it is sunny and if it is warm, take sunglasses and a t-shirt.
If it is anything else, stay home!

Can you translate this into a Python program? When you are done, translate it to JavaScript as well! */

var weatherInput = window.prompt("Is it today raining or sunny ? : ")
var temperatureInput = window.prompt("Is it today warm or cold ? : ")

if (weatherInput == "raining" && temperatureInput == "cold"){
    console.log("Take an umbrella and a jacket");
}
else if (weatherInput == "raining" && temperatureInput == "warm"){
    console.log("Take an umbrella and a t-shirt");
}
  
else if (weatherInput == "sunny" && temperatureInput == "cold"){
    print("Take sunglasses and a jacket");
}
  
else if (weatherInput == "sunny" && temperatureInput == "warm"){
    console.log("Take sunglasses and a t-shirt");
}
  
else{
    print("Stay home !");
}
  