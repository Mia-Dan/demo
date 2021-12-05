
'''Run Test Cases
Input: your function object, test cases'''

# build a runTestCases function. To test: 
# 1. function with 1, 2, 3, ... variables; ✅
# 2. function with default keys [Mark pp.535] ✅

# TODO: use assert

testCases = []

# Your Test Cases Goes Here


# def fun1(a):
#     ''' Function receiving one specific argument only '''
#     print("One arg. Print it:",a)
#     return a*2
# argType = 'one'
# testCases.append(0) # trival case
# testCases.append(1)

def fun2(a=9, b=10):
    ''' Function receiving several arguments, with default value '''
    print(f"Two arg, one default value. Print it: {a}, {b},")
    print("and add them...")
    return a+b
# argType = 'several'
# testCases.append(())
# testCases.append((0,))
# testCases.append((1,2))

argType = 'key'
testCases.append({})
testCases.append({'a':0})
testCases.append({'a':1, 'b':2})


fun = fun2 # Your Function Object Goes Here
if argType == 'one':
    for testCase in testCases:
        print(f"Case: {testCase}")
        print(f"result: {fun(testCase)}\n")
elif argType == 'several':
    for testCase in testCases:
        print(f"Case: ",end=''); print(*testCase)
        print(f"result: {fun(*testCase)}\n")
elif argType == 'key':
    for testCase in testCases:
        print(f"Case: ",end=''); print(testCase)
        # print(type(**testCase)) #TypeError: type() takes 1 or 3 arguments
        # print(**testCase) #TypeError: 'a' is an invalid keyword argument for print()
        print(f"result: {fun(**testCase)}\n")

        