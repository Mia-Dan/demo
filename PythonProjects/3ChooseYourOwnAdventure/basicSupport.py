
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

def ifQuit(action):
    '''User should be allowed to quit and save the game halfway
    Returns:
        True, if is to quit
        False, if is not to quit
    '''
    print("asd")
    if action == ':q': 
        save()
        print("Will quit...")
        time.sleep(0.1)
        quit()
        return True
    if action == ':qr':
        print("Will quit...")
        time.sleep(0.1)
        quit()
        return True
    return False