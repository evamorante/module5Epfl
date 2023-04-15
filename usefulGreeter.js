//exercise 22. - useful greeter
/**The program will be written in JavaScript.
Write a greet() function that takes a parameter called gender.
If the parameter is male, return the string Hello Sir! Welcome back. from the function.
If the parameter is female, return the string Hello Madam! Welcome back. from the function.
If the parameter is anything else, return the string Hello! Welcome back. from the function.
Test your function by calling it with:

male
female
not specified

Display the function result in your tests in the console. */



function askGender(gender){
    if (gender == "male"){
        return "Hello Sir ! Welcome back.";
    }
    else if(gender == "female"){
        return ("Hello Madam ! Welcome back.");
    }
    else {
        return ("Hello ! Welcome back.");
    }
}
//it works with or without parenthesis in the return function
console.log(askGender("male"));
console.log(askGender("female"));
console.log(askGender("not specified"));

