"""
This module provides classes for representing and manipulating alphabet sets of 
deterministic finite automata (DFA).

Classes:
    - Alphabet: Represents a single symbol in the automaton's alphabet.
    - AlphabetSet: Represents the complete set of symbols in the automaton's alphabet.
"""

from typing import Dict

class Alphabet:
    """
    Represents a single symbol in the alphabet of a DFA.

    Attributes:
        symbol (str): The symbol represented by this Alphabet object.
    """

    def __init__(self, symbol: str) -> None:
        if len(symbol) != 1 or not symbol.isalnum():
            raise ValueError(
                f"Invalid alphabet symbol: '{symbol}'. Must be a single alphanumeric symbol."
            )
        self.symbol = symbol

    def __eq__(self, other) -> bool:
        return isinstance(other, Alphabet) and self.symbol == other.symbol

    def __hash__(self) -> int:
        return hash(self.symbol)

    def __len__(self) -> int:
        return len(self.symbol)

    def __repr__(self) -> str:
        return f"Alphabet(symbol='{self.symbol}')"

    def __str__(self) -> str:
        return self.symbol


class AlphabetSet:
    """
    Represents the complete set of symbols in the alphabet of a DFA.

    Attributes:
        symbols (dict[str, Alphabet]): The dictionary of alphabet symbols mapped by their symbols.
    """

    def __init__(self, alphabets: str) -> None:
        """
        Initializes the AlphabetSet.

        Args:
            alphabets (str): A string of unique alphanumeric symbols.

        Raises:
            ValueError: If the input string is empty or contains duplicates.
        """
        if not alphabets:
            raise ValueError("AlphabetSet cannot be initialized with an empty string.")

        self.symbols: Dict[str, Alphabet] = {} # maps str to its alphabet instance
        self._validate_and_add_alphabets(alphabets)

    def _validate_and_add_alphabets(self, alphabets: str) -> None:
        """
        Validates and adds alphabets to the set, ensuring uniqueness.

        Args:
            alphabets (str): The string of symbols to validate and add.

        Raises:
            ValueError: If duplicate symbols are found in the input.
        """
        for char in alphabets:
            if char in self.symbols:
                raise ValueError(
                    f"AlphabetSet cannot be initialized with duplicate elements. '{char}' found."
                )
            self.add(char)

    @property
    def size(self) -> int:
        """Returns the size of the alphabet set."""
        return len(self.symbols)

    def add(self, char: str) -> None:
        """
        Adds a new symbol to the alphabet set.

        Args:
            char (str): The symbol to add.

        Raises:
            ValueError: If the symbol is not alphanumeric.
        """
        if not char.isalnum():
            raise ValueError(
                f"Only alphanumeric symbols are allowed. '{char}' is invalid."
            )

        alphabet = Alphabet(char)
        self.symbols[char] = alphabet

        # Dynamically add the symbol as an attribute
        setattr(self, char, alphabet)

    def remove(self, char: str) -> None:
        """
        Removes a symbol from the alphabet set.

        Args:
            char (str): The symbol to remove.

        Raises:
            ValueError: If the symbol does not exist in the alphabet set.
        """
        if char not in self.symbols:
            raise ValueError(f"'{char}' does not belong in the alphabet set.")

        del self.symbols[char]

        # Remove the dynamically added attribute
        delattr(self, char)


    def contains(self, char: str) -> bool:
        """
        Checks if a symbol exists in the alphabet set.

        Args:
            char (str): The symbol to check.

        Returns:
            bool: True if the symbol exists, False otherwise.
        """
        return char in self.symbols

    def __contains__(self, other: Alphabet) -> bool:
        letter_str = other.symbol
        return letter_str in self.symbols and self.symbols[letter_str] == other

    def __iter__(self):
        """Allows iteration over the symbols in the alphabet set."""
        return iter(sorted(self.symbols.values(), key=lambda x: x.symbol))

    def __repr__(self) -> str:
        """Returns a developer-friendly representation of the AlphabetSet."""
        return f"AlphabetSet(size={self.size}, symbols={list(self.symbols.keys())})"

    def __str__(self) -> str:
        """Returns a string representation of the AlphabetSet."""
        return "{" + ", ".join(sorted(self.symbols.keys())) + "}"
