# Theory of Computation Library

This library provides tools for creating and manipulating deterministic finite automata (DFA). It includes classes to represent states (`State`) and collections of states (`StateSet`).

## Installation

To use this library, clone the repository and add it to your Python path:

```bash
git clone https://github.com/RushabhMehta2005/theory-of-computation.git
```

Then, import the desired classes in your Python scripts:

```python
from theory_of_computation import State, StateSet
```

## Usage

Below are some examples to help you get started.

### **Creating a State Set**

```python
from theory_of_computation import State, StateSet

# Create a StateSet with 4 states
Q = StateSet(4)

# Set the start state to state 0
Q.set_start_state(0)

# Mark states 2 and 3 as accepting states
Q.set_accepting_states([2, 3])

# Print the start state
print(Q.start_state)  # Output: q0 (start)

# Print all states in the set
print(Q)
# Output: {q0 (start), q1, q2 (accept), q3 (accept)}
```

### **Manipulating Individual States**

```python
state = Q.states[1]  # Get the state with ID 1
state.set_accepting()  # Mark it as accepting
print(state)
# Output: q1 (accept)
```

## Features

- Define a state set for a DFA with a given size.
- Mark states as start or accepting states.
- Easily access the start state and manipulate individual states.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
