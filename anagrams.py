import unittest
from unittest.mock import patch, MagicMock


class Anagrams:
    def __init__(self, file_name):
        self.file_name = file_name
        self.map = {}

    def initialise(self):
        self.words = self.get_file()
        self.map = self.mapping()

    def key(self, word):
        abbr = sorted(word)
        return ''.join(abbr)

    def mapping(self):
        word_mapped = {}
        for word in self.words:
            key = self.key(word)
            word_mapped.setdefault(key, []).append(word)

        return word_mapped

    def get_anagrams(self, word):
        key = self.key(word)
        try:
            return self.map[key]

        except KeyError:
            print('Not found!')

    def get_file(self):
        return open(self.file_name).read().splitlines()


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        anagrams = Anagrams('words.txt')
        anagrams.initialise()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])


class TestGetAnagrams(unittest.TestCase):
    def test_include_word(self):
        anagrams = Anagrams('words.txt')
        anagrams.key = MagicMock(return_value='key')
        anagrams.map = {'key': ['Anacreon1', 'Anacreon2']}
        result = anagrams.get_anagrams('word')
        self.assertEqual(result, ['Anacreon1', 'Anacreon2'])

    @patch('builtins.print')
    def test_missing_word(self, mock_print):
        anagrams = Anagrams('words.txt')
        anagrams._get_key = MagicMock(return_value='key')
        anagrams.map = {'notkey': ['Anacreon1', 'Anacreon2']}
        result = anagrams.get_anagrams('word')
        mock_print.assert_called_once_with('Not found!')


if __name__ == '__main__':
    unittest.main()
