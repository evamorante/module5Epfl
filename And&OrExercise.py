#If the language is Python or JavaScript, it is a good course.
#If the languages are Python and JavaScript, this is the Thinking and Creating with Code course.
#If the number is bigger than 10 or the color is blue, the test is true.
#If the number is not bigger than 10 and the color is not blue, the test is true.

python = True
javascript = True
number = 8
color = "blue"

if python or javascript:
    print("this is a good course")
if python and javascript:
    print("this is a TTC course")
if number >10 or color == "blue":
    print("the test is true")
if number <10 and color =="blue":
    print("the test is True")

# pourquoi le print() -- output --> True or False ne marche pas avec if/and/or condition ?
if number >10 and color == "blue":
    print()
if number <=10 and color !="blue":
    print()