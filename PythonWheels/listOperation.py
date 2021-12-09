

def removeEmptyStrs(strings): 
    '''Remove all empty strs in a list'''
    # Using a list comprehension is the most Pythonic way

    # newStrings = [x for x in strings if x]
    # If the list must be modified in-place, because there are other references which must see the updated data, 
    # then use a slice assignment:
    strings[:] = [x for x in strings if x]
    return

# Test Cases
strings = ["first", "", "second",""]
removeEmptyStrs(strings)
print(strings)