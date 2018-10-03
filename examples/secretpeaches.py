from textblob import TextBlob
import random
import pycorpora
import pronouncing

# TODO: Figure out how to make some ryhming pairs within my template 

def get_foods():
    keepers = []
    
    food_lists = [
        pycorpora.foods.fruits["fruits"],
        pycorpora.foods.sausages["sausages"],
        pycorpora.foods.vegetables["vegetables"],
        pycorpora.foods.pizzaToppings["pizzaToppings"],
        pycorpora.foods.breads_and_pastries["breads"],
        pycorpora.foods.breads_and_pastries["pastries"],
        pycorpora.foods.beer_styles["beer_styles"],
        pycorpora.foods.bad_beers["bad_beers"],
        pycorpora.foods.tea["teas"],
        pycorpora.foods.apple_cultivars["cultivars"],
        pycorpora.foods.condiments["condiments"],
        pycorpora.foods.iba_cocktails["cocktails"],
        [food["name"] for food in pycorpora.foods.sandwiches["sandwiches"]]
    ]
    
    big_food_list = []
    
    for fl in food_lists:
        big_food_list += fl
    
    for food in big_food_list:
        pronunciation_list = pronouncing.phones_for_word(food)
        if (len(pronunciation_list) > 0):
            syllable_count = pronouncing.syllable_count(pronunciation_list[0])
            if (syllable_count <= 2):
                keepers.append(food)
    
    return keepers

def get_animal():
    keepers = []
    for animal in pycorpora.animals.common["animals"]:
        pronunciation_list = pronouncing.phones_for_word(animal)
        if (len(pronunciation_list) > 0):
            syllable_count = pronouncing.syllable_count(pronunciation_list[0])
            if (syllable_count <= 2):
                keepers.append(animal)
            
    return random.choice(keepers)
    
def get_places():
    keepers = []  
    
    place_lists = [
        [place["city"] for place in pycorpora.geography.us_cities['cities']],
        [place["city"] for place in pycorpora.geography.norwegian_cities['cities']],
        pycorpora.geography.english_towns_cities['towns'],
        pycorpora.geography.english_towns_cities['cities'],
        [river["name"] for river in pycorpora.geography.rivers["rivers"]],
        pycorpora.geography.countries['countries'],
        [place["name"] for place in pycorpora.geography.canadian_municipalities["municipalities"]],
        [place['name'] for place in pycorpora.geography.london_underground_stations['stations']]  
    ]
    
    big_places_list = []
    
    for pl in place_lists:
        big_places_list += pl
    
    for place in big_places_list:
        
        pronunciation_list = pronouncing.phones_for_word(place)   
        
        if (len(pronunciation_list) > 0):
            syllable_count = pronouncing.syllable_count(pronunciation_list[0])
            stresses = pronouncing.stresses(pronunciation_list[0])
            
            
            
            if (syllable_count == 3 and stresses[1] == '1'):
                keepers.append(place)
            elif (syllable_count == 2 and stresses[0] == '1'):
                keepers.append(place)

                    
                    
    return keepers    

def get_pairs():
    # get a pair of 1 place + 1 food that rhyme
    # return these as a tuple
    
    foods = get_foods()
    places = get_places()

    pairs = []
    
    for f in foods:
        for p in places:
            #print("comparing " + f,p)
            if (f in pronouncing.rhymes(p)):
                pairs.append( (p,f) )
                
    
    return pairs

def an(word):
    if (word[0] in ["a","e","i","o","u"]):
        return "an " + word
    else:
        return "a " + word

template = """
    I am a {0}
    I live near {1}.
    If you come visit
    I'll give you {2}.

"""

for s in range(3):
    pair = random.choice(get_pairs())

    arranged = template.format(
        get_animal(),
        pair[0],
        an(pair[1]))

    print(arranged)