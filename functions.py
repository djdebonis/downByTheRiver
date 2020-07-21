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
    
