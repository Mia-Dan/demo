# Mac OS Specific.
# Place this file under 'project', on the same level as root files of each task.
# whitespaces in path is currenly not supported.

import os
from dragPathTools import dragFileHere

tasks = ['river','cloud','buildings']
codeDir = os.path.dirname(__file__)

def emptyDir(dirpath):
    if not os.path.isdir(dirpath):
        return f"Not a dir: {dirpath}"
    for filename in os.listdir(dirpath):
        print(filename)
        os.remove(f"{dirpath}/{filename}")
    return f"Done: {dirpath}"

def XXForBoth(names):
    '''str XX reversed as shorthand for both img and label'''
    bothNames = []
    for name in names:
        if 'XX' in name:
            bothNames.append(name.replace('XX', 'img'))
            bothNames.append(name.replace('XX', 'label'))
        else:
            bothNames.append(name)
    return bothNames

def doForAll():   
    op = ''
    while op not in ['mkdir', 'rmdir', 'rename']:
        op = input('Operation? (mkdir rmdir rename)\n')
    '''str XX reversed as shorthand for both img and label'''
    str1 = input('Dirname? (*seperate with whitespace, use XX for both img and label)\n')
    dirnames = (str1.strip()).split(' ')
    dirnames = XXForBoth(dirnames)

    if op == 'rename':
        str2 = input('Rename as? (*in corresponding order with previous)\n')
        renames = (str2.strip()).split(' ')
        renames = XXForBoth(renames)

    for task in tasks:
        for i, dirname in enumerate(dirnames):
            dirpath = f"{codeDir}/{task}/{dirname}" # relative path
            print('processing dirname  ', dirpath)

            if op == 'mkdir':
                os.makedirs(dirpath)

            elif op == 'rmdir':
                if os.path.exists(dirpath):
                    os.rmdir(dirpath)
                else:
                    print(f"Dir {dirpath} does not exist")

            elif op == 'rename':
                if os.path.exists(dirpath):
                    renamepath = f"{codeDir}/{task}/{renames[i]}"
                    os.rename(dirpath, renamepath)
                else:
                    print(f"Dir {dirpath} does not exist")

# print("\n*** MODE: Empty These Dirs ***\n")
# paths = dragFileHere()
# for path in paths:
#     print(emptyDir(path))
# print("All Done")

print("\n*** MODE: File Operation For All in Tasks***\n")
doForAll()
print("All Done")

