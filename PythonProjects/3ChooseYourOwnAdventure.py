
# The first step is still outlining input.
# input: you make the decision - so, in capital letter only 

plot0 = "You are on a deserted island in a 2D world.\n"
plot0 += "Try to survive until rescue arrives!\n"
plot0 += "Available commands are in CAPITAL letters.\n"
plot0 += "Any other command exits the program\n"
plot0 += "First LOOK around..."
print(plot0)

def msgIllegalEnter():
    print("You can only do actions shown in capital letters.")
    print("Try again!")
    action = input("")
    return action

action = input("")
# TODO：可以使用dictionary+exception实现switch。见，https://www.jianshu.com/p/e4d3cb75e532
while action not in ["LOOK"]:
    action = msgIllegalEnter()
if action == "LOOK":
    plot1 = "You are stuck in a sand ditch.\n"
    plot1 += "Crawl out LEFT or RIGHT."
    print(plot1)
    action = input("")
    while action not in ["LEFT", "RIGHT"]: # illegal enter, try again
        action = msgIllegalEnter()
    if action == "LEFT":
        print("You make it out and see a ship!")
        print("You survived!")
    elif action == "RIGHT":
        print("No can do. That side is very slippery.")
        print("You fall very far into some weird cavern.")
        print("You do not survive :(")