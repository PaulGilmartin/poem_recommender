from structures.stanza import Stanza


def poem_type_classifier(poem):
    """
    :param poem: A string poem
    :return: A Poem object. If the type of input poem has an identifiable type (e.g. Haiku) we return an object
    whose type is the corresponding Poem subclass
    """
    identifiable_poem_types = (Haiku, Tanka, Limerick, Poem)
    poem_object = Poem(poem)
    for poem_type in identifiable_poem_types:
        if poem_type.poem_is_of_same_type(poem_object):
            return poem_type(poem)


class Poem:
    """
    Object which, when instantiated with a correctly formatted, english-language poem, can extract, store and present
    certain characteristics of that poem, e.g. the rhyming scheme.

    We model a Poem as a composition of Stanza objects - mimicking the fact that poems are collation of stanzas/verses
    """
    def __init__(self, poem, rhyming_scheme=None, syllable_scheme=None):
        self.poem = poem
        self.stanzas = tuple(Stanza(stanza) for stanza in self.poem.split("\n\n"))
        self.no_of_stanzas = len(self.stanzas)
        self.no_of_lines = sum(stanza.no_of_lines for stanza in self.stanzas)

        self.poem_type = self.__class__.__name__.upper()

        self._rhyming_scheme = rhyming_scheme
        self._syllable_scheme = syllable_scheme

    def __str__(self):
        return 'rhyming_scheme={}, syllable_scheme={}, form={}'.format(self.rhyming_scheme,
                                                                       self.syllable_scheme,
                                                                       self.poem_type)

    def __repr__(self):
        return '{}(poem={}, rhyming_scheme={}, syllable_scheme={})'.format(self.__class__.__name__,
                                                                           self.poem,
                                                                           self.rhyming_scheme,
                                                                           self.syllable_scheme)

    @property
    def rhyming_scheme(self):
        """
        :return: (tup) Tuple of tuples, where each tuple element is the rhyming scheme of a stanza of the underlying
        poem
        """
        if self._rhyming_scheme is None:
            self._rhyming_scheme = tuple(stanza.rhyming_scheme for stanza in self.stanzas)
        return self._rhyming_scheme

    @property
    def syllable_scheme(self):
        """
        :return: Tuple of tuples, where each tuple element is the syllable scheme of a stanza of the underlying
        poem
        """
        if self._syllable_scheme is None:
            self._syllable_scheme = tuple(stanza.syllable_scheme for stanza in self.stanzas)
        return self._syllable_scheme

    @classmethod
    def poem_is_of_same_type(cls, other_poem):
        """
        Does the input poem have the same structure?
        :param other_poem: Poem object
        :return: Default True for unspecified poem. To be overridden in subclasses with specific conditions
        """
        return True


class Haiku(Poem):

    @classmethod
    def poem_is_of_same_type(cls, other_poem):
        """
        We define a Haiku to be a poem with:
         1. No specified rhyming scheme
         2. A syllable scheme ((set(range(2, 9)), set(range(3, 11)), set(range(2, 9)),)
        TODO: add extra condition around juxtaposition and subject related to nature
        """
        same_type = True
        if other_poem.no_of_stanzas == 1 and other_poem.no_of_lines == 3:
            scheme = other_poem.syllable_scheme[0]
            for haiku_syll_range, other_syll_range in zip((set(range(2, 9)), set(range(3, 11)), set(range(2, 9)) ),
                                                           scheme):
                if not haiku_syll_range.intersection(other_syll_range):
                    same_type = False
        else:
            same_type = False
        return same_type


class Tanka(Poem):

    @classmethod
    def poem_is_of_same_type(cls, other_poem):
        """
        We define a Tanka to be a poem with:
         1. No specified rhyming scheme
         2. A syllable scheme (set(range(3, 7)), set(range(5, 9)), set(range(3, 7)), set(range(5, 9)), set(range(5, 9)))
        """
        same_type = True
        if other_poem.no_of_stanzas == 1 and other_poem.no_of_lines == 5:
            scheme = other_poem.syllable_scheme[0]
            for tanka_syll_range, other_syll_range in zip((set(range(3, 7)), set(range(5, 9)), set(range(3, 7)),
                                                           set(range(5, 9)), set(range(5, 9))), scheme):
                if not tanka_syll_range.intersection(other_syll_range):
                    same_type = False
        else:
            same_type = False
        return same_type


class Limerick(Poem):
    """
    We define a Limerick to be a poem with:
     1. ('A', 'A', 'B', 'B', 'A') rhyming scheme
     2. No specified syllable scheme
    """
    @classmethod
    def poem_is_of_same_type(cls, other_poem):
        if other_poem.no_of_stanzas == 1:
            scheme = other_poem.rhyming_scheme[0]
            return scheme == ('A', 'A', 'B', 'B', 'A')
        return False
