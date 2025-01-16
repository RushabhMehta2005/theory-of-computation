from typing import Iterable


class State:
    def __init__(self, id: int, start: bool = False, accepting: bool = False) -> None:
        self._id = id
        self._start = start
        self._accepting = accepting

    def set_accepting(self) -> None:
        self._accepting = True

    @property
    def is_accepting(self) -> bool:
        return self._accepting

    def set_start(self) -> None:
        self._start = True

    def unset_start(self) -> None:
        self._start = False

    @property
    def is_start(self) -> bool:
        return self._start

    @property
    def id(self) -> int:
        return self._id

    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self._id == other.id
        return False

    def __repr__(self) -> str:
        return f"State(id={self._id}, start={self._start}, accepting={self._accepting})"

    def __str__(self) -> str:
        parts = [f"q{self._id}"]
        if self._start:
            parts.append("(start)")
        if self._accepting:
            parts.append("(accept)")
        return " ".join(parts)


class StateSet:
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError(f"`size` expected greater than 0, received {size}.")
        self.size = size
        self.states = [State(q_i) for q_i in range(size)]
        self._start_state = None

    def accepting_states(self, indices: Iterable[int]) -> None:
        for i in indices:
            self._validate_index(i)
            self.states[i].set_accepting()

    def set_start_state(self, index: int) -> None:
        self._validate_index(index)
        for state in self.states:
            state.unset_start()
        self.states[index].set_start()
        self._start_state = self.states[index]

    @property
    def start_state(self) -> State:
        if self._start_state is None:
            raise ValueError(
                f"No start state provided, see StateSet.set_start_state(index) for more details."
            )
        return self._start_state

    def _validate_index(self, index: int) -> None:
        if not (0 <= index < self.size):
            raise IndexError(
                f"Index {index} out of bounds for StateSet of size {self.size}."
            )

    def __repr__(self) -> str:
        return f"StateSet(size={self.size}, states={self.states})"

    def __str__(self) -> str:
        str_repr = "{" + ", ".join(str(state) for state in self.states) + "}"
        return str_repr
