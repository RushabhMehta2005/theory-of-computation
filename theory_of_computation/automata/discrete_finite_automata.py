"""
This module provides classes for representing and manipulating
deterministic finite automata (DFA).

Classes:
    - DFA: Represents a discrete finite automaton.
"""

from typing import List
from .state import StateSet
from .alphabet import Alphabet, AlphabetSet
from .transition_function import TransitionFunction


class DFA:
    def __init__(self, Q: StateSet, sigma: AlphabetSet, delta: TransitionFunction) -> None:
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.reset()

    def feed(self, input_string: List[Alphabet]) -> None:
        """Feed given string input to the DFA, updating its state."""
        for letter in input_string:
            if letter not in self.sigma:
                raise ValueError(
                    f"Input symbol '{letter}' is not in the given alphabet."
                )
            self._eat(letter)

    def accepts(self, input_string: List[Alphabet] | str) -> bool:
        if isinstance(input_string, str):
            input_string = self._convert_str_to_alphabet_list(input_string)
        self.feed(input_string)
        accepted = self.accepting
        self.reset()
        return accepted

    def _eat(self, letter: List[Alphabet]):
        if len(letter) != 1:
            raise ValueError(f"_eat() called on multi-character string {letter}.")

        # Update state
        self.current_state = self.delta(self.current_state, letter)

    def _initialise_current_state(self) -> None:
        self.current_state = self.Q.start_state.id

    @property
    def accepting(self) -> bool:
        return self.Q.states[self.current_state].is_accepting

    def reset(self) -> None:
        """Reset the DFA to its initial state."""
        self._initialise_current_state()

    def _convert_str_to_alphabet_list(self, input_string: str) -> List[Alphabet]:
        return [self.sigma.symbols[symbol] for symbol in input_string]

    def __repr__(self) -> str:
        return (
            f"DFA(Q={self.Q}, sigma={self.sigma}, "
            f"start_state=q{self.Q.start_state.id}, current_state=q{self.current_state})"
        )

    def __str__(self) -> str:
        return f"DFA({self.Q}, {self.sigma}, {self.delta}, {self.Q.start_state}, {self.Q.accepting_states})"
