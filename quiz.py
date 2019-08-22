import json

with open('quiz.json') as json_file: 
    data = json.load(json_file)    #loads json data file

score=0           
attempted_sport=0  #set attempt sports section to false
attempted_math=0   #set attempt sports section to false

#welcome message is printed using this
def welcome():
    print("Welcome to the quiz!", end="\n\n")
    print("Instruction : \n\n1)For selecting the group please enter the corresponding group no. for ex - '1','2' etc.")
    print("2)For mcqs valid answer's inputs are the corresponding option's name.")
    print("'a','b','c' and 'd' are only valid answer's inputs in mcqs.\n\n")
    

#calculates total score
def totalscore():
    global score
    score+=1

#prints questions of the corresponding group and checks answer
def question(key,val):
    global score
    print("\n",val['question'],"\n",sep="")
    char = "a"
    i = ord(char[0])
    for option in val['options']:
        print(chr(i),")",option,sep="")
        if option==val['answer']: 
            corr=chr(i)  #stores the correct option
        i=i+1
    print('\n')
    while(1):
        ans=input("Enter the correct option : ")
        if ans in ['a','b','c','d']: #checks valid input
            break
        else:
            print("Please enter a valid option\n")
    if ans==corr:
        totalscore()

#for entering into sports quiz section  
def sport():
    global attempted_sport
    attempted_sport=1      #sports group is attempted is set true
    print("\nSports Quiz")
    for key,val in data['quiz']['sport'].items():
        question(key,val)

#for entering into math quiz section        
def maths():
    global attempted_math
    attempted_math=1       #maths group is attempted is set true
    print("\nMaths Quiz")
    for key,val in data['quiz']['maths'].items():
        question(key,val)

#choosing the section
def section():
    print("Select the quiz section\n")
    opt=1
    for i in data['quiz'].keys():
        print(opt,")",i,sep="")
        opt+=1
    while (1):
        sect=input("\nEnter option 1 or 2 : ")
        if sect=="1":
            sport()    #sports section is selected  
            break
        elif sect=="2":
            maths()    #maths section is selected
            break
        else:
            print("Please enter a valid option")

#to attempt another section
def attemptanother():
    if (attempted_math==1) and (attempted_sport==1):
        return            #all the sections are attempted
    else:
        while(1):
            att=input("\nDo you want to attempt another group? [Enter:y/n] : ")
            if att=="y":          #user want to attempt another section
                if (attempted_sport==1):
                    maths()
                elif (attempted_math==1):
                    sport()
                break
            elif att=="n":
                return         #user doesn't want to attempt another section
            else:
                print("Enter valid input")
            
def printscore():
    print("\nYour total score is :", score)  #prints total score  
    
welcome()  
section()
attemptanother()
printscore()   