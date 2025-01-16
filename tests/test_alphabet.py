import unittest
from theory_of_computation import Alphabet, AlphabetSet


class TestAlphabet(unittest.TestCase):
    def test_create_valid_alphabet(self):
        alphabet = Alphabet("a")
        self.assertEqual(alphabet.character, "a")

    def test_create_invalid_alphabet_empty(self):
        with self.assertRaises(ValueError):
            Alphabet("")

    def test_create_invalid_alphabet_non_alphanumeric(self):
        with self.assertRaises(ValueError):
            Alphabet("!")

    def test_create_invalid_alphabet_multiple_chars(self):
        with self.assertRaises(ValueError):
            Alphabet("ab")


class TestAlphabetSet(unittest.TestCase):
    def test_create_valid_alphabet_set(self):
        alphabet_set = AlphabetSet("abc")
        self.assertEqual(alphabet_set.size, 3)

    def test_create_invalid_alphabet_set_empty(self):
        with self.assertRaises(ValueError):
            AlphabetSet("")

    def test_create_invalid_alphabet_set_non_alphanumeric(self):
        with self.assertRaises(ValueError):
            AlphabetSet("ab#")

    def test_create_invalid_alphabet_set_duplicates(self):
        with self.assertRaises(ValueError):
            AlphabetSet("aab")

    def test_add_symbol(self):
        alphabet_set = AlphabetSet("abc")
        alphabet_set.add("d")
        self.assertEqual(alphabet_set.size, 4)
        self.assertTrue(alphabet_set.contains("d"))

    def test_remove_symbol(self):
        alphabet_set = AlphabetSet("abc")
        alphabet_set.remove("a")
        self.assertEqual(alphabet_set.size, 2)
        self.assertFalse(alphabet_set.contains("a"))

    def test_remove_non_existing_symbol(self):
        alphabet_set = AlphabetSet("abc")
        with self.assertRaises(ValueError):
            alphabet_set.remove("z")

    def test_contains_symbol(self):
        alphabet_set = AlphabetSet("abc")
        self.assertTrue(alphabet_set.contains("a"))
        self.assertFalse(alphabet_set.contains("z"))

    def test_iterate_over_alphabet_set(self):
        alphabet_set = AlphabetSet("abc")
        alphabets = [str(alphabet) for alphabet in alphabet_set]
        self.assertEqual(alphabets, ["a", "b", "c"])
