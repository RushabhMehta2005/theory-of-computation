import unittest
from theory_of_computation import State, StateSet


class TestState(unittest.TestCase):
    def test_state_creation(self):
        state = State(id=1)
        self.assertEqual(state.id, 1)
        self.assertFalse(state.is_start)
        self.assertFalse(state.is_accepting)

    def test_set_accepting(self):
        state = State(id=2)
        state.set_accepting()
        self.assertTrue(state.is_accepting)

    def test_set_start(self):
        state = State(id=3)
        state.set_start()
        self.assertTrue(state.is_start)

    def test_set_start(self):
        state = State(id=4)
        state.set_start()
        state.unset_start()
        self.assertFalse(state.is_start)

    def test_equality(self):
        state1 = State(id=1)
        state2 = State(id=1)
        state3 = State(id=2)
        self.assertEqual(state1, state2)
        self.assertNotEqual(state2, state3)
        self.assertNotEqual(state1, state3)

    def test_string_representation(self):
        state = State(id=4, start=True, accepting=True)
        self.assertEqual(str(state), "q4 (start) (accept)")


class TestStateSet(unittest.TestCase):
    def test_state_set_creation(self):
        state_set = StateSet(size=3)
        self.assertEqual(state_set.size, 3)
        self.assertEqual(len(state_set.states), 3)

    def test_set_start_state(self):
        state_set = StateSet(size=3)
        state_set.set_start_state(1)
        self.assertEqual(state_set.start_state.id, 1)
        self.assertTrue(state_set.states[1].is_start)

    def test_set_accepting_states(self):
        state_set = StateSet(size=4)
        state_set.set_accepting_states([1, 3])
        self.assertTrue(state_set.states[1].is_accepting)
        self.assertTrue(state_set.states[3].is_accepting)
        self.assertFalse(state_set.states[0].is_accepting)

    def test_accepting_states(self):
        state_set = StateSet(size=4)
        state_set.set_accepting_states([1, 3])
        self.assertEqual(
            state_set.accepting_states, [state_set.states[1], state_set.states[3]]
        )

    def test_invalid_start_state(self):
        state_set = StateSet(size=2)
        with self.assertRaises(IndexError):
            state_set.set_start_state(5)

    def test_invalid_accepting_state(self):
        state_set = StateSet(size=2)
        with self.assertRaises(IndexError):
            state_set.set_accepting_states([3])

    def test_no_start_state_error(self):
        state_set = StateSet(size=2)
        with self.assertRaises(ValueError):
            _ = state_set.start_state

    def test_string_representation(self):
        state_set = StateSet(size=2)
        state_set.set_start_state(0)
        state_set.set_accepting_states([1])
        expected = "{q0 (start), q1 (accept)}"
        self.assertEqual(str(state_set), expected)


if __name__ == "__main__":
    unittest.main()
