#imports

import random as r

from termcolor import colored

#global configuration and variables

puzzle = []
words = []
pos = []
all = []
locations = []

colors = ["green","cyan","red","light_red","light_green","blue","magenta",]

#functions

def readFile(puzzleFile,wordFile):

    global puzzle
    global words

    file1 = open(puzzleFile,"r")
    file = file1.readlines()
    row = []
    
    i = 0
    
    for lines in file:
        i += 1
        for l in range(len(lines)):
            char = lines[l]
            # print(char)
            if char == "\n" or char == "\t" or  char == "-" or char == " " or char == ",":
                lines.replace(char,",")
            else:
                row.append(char)
        
        
        if i == 1:
            length = len(row)
            
        if len(row) != length:
            print("Data Unusable")
            puzzleFile = input("Input Puzzle File: ")
            wordFile = input("Input Wordbank File: ")
            puzzle = []
            readFile(puzzleFile,wordFile)
        else:
            puzzle.append(row)
            row = []

    print("Puzzle Recognized")

    file1 = open(wordFile,"r")
    file = file1.readlines()

    word = ""
    for line in file:
        
        for l in range(len(line)):
                if line[l] == " " or line[l] =="\n" or line[l] =="\t" or line[l] == "," or line[l] == "-":
                    words.append(word)
                    word = ""
                else:
                    word+= line[l]
        
    print(puzzle)
    print()
    print(words)


def printPuzzle():
    global puzzle

    line = ""

    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            line += puzzle[row][col] + " "
        print(line)
        line = ""

def firstLetterFind(word,puzzle):
    global locations
    global pos

    letter = word[0]
    pos = []

    for r in range(0,len(puzzle)):
        for c in range(0,len(puzzle[r])):
            if puzzle[r][c] == letter:
                
                locations.append([r,c])

    for p in locations:
            if checkFirstMatch(puzzle,word,p):
                all.append(p)
                return
    print("word can't be found")

def checkFirstMatch(puzzle,word,pos):

    directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]

    for d in directions:
        if (checkAround(puzzle,word,pos,d)):
            return True

def checkAround(puzzle,word,pos,dir):
    global locations
    global colors
    global all
    
    found = [word[0]]
    start = pos
    posts = [locations]

    while checkMatch(found,word):

        if len(found) == len(word):
            print("word found")

            for row in range(len(puzzle)):
                line = ""
                for col in range(len(puzzle[row])):
                    color = r.choice(colors)
                    spot = False
                    for z in posts:
                        if (z[0] == row) and (z[1] == col):
                            spot = True
                            place = [row,col]
                            all.append(place)
                    if (spot):
                        line = line + " " + colored(puzzle[row][col],color)
                    else:
                        line = line + " " + puzzle[row][col]
            return True

        start = [start[0] + dir[0], start[1] + dir[1]]
        posts.append(start)
        if (checkIndex(puzzle, start[0], start[1])):
            found.append(puzzle[start[0]][start[1]])
        else:
            #edge of wordsearch
            return

def checkMatch(found,word):
    index = 0

    for i in found:
        if (i != word[index]):
            return False
        index += 1
    return True

def checkIndex(puzzle,row,col):
    if ((row >= 0) and (row < len(puzzle))):
        if ((col >= 0) and (col < len(puzzle[row]))):
            return True
    return False

def finishedPuzzle():
    global colors
    global all
    global locations
    color = r.choice(colors)

    for row in range(len(puzzle)):
        line = ""
        for c in range(len(puzzle[row])):
            
            if [row,c] in all:
                line += colored(puzzle[row][c],color) + " "
            else:
                line += puzzle[row][c] + " "
        print(line)
        
               

#main
print(f"Enter puzzle file below(make sure they're no spaces in file contents)")
puzzleFile = input("Enter Wordsearch Puzzle File: ")

print(f"Enter wordbank file(make sure all the words are ALL CAPS and each have a new line)")
wordFile = input("Enter Wordbank File: ")

readFile(puzzleFile,wordFile)
printPuzzle()

for word in words:
    firstLetterFind(word,puzzle)

finishedPuzzle()
