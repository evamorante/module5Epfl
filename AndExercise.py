# exercise 26. in python
#Look at the following program written in plain English:

#If it is raining and if it is cold, take an umbrella and a warm jacket.
#If it is raining and if it is warm, take an umbrella and a t-shirt.
#If it is sunny and if it is cold, take sunglasses and a warm jacket.
#If it is sunny and if it is warm, take sunglasses and a t-shirt.
#If it is anything else, stay home!

#Can you translate this into a Python program? When you are done, translate it to JavaScript as well!

weather_input = input("Is it today raining or sunny ? : ")
temperature_input = input("Is it today warm or cold ? : ")

if weather_input == "raining" and temperature_input == "cold":
  print("Take an umbrella and a jacket")
elif weather_input == "raining" and temperature_input != "cold":
  print("Take an umbrella and a t-shirt")
elif weather_input != "raining" and temperature_input == "cold":
  print("Take sunglasses and a jacket")
elif weather_input != "raining" and temperature_input != "cold":
  print("Take sunglasses and a t-shirt")
else:
  print("Stay home !")
    
