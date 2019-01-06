import csv
from structures.poem import poem_type_classifier
from structures.poem_recommender import PoemRecommender


def persist_new_poem(poem_object, poem_file_name):
    with open(poem_file_name, 'a') as poem_file:  # could make __enter__
        writer = csv.writer(poem_file)
        writer.writerow((poem_object.poem, poem_object.rhyming_scheme,
                         poem_object.syllable_scheme,
                         poem_object.no_of_stanzas,
                         poem_object.poem_type))


def _recommend_poem(poem):
    poem = poem_type_classifier(poem)
    recommender = PoemRecommender(poem)
    recommendation = recommender.recommendation()
    persist_new_poem(recommendation, recommender.poem_file_name())
    return recommendation


def recommend_poem_to_user():
    """
    Takes as its input a (correctly formatted!) poem and recommends (from the currently available poems)
    a poem with a similar structure (based off a comparison of rhyming scheme, syllable scheme and stanza structure).
    If the input poem was not already saved in one of the csv files, it will be after executing this function
    (so, theoretically, the more this is used, the better the recommendations should become).

    #TODO: Improve this. Eventually to build a proper UI on website
    """
    poem_string = input('Please enter a poem: ')
    recommendation = _recommend_poem(poem_string)

    if recommendation:
        print('Some info about your poem:\n', recommendation)
        print('\n')
        print('A similar poem you might like:\n', recommendation.poem)
    else:
        # TODO: Handle this better
        print('No recommendation found')
