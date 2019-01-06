from structures.poem import Stanza
from unittest import TestCase
from tests.stanza_test_config import TEST_HAIKU_STANZA, TEST_HAIKU_2_STANZA, TEST_LIMERICK_STANZA, TEST_SONNET_STANZA


class TestPoem(TestCase):

    def setUp(self):
        self.test_haiku_stanza, self.test_haiku_2_stanza = Stanza(TEST_HAIKU_STANZA), Stanza(TEST_HAIKU_2_STANZA)
        self.test_limerick_stanza = Stanza(TEST_LIMERICK_STANZA)
        self.test_sonnet_stanza = Stanza(TEST_SONNET_STANZA)

    def test_normalize_stanza(self):
        self.assertEqual(self.test_haiku_stanza.stanza,
                         'an old silent pond\na frog jumps into the pond\nsplash silence again')

    def test_no_of_lines(self):
        self.assertEqual(self.test_haiku_stanza.no_of_lines, 3)
        self.assertEqual(self.test_limerick_stanza.no_of_lines, 5)

    def test_rhyming_scheme_haiku(self):
        self.assertEqual(self.test_haiku_stanza.rhyming_scheme, ('A', 'A', 'B'))
        self.assertEqual(self.test_haiku_2_stanza.rhyming_scheme, ('A', 'B', 'C'))

    def test_rhyming_scheme_limerick(self):
        self.assertEqual(self.test_limerick_stanza.rhyming_scheme, ('A', 'A', 'B', 'B', 'A'))

    def test_syllable_scheme(self):
        self.assertEqual(self.test_haiku_stanza.syllable_scheme, ({5}, {7}, {5}))
        self.assertEqual(self.test_haiku_2_stanza.syllable_scheme, ({6}, {7}, {4}))
