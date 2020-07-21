from nltk.tokenize import sent_tokenize, regexp_tokenize
import re
from nltk.corpus import stopwords


def openAndRead(infilePathAndName):
    """
    opens a file and returns a long long long string
    
    Parameters
    ----------
    infilePathAndName : str
        `infilePathAndName` is the string containing the filepath to the doc the user would like
        to read in; it is the relative filepath from the current working directory.
        
    Returns
    -------
    string : str
        returns a string with all of the text read in from the .txt document directed by `infilePathAndName`
    
    See Also
    --------
        functions.readData : function tailored to read the specific datasets in this repository
    
    
    """
    with open(infilePathAndName, 'r') as file:
        string = file.read()
        
    return(string)

def fixDashes(string):
    """
    Replaces the incorrect way I used to write em dashes (followed by a space) and replaces it with the 'correct' way.
    
    """
    
    newString = string.replace('-- ', '--')
    
    return(newString)

def fixDashesTwo(string):
    """
    Replaces hyphens with nothing?
    
    """
    
    newString = string.replace('—', '')
    
    return(newString)

def tokenizeToSent(newString):
    """
    Uses nltk sent_tokenize to break up the string into a list of strings, one sentence per string.
    
    See nltk.sent_tokenize
    
    """
    lsOfSent = sent_tokenize(newString)
    
    return(lsOfSent)

def tokenizeToWord(lsOfSent):
    """
    Uses re and nltk to tokenize each string (sentence) in a list into a list of tokens (words).
    
    Parameters
    ----------
    lsOfSent : list of str(s)
        `lsOfSent` is a list of strings, where each string is a sentence (one token of the total doc).
        
    Returns
    -------
    lsOfLsOfToken : list of list(s) of str(s)
        returns a string with all of the text read in from the .txt document directed by `infilePathAndName`
    
    See Also
    --------
        functions.readData : function tailored to read the specific datasets in this repository
    
    """
    
    pattern = r"\w+|\d+" # grabs words and numbers; removes punctuation
    lsOfLsOfToken = [regexp_tokenize(token, pattern) for token in lsOfSent]
    
    return(lsOfLsOfToken)

def cleanAndPreProcessWord(lsOfToken):
    """
    (1) turns all of the tokens in a ls lowercase
    (2) removes all 'stopwords' in a ls leaving the more semantically valuble words
    
    """
    lsOfTokensLow = [token.lower() for token in lsOfLsOfToken]
    lsOfTokensNoStops = [token for token in lsOfTokensLow if token not in stopwords.words('english')]
    
    return(lsOfTokensNoStops)

def cleanAndPreProcessSent(lsOfLsOfToken):
    
    newLsofLs = [cleanAndPreprocessWord(token) for token in lsOfLsOfToken]
    return(newLsofLs)

def removeEmptyData(lsOfTokensNoStops):
    """
    Removes empty lists from a set of lists and returns the new, cleaned out list.
    
    """
    newLs = [x for x in lsOfLs if x != []]
    
    return(newLs)

def writeToFile(newLs):
    """
    write the data to a file so I can upload to github without uploading all of the writing.
    
    """
    for sentIndex, sent in enumerate(newLs):
        for wordIndex, word in enumerate(sent):
            file = open("salientWords.txt", "a")
            file.write(word)
            if wordIndex < (len(sent) - 1):
                file.write(" ")
            else:
                file.write("\n")
            file.close()

def getOriginalSentences(lsOfSent, lsOfPointers, lengthOfSet):
    """
    According to the pointers obtained from running a random sample, create len(lsOfPointers) text documents in a folder sentSamples/
    that store the full sentences.
    
    """
    
    sets = []

    for index, ptr in enumerate(lsofPointers):
        cap = ptr + length # cap is the top index in DataFrame[ptr:cap]
        subSet = lsOfSent[ptr:cap]
        string = "\n".join(subSet)
        print(string)
        print("")
        #sets.append(subSet)
        filePath = "sentSamples/set" + str(index) + ".txt"
    