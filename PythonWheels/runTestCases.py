
# build a runTestCases function. To test: 
# 1. function with 1, 2, 3, ... variables; ✅
# 2. function with default keys [Mark pp.535] ✅

# TODO: use assert

def runTestCases(fun, testCases, argType='several'):
    '''Run Test Cases. Print, but no return.

    fun: your function object
    testCases: test cases
    argType: format of your testCases. List as below: 
        'one': testCases is a list of args, 
            use when function-to-test has only one arg.
        'several': a list of tuples of args,
            use when function-to-test may have several args.
            Default behavior tests are also allowed.
            Call it by postional arg.
        'key': a list of dicts of args, 
            Default behavior tests are also allowed.
            Call it by postional arg.
    '''
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


# Your Test Cases Goes Here


def fun1(a):
    ''' Function receiving one specific argument only '''
    print("One arg. Print it:",a)
    return a*2

def fun2(a=9, b=10):
    ''' Function receiving several arguments, with default value '''
    print(f"Two arg, two default value. Print it: {a}, {b},")
    print("and add them...")
    return a+b

# argType = 'one'
# fun = fun1
testCases = []
testCases.append(0) # trival case
testCases.append(1)

# argType = 'several'
# fun = fun2
testCases2 = []
testCases2.append(())
testCases2.append((0,))
testCases2.append((1,2))

# argType = 'key'
# fun = fun2
testCases3 = []
testCases3.append({})
testCases3.append({'a':0})
testCases3.append({'a':1, 'b':2})

runTestCases(fun=fun1, testCases=testCases, argType='one')
runTestCases(fun=fun2, testCases=testCases2, argType='several')
runTestCases(fun=fun2, testCases=testCases3, argType='key')
