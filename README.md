# downByTheRiver
brief nlp analysis of all of the writing I did while living in a van (down by the river)

## writing
[salientWords.txt](salientWords.txt) contains cleaned & preprocessed writing that I did in 2017 when I was living in a van & traveling across the country. The document has already been preprocessed to remove punctuation & stop words and convert to lowercase (why? because the writing has never since been revised, and I don't want to share it yet). In the document each sentence of the original piece is separated by a line-break, while each word is separated by a space. This makes it easy to iterate through and split it into a list of lists, where each sub-list is a sentence from the original piece (see the functions I used to open, clean, & preprocess the text, then to export the dataset in [preFunctions.py](preFunctions.py).

The point of this short repo is to explore how much context & semantic value one can retrieve from only the most salient words. When I open [salientWords.txt](salientWords.txt)--which only has the stop-words removed--I can practiacally still follow the narrative. However, my bias (due to me being the person who experienced and wrote all of this) obviously gives me an upper hand. However, a lot can be gained from just the top three words, since often at least ones telling noun and verb is returned for each set, and subject-verb is the nucleus of the English sentence.

My research question then becomes: for each sentence, can you systematically filter out *only the most important/relevant of these words*, and how many of these does it take for an unfamiliar party to get the gist?
