# exercise 13. - fullConverter with if condition
def changeMoney(dollars):
    if dollars >= 100:
        print("You're converting more than 99 dollars and you're very rich")

    francs = dollars*1.02
    message = str(dollars)+" dollars are "+str(francs)+" francs."
    return message

print(changeMoney(102))




def changeWater(liters):
    if liters >100:
        print("Pay attention at the energie consommation")

    gallons = liters*0.17
    message = str(liters)+" liters are "+str(gallons)+" gallons."
    return message

print(changeWater(102))

def changeHeigth(meters):
    if meters >100:
        print("That's very long")
    centimeters = meters*100
    message = str(centimeters)+" centimeters are "+str(meters)+" meters."
    return message

print(changeHeigth(200))

