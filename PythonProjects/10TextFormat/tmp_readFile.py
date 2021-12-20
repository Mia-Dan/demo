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

# TBC: format AU names

filepath = "savedrecs.txt"
outputFilepath = "formatted.txt"
targetKey = ['PT', 'AU', 'TI', 'SO', 'VL', 'IS', 'BP', 'EP', 'PY']
pb = {}
key = ''

def formatPb(pb):
    ''' Format one dictionary -> GB/T 7714—2005 bibliography
    Example: Kanamori H．Shaking without quaking[J]．Science，1998，279(5359)：2063-2064．
    '''
    return f"{pb['AU']}. {pb['TI']}[{pb['PT']}]. {pb['SO']}, {pb['PY']}, {pb['VL']}({pb['IS']}): {pb['BP']}-{pb['EP']}.\n"
  
def formatValue(key, raw):
    '''
    '''
    if key == 'AU':
        return formatAU(raw)
    else: 
        return raw

def appendValue(pb, key, valueField):
    '''
    '''
    if key == 'AU':
        pb[key] += ', ' + formatValue('AU', valueField)
    else:
        pb[key] += ' ' + formatValue(key, valueField)

def formatAU(au):
    ''' Format authors -> GB/T 7714—2005
    Example: J. C. Smith -> Smith J C; Albert Einstein -> Einstein A; Hiroo Kanamori -> Kanamori H; Liang Fujun
    '''
    # au.replace('.', '') #%%%
    # print(au)
    # [lastNames, firstNames] = au.split(', ')
    # firstNames = firstNames.split( )
    # firstName = str(firstNames[-1])
    # print(firstName)
    # upper = []
    # # upper = re.#%%%
    # # upper += re.#%%%
    # return f"#{firstName} {' '.join(upper)}#"

    [lastNames, firstNames] = au.split(', ')
    au = ' '.join([firstNames, lastNames])
    return au

with open(outputFilepath,'a') as fOut:
    with open(filepath) as f:
        for line in f:
            if line == '\n':
                ref = formatPb(pb)
                fOut.write(ref)
                continue

            keyField = line[0:2]; valueField = line[3:-1]
            if keyField == '  ': # continue last line
                if key in targetKey:
                    appendValue(pb, key, valueField)
            else: 
                key = keyField
                if key in targetKey:
                    pb[key] = formatValue(key, valueField)

# outputpath = '/Users/admin/Downloads/output.txt'
# with open(outputpath, 'w') as f:
#     f.writelines(content)


