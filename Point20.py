# Ask the user to enter a first number.
#Ask the user to enter a second number.
#Subtract the first number from the second one.
#If the result is bigger than 10, then display The result is greater than 10.
#If the result is bigger than 0 (but not bigger than 10!), display The result is greater than 0 but not than 10.
#If the result is 0, display The result is zero.
#For any other result, display The result is a negative number.
#Whatever happens, display You can try again! just before the program exits.

    
number_one = input("Enter a number : ")
number_two = input("Enter a second number : ")
result = int(number_one) - int(number_two)

if result >10:
    print("The result is bigger than 10")
elif result <10:
    print("The result is between 0 and 10")
elif result == 0:
    print("The result is zero")
else:
    print("The result is not available")

print("You can try again !")





