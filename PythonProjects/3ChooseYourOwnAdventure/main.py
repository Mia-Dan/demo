# 20211129 正在将不同功能区分不同py文件
# 理由是，多个文件方便找到需要的函数，滑动条的拖动也容易操作；避免长距离scrolling。
# 此外，函数间的独立性更分明，因而也更易测试。

import basicSupport
import timeSystem
# Term used in comments/code
# BE: bad ending
# GE: good ending
# PC: player character
# PL: player
# plot: game plot

import time

pcInfo = {} # dictionary
actionSeq = [] # record the sequence of action taken
# TODO: change into dict to allow for randomn event 
# TODO: if pl want to redo this choice, just delete the last one in actionSeq and run the game instead.
# I think this is better than using function call(call the previous function) to redo, as it makes it easier to expand the game


# --- 基本功能组件 - 存档 ---
# basic functions - dataFile

# TODO
def save():
    '''save current process'''
    pass


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
    ifQuit(action) # BUG: NOT CALLED
    if ifQuit(action): return
    elif action == "RIGHT": return endCave() # remember endCave() returns nothing
    # action == "LEFT": 
    action = plotHunger()
    if ifQuit(action): return
    elif action == "STARFISH": return endStarfish()
    # action == "CRAB"
    action = plotReconsider()
    if ifQuit(action): return
    elif action == "NO": return endHunger()
    # action == "YES"
    plotFindTree() # no branch in this section
    action = plotCoconut()
    if ifQuit(action): return
    elif action == "YES": return endCrabAndCoconut()
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







