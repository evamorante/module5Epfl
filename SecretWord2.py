#exercise 10. - you find the secret word - with if condition
secret_word = "Heyyy"
user_guess = input("Try to guess the secret word : ")
print(secret_word)
print(user_guess)
#print(secret_word) - if not working properly, do the print test
#print(user_guess) - with the different variables

if secret_word == user_guess:
  print("You find the secret word !")
