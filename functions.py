import numpy as np
import pandas as pd

def readData(infilePathAndName):
    """
    Takes in the preprocessed/precleaned wordset that I wrote and returns a list of lists
    containing the words tokenized into sentences (lists) and words (elements of lists)
    
    
    """
    
    with open(infilePathAndName, "r") as f:
        string = f.read()
        ls1 = string.split("\n")
        finalLs = []
        for index, string in enumerate(ls1):
            subLs = string.split(" ")
            finalLs.append(subLs)
            
    return(finalLs)
    
def uniqueArr(lsOfAllWords):
    
    uniqueTokens, uniqueFirstOccurance, uniqueTokenCounts = np.unique(lsOfAllWords, return_index=True, return_counts=True) # how many unique words did I use in the writing of 
    # this book? what were the counts?
    uniqueArr = np.asarray((uniqueTokens,uniqueFirstOccurance,uniqueTokenCounts)).T # turns tuple into ndarray then .T transposes it over its axis
    
    return(uniqueArr)

def uniqueDf(uniqueArr):
    unique = pd.DataFrame(uniqueArr, columns=['token', 'indexFirstTokenOccur','frequency']) # convert to dataframe for easier wrangling
    unique.frequency = unique.frequency.astype(int) # before this line was added, the count/frequency had at some point been converted to a string and so
    # the sort values function was sorting it based upon the first value in a string (e.g. 1 comes before 9, so 1203 is smaller tahn 99)
    unique = unique.sort_values(by='frequency', ascending = False)
    #pring the head
    
    return(unique)

def codeToWord(code, transTable, codeColumn = "type", wordColumn = "word"):
    row = transTable[transTable[codeColumn] == code]
    ser = row[wordColumn]
    word = (ser.values)[0]
    return(word)

def getPointers(quantity, rangeCap, seed = 120):
    random.seed(seed)
    pointers = []
    
    for i in range(quantity):
        ptr = random.randint(0, rangeCap)
        pointers.append(ptr)
        
    return(pointers)

def getWordsFromPtrs(lsOfPtrs, numWords):
    sets = []
    
    for index,ptr in enumerate(lsOfPtrs):
        cap = ptr + numWords
        cap = ptr + length # cap is the top index in DataFrame[ptr:cap]
        tempDf = topThreeWords[ptr:cap]
        sets.append(tempDf)
        filePath = "randomSamples/randomSet" + str(index) + ".csv"
        tempDf.to_csv(filePath)
       
    return(sets)