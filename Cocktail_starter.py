# requests and xmltodict packages are not native, you migh want to install them
# in your terminal "pip install requests xmltodict"
# if using anaconda "conda install requests xmltodict"

import requests, xmltodict, pickle, os, random, re
from nltk.corpus import cmudict
arpabet = cmudict.dict()
from nltk.metrics import edit_distance

def category(category):
    """""
        YOU DON'T NEED TO CHANGE THIS FUNCTION, ONLY USE IT!!!
        This function mines the thesaurus rex for a list of words related to a chosen category.
        Note that it saves a cache of the list to avoid downloading all the time.
    """""
    file_path = "./"+category+".pkl"
    if os.path.isfile(file_path): # load stored results
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    url = "http://ngrams.ucd.ie/therex3/common-nouns/head.action?head="+category+"&xml=true"
    response = requests.get(url)
    result = xmltodict.parse(response.content)
    _root_content = result['HeadData']
    print(_root_content)
    result_dict = dict(map(lambda r: tuple([r['#text'].replace('_', '').strip(), int(r['@weight'])]),
                         _root_content['Members']['Member']))
    result_list = list(result_dict.keys())

    with open(file_path, 'wb') as f:  # store the results locally (as a cache)
        pickle.dump(result_list, f, pickle.HIGHEST_PROTOCOL)

    return result_list


def pronounce(word):
    """""
        YOU DON'T NEED TO CHANGE THIS FUNCTION, ONLY USE IT!!!
        This function looks into the cmu dictionnary to translate a word into its phonetic spelling.
        Input a string, outputs a list of phonemes
    """""
    return arpabet[word.lower()][0] if word.lower() in arpabet else None # make sure the word is lowercased and exists in the dictionary


def pun(string,cat):
    """""
        THIS IS THE FUNCTION YOU HAVE TO WRITE
        It takes an expression and a category as input,
        Chooses a word in the expression,
        Find a word related to the category that sounds similar,
        replace the word chosen by this similar sounding word,
        to build a new expression
    """""

    string = re.sub(r'[^\w\s]','',string.lower())
    str_split = string.split()
    # 
    

    #second, load the category
    our_cat = category(cat)
    #careful, not all words are in the spelling dictionnary, make sure to only keep those that are
    our_cat = [c for c in our_cat if c in arpabet.keys()]
    str_filter = [w for w in str_split if w in arpabet.keys()]    
    #third, translate the list of words into a list of their phonetic representation
    cat_pron = [pronounce(c) for c in our_cat]
    str_pron = [pronounce(w) for w in str_filter]

    # Finding a target index (word)          
    idx = random.randint(0,len(str_pron))
    random_word = str_pron[idx]
    #fourth, create a list of distances (use the edit_distance function from nltk)
    dists = [edit_distance(cat, random_word) for cat in cat_pron]

    #fifth, create a list of words with the minimum distance from the target word
    min_dist_words = [our_cat[idx] for idx, d in enumerate(dists) if d == min(dists)]
    #sixth, choose a substitute in the list created above
    sub = random.choice(min_dist_words)

    #seventh, replace the target word with its substitute
    str_split[idx] = sub
    #rebuild a string out of the list
    remade_string = ' '.join(str_split)
    
    return(remade_string)


sentence = input("enter any kind of idioma:")
print(pun(sentence,"drink"))