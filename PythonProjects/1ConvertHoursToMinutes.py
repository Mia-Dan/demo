# 
# input: minutes_to_convert
# output: hours_part, minutes_part
# * all are positive integer

# test cases: 
# input: 0, output: 0, 0. 
# input: 42, output: 0, 42.
# input: 61, output: 1, 1.

minutes_to_convert = int(input("input minutes: ")) 
hours_part = int(minutes_to_convert / 60) # take floor of division
minutes_part = minutes_to_convert % 60 # take mod, which gives minutes remaining
print("Hours\n", hours_part, "\nMinutes\n", minutes_part)