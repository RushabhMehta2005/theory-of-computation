"""
This module provides classes for representing and manipulating
non deterministic finite automata (NFA).

Classes:
    - NFA: Represents a discrete finite automaton.
"""

from typing import List, Set
from .state import State, StateSet
from .alphabet import Alphabet, AlphabetSet
from .transition_function import MultiValuedTransitionFunction


class NFA:
    def __init__(
        self, Q: StateSet, sigma: AlphabetSet, delta: MultiValuedTransitionFunction
    ) -> None:
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self._trace = []
        self._current_states: Set[int] = set()
        self.reset()

    def feed(self, input_string: List[Alphabet], verbose: bool = False) -> None:
        """Feed given string input to the NFA, updating its states."""
        for letter in input_string:
            if letter not in self.sigma:
                raise ValueError(
                    f"Input symbol '{letter}' is not in the given alphabet."
                )
            self._eat(letter)

    def accepts(
        self,
        input_string: List[Alphabet] | str,
        verbose: bool = False,
        reset_after: bool = True,
    ) -> bool:
        """Check if the NFA accepts the input string."""
        if isinstance(input_string, str):
            input_string = self._convert_str_to_alphabet_list(input_string)
        self.feed(input_string, verbose)
        accepted = self.accepting
        if reset_after:
            self.reset()
        return accepted

    def _eat(self, letter: Alphabet) -> None:
        """Process a single input symbol, updating possible states."""
        if len(letter) != 1:
            raise ValueError(f"_eat() called on multi-character string {letter}.")

        next_states = set()
        for current_state in self._current_states:
            try:
                possible_next_states = self.delta(current_state, letter)
                next_states.update(possible_next_states)
                # Record trace for each transition
                for next_state in possible_next_states:
                    self._trace.append([current_state, letter, next_state])
            except KeyError:
                # If no transition exists for a state, skip it (dead branch)
                pass

        # Update current states
        self._current_states = next_states

    def _initialise_current_state(self) -> None:
        """Set initial state(s) to the DFA's start state."""
        self._current_states = {self.Q.start_state.id}

    @property
    def accepting(self) -> bool:
        """Check if any current state is an accepting state."""
        return any(self.Q.states[state].is_accepting for state in self._current_states)

    @property
    def trace(self) -> List[List[State]]:
        """Return the trace of state transitions."""
        return self._trace

    def reset(self) -> None:
        """Reset the NFA to its initial state."""
        self._initialise_current_state()
        self._trace = []

    def _convert_str_to_alphabet_list(self, input_string: str) -> List[Alphabet]:
        """Convert input string to list of Alphabet symbols."""
        return [self.sigma.symbols[symbol] for symbol in input_string]

    def __repr__(self) -> str:
        """Provide a string representation of the NFA."""
        return (
            f"NFA(Q={self.Q}, sigma={self.sigma}, "
            f"start_state=q{self.Q.start_state.id}, "
            f"current_states={self._current_states})"
        )

    def __str__(self) -> str:
        """Provide a detailed string representation of the NFA."""
        return (
            f"NFA({self.Q}, {self.sigma}, \n"
            f"{self.delta}\n"
            f"{self.Q.start_state}, {self.Q.accepting_states})"
        )
