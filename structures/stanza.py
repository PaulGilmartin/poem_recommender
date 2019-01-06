import logging
import pronouncing
import string

ALPHABET = list(string.ascii_uppercase)
REMOVABLE_PUNCTUATION = string.punctuation


class Stanza(object):
    """
    Object which, when instantiated with a correctly formatted, english-language poem stanza, can extract,
    store and present certain characteristics of that stanza, e.g. the rhyming scheme.
    """
    def __init__(self, stanza, rhyming_scheme=None, syllable_scheme=None):
        self._stanza = stanza
        self._lines = self.stanza.split('\n')
        self.no_of_lines = len(self._lines)
        self._rhyming_scheme = rhyming_scheme
        self._syllable_scheme = syllable_scheme

    def __str__(self):
        return 'stanza={}, rhyming_scheme={}, syllable_scheme={}'.format(self.stanza,
                                                                          self.rhyming_scheme,
                                                                          self.syllable_scheme)

    def __repr__(self):
        return '{}(stanza={})'.format(self.__class__.__name__, self.stanza)

    @property
    def stanza(self):
        """
        :return: Normalized stanza string - lower case and punctuation removed
        We separate this as a property since the normalization logic may become
        more cumbersome/complex in later versions, so easier to read than storing
        in the innit
        """
        _trans_table = str.maketrans(dict.fromkeys(REMOVABLE_PUNCTUATION))
        return self._stanza.translate(_trans_table).rstrip().lower()

    @property
    def rhyming_scheme(self):
        """
        :return: (tup) Tuple of capital letter values to represent the rhyming scheme of the poem (e.g. ('A', 'A', 'B')
        """
        if self._rhyming_scheme is None:
            self._rhyming_scheme = self._compute_rhyming_scheme()
        return self._rhyming_scheme

    def _compute_rhyming_scheme(self):
        """
        :return: Tuple of capital letter values to represent the rhyming scheme of the poem (e.g. ('A', 'A', 'B')
        Basic idea is to take the first line and search for all line-ending words which rhyme with that word and group
        them into a rhyming scheme tuple - these are the 'A' words. We then remove all such lines, take the next
        remaining line and repeat the process - this time we compute a list of 'B' words and we insert them into the
        rhyming scheme, with position in scheme defined by the line number of the word. We repeat this process until
        our rhyming scheme tuple has length the same as the no of lines of the poem.
        """
        rhyming_scheme = []
        alphabet_ind = 0
        letter = ALPHABET[alphabet_ind]
        words_and_positions_left = self._line_no_last_word_pairs()
        while words_and_positions_left:
            line_no, last_word_in_line = words_and_positions_left.pop(0)
            rhyming_scheme.insert(line_no, letter)
            rhymes = pronouncing.rhymes(last_word_in_line) + [last_word_in_line]  # allow a word to rhyme with itself
            words_and_positions_left_copy = words_and_positions_left.copy()
            for next_line_num, next_last_word in words_and_positions_left_copy:
                if next_last_word in rhymes:
                    rhyming_scheme.insert(next_line_num, letter)
                    words_and_positions_left.remove((next_line_num, next_last_word))
            alphabet_ind += 1
            letter = ALPHABET[alphabet_ind]
        return tuple(rhyming_scheme)

    def _line_no_last_word_pairs(self):
        """
        :return:  List of tuples of form (line_no, last_word_in_line)
        """
        _line_no_last_word_pairs = []
        for line_no, line in enumerate(self._lines):
            words = line.split()
            last_word = words[-1]
            _line_no_last_word_pairs.append((line_no, last_word))
        return _line_no_last_word_pairs

    @property
    def syllable_scheme(self):
        """
        The syllable scheme of a stanza is defined to be the tuple whose i^th element is the
        total number of syllables in line i
        :return: A tuple of singleton sets, each of which contains an integer which is the count
        of the number of syllables in the line defined by the integer's position in the tuple
        e.g. ({3}, {3}, {2})
        """
        if self._syllable_scheme is None:
            syllable_scheme = []
            for line in self._lines:
                words = line.split()
                line_syllable_count = sum(self._word_syllable_count(word) for word in words)
                syllable_scheme.append({line_syllable_count})
            self._syllable_scheme = tuple(syllable_scheme)
        return self._syllable_scheme

    @staticmethod
    def _word_syllable_count(word):
        """
        :param word: A string
        :return: The number of syllables in the input word. If the input word is not a recognized word
        in our rhyming corpus, we assign a default syllable count of 1
        TODO: Have a better way to handle unrecognised words - better default and also have a way to
        persist them so that they become part of the corpus for later use
        """
        pronunciation_list = pronouncing.phones_for_word(word)
        try:
            return pronouncing.syllable_count(pronunciation_list[0])
        except IndexError:
            logging.log(1, '{} not a recognized word'.format(word))
            return 1


