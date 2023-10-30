import random
from Conversion import *






#convert any unit to any unit... kind of
menu='''
    in to cm (ic)
    cm to in (ci)
    kg to g  (kgg)
    g to kg  (gkg)
    o to c   (oc)
    c to o   (co)

    which conversion? 
'''
def in2cm():
    inches = int(input("inches: "))
    print(inches*2.54)

def cm2in():
    cm = int(input("cm: "))
    print(cm/2.54)
    
#kg to g
# moles to g
# mil to inches
# meters to feet
# cen to meters
# mil to centi
# ounces to cup
# tsp to Tsp
# joules to watts
# m/s to ft/s

#post on py python channel



user=input(menu)
#loop until the user says quit
while(user!="quit"):
    if user =="ic":
        in2cm()
    elif user =="ci":
        cm2in()
    elif user =="kgg":
        kg2g()
    elif user =="gkg":
        g2kg()
    elif user =="oc":
        oz2cup()
    elif user =="co":
        cup2oz()
    

    user = input(menu)
