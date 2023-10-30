#Money Making Life
#Have different jobs that have different income
#Players choose their way throughout their life


import math

from pdb import find_function


menu='''
    Welcome to Teaching Mania!
    The game where you get to choose your way!
    Type "start" to begin the game

    ***type "quit" at anytime to stop the game

'''

def checkPapers():
                        classnames=["Alvin", "JJ", "Nick", "Dallas", "Danny"]
                        classperiod=["0","3","5","100"]
                        papers='''
                        select a paper
                        ---------------
                        if you wish to stop grading papers type "done"
                        ---------------
                        paper1 (p1)
                        paper2 (p2)
                        paper3 (p3)
                        paper4 (p4)
                        paper5 (p5)
                        -----------
                        if you would like to open the classlist with the papers
                        add "cl" to the end of what paper you choose (NO SPACES)
                        Ex. "p1cl" or if you wish to view a paper without the classlist
                        just type the paper for Ex. "p1"
                    
                        '''
                        classlist='''
                        Alvin -- Period 5
                        JJ -- Period 3
                        Nick -- Period 3
                        Dallas -- Period 5
                        Danny -- Period 5
                        
                        '''
                        user=input(papers)
                        if user =="p1cl":

                            print("Name:",classnames[0],"Period:",classperiod[0])
                            print(classlist)  
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Alvin's paper!")
                                feedback=input("What would you like to say to Alvin?: ")
                                user=input("type | p1 | to see Alvins new paper: ")
                                if user =="p1":
                                    print(f"Name: Alvin | Period:0 | Teacher Comment: {feedback}")
                                    checkPapers()
                                    
                                    
                                    
                                                      
                        elif user =="p1":
                            print("Name:",classnames[0],"Period:",classperiod[0])
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Alvin's paper!")
                                feedback=input("What would you like to say to Alvin?: ")
                                user=input("type | p1 | to see Alvins new paper: ")
                                if user =="p1":
                                    print(f"Name: Alvin | Period:0 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p2cl":
                            print("Name:",classnames[1],"Period:",classperiod[1])   
                            print(classlist) 
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on JJ's paper!")
                                feedback=input("What would you like to say to JJ?: ")
                                user=input("type | p2 | to see JJ's new paper: ")
                                if user =="p2":
                                    print(f"Name: JJ | Period:3 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p2":
                            print("Name:",classnames[1],"Period:",classperiod[1])
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on JJ's paper!")
                                feedback=input("What would you like to say to JJ?: ")
                                user=input("type | p2 | to see JJ's new paper: ")
                                if user =="p2":
                                    print(f"Name: JJ | Period:3 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p3cl":
                            print("Name:",classnames[2],"Period:",classperiod[1])
                            print(classlist)
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Nick's paper!")
                                feedback=input("What would you like to say to Nick?: ")
                                user=input("type | p3 | to see Nick's new paper: ")
                                if user =="p3":
                                    print(f"Name: Nick | Period:3 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p3":
                            print("Name:",classnames[2],"Period:",classperiod[1])
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Nick's paper!")
                                feedback=input("What would you like to say to Nick?: ")
                                user=input("type | p3 | to see Nick's new paper: ")
                                if user =="p3":
                                    print(f"Name: Nick | Period:3 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p4cl":
                            print("Name:",classnames[3],"Period:",classperiod[1])
                            print(classlist)
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Dallas's paper!")
                                feedback=input("What would you like to say to Dallas?: ")
                                user=input("type | p4 | to see Dallas's new paper: ")
                                if user =="p4":
                                    print(f"Name: Dallas | Period:3 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p4":
                            print("Name:",classnames[3],"Period:",classperiod[1])
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Dallas's paper!")
                                feedback=input("What would you like to say to Dallas?: ")
                                user=input("type | p4 | to see Dallas's new paper: ")
                                if user =="p4":
                                    print(f"Name: Dallas | Period:3 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p5cl":
                            print("Name:",classnames[4],"Period:",classperiod[3])
                            print(classlist)
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Danny's paper!")
                                feedback=input("What would you like to say to Danny?: ")
                                user=input("type | p5 | to see Danny's new paper: ")
                                if user =="p5":
                                    print(f"Name: Danny | Period:100 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="p5":
                            print("Name:",classnames[4],"Period:",classperiod[3])
                            user=input("Is this correct?:(y/n)")   
                            if user =="y":
                                print("Good job!")
                                checkPapers()
                            elif user =="n":
                                print("Leave a mean comment on Danny's paper!")
                                feedback=input("What would you like to say to Danny?: ")
                                user=input("type | p5 | to see Danny's new paper: ")
                                if user =="p5":
                                    print(f"Name: Danny | Period:100 | Teacher Comment: {feedback}")
                                    checkPapers()
                        elif user =="done":
                            print("Done grading!")
                        else:
                            print("Invalid Value")                     
def signB50():
    signBonus='''
                 _____________________________________________________________________
                |.============[_F_E_D_E_R_A_L___R_E_S_E_R_V_E___N_O_T_E_]============.|
                ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _ %&%&%&%&||
                ||%&%&%&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ \%&%&%||
                ||&%.--.}|| ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_||{.--.%&||
                ||%/__ _\                ,-----,-'____'-,-----,               /__ _\ ||
                ||||_ / \|              [    .-;"`___ `";-.    ]             ||_ / \|||
                |||  \| || """""""""" 1  `).'.'.'`_ _'.  '.'.(` A 76355942 J |  \| ||||
                |||,_/\_/|                //  / .'    '\    \\               |,_/\_/|||
                ||%\    /   d8888b       //  | /   _  _ |    \\      .-"""-.  \    /%||
                ||&%&--'   8P |) Y8     ||   //;   a \a \     ||    //A`Y A\\  '--'%&||
                ||%&%&|    8b |) d8     ||   \\ '.   _> .|    ||    ||.-'-.||   |&%&%||
                ||%&%&|     Y8888P      ||    `|  `-'_ ` |    ||    \\_/~\_//   |&%&%||
                ||%%%%|                 ||     ;'.  ' ` /     ||     '-...-'    |%&%&||
                ||%&%&|  A 76355942 J  /;\  _.-'. `-..'`>-._  /;\               |%&%&||
                ||&%.--.              (,  ':     \; >-'`    ;` ,)              .--.%&||
                ||%( 50 ) 1  """""""  _( \  ;...---""---...; / )_```"""""""1  ( 50 )%||
                ||&%'--'============\`----------,----------------`/============'--'%&||
                ||%&JGS&%&%&%&%&&%&%&) F I F T Y   D O L L A R S (%&%&%&%&%&%&&%&%&%&||
                '"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""`
                Your were rewarded $50 for your signing bonus!
                ---------------------------------------------
    '''
    print(signBonus)





user=input(menu)
while(user !="quit"):
    if user =="start":
        
        
            screen1='''
                                                                ___
                                                        ___..--'  .`.
                                                ___...--'     -  .` `.`.
                                    ___...--' _      -  _   .` -   `.`.
                            ___...--'  -       _   -       .`  `. - _ `.`.
                    __..--'_______________ -         _  .`  _   `.   - `.`.
                    .`    _ /\    -        .`      _     .`__________`. _  -`.`.
                .` -   _ /  \_     -   .`  _         .` |Career Fair|`.   - `.`.
              .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
            .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
                |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
                | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
                |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
                |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
             ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
             -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
            `--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
            _____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
            ----------`--._          ''      ``--.._|:::::::::::::::::::::::|
            `--._ _________`--._'        --     .   ''-----.................'
                `--._----------`--._.  _           -- . :''           -    ''
                    `--._ _________`--._ :'              -- . :''      -- . ''
            -- . ''       `--._ ---------`--._   -- . :''
                    :'        `--._ _________`--._:'  -- . ''      -- . ''
            -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                                        `--._ _________`--._
            -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
                    -- . ''       -- . ''         `--._ _________`--._   -- . ''
            :'                 -- . ''          -- . ''  `--._----------`--._
            You're at a career fair and currently not getting a lot of interest:(
            --------------------------------------------------
            Your only offer is in:
            Middle School Teacher (mst)
            --------------------------------------------------
            Type the letters in parenthesis to choose that job
            
            '''

  
            user=input(screen1)
            if user =="mst":
                teacher='''
                You chose to be a Middle School Teacher!
                                 _,._      
                     .||,       /_ _\\     
                    \.`',/      |'L'| |    
                    = ,. =      | -,| L    
                    / || \    ,-'\"/,'`.   
                    ||     ,'   `,,. `.  
                    ,|____,' , ,;' \| |  
                    (3|\    _/|/'   _| |  
                    ||/,-''  | >-'' _,\\ 
                    ||'      ==\ ,-'  ,' 
                    ||       |  V \ ,|   
                    ||       |    |` |   
                    ||       |    |   \  
                    ||       |    \    \ 
                    ||       |     |    
                    ||       |      \_,-'
                    ||       |___,,--")_
                    ||         |_|   ccc/
                    ||        ccc/       
                    ||                

            You were enrolled for teaching at Bandera Academy of Losers!
            ------------------------------------------------------------
            First you need to enter into the school system!
            type "login" to create a username and password
            
            
            '''
            user=input(teacher)
            if user =="login":
                username=input("set username: ")
                userpassword=input("set password: ")
                print(f"{username} {userpassword}")
                checkK='''
                You now have to do a robot check!
                type "rc" to start
                '''
                user=input(checkK)
                if user=="rc":
                    
                    answer=input("What is 2+2: ")
                    if answer=="4":
                        num1=input("Put a random number to multiply: ")
                        num2=input("Put another random number to multiply: ")
                        print(int(num1)*int(num2), "Here's your created number --- you passed the robot check!")
                    else: answer=input
                boom='''
                You can now accept your signing bonus after you confirm your password!
                ----------------------------------------------------------------------
                '''
                print(boom)
                while(user != userpassword):
                    user=input("password: ")
                else:
                    print("You're in the banking system type | sb | to collect money!")
            user=input(boom)
            if user =="sb":
                signB50()
            def startAgain():
                print('''
                 You're now at work you have a couple of tasks to be done!
                -Grade papers (gp)
                -Mix kids names up (mx)
                -----------------------
                -quit life (quit)
                
                 
                ''')
                user=input()
                if user=="gp":
                    desk='''
                    You sit down at your desk and throw a fat stack down!
                    -----------------------------------------------------
                    You specifcally told your class to put their correct name and period number before turning in the test.
                    You are going to check if they all did that right.
                    -----------------------------------------------------
                    type "c" to start checking
                    
                    '''
                  
                    user=input(desk)
                    if user=="c":
                        classnames=["Alvin", "JJ", "Nick", "Dallas", "Danny"]
                        classperiod=["0","3","5","100"]
                        papers='''
                        select a paper
                        ---------------
                        if you wish to stop grading papers type "done"
                        ---------------
                        paper1 (p1)
                        paper2 (p2)
                        paper3 (p3)
                        paper4 (p4)
                        paper5 (p5)
                        -----------
                        if you would like to open the classlist with the papers
                        add "cl" to the end of what paper you choose (NO SPACES)
                        Ex. "p1cl" or if you wish to view a paper without the classlist
                        just type the paper for Ex. "p1"
                    
                        '''
                        classlist='''
                        Alvin -- Period 5
                        JJ -- Period 3
                        Nick -- Period 3
                        Dallas -- Period 5
                        Danny -- Period 5
                        
                        '''
                        checkPapers()
                if user=="mx":
                    room='''
                    It's the first day of school!
                    You're one of the weird teachers that likes to mix kids names up on purpose
                    You want to see every possible combination of everyone's names.
                    -------------------------------------------------------------
                    type "m" to start mixing names up
                    
                    '''
                    user=input(room)
                    if user=="m":
                        first=["Alvin","JJ","Nick","Dallas","Danny"]
                        last=["Bacon","Durant","Looper","Red","Lucas"]
                        for x in first:
                            for y in last:
                                print(x,y)
                        print("When done viewing type | r | to reset")
                        user=input("type here: ")
                        if user=="r":
                                        startAgain()
                    elif user=="quit":
                        done='''
                        ____________________________________________
                        
                        
                        
                        You quit the game!




                        
                        
                        
                        
                        
                        
                        ____________________________________________
                        '''
                        print(done)     
    
                                
                        
                   
    startAgain()                          
                            
                            
                            
                            
                                
                        
                            
                            
                            
                            

                
            

            
            
        # elif user =="ffm":
        #     chef='''
        #     // ""--.._
        #     ||  (_)  _ "-._
        #     ||    _ (_)    '-.
        #     ||   (_)   __..-'
        #     \\__..--""

        #     You got a job at Joe's Plentiful Pizza!
        #     ---------------------------------------
        #     You have a few options:
        #     You can collect your signing bonus (sb)
            
            
        #     '''
            
        #     user=input(chef)
        #     if user =="sb":
        #         signB50()
        #         print('''  
        #         You're now at work you have mutliple tasks to be done!
        #         -Make pizzas (mk)
        #         -Cut vegetables (cv)
        #         -Delievery driver (dd)
                
        #         ''')
            

        # elif user =="zk":
        #     zoo='''
        #         ___            ___
        #         /   \          /   \
              
        #         _\   \      /  /__
        #         \___  \____/   __/
        #             \_       _/
        #             | @ @  \_
        #             |
        #           _/     /\
                 
        #           \_____/ /
        #             \____/
        #     You got a job at the Zoominous Zoo!
        #     -----------------------------------
        #     You have a few options:
        #     You can collect your signing bonus (sb)
           
        #     '''
        #     user=input(zoo)
        #     if user =="sb":
        #         signB50()
        #         print('''
        #         -Scoop poop (sp)
        #         -Feed the animals (fa)
        #         -Repair habitats (rh)
        #         ''')
        
            

        # elif user =="cw":
        #     work='''
        #         /'~~~~~~~\|/
        #       ,/'     ____ `\
        #       |             |
        #       |-(  .)-(.  )`|,'
        #      (|  ~~~   ~~~   |)
        #       |     `-'      |'
        #        \   ,____,   /
        #         \   `--'   /
        #          |\______/|
        #         |\________/|
        #         \----------/


        #     You got a job at Rick's Construction!
        #     ---------------------------------------
        #     You have a few options:
        #     You can collect your signing bonus (sb)
            
            
            
            
        #     '''
        #     user=input(work)
        #     if user =="sb":
        #         signB50()
        #         print('''
        #         Build a house (bh)
        #         Jackhammer concrete (jc)
        #         Hand out safety glasses (sg)
        #         ''')
                



        # elif user =="rd":
        #     race='''
        #                                  _.-="_-         _
        #                             _.-="   _-          | ||"""""""---._______     __..
        #                 ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
        #         __.--""     __        ,'                   o \           __        [__|
        #     __-""=======.--""  ""--.=================================.--""  ""--.=======:
        #     ]       [w] : /        \ : |========================|    : /        \ :  [w] :
        #     V___________:|          |: |========================|    :|          |:   _-"
        #     V__________: \        / :_|=======================/_____: \        / :__-"
        #     -----------'  "-____-"  `-------------------------------'  "-____-"
        #     You got a job at NASCAR!
        #     ---------------------------------------
        #     You have a few options:
        #     You can collect your signing bonus (sb)
            
           
            
            
        #     '''
        #     user=input(race)
        #     if user =="sb":
        #         signB50()
            
            
        #     print('''
        #     Practice around the track (p)
        #     Put new tires on (pt)
        #     Add more NOS (n)
        #     ''')
           


        # elif user =="continue":
        #     screen2='''
        #                                                         ___
        #                                                 ___..--'  .`.
        #                                         ___...--'     -  .` `.`.
        #                             ___...--' _      -  _   .` -   `.`.
        #                     ___...--'  -       _   -       .`  `. - _ `.`.
        #             __..--'_______________ -         _  .`  _   `.   - `.`.
        #             .`    _ /\    -        .`      _     .`__________`. _  -`.`.
        #         .` -   _ /  \_     -   .`  _         .` |Career Fair|`.   - `.`.
        #       .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
        #     .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
        #         |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
        #         | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
        #         |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
        #         |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
        #      ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
        #      -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
        #     `--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
        #     _____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
        #     ----------`--._          ''      ``--.._|:::::::::::::::::::::::|
        #     `--._ _________`--._'        --     .   ''-----.................'
        #         `--._----------`--._.  _           -- . :''           -    ''
        #             `--._ _________`--._ :'              -- . :''      -- . ''
        #     -- . ''       `--._ ---------`--._   -- . :''
        #             :'        `--._ _________`--._:'  -- . ''      -- . ''
        #     -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
        #                                 `--._ _________`--._
        #     -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
        #             -- . ''       -- . ''         `--._ _________`--._   -- . ''
        #     :'                 -- . ''          -- . ''  `--._----------`--._
        #     You then find a back area that is getting no attention...
        #     and there just so happens to be some prestigous companies populated here!
        #     You go and praise yourself to them and they are impressed!
        #     --------------------------------------------------
        #     Your current offers that are in
        #     Software Developer (sd)
        #     Lawyer (l)
        #     Doctor (d)
        #     ---------------------------
        #     type (back) to go back to other job offers
        #     --------------------------------------------------
        #     Type the letters in parenthesis to choose that job


        # '''
        #     user=input(screen2) 
        # if user =="sd":
        #     software='''
        #                     .----.
        #         .---------. | == |
        #         |.-"""""-.| |----|
        #         ||       || | == |
        #         ||       || |----|
        #         |'-.....-'| |::::|
        #         `"")---(""` |___.|
        #         /:::::::::::\" _  "
        #         /:::=======:::\`\`\
        #        `"""""""""""""`  '-'
        #     You got a job at Lionstrong Electronic & Stuff!
        #     ---------------------------------------
        #     You have a few options:
        #     You can collect your signing bonus (sb)
        #     You can start working (w)
           
        #     '''
        #     if user =="sb":
        #         signB200()
        #     print('''
        #          You're now at work you have mutliple tasks to be done!
        #         -code games (cg)
        #         -Build new company app (ba)
        #         ''')
                
        

