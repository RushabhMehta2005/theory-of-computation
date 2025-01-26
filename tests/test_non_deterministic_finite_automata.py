import unittest
from theory_of_computation import (
    StateSet,
    AlphabetSet,
    MultiValuedTransitionFunction,
    NFA,
)


class TestNFA(unittest.TestCase):
    def setUp(self):
        Q = StateSet(3)
        Q.set_start_state(0)
        Q.set_accepting_states([2])

        sigma = AlphabetSet("ab")

        delta = MultiValuedTransitionFunction(sigma)
        delta.add_transition(0, sigma.a, 0)
        delta.add_transition(0, sigma.a, 1)
        delta.add_transition(0, sigma.b, 0)
        delta.add_transition(1, sigma.b, 2)
        delta.add_transition(2, sigma.a, 2)
        delta.add_transition(2, sigma.b, 2)

        self.M = NFA(Q, sigma, delta)

    def test_accepts_valid_strings(self):
        valid_strings = ["abb", "aabb", "baabb"]
        for s in valid_strings:
            self.assertTrue(self.M.accepts(s), f"Failed to accept valid string: {s}")

    def test_rejects_invalid_strings(self):
        invalid_strings = ["", "a", "ba", "aaa"]
        for s in invalid_strings:
            self.assertFalse(
                self.M.accepts(s), f"Incorrectly accepted invalid string: {s}"
            )

    def test_reset_functionality(self):
        self.M.accepts("abb", reset_after=False)
        initial_trace = self.M.trace
        self.assertNotEqual(initial_trace, [])

        self.M.reset()
        self.assertEqual(self.M.trace, [], "Trace not cleared after reset")

    def test_non_deterministic_transitions(self):
        # Test multiple possible paths
        Q = StateSet(3)
        Q.set_start_state(0)
        Q.set_accepting_states([2])

        sigma = AlphabetSet("ab")

        delta = MultiValuedTransitionFunction(sigma)
        delta.add_transition(0, sigma.a, 0)
        delta.add_transition(0, sigma.a, 1)
        delta.add_transition(1, sigma.b, 2)

        M = NFA(Q, sigma, delta)

        self.assertTrue(M.accepts("aab"))


if __name__ == "__main__":
    unittest.main()
