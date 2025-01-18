import unittest
from theory_of_computation import DFA


import unittest
from theory_of_computation import StateSet, AlphabetSet, TransitionFunction, DFA

class TestDFA(unittest.TestCase):
    def setUp(self):
        self.Q = StateSet(3)
        self.Q.set_start_state(0)
        self.Q.set_accepting_states([2])

        self.sigma = AlphabetSet("ab")

        self.delta = TransitionFunction(self.sigma)
        self.delta.add_transition(0, self.sigma.a, 1)
        self.delta.add_transition(0, self.sigma.b, 0)
        self.delta.add_transition(1, self.sigma.a, 1)
        self.delta.add_transition(1, self.sigma.b, 2)
        self.delta.add_transition(2, self.sigma.a, 2)
        self.delta.add_transition(2, self.sigma.b, 1)

        self.M = DFA(self.Q, self.sigma, self.delta)

    def test_initialization(self):
        self.assertEqual(self.M.current_state, self.Q.start_state.id)
        self.assertFalse(self.M.accepting)

    def test_accepts_valid_strings(self):
        self.assertTrue(self.M.accepts("abbabaaa"))
        self.assertFalse(self.M.accepts("abb"))

    def test_rejects_invalid_strings(self):
        self.assertFalse(self.M.accepts("a"))
        self.assertFalse(self.M.accepts("babab"))

    def test_empty_string(self):
        self.assertFalse(self.M.accepts(""))

    def test_invalid_symbol(self):
        with self.assertRaises(KeyError):
            self.M.accepts("abc")

    def test_reset_behavior(self):
        self.M.accepts("abbabaaa")
        self.assertEqual(self.M.current_state, self.Q.start_state.id)

    def test_edge_cases(self):
        # Edge case: Very long valid string
        self.assertTrue(self.M.accepts("abb" * 1000 + "b"))

        # Edge case: Single-character strings
        self.assertFalse(self.M.accepts("a"))
        self.assertFalse(self.M.accepts("b"))

    def test_repr_and_str(self):
        self.assertIn("DFA", repr(self.M))
        self.assertIn("start_state=q0", repr(self.M))
        self.assertIn("sigma", repr(self.M))

if __name__ == "__main__":
    unittest.main()
