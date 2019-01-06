from structures.poem import Poem, poem_type_classifier
from unittest import TestCase
from tests.poem_test_config import TEST_HAIKU, TEST_HAIKU_2, TEST_LIMERICK, TEST_NON_STANDARD_FORM


class TestPoem(TestCase):

    def setUp(self):
        self.test_haiku, self.test_haiku_2 = Poem(TEST_HAIKU), Poem(TEST_HAIKU_2)
        self.test_limerick = Poem(TEST_LIMERICK)
        self.test_non_standard = Poem(TEST_NON_STANDARD_FORM)

    def test_no_of_lines(self):
        self.assertEqual(self.test_haiku.no_of_lines, 3)
        self.assertEqual(self.test_limerick.no_of_lines, 5)
        self.assertEqual(self.test_non_standard.no_of_lines, 14)

    def test_no_of_stanzas(self):
        self.assertEqual(self.test_haiku.no_of_stanzas, 1)
        self.assertEqual(self.test_non_standard.no_of_stanzas, 2)

    def test_rhyming_scheme(self):
        self.assertEqual(self.test_haiku.rhyming_scheme, (('A', 'A', 'B'), ))
        self.assertEqual(self.test_haiku_2.rhyming_scheme, (('A', 'B', 'C'), ))
        self.assertEqual(self.test_limerick.rhyming_scheme, (('A', 'A', 'B', 'B', 'A'), ))

    def test_rhyming_scheme_non_standard(self):
        self.assertEqual(self.test_non_standard.rhyming_scheme,
                         (('A','B','B','A','A','B','B','A'), ('A','B','C','A','B','C')))

    def test_syllable_scheme(self):
        self.assertEqual(self.test_haiku.syllable_scheme, (({5}, {7}, {5}), ))
        self.assertEqual(self.test_haiku_2.syllable_scheme, (({6}, {7}, {4}), ))

    def test_form_haiku(self):
        classified_poem = poem_type_classifier(TEST_HAIKU)
        self.assertEqual(classified_poem.poem_type, 'HAIKU')

    def test_form_limerick(self):
        classified_poem = poem_type_classifier(TEST_LIMERICK)
        self.assertEqual(classified_poem.poem_type, 'LIMERICK')
