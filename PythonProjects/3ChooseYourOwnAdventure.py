
# The first step is still outlining input.
# input: you make the decision - so, in CAPTITAL letter only 

# Term used in comments/code
# BE: bad ending
# GE: good ending
# PC: player character
# PL: player
# plot: game plot

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
def msgIllegalEnter():
    '''
    used as following:
    while action not in validEnterList: 
        action = msgIllegalEnter() # illegal enter, try again
    TODO: refactor this function into reEnterIfInputNotValid(validEnterList)
    '''
    print("You can only do actions shown in capital letters.")
    print("Try again!")
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
    prompt = "\n\n\nNow, first LOOK around...\n"
    action = input(prompt)
    # TODO：可以使用dictionary+exception实现switch。见，https://www.jianshu.com/p/e4d3cb75e532
    while action not in ["LOOK"]: action = msgIllegalEnter()
    choiceSaver(action)
    daysPast += 0

def plotSandDitch():
    '''
    input = None
    output = either one of "LEFT" or "RIGHT"
    '''
    global daysPast
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
    print(f"It's {currentTime()}, and you're hungry!")
    print("You look around, and see a STARFISH and a CRAB on the sand.")
    prompt = "Which do you eat?"
    action = input(prompt).strip()
    while action not in ["STARFISH", "CRAB"]: action = msgIllegalEnter() 
    choiceSaver(action)
    daysPast += 0.05
    return action

def plotReconsider():
    global daysPast
    prompt = "Raw crab should be fine, right? YES or NO."
    action = input(prompt).strip()
    while action not in ["YES", "NO"]: action = msgIllegalEnter()
    choiceSaver(action)
    daysPast += 0
    return action

def plotFindTree():
    global daysPast
    print("Ok, You eat it raw. Fingers crossed.")
    prompt = "Food in your belly helps you see a TREE."
    action = input(prompt).strip()
    while action not in ["TREE"]: action = msgIllegalEnter() 
    choiceSaver(action)
    daysPast += 0.2
    return action

def plotCoconut():
    global daysPast
    print("It's a coconut tree! And you're thirsty!")
    prompt = "Do you drink the coconut water? YES OR NO."
    action = input(prompt).strip()
    while action not in ["YES", "NO"]: action = msgIllegalEnter()
    choiceSaver(action)
    daysPast += 0.05
    return action


# --- 选项回音 ---
# messages as a respondence to choice
def msgNotCoconut():
    print("Good choice.")


# --- 结局 ---
def endShip():
    '''
    input = None
    output = either one of "LEFT" or "RIGHT"
    '''
    print("\n\n\nYou make it out and see a ship!")
    print("You survived!")

def endCave():
    print("\n\n\nNo can do. That side is very slippery.")
    print("You fall very far into some weird cavern.")
    print("You do not survive :(")

def endStarfish():
    print("Oh no! You immediately don't feel well.")
    print("You do not survive :(")

def endHunger():
    print("Well, there's nothing else left to eat.")
    print("You do not survive :(")

def endCrabAndCoconut():
    print("Oh boy. Coconut water and raw crab don't mix.")
    print("You do not survive :(")

def endRescurePlane():
    print("Look! It's a rescue plane! You made it! \o/")


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
    if action == "RIGHT": 
        endCave() # return
        return
    # action == "LEFT": 
    action = plotHunger()
    if action == "STARFISH":
        endStarfish()
        return
    # action == "CRAB"
    action = plotReconsider()
    if action == "NO":
        endHunger()
        return
    # action == "YES"
    plotFindTree() # no branch in this section
    action = plotCoconut()
    if action == "YES":
        endCrabAndCoconut()
        return
    # action == "NO"
    plotNotCoconut()
    endRescurePlane()

# --- 主函数 ---
while(1):
    game()
    print(actionSeq)
    if ifRestrat() == 'NO': exit()







