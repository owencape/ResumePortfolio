# global configuration and variables
wordsToFind = ["Harry","Ron","Albus","Hagrid","Hermione","Draco"]
total = 0
​
# read file
file = open("CleanBook1.txt","r",encoding="utf8")
file = file.readlines()
​
# main loop
​
# for i in range(len(file)):
#     if wordToFind in file[i]:
#         total += 1
#         print(f"row:{i}")
​
for name in wordsToFind:
    total = 0
    for line in file:
        wordsInALine = line.split(" ")
        # print(wordsInALine)
        for eachWord in wordsInALine:
            if name == "Harry": 
                if "HARRY" in eachWord:
                    total += 1
                elif name in eachWord:
                    total += 1
            elif name == "Albus": 
                if "ALBUS" in eachWord:
                    total += 1
                elif name in eachWord:
                    total += 1
            elif name in eachWord:
                total += 1
                # print(f"row:{file.index(line)+1}")
    print(f"{name}: {total} count")