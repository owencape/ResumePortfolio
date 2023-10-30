menu='''
    kilogram to gram converter)
    kg to g (kg)
    g to kg (gk)

'''
def kg2g():
    kg = int(input("kilograms: "))
    print(kg*1000)

def g2kg():
    g = int(input("grams: "))
    print(g/1000,)

user=input(menu)

while(user!="quit"):
    if user =="kg":
        kg2g()
    elif user =="gk":
        g2kg()

    user = input(menu)