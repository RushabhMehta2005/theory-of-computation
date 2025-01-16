"""
This module provides classes for representing and manipulating states of 
deterministic finite automata (DFA).

Classes:
    - State: Represents a state in the automaton.
    - StateSet: Represents a collection of states in the automaton.
"""

from typing import Iterable


class State:
    """
    Represents a state in a deterministic finite automaton (DFA).

    Attributes:
        id (int): A unique identifier for the state.
        is_accepting (bool): Whether the state is an accepting state.
        is_start (bool): Whether the state is the start state.
    """

    def __init__(self, id: int, start: bool = False, accepting: bool = False) -> None:
        """
        Initializes a new state.

        Args:
            id (int): The unique identifier for the state.
            start (bool, optional): Whether the state is the start state. Defaults to False.
            accepting (bool, optional): Whether the state is an accepting state. Defaults to False.
        """
        self._id = id
        self._start = start
        self._accepting = accepting

    def set_accepting(self) -> None:
        """
        Marks the state as an accepting state.
        """
        self._accepting = True

    @property
    def is_accepting(self) -> bool:
        """
        Indicates whether the state is an accepting state.

        Returns:
            bool: True if the state is accepting, False otherwise.
        """
        return self._accepting

    def set_start(self) -> None:
        """
        Marks the state as the start state.
        """
        self._start = True

    def unset_start(self) -> None:
        """
        Unmarks the state as the start state.
        """
        self._start = False

    @property
    def is_start(self) -> bool:
        """
        Indicates whether the state is the start state.

        Returns:
            bool: True if the state is the start state, False otherwise.
        """
        return self._start

    @property
    def id(self) -> int:
        """
        The unique identifier for the state.

        Returns:
            int: The state ID.
        """
        return self._id

    def __eq__(self, other) -> bool:
        """
        Checks equality with another state based on their IDs.

        Args:
            other (State): The other state to compare.

        Returns:
            bool: True if the states have the same ID, False otherwise.
        """
        if isinstance(other, State):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        """
        Returns a string representation for debugging.

        Returns:
            str: Debug-friendly string representation of the state.
        """
        return f"State(id={self._id}, start={self._start}, accepting={self._accepting})"

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the state.

        Returns:
            str: A readable string representation.
        """
        parts = [f"q{self._id}"]
        if self._start:
            parts.append("(start)")
        if self._accepting:
            parts.append("(accept)")
        return " ".join(parts)


class StateSet:
    """
    Represents a collection of states in a DFA.

    Attributes:
        size (int): The number of states in the set.
        states (List[State]): The list of states in the set.
        start_state (State): The start state of the automaton.

    Methods:
        set_accepting_states(indices: Iterable[int]) -> None:
            Marks specified states as accepting.
        set_start_state(index: int) -> None:
            Sets the start state of the automaton.
    """

    def __init__(self, size: int) -> None:
        """
        Initializes a collection of states for a DFA.

        Args:
            size (int): The number of states in the set.

        Raises:
            ValueError: If `size` is not greater than 0.
        """
        if size <= 0:
            raise ValueError(f"`size` expected greater than 0, received {size}.")
        self.size = size
        self.states = [State(q_i) for q_i in range(size)]
        self._start_state = None

    def set_accepting_states(self, indices: Iterable[int]) -> None:
        """
        Marks specified states as accepting.

        Args:
            indices (Iterable[int]): A collection of state indices to mark as accepting.

        Raises:
            IndexError: If any index is out of bounds.
        """
        for i in indices:
            self._validate_index(i)
            self.states[i].set_accepting()

    def set_start_state(self, index: int) -> None:
        """
        Sets the start state of the automaton.

        Args:
            index (int): The index of the state to set as the start state.

        Raises:
            IndexError: If the index is out of bounds.
        """
        self._validate_index(index)
        for state in self.states:
            state.unset_start()
        self.states[index].set_start()
        self._start_state = self.states[index]

    @property
    def start_state(self) -> State:
        """
        Retrieves the start state of the automaton.

        Returns:
            State: The start state.

        Raises:
            ValueError: If no start state has been set.
        """
        if self._start_state is None:
            raise ValueError(
                f"No start state provided, see StateSet.set_start_state(index) for more details."
            )
        return self._start_state

    def _validate_index(self, index: int) -> None:
        """
        Validates that the given index is within bounds.

        Args:
            index (int): The index to validate.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not (0 <= index < self.size):
            raise IndexError(
                f"Index {index} out of bounds for StateSet of size {self.size}."
            )

    def __repr__(self) -> str:
        """
        Returns a string representation for debugging.

        Returns:
            str: Debug-friendly string representation of the state set.
        """
        return f"StateSet(size={self.size}, states={self.states})"

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the state set.

        Returns:
            str: A readable string representation.
        """
        str_repr = "{" + ", ".join(str(state) for state in self.states) + "}"
        return str_repr
