/**Define and assign two number variables.
Subtract the first number from the second one.
If the result is bigger than 10, then display The result is greater than 10.
If the result is bigger than 0 (but not bigger than 10!), display The result is greater than 0 but not than 10.
If the result is 0, display The result is zero.
For any other result, display The result is a negative number.
Whatever happens, display You can try again! just before the program exits. */

var numberOne = 23;
var numberTwo = 12;
var result = numberOne-numberTwo;

console.log(result);

if (result >10){
    console.log("The result is greater than 10");
}
else if (result >0){
    console.log("The result is between 0 and 10");
}
else if (result == 0){
    console.log("The result is zero");
}
else {
    console.log("The result is unavailable");
}



