
# The first step is still outlining input.
# input: you make the decision - so, in CAPTITAL letter only 

# Term used in comments/code
# BE: bad ending
# GE: good ending
# PC: player character
# PL: player
# plot: game plot

import time

pcInfo = {}
actionSeq = [] # record the sequence of action taken
# TODO: if pl want to redo this choice, just delete the last one in actionSeq and run the game instead.
# I think this is better than using function call(call the previous function) to redo, as it makes it easier to expand the game

# Time system 
daysPast = 0
# daysPast = 0.4 # The game starts at around 10am in the morning. 
# x.25 - 6am, x.5 - 12pm, x.75 - 6pm, x.00 - 12am; 
# 0.1 - 2.4h


# --- 基本功能组件 ---
# basic functions
def msgIllegalEnter(count=0, optList=''):
    '''
    used as following:
    while action not in validEnterList: 
        action = msgIllegalEnter() # illegal enter, try again

    When not given count&optList, this function act as the previous version, namely:
        show error message regardless of count of illegal enters.

    TODO: 
    1. refactor this function into reEnterIfInputNotValid(validEnterList)
    2. rename msgSoManyIllegalEnters() into msgIllegalEnter()
    '''
    msgSoManyIllegalEnters(count, optList)
    action = input("")
    return action

def choiceSaver(action):
    '''save user's choice sequence
    input: a newly-taken action(str)
    output: None
    '''
    global actionSeq
    actionSeq.append(action)

def ifRestrat():
    ''' At the end of a game, ask player if they would start a new adventure
    input: None
    output: one of "Y" or "N"
    '''
    print("\n\n\nHere we reached the end of our adventure.")
    action = input("Do you want to start a new game?(YES/NO)")
    while action not in ["YES", "NO"]: action = msgIllegalEnter()
    return action


# --- 扩展功能组件 ---
# time
def currentTime():
    ''' tell current period of day given daysPast
    input: None - but use global daysPast(int)
    output: dayPeriod(str)
    '''
    daytime = daysPast % 1
    if daytime<0.25:
        dayPeriod = 'dawn'
    elif daytime<0.45:
        dayPeriod = 'morning'
    elif daytime<0.55:
        dayPeriod = 'noon'
    elif daytime<0.70:
        dayPeriod = 'afternoon' 
    elif daytime<0.80:
        dayPeriod = 'dawn'
    else:
        dayPeriod = 'night'
    return dayPeriod


# --- 角色设定 ---
# get Player Character information
def getPCDefault():
    pcInfo['name'] = "Mia"
    pcInfo['age'] = "20"
    pcInfo['story'] = "A math major student. Nothing special.\nNobody even the author knows why this guy would be on a deserted island."  

def getPCNew():
    print("Okay. So why don't you tell me something about you")

    pcInfo['name'] = input(" - what's your name?").strip()
    if pcInfo['name'] == None: 
        action = input("Continue without giving a name?(Y/N)")
        while action not in ['Y','N']: action = input("Continue without giving a name?(Y/N)")
        if action == 'Y': pcInfo['name'] = input("You can type the name of your character here: ")
        # 如果action == 'N', 什么都不做 - 让pcInfo['name']取值保持None

    pcInfo['age'] = int(input(" - age? "))
    if pcInfo['age'] > 100 : print("wow, fantastic!")

    pcInfo['story'] = "" # 处理：如果之前的pc有小传，而新pc没有小传
    pcInfo['story'] = input("and if you like, a short story about you?\n")

def getPCInfo():  
    if pcInfo:
        print("Would you use the same character as you made up in PREVIOUS adventure, make up a NEW one, or use the DEFAULT character?")
        action = input("").strip()
        while action not in ["PREVIOUS", "DEFAULT", "OWN"]: action = msgIllegalEnter()
    else:
        print("Would you use the DEFAULT character, or make up your OWN?")
        action = input("").strip()
        while action not in ["DEFAULT", "OWN"]: action = msgIllegalEnter()

    if action == "DEFAULT": getPCDefault()
    elif action == "OWN": getPCNew()  

    print("\n\n\n")
    print(f"So, here'r your character:\nName: {pcInfo['name']}\nAge: {pcInfo['age']}\n\n{pcInfo['story']}")


# --- 章节 ---
def introPlot():
    plot = "You are on a deserted island in a 2D world.\n"
    plot += "Try to survive until rescue arrives!\n"
    plot += "Available commands are in CAPITAL letters.\n"
    plot += "Any other command exits the program\n"
    print(plot)

def plotBegining():
    ''' Tutorial plot, no brach selection in this plot
    input = None
    output = None
    '''
    global daysPast # UnboundLocalError: local variable 'daysPast' referenced before assignment
    print("\n\n\n")
    prompt = "Now, first LOOK around...\n"
    action = input(prompt)
    # TODO：可以使用dictionary+exception实现switch。见，https://www.jianshu.com/p/e4d3cb75e532
    countIllegalEnter = 0
    while action not in ["LOOK"]: countIllegalEnter+=1; action = msgIllegalEnter(countIllegalEnter, ["LOOK"])
    choiceSaver(action)
    daysPast += 0

def plotSandDitch():
    '''
    input = None
    output = either one of "LEFT" or "RIGHT"
    '''
    global daysPast
    print("\n\n\n")
    plot = "You are stuck in a sand ditch."
    print(plot)
    prompt = "Crawl out LEFT or RIGHT.\n"
    action = input(prompt).strip()
    while action not in ["LEFT", "RIGHT"]: action = msgIllegalEnter() # illegal enter, try again
    choiceSaver(action)
    daysPast += 0.2 
    return action

def plotHunger():
    global daysPast
    print("\n\n\n")
    print(f"It's {currentTime()}, and you're hungry!")
    print("You look around, and see a STARFISH and a CRAB on the sand.")
    prompt = "Which do you eat?\n"
    action = input(prompt).strip()
    while action not in ["STARFISH", "CRAB"]: action = msgIllegalEnter() 
    choiceSaver(action)
    daysPast += 0.05
    return action

def plotReconsider():
    global daysPast
    print("\n\n\n")
    prompt = "Raw crab should be fine, right? YES or NO.\n"
    action = input(prompt).strip()
    while action not in ["YES", "NO"]: action = msgIllegalEnter()
    choiceSaver(action)
    daysPast += 0
    return action

def plotFindTree():
    global daysPast
    print("\n\n\n")
    print("Ok, You eat it raw. Fingers crossed.")
    prompt = "Food in your belly helps you see a TREE.\n"
    action = input(prompt).strip()
    while action not in ["TREE"]: action = msgIllegalEnter() 
    choiceSaver(action)
    daysPast += 0.2
    return action

def plotCoconut():
    global daysPast
    print("\n\n\n")
    print("It's a coconut tree! And you're thirsty!")
    prompt = "Do you drink the coconut water? YES OR NO.\n"
    action = input(prompt).strip()
    while action not in ["YES", "NO"]: action = msgIllegalEnter()
    choiceSaver(action)
    daysPast += 0.05
    return action


# --- 选项回音 --- / feedback / comment %%% - which word to use?
# messages as a respondence to choice
def msgNotCoconut():
    print("Good choice.")


def msgSoManyIllegalEnters(count, optList):
    '''Print something (doesn't accumulate through different section)
    input: 
    count[int] - count of illegal enters in a single dialog
    optList[list of str] - a list of all options available
    '''
    # TODO: could that be caused by some hidden bugs in program? 
    # - Perhaps I should add a "report a bug" choice in this function

    optStr = ""
    if len(optList) == 1: optStr = 'a ' + optList[0]
    elif len(optList) == 2: optStr = f'a {optList[0]} or a {optList[1]}'
    elif len(optList) > 2: optStr = 'one of ' + ', '.join(optList)

    msg = "You can only do actions shown in capital letters.\n"
    msg += "Try again:"

    if count < 4: 
        #pass
        # test TBC
        print("*Sigh*",end='')
        time.sleep(1)
        print(f"Alright, {pcInfo['name']}, type whatever you want.")
        time.sleep(0.3)
        print("I won't say anything from now on.")
        msg = ""

    elif count == 4:
        msg = "Okay, I get it. You don't like following rules.\n"
        msg += "That's why you're on this adventure!\n"
        msg += f"But I'm going to need {optStr} to go forward anyway."

    elif count == 6:
        msg = f"Please, you're giving me a headache. {optStr} only."

    elif count == 10: 
        # test TBC
        print("*Sigh*",end='')
        time.sleep(1)
        print(f"Alright, {pcInfo['name']}, type whatever you want.")
        time.sleep(0.3)
        print("I won't say anything from now on.")
        msg = ""

    elif count > 10:
        msg = "Illegal enter. Try again:"
    
    print(msg)


# --- 结局 ---
# input = None, output = None
def endShip():
    '''
    input = None
    output = None
    '''
    print("\n\n\n")
    print("You make it out and see a ship!")
    print("You survived!")

def endCave():
    print("\n\n\n")
    print("No can do. That side is very slippery.")
    print("You fall very far into some weird cavern.")
    print("You do not survive :(")

def endStarfish():
    print("\n\n\n")
    print("Oh no! You immediately don't feel well.")
    print("You do not survive :(")

def endHunger():
    print("\n\n\n")
    print("Well, there's nothing else left to eat.")
    print("You do not survive :(")

def endCrabAndCoconut():
    print("\n\n\n")
    print("Oh boy. Coconut water and raw crab don't mix.")
    print("You do not survive :(")

def endRescurePlane():
    print("\n\n\n")
    print("Look! It's a rescue plane! You made it! \\o/")


# --- 主要游戏逻辑 ---
# main game
def game():
    '''
    input: None
    output: None
    have multiple early returns to reduce #(nested loops)
    '''
    print("\n\n\n")
    # Introduction, tutorial, character made-up
    introPlot()
    getPCInfo()
    plotBegining() # Tutorial plot, no brach selection in this plot

    # Plots
    action = plotSandDitch() 
    if action == "RIGHT": return endCave() # remember endCave() returns nothing
    # action == "LEFT": 
    action = plotHunger()
    if action == "STARFISH": return endStarfish()
    # action == "CRAB"
    action = plotReconsider()
    if action == "NO": return endHunger()
    # action == "YES"
    plotFindTree() # no branch in this section
    action = plotCoconut()
    if action == "YES": return endCrabAndCoconut()
    # action == "NO"
    msgNotCoconut()
    endRescurePlane()


# TODO: 给定actionSeq，自动执行这一串action
# --- 平行世界 ---
def AUTraveller(artificailActionSeq):
    pass


# --- 主函数 ---
while(1):
    game()
    print(f"\nActions {pcInfo['name']} took in this adventure: {actionSeq}")
    if ifRestrat() == 'NO': exit()







