# Theory of Computation Library

A powerful, extensible Python library for exploring and simulating computational models.

## 🚀 Features

### Current Capabilities
- **State Management**
  - Create and manage states for finite automata
  - Define start and accepting states dynamically
- **Alphabet Handling**
  - Flexible alphabet set creation and manipulation
  - Symbol membership validation
- **Transition Functions**
  - Support for deterministic and non-deterministic transitions
  - Comprehensive state transition modeling

### Roadmap
- Regular expression to DFA conversion
- DFA minimization algorithms
- Extended computational models support

## 🛠 Installation

```bash
pip install theory-of-computation
```

## 📘 Quick Examples

### Creating a DFA

```python
from theory_of_computation import StateSet, AlphabetSet, TransitionFunction, DFA

# Define states and alphabet
Q = StateSet(3)
Q.set_start_state(0)
Q.set_accepting_states([2])

sigma = AlphabetSet("ab")

# Configure transitions
delta = TransitionFunction(sigma)
delta.add_transition(0, sigma.a, 1)
delta.add_transition(0, sigma.b, 0)
delta.add_transition(1, sigma.b, 2)

# Create and test DFA
M = DFA(Q, sigma, delta)
print(M.accepts("abbab"))  # True
```

### Working with Alphabet Sets

```python
from theory_of_computation import AlphabetSet

sigma = AlphabetSet("abc")
sigma.add("d")     # Add symbol
sigma.remove("a")  # Remove symbol
print(sigma.contains("b"))  # True
```

## 🧪 Testing

```bash
python -m unittest discover tests/
```

## 📚 Documentation

- **`StateSet`**: Manage automata states
- **`AlphabetSet`**: Define input symbol sets
- **`TransitionFunction`**: Model state transitions
- **`DFA`/`NFA`**: Simulate deterministic/non-deterministic automata

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Submit a pull request
