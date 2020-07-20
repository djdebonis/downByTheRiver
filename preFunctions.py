from nltk.tokenize import sent_tokenize, regexp_tokenize
import re
from nltk.corpus import stopwords


def openAndRead(infilePathAndName):
    """
    opens a file and returns a long long long string
    
    :infilePathAndName: string of the path/path/txtFileName.txt from the current directory
    
    :returns
    
    
    """
    with open(infilePathAndName, 'r') as file:
        string = file.read()
        
    return(string)

def fixDashes(string):
    """
    Replaces the dumb & incorrect way I used to write em dashes (followed by a space) and replaces it with the 'correct' way.
    
    """
    
    newString = string.replace('-- ', '--')
    
    return(newString)

def fixDashesTwo(string):
    """
    Replaces the dumb & incorrect way I used to write em dashes (followed by a space) and replaces it with the 'correct' way.
    
    """
    
    newString = string.replace('—', '')
    
    return(newString)

def tokenizeToSent(newString):
    """
    Uses nltk sent_tokenize to break up the string into a list of strings, one sentence per string.
    
    """
    lsOfSent = sent_tokenize(newString)
    
    return(lsOfSent)

def tokenizeToWord(lsOfSent):
    """
    Uses re and nltk to tokenize each string (sentence) in a list into a list of tokens (words).
    
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

