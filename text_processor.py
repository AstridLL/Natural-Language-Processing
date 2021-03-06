"""
This script contain an example Text class

Each function contains:
An explanation as well as an example
Your job as a studygroup is to make the functions in class 2 and 3.

In class 3 we will then assemble a pipeline using the Text class at the end.


I suggest you start from the top and for each function:
    1) discuss potential solution (e.g. sentence segmentation splitting by ".")
    2) implement the simplest solution first for each function
    3) go back and improve upon the initial function

for class 2 it would be ideal if you have a simple version of the following
functions:
    sentence_segment
    tokenize 
    ner_regex

Additional stuff which you might add is:
    A function for dependency parsing using stanza
    alternatives to each of the function (e.g. using tokenization using nltk)
    Add a function for stemming
    Add plotting functionality for word frequencies
    Add plotting functionality for dependency trees
"""

import re
re.split("\.|\!|\?", "This is an example. Another")

# pointer to the start of sentence
start_ptr = 0
# Array of sentences
sentences = []

for i in range(len(txt)):
    # Identify candidate EOS
    while txt[i] != ".":
        i = i+1
    # Decide on the EOS 
    if txt[i+1] == " " and txt[i+2] == capital letter:
        # segment sentence
        sentences.append(txt.substring(start_ptr, i))
        start_ptr = i+2
        i = i+1
return sentences

# Malthes
# re. split takes out evertyhing you match (you can use a non-capturing group )
# s.strip removes space (use on each sentence)

def sentence_segment(txt):
    for character in txt:
    


        if character == [\.|\?|\!]
            
    """
    if 
    txt (str): Text which you want to be segmented into sentences.

    Example:
    >>> txt = "NLP is very cool. It is also useful"
    >>> sentence_segment(txt)
    ["NLP is very cool", "It is also useful"]
    """
    pass


def tokenize(sentences):
    """
    sentences (list): Sentences which you want to be tokenized

    Example:
    >>> sent = ["NLP is very cool"]
    >>> tokenize(sent)
    [["NLP", "is", "very", "cool"], ["It", "is", "also", "useful"]]
    """
    pass


def n_grams(tokenlist, n):
    """
    tokenlist (list): A list of tokens
    n (int): Indicate the n in n-gram. n=2 denotes bigrams

    creates n-grams from a given tokenlist

    Example:
    >>> tokens = ["NLP", "is", "very", "cool"]
    >>> n_grams(tokens, n=2)
    [["NLP", "is"], ["is", "very"], ["very", "cool"]]
    """
    pass


def ner_regex(tokenlist):
    """
    tokenlist (list): A list of tokens

    peforms named entity recognition using regular expressions
    Example:
    >>> sent = ["Karl Friston is very cool"]
    >>> ner_regex(sent)
    ["Karl Friston"]
    """
    pass


def token_frequencies(tokenlist):
    """
    tokenlist (list): A list of tokens

    return a list of tokens and their frequencies

    Example:
    >>> tokens = [["NLP", "is", "very", "cool"],
                  ["It", "is", "also", "useful"]]
    >>> token_frequencies(sent)
    {"NLP": 1, "is": 2, "very": 1, "cool": 1, "It": 1, "also": 1, "useful": 1}
    """
    pass


def lemmatize_stanza(tokenlist):
    """
    tokenlist (list): A list of tokens

    lemmatize a tokenlist using stanza
    """
    pass


def postag_stanza(tokenlist):
    """
    tokenlist (list): A list of tokens

    add a part-of-speech (POS) tag to each tokenlist using stanza
    """
    pass


class Text():
    def __init__(self, txt):
        self.sentences = sentence_segment()
        self.tokens = tokenize(self.sentences)

    def ner(self, method="regex"):
        res = ner_regex(self.tokens)
        return res

    def get_df(self):
        """
        returns a dataframe containing the columns:
        sentence number, token, lemma, pos-tag, named-entity
        """
        pass