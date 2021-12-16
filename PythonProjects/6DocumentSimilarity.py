from string import punctuation # string: A collection of string constants.
# TODO: fun rateSimilarity(l1,l2)

def readText(filename):
    ''' 
    filepath(str): file path
    Returns:
        content(str): it contains content of the given file.
    '''
    with open(filename) as f:
        content = f.read()
    return content

def seperateWords(text):
    '''Seperate a str into words.
    text(str): * '\n' is allowed
    Returns:
        words (list of str): a list of words in string, repeatation allowed
    '''
    text = text.replace('\n',' ') # replace '/n' with white space
    for ch in punctuation: text = text.replace(ch, '') # remove punctuation
    words = text.split(' ')
    words = [x for x in words if x] # in case duplicate whitespaces exist in original text
    return words

def countWords(words):
    ''' Count the frequency of each word in words.
    words (list of str)
    Returns:
        wordCount(dict): it maps each word with its frequency in words
    '''
    wordCount = {}
    for word in words:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    return wordCount

def rateSimilarity(dA, dB):
    '''
    Similarity evaluation method used here:  
        1 - total(differences between word counts of the two dicts) / total(word counts of 2 dicts)
    Returns:
        similarity(float): [0, 1]. The higher, more the similar. 
    '''
    dDiff = dA.copy()
    for w in dB:
        if w in dDiff:
            dDiff[w] = abs(dDiff[w] - dB[w])
        else:
            dDiff[w] = dB[w]
    totalDiff = sum(dDiff.values())
    totalSum = sum(dA.values()) + sum(dB.values())
    similarity = 1 - totalDiff / totalSum
    return similarity

filenameA = '6DocumentSimilarity_file/vocabularyA.txt'
filenameB = '6DocumentSimilarity_file/vocabularyD.txt'
textA, textB = readText(filenameA), readText(filenameB)
# print('Text: \n',text,'\n\n\n') #T
wordsA, wordsB = seperateWords(textA), seperateWords(textB)
# print('Seperate: \n',words,'\n\n\n') #T
wordsCountA, wordsCountB = countWords(wordsA), countWords(wordsB)
# print('wordsCount: \n2',wordsCount,'\n\n\n') #T
similarity = rateSimilarity(wordsCountA, wordsCountB)
print(similarity)