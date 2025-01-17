import unittest
from theory_of_computation import AlphabetSet, TransitionFunction


class TestTransitionFunction(unittest.TestCase):
    def setUp(self):
        """Set up the AlphabetSet and TransitionFunction for testing."""
        self.alphabet_set = AlphabetSet("abc")
        self.transition_function = TransitionFunction(self.alphabet_set)

    def test_add_transition(self):
        """Test adding valid transitions."""
        self.transition_function.add_transition(0, self.alphabet_set.a, 1)
        self.transition_function.add_transition(1, self.alphabet_set.b, 2)

        # Verify transitions
        self.assertEqual(self.transition_function.get_next_state(0, self.alphabet_set.a), 1)
        self.assertEqual(self.transition_function.get_next_state(1, self.alphabet_set.b), 2)

    def test_add_duplicate_transition(self):
        """Test adding a duplicate transition raises a ValueError."""
        self.transition_function.add_transition(0, self.alphabet_set.a, 1)
        with self.assertRaises(ValueError):
            self.transition_function.add_transition(0, self.alphabet_set.a, 2)

    def test_add_invalid_symbol(self):
        """Test adding a transition with an invalid symbol raises a ValueError."""
        with self.assertRaises(ValueError):
            self.transition_function.add_transition(0, "d", 1)  # 'd' is not in the alphabet set

    def test_get_next_state_invalid_transition(self):
        """Test retrieving a transition that does not exist raises a KeyError."""
        with self.assertRaises(KeyError):
            self.transition_function.get_next_state(0, self.alphabet_set.a)  # No transition defined for (0, 'a')

    def test_str_representation(self):
        """Test the string representation of the transition function."""
        self.transition_function.add_transition(0, self.alphabet_set.a, 1)
        self.transition_function.add_transition(1, self.alphabet_set.b, 2)

        expected_output = (
            "δ(q0, 'a') -> q1\n"
            "δ(q1, 'b') -> q2"
        )
        self.assertEqual(str(self.transition_function), expected_output)
