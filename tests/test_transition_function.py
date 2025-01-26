import unittest
from theory_of_computation import (
    AlphabetSet,
    TransitionFunction,
    MultiValuedTransitionFunction,
)


class TestTransitionFunction(unittest.TestCase):
    def setUp(self):
        """Set up the AlphabetSet and TransitionFunction for testing."""
        self.alphabet_set = AlphabetSet("abc")
        self.transition_function = TransitionFunction(self.alphabet_set)

    def test_add_transition(self):
        """Test adding valid transitions."""
        self.transition_function.add_transition(0, self.alphabet_set.a, 1)
        self.transition_function.add_transition(1, self.alphabet_set.b, 2)

        self.assertEqual(self.transition_function(0, self.alphabet_set.a), 1)
        self.assertEqual(self.transition_function(1, self.alphabet_set.b), 2)

    def test_add_duplicate_transition(self):
        """Test adding a duplicate transition raises a ValueError."""
        self.transition_function.add_transition(0, self.alphabet_set.a, 1)
        with self.assertRaises(ValueError):
            self.transition_function.add_transition(0, self.alphabet_set.a, 2)

    def test_add_invalid_symbol(self):
        """Test adding a transition with an invalid symbol raises a ValueError."""
        with self.assertRaises(AttributeError):
            self.transition_function.add_transition(0, self.alphabet_set.d, 1)

    def test_get_next_state_invalid_transition(self):
        """Test retrieving a transition that does not exist raises a KeyError."""
        with self.assertRaises(KeyError):
            self.transition_function(0, self.alphabet_set.a)

    def test_str_representation(self):
        """Test the string representation of the transition function."""
        self.transition_function.add_transition(0, self.alphabet_set.a, 1)
        self.transition_function.add_transition(1, self.alphabet_set.b, 2)

        expected_output = "δ(q0, 'a') -> q1\n" "δ(q1, 'b') -> q2"
        self.assertEqual(str(self.transition_function), expected_output)


class TestMultiValuedTransitionFunction(unittest.TestCase):
    def setUp(self):
        self.sigma = AlphabetSet("ab")
        self.delta = MultiValuedTransitionFunction(self.sigma)

    def test_add_transition(self):
        self.delta.add_transition(0, self.sigma.a, 1)
        self.delta.add_transition(0, self.sigma.a, 2)

        transitions = self.delta(0, self.sigma.a)
        self.assertIn(1, transitions)
        self.assertIn(2, transitions)

    def test_remove_transition(self):
        self.delta.add_transition(0, self.sigma.a, 1)
        self.delta.add_transition(0, self.sigma.a, 2)

        self.delta.remove_transition(0, self.sigma.a, 1)

        transitions = self.delta(0, self.sigma.a)
        self.assertNotIn(1, transitions)
        self.assertIn(2, transitions)

    def test_multiple_transitions(self):
        self.delta.add_transition(0, self.sigma.a, 1)
        self.delta.add_transition(0, self.sigma.a, 2)
        self.delta.add_transition(0, self.sigma.b, 3)

        a_transitions = self.delta(0, self.sigma.a)
        b_transitions = self.delta(0, self.sigma.b)

        self.assertEqual(set(a_transitions), {1, 2})
        self.assertEqual(set(b_transitions), {3})

    def test_invalid_symbol(self):
        with self.assertRaises(AttributeError):
            self.delta.add_transition(0, self.sigma.c, 1)


if __name__ == "__main__":
    unittest.main()
