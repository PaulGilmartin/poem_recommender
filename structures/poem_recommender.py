import csv
from structures.poem import Poem, poem_type_classifier
import os
import random


CURRENT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'persisted_poem_data'))


class PoemRecommender:
    """
    Given an input string poem, an object of this type can scan available poems (from csv files) and choose
    from these a poem which is similar in structure to the one it was instantiated with
    """
    # this is ugly : improve
    FORM_TO_CVS_FILE = {'HAIKU': CURRENT + '/haiku.csv',
                        'LIMERICK': CURRENT + '/limerick.csv',
                        'TANKA': CURRENT + '/tanka.csv'}

    def __init__(self, poem_object):
        self.poem_object = poem_object

    def poem_file_name(self):
        return self._get_relevant_file_name()

    def recommendation(self):
        """
        """
        matches = self._get_poems_from_relevant_file()
        return self._random_choice(matches)

    def _get_poems_from_relevant_file(self):
        """
        Build and return list of poem objects from relevant file
        """
        with open(self.poem_file_name(), 'r') as poem_file:
            reader = csv.reader(poem_file)
            rows = {self._build_poem_object_from_cvs_row(row) for row in reader}
        return rows

    def _get_relevant_file_name(self):
        """
        :return: The path to the CVS file which contains poems with structures most similar to that of the input poem
        """
        if self.poem_object.poem_type in self.FORM_TO_CVS_FILE:
            return self.FORM_TO_CVS_FILE[self.poem_object.poem_type]
        return CURRENT+'/non_standard_forms.csv'

    def _random_choice(self, poems):
        poem = random.choice(list(poems))
        if self.poem_object.poem == poem.poem:
            # if our input poem already existed in the file and we randomly chose it, choose again
            poem = random.choice(list(poems - {poem}))
        return poem

    @staticmethod
    def _build_poem_object_from_cvs_row(row):
        poem, rhyming_scheme, syllable_scheme, _num_stanzas, poem_type = row
        poem_obj = Poem(poem, rhyming_scheme, syllable_scheme)
        poem_obj.poem_type = poem_type
        return poem_obj
