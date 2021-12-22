# Bibliography formatting (GB/T 7714—2005)
# Convert bibliography exported from Web of Science -> GB/T 7714—2005 format
# Example: Kanamori H．Shaking without quaking[J]．Science，1998，279(5359)：2063-2064．

''' Reference:
https://images.webofknowledge.com/images/help/WOS/hs_wos_fieldtags.html
https://zhuanlan.zhihu.com/p/355312827
PT      Publication Type (J=Journal; B=Book; S=Series; P=Patent)
AU      Authors
TI      Document Title
SO      Publication Name
VL      Volume(卷)
IS      Issue(期)
PY      Year Published
BP      Beginning Page
EP      Ending Page
'''

# TBC1: format AU names

# # filepath = "savedrecs.txt"
# filepath = "bbb.txt"
# # outputFilepath = "formatted.txt"
# outputFilepath = "aaa2.txt"
# act = 'reorder'
filepath = "formatted.txt"
act = 'wos2gb'
# act = 'deduplicate'
filepath = "aaa.txt"


targetKeys = ['PT', 'AU', 'TI', 'SO', 'VL', 'IS', 'BP', 'EP', 'PY']
pb = {}
key = ''

def formatPb(pb):
    ''' Format one dictionary -> GB/T 7714—2005 bibliography
    Example: Kanamori H．Shaking without quaking[J]．Science，1998，279(5359)：2063-2064．
    '''
    # BUG: reorganize code. test missing -> behavior under different missing
    if 'IS' not in pb:
        return f"{pb['AU']}. {pb['TI']}[{pb['PT']}]. {pb['SO']}, {pb['PY']}, {pb['VL']}: {pb['BP']}-{pb['EP']}.\n"
    else:
        for k in targetKeys:
            if not k in pb:
                print(f"'{pb['TI']}' value missing: {k}")
                pb[k] = ''
                # return "\n"
        return f"{pb['AU']}. {pb['TI']}[{pb['PT']}]. {pb['SO']}, {pb['PY']}, {pb['VL']}({pb['IS']}): {pb['BP']}-{pb['EP']}.\n"
  
def formatValue(key, raw):
    if key == 'AU':
        return formatAU(raw)
    if key == 'TI':
        return formatTI(raw)
    else: 
        return raw

def appendValue(pb, key, valueField):
    if key == 'AU':
        pb[key] += ', ' + formatValue('AU', valueField)
    else:
        pb[key] += ' ' + formatValue(key, valueField)

def formatAU(au):
    ''' Format authors -> GB/T 7714—2005
    Example: J. C. Smith -> Smith J C; Albert(名) Einstein(姓) -> Einstein A; Hiroo Kanamori -> Kanamori H; Liang Fujun
    '''
    # TODO: s(TBC1) 
    # 1. ISSUE: raw names are in different format "Antzaka, A.","Tao, Haicheng", "Ghosh, Kushal Kanti", "Fendt, Matthew William"
    # 2. Chinese name detection.
    #    What about Korean names? 
    au = au.replace('.','')
    [firstName, lastName] = au.split(', ') # really?%%%
    # print(f"## {firstName}")
    firstNames = firstName.split(' ')
    firstNameAb = [name[0] for name in firstNames]
    # print(f"### {firstNameAb}")
    firstNameAb = ' '.join(firstNameAb)
    au = ' '.join([lastName, firstNameAb]) 
    # print(au)
    return au

def formatTI(raw):
    # TODO: Capitalize(Aaa Bbb, not AAA BBB)
    return raw

def clearFileContent(filepath):
    with open(filepath,'w') as fOut:
        fOut.write('')

def refreshOrder(filepath):
    lines = []
    with open(filepath) as f:
        i = 1
        for line in f:
            index = line.find(']')
            line = f"[{i}{line[index:]}"
            print(line)
            lines.append(line)
            i += 1
    clearFileContent(filepath) #?BUG: 没清空成功
    with open(filepath,'a') as fOut:
        fOut.writelines(lines)

def addOrder(filepath):
    lines = []
    with open(filepath) as f:
        i = 1
        for line in f:
            if line != '\n':
                line = f"[{i}]{line}"
                lines.append(line)
                i += 1
    clearFileContent(filepath) #?BUG: 没清空成功
    print(lines)
    with open(filepath,'a') as fOut:
        fOut.writelines(lines)

def deduplicate(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            index = line.find(']')
            line = line[index+1:]
            if line not in lines:
                lines.append(line)
    clearFileContent(filepath) #?BUG: 没清空成功
    with open(filepath,'a') as fOut:
        fOut.writelines(lines)

    clearFileContent(filepath) #?BUG: 没清空成功
    with open(filepath,'a') as fOut:
        fOut.writelines(lines)

if act == 'wos2gb':
    filepath = "savedrecs.txt"
    outputFilepath = "formatted.txt"
    with open(outputFilepath,'a') as fOut:
        with open(filepath) as f:
            for line in f:
                if line == '\n':
                    ref = formatPb(pb)
                    fOut.write(ref)
                    continue

                keyField = line[0:2]
                valueField = line[3:-1]
                if keyField == '  ': # continue last key
                    if key in targetKeys:
                        appendValue(pb, key, valueField)
                else: 
                    key = keyField
                    if key in targetKeys:
                        pb[key] = formatValue(key, valueField)
    addOrder(outputFilepath)

if act == 'reorder':
    refreshOrder(filepath)

if act == 'deduplicate':
    deduplicate(filepath)
    addOrder(filepath)

# with open(outputFilepath,'a') as fOut:
#     with open(filepath) as f:
#         for line in f:
#             i = line.find('DOI')
#             line = line[:i] + '\n'
#             fOut.write(line)


            # fOut.write(line)
            #     continue

            # keyField = line[0:2]
            # valueField = line[3:-1]
            # if keyField == '  ': # continue last key
            #     if key in targetKeys:
            #         appendValue(pb, key, valueField)
            # else: 
            #     key = keyField
            #     if key in targetKeys:
            #         pb[key] = formatValue(key, valueField)
