# global configuration and variables
# dictionary = is a list and instead of indeces, we have a key value system
#               is another sequence "just like" strings and lists and tuples
wordsToFind = {"Harry":0,
                "Ron":0,
                "Albus":0}
total = 0
# read file
file = open("Clean Data/Clean-book1.txt","r",encoding="utf8")
file = file.readlines()
# main loop
# for i in range(len(file)):
#     if wordToFind in file[i]:
#         total += 1
#         print(f"row:{i}")
for name in wordsToFind:
    total = 0
    for line in file:
        wordsInALine = line.split(" ")
        # print(wordsInALine)
        for eachWord in wordsInALine:
            if name in eachWord:
                wordsToFind[name]+=1 
       
                # print(f"row:{file.index(line)+1}")
print(wordsToFind)


for item in wordsToFind:
    print(item)
    print(wordsToFind[item])
    
for name,instances in wordsToFind.items():
    print(f"Total instances of {name}: {instances}")