"""
This module provides classes for representing and manipulating transition functions of 
deterministic finite automata (DFA) and non deterministic finite automata (NFA).

Classes:
    - TransitionFunction: Represents a the transition function of the DFA, mapping states and alphabets
    to the next state
    - MultiValuedTransitionFunction: Represents a the transition function of the NFA, mapping states and alphabets
    to the next state
"""

from typing import Dict, Tuple, List, Union, Set
from collections import defaultdict
from .alphabet import Alphabet, AlphabetSet


class BaseTransitionFunction:
    """
    Base class for transition functions in finite automata.

    Attributes:
        alphabet_set (AlphabetSet): The alphabet set defining valid symbols.
        transitions (Dict): A mapping of (current state, input symbol) to next state(s).
    """

    def __init__(self, alphabet_set: AlphabetSet) -> None:
        """
        Initializes the base transition function with a defined AlphabetSet.

        Args:
            alphabet_set (AlphabetSet): The alphabet set defining valid symbols.
        """
        self.alphabet_set = alphabet_set
        self.transitions: Dict[Tuple[int, Alphabet], Union[int, Set[int]]] = {}

    def _validate_symbol(self, symbol: Alphabet) -> None:
        """
        Validates that the symbol is part of the alphabet set.

        Args:
            symbol (Alphabet): The input symbol to validate.

        Raises:
            ValueError: If the symbol is not part of the AlphabetSet.
        """
        if symbol not in self.alphabet_set:
            raise ValueError(
                f"Symbol '{symbol}' is not part of the defined AlphabetSet."
            )

    def __str__(self) -> str:
        """
        Returns a string representation of the transition function.

        Returns:
            str: A formatted string of transitions.
        """
        raise NotImplementedError("Subclasses must implement __str__ method")

    def has_transition(self, current_state: int, symbol: Alphabet) -> bool:
        """
        Checks if a transition exists for the given state and symbol.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.

        Returns:
            bool: True if a transition exists, False otherwise.
        """
        return (current_state, symbol) in self.transitions


class TransitionFunction(BaseTransitionFunction):
    """
    Represents the transition function for a deterministic finite automaton (DFA).
    """

    def __init__(self, alphabet_set: AlphabetSet) -> None:
        """
        Initializes the DFA transition function.

        Args:
            alphabet_set (AlphabetSet): The alphabet set defining valid symbols.
        """
        super().__init__(alphabet_set)
        self.transitions: Dict[Tuple[int, Alphabet], int] = {}

    def add_transition(
        self, current_state: int, symbol: Alphabet, next_state: int
    ) -> None:
        """
        Adds a transition to the transition function.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol (validated against the AlphabetSet).
            next_state (int): The ID of the next state.

        Raises:
            ValueError: If the symbol is not part of the AlphabetSet or the transition already exists.
        """
        self._validate_symbol(symbol)

        if (current_state, symbol) in self.transitions:
            raise ValueError(
                f"Transition for state {current_state} and symbol '{symbol}' already exists."
            )

        self.transitions[(current_state, symbol)] = next_state

    def remove_transition(self, current_state: int, symbol: Alphabet) -> None:
        """
        Removes a specific transition from the transition function.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.

        Raises:
            KeyError: If the transition does not exist.
        """
        if (current_state, symbol) not in self.transitions:
            raise KeyError(
                f"Transition for state {current_state} with symbol '{symbol}' does not exist."
            )
        del self.transitions[(current_state, symbol)]

    def get_transitions(self, current_state: int, symbol: Alphabet) -> int:
        """
        Retrieves the next state for a given state and input symbol.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.

        Returns:
            int: The ID of the next state.

        Raises:
            KeyError: If no transition exists for the given (state, symbol) pair.
        """
        if (current_state, symbol) not in self.transitions:
            raise KeyError(
                f"No transition defined for state {current_state} with symbol '{symbol}'."
            )
        return self.transitions[(current_state, symbol)]

    def __call__(self, current_state: int, symbol: Alphabet) -> int:
        """
        Retrieves the next state for a given state and input symbol.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.

        Returns:
            int: The ID of the next state.

        Raises:
            KeyError: If no transition exists for the given (state, symbol) pair.
        """
        return self.get_transitions(current_state, symbol)

    def __str__(self) -> str:
        """
        Returns a string representation of the transition function.

        Returns:
            str: Formatted string of DFA transitions.
        """
        transitions = [
            f"δ(q{state}, '{symbol}') -> q{next_state}"
            for (state, symbol), next_state in self.transitions.items()
        ]
        return "\n".join(transitions)


class MultiValuedTransitionFunction(BaseTransitionFunction):
    """
    Represents the transition function for a non-deterministic finite automaton (NFA).
    """

    def __init__(self, alphabet_set: AlphabetSet) -> None:
        """
        Initializes the NFA transition function.

        Args:
            alphabet_set (AlphabetSet): The alphabet set defining valid symbols.
        """
        super().__init__(alphabet_set)
        self.transitions: Dict[Tuple[int, Alphabet], Set[int]] = defaultdict(set)

    def add_transition(
        self, current_state: int, symbol: Alphabet, next_state: int
    ) -> None:
        """
        Adds a transition to the transition function.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol (validated against the AlphabetSet).
            next_state (int): The ID of the next state.

        Raises:
            ValueError: If the symbol is not part of the AlphabetSet.
        """
        self._validate_symbol(symbol)
        self.transitions[(current_state, symbol)].add(next_state)

    def remove_transition(
        self, current_state: int, symbol: Alphabet, next_state: int
    ) -> None:
        """
        Removes a specific transition from the transition function.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.
            next_state (int): The ID of the next state.

        Raises:
            KeyError: If the transition does not exist.
        """
        if next_state not in self.transitions[(current_state, symbol)]:
            raise KeyError(
                f"Transition for state {current_state}, symbol '{symbol}' to state {next_state} does not exist."
            )

        self.transitions[(current_state, symbol)].remove(next_state)

        # Remove the key if no transitions remain for this state and symbol
        if not self.transitions[(current_state, symbol)]:
            del self.transitions[(current_state, symbol)]

    def get_transitions(self, current_state: int, symbol: Alphabet) -> Set[int]:
        """
        Retrieves all possible next states for a given state and input symbol.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.

        Returns:
            Set[int]: A set of IDs of the possible next states.
        """
        return self.transitions[(current_state, symbol)]

    def __call__(self, current_state: int, symbol: Alphabet) -> List[int]:
        """
        Retrieves the next states for a given state and input symbol.

        Args:
            current_state (int): The ID of the current state.
            symbol (Alphabet): The input symbol.

        Returns:
            List[int]: List of the IDs of the possible next states.

        Raises:
            KeyError: If no transition exists for the given (state, symbol) pair.
        """
        if (current_state, symbol) not in self.transitions:
            raise KeyError(
                f"No transition defined for state {current_state} with symbol '{symbol}'."
            )
        return list(self.transitions[(current_state, symbol)])

    def __str__(self) -> str:
        """
        Returns a string representation of the transition function.

        Returns:
            str: Formatted string of NFA transitions.
        """
        transitions = []
        for (state, symbol), next_states in self.transitions.items():
            for next_state in next_states:
                transitions.append(f"δ(q{state}, '{symbol}') -> q{next_state}")
        return "\n".join(transitions)
