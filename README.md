# downByTheRiver
brief nlp analysis of all of the writing I did while living in a van (down by the river)

## writing
[salientWords.txt](salientWords.txt) contains cleaned & preprocessed writing that I did in 2017 when I was living in a van & traveling across the country. The document has already been preprocessed to remove punctuation & stop words and convert to lowercase (why? because the writing has never since been revised). In the document each sentence of the original piece is separated by a line-break, while each word is separated by a spacee. This makes it easy to iterate through and split it into a list of lists, where each sub-list is a sentence from the original piece (see functions that open the dataset in (functions.py)[functions.py])

The point of this short repo is to explore how much context & semantic value one can retrieve from only the most salient words. Clearly, if you open [salientWords.txt](salientWords.txt)--which only has the stop-words removed--you can practiacally still follow the narrative. My research question then becomes: can you systematically filter out *only the most important of these words*, and how many of these does it take to get the gist?
