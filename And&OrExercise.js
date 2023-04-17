//exercice 30. module 5
/**If the language is Python or JavaScript, it is a good course.
If the languages are Python and JavaScript, this is the Thinking and Creating with Code course.
If the number is bigger than 10 or the color is blue, the test is true.
If the number is not bigger than 10 and the color is not blue, the test is true.*/

var python = true
var javascript = true
var number = 12
var color = "blue"

if (python || javascript){
     console.log("this is a good course");
}
   
if (python && javascript){
    console.log("this is a TTC course");
}
    
if (number >10 || color == "blue"){
    console.log("The number is greater than 10 OR the color is blue");
}
if (number >10 && color == "blue"){
    console.log("The number is greater than 10 AND the color is blue");
}
    