
# input: name1, name2
# output: nameA, nameB
# * all in the format FIRSTNAME LASTNAME

# Test Cases: 
# input1: Ann Bb, Emma White. 
# output1: ??? not unique. Amma Bhite, Enn Wb. Seems to fit the requirements.
# input2: A Bb, Emma White. 
# output2?: doesn't make sense as A can't be splitted.
# Lets' just switch the first char of the two name.

# input
name1 = input("Enter a name (FIRSTNAME LASTNAME):")
name2 = input("Enter another name (FIRSTNAME LASTNAME):")

# split name into firstname, lastname
firstname1, lastname1 = name1.split(" ", 2)
firstname2, lastname2 = name2.split(" ", 2)

# mesh up
firstnameA = firstname1[0] + firstname2[1:]
firstnameB = firstname2[0] + firstname1[1:]
lastnameA = lastname1[0] + lastname2[1:]
lastnameB = lastname2[0] + lastname1[1:]

# join firstname, lastname into name
nameA = " ".join([firstnameA, lastnameA])
nameB = " ".join([firstnameB, lastnameB])

# output
print(f'New names are: {nameA}, {nameB}')
