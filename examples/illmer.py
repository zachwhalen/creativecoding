import pronouncing
import pycorpora
import random

def get_words(pos):

    
    if (pos is "nouns"):
        all_words = pycorpora.words.nouns["nouns"]
    elif (pos is "verbs"):
        all_words = [w["present"] for w in pycorpora.words.verbs["verbs"]]
 
    keepers = []
    for n in all_words:
        pl = pronouncing.phones_for_word(n)
        if (len(pl) > 0):      
            sc = pronouncing.syllable_count(pl[0])
            if (sc == 1):
                keepers.append(n)
            
    return keepers

def get_pairs():
    
    verbs = get_words("verbs")
    nouns = get_words("nouns")

    pairs = []
    
    for n in nouns:
        for v in verbs:
            #print("comparing " + f,p)
            if (v in pronouncing.rhymes(n)):
                pairs.append( (v,n) )
                
    
    return pairs

def an(word):
    if (word[0] in ["a","e","i","o","u"]):
        return "an " + word
    else:
        return "a " + word
    
    

template = """
    I think that I shall never {0}
    a poem as lovely as {1}
"""

pair = random.choice(get_pairs())

poem = template.format(
    pair[0],
    an(pair[1])
)

print(poem)
