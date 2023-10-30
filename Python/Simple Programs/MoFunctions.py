import random
#function to generate a list of random numbers

def giveMeSomeNumbers(size,lowEnd,highEnd):
    #generate 10 random numbers 
    someNumbers=[]

    for i in range(size):
        someNumbers.append(random.randint(lowEnd,highEnd))
    return someNumbers
#variable = returnFunction()
randomListOfNumbers=giveMeSomeNumbers(1000000,-10000000,7000000000)
print(randomListOfNumbers)

'''
    When do you create function?
        Use things more than once - looking for repeating code
        Abstraction 
        


'''

