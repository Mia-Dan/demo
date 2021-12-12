# --- 角色设定 ---
# get Player Character information


pcInfo = {}


def setPCDefault():
    '''Build a PC for Testing.'''
    pcInfo['name'] = "Mia"
    pcInfo['age'] = "20"
    pcInfo['story'] = "A math major student. Nothing special.\nNobody even the author knows why this guy would be on a deserted island."  


def isAttributeUnlocked(attributeName):
    '''Check if PC has the given attribute.
    Returns (Boolean)
    '''
    if pcInfo.get(attributeName) == None:
        return False
    else:
        return True
# Test Cases: 
# assume: pcInfo = {}, pcInfo = {"name": "Mia"}, setPCDefault()
# test: isAttributeUnlocked("name") ✅


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

