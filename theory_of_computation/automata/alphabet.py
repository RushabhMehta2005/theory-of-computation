"""
This module provides classes for representing and manipulating alphabet sets of 
deterministic finite automata (DFA).

Classes:
    - Alphabet: Represents a single symbol in the automaton's alphabet.
    - AlphabetSet: Represents the complete set of symbols in the automaton's alphabet.
"""


class Alphabet:
    """
    Represents a single symbol in the alphabet of a DFA.

    Attributes:
        character (str): The character represented by this Alphabet object.
    """

    def __init__(self, character: str) -> None:
        if len(character) != 1 or not character.isalnum():
            raise ValueError(
                f"Invalid alphabet character: '{character}'. Must be a single alphanumeric character."
            )
        self.character = character

    def __eq__(self, other) -> bool:
        return isinstance(other, Alphabet) and self.character == other.character

    def __hash__(self) -> int:
        return hash(self.character)

    def __repr__(self) -> str:
        return f"Alphabet(character='{self.character}')"

    def __str__(self) -> str:
        return self.character


class AlphabetSet:
    """
    Represents the complete set of symbols in the alphabet of a DFA.

    Attributes:
        characters (set[Alphabet]): The set of alphabet symbols.
    """

    def __init__(self, alphabets: str) -> None:
        if not alphabets:
            raise ValueError("AlphabetSet cannot be initialized with an empty string.")
        self.characters = set()
        self._validate_and_add_alphabets(alphabets)

    def _validate_and_add_alphabets(self, alphabets: str) -> None:
        for char in alphabets:
            if not self.contains(char):
                self.add(char)
            else:
                raise ValueError(
                    f"AlphabetSet cannot be initialized with duplicate elements. {char} found."
                )

    @property
    def size(self) -> int:
        return len(self.characters)

    def add(self, char: str) -> None:
        """Adds a new symbol to the alphabet set."""
        alphabet = Alphabet(char)
        self.characters.add(alphabet)

    def remove(self, char: str) -> None:
        """Removes a symbol from the alphabet set."""
        if not self.contains(char):
            raise ValueError(f"{char} does not belong in the alphabet set.")
        self.characters.discard(Alphabet(char))

    def contains(self, char: str) -> bool:
        """Checks if a symbol exists in the alphabet set."""
        return Alphabet(char) in self.characters

    def __iter__(self):
        return iter(sorted(self.characters, key=lambda x: x.character))

    def __repr__(self) -> str:
        return f"AlphabetSet(size={self.size}, characters={list(self.characters)})"

    def __str__(self) -> str:
        return (
            "{"
            + ", ".join(
                str(char) for char in sorted(self.characters, key=lambda x: x.character)
            )
            + "}"
        )
