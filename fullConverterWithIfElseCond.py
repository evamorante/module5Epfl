# exercise 13. - fullConverter with if condition
def changeMoney(dollars):
    if dollars >= 100:
        print("You're very rich")

    francs = dollars*1.02
    message = str(dollars)+" dollars are "+str(francs)+" francs."
    return message

print(changeMoney(102))




def changeWater(liters):
    gallons = liters*0.17
    message = str(liters)+" liters are "+str(gallons)+" gallons."
    return message

print(changeWater(3))

def changeHeigth(meters):
    centimeters = meters*100
    message = str(centimeters)+" centimeters are "+str(meters)+" meters."
    return message

print(changeHeigth(34))

