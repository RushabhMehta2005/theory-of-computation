"""
This module provides classes for representing and manipulating transition functions of 
deterministic finite automata (DFA).

Classes:
    - TransitionFunction: Represents a the transition function of the DFA, mapping states and alphabets
    to the next state
"""

from typing import Dict, Tuple
from .alphabet import Alphabet, AlphabetSet


class TransitionFunction:
    """
    Represents the transition function for a deterministic finite automaton (DFA).

    Attributes:
        transitions (Dict[Tuple[int, str], int]): A mapping of (current state, input symbol)
            to the next state.
    """

    def __init__(self, alphabet_set: AlphabetSet) -> None:
        """
        Initializes the transition function with a defined AlphabetSet.

        Args:
            alphabet_set (AlphabetSet): The alphabet set defining valid symbols.
        """
        self.transitions: Dict[Tuple[int, str], int] = {}
        self.alphabet_set = alphabet_set

    def add_transition(
        self, current_state: int, symbol: Alphabet, next_state: int
    ) -> None:
        """
        Adds a transition to the transition function.

        Args:
            current_state (int): The ID of the current state.
            symbol (str): The input symbol (validated against the AlphabetSet).
            next_state (int): The ID of the next state.

        Raises:
            ValueError: If the symbol is not part of the AlphabetSet or the transition already exists.
        """
        if symbol not in self.alphabet_set:
            raise ValueError(
                f"Symbol '{symbol}' is not part of the defined AlphabetSet."
            )
        if (current_state, symbol) in self.transitions:
            raise ValueError(
                f"Transition for state {current_state} and symbol '{symbol}' already exists."
            )
        self.transitions[(current_state, symbol)] = next_state

    def __call__(self, current_state: int, symbol: str) -> int:
        """
        Retrieves the next state for a given state and input symbol.

        Args:
            current_state (int): The ID of the current state.
            symbol (str): The input symbol.

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

    def __str__(self) -> str:
        """
        Returns a string representation of the transition function.
        """
        transitions = [
            f"δ(q{state}, '{symbol}') -> q{next_state}"
            for (state, symbol), next_state in self.transitions.items()
        ]
        return "\n".join(transitions)
