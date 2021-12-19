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

# TODO: format AU names

filepath = "savedrecs.txt"
outputFilepath = "formatted.txt"
targetAttr = ['PT', 'AU', 'TI', 'SO', 'VL', 'IS', 'BP', 'EP', 'PY']
pb = {}
key = ''

def formatPb(pb):
    ''' Format one entry -> GB/T 7714—2005 
    Example: Kanamori H．Shaking without quaking[J]．Science，1998，279(5359)：2063-2064．
    '''
    return f"{pb['AU']}. {pb['TI']}[{pb['PT']}]. {pb['SO']}, {pb['PY']}, {pb['VL']}({pb['IS']}): {pb['BP']}-{pb['EP']}.\n"
                    
with open(outputFilepath,'a') as fOut:
    with open(filepath) as f:
        for line in f:
            if line[0:2] == '  ':
                if key in targetAttr:
                    pb[key] += ' ' + line[3:-1]
            else: 
                key = line[0:2]
                if key in targetAttr:
                    pb[key] = line[3:-1]
                elif key == '\n':
                    ref = formatPb(pb)
                    fOut.write(ref)

        # if line[0:2] == 'TI':
        #     flag = True
        #     content.append(str(i)+'\t'+line[3:])
        #     i += 1
        # if flag == True:
        #     if line[0:2] != 'TI':
        #         flag = False
        #     if line[0:2] == '  ':
        #         content.append(line)
# print(content)

# outputpath = '/Users/admin/Downloads/output.txt'
# with open(outputpath, 'w') as f:
#     f.writelines(content)


