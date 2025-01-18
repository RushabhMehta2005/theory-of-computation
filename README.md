# **Theory of Computation Library**

This library provides tools for creating and manipulating Deterministic Finite Automata (DFA) and serves as a foundation for exploring various computational models. It is designed to be modular and extensible, making it easy to work with automata theory in Python.

---

## **Features**

### Current Capabilities:
- **State Management**:
  - Create, modify, and manage states in a DFA.
  - Define start and accepting states.
- **Alphabet Manipulation**:
  - Define and manage alphabet sets for the DFA.
  - Perform operations like adding, removing, or checking membership of symbols.
- **Transition Functions**:
  - Define state transitions based on input symbols.
  - Support for deterministic state transitions.
- **DFA Simulation**:
  - Simulate a DFA for a given input string.
  - Check whether a DFA accepts or rejects input.

### Upcoming Features:
- Nondeterministic Finite Automata (NFA) support.
- Regular expression to DFA conversion.
- Minimization of DFA.
- Visualizations for automata and state transitions.
- Extended functionality for other computational models, like Pushdown Automata and Turing Machines.

---

## **Installation**

Clone the repository to your local machine:

```bash
git clone https://github.com/RushabhMehta2005/theory-of-computation.git
```

Then, import the desired classes in your Python scripts:

```python
from theory_of_computation import State, StateSet, AlphabetSet, TransitionFunction, DFA
```

---

## **Usage**

### **1. Creating a DFA**
Here’s a complete example to create and test a DFA:

```python
from theory_of_computation import StateSet, AlphabetSet, TransitionFunction, DFA

# Step 1: Define States
Q = StateSet(3)
Q.set_start_state(0)
Q.set_accepting_states([2])

# Step 2: Define Alphabet
sigma = AlphabetSet("ab")

# Step 3: Define Transitions
delta = TransitionFunction(sigma)
delta.add_transition(0, sigma.a, 1)
delta.add_transition(0, sigma.b, 0)
delta.add_transition(1, sigma.a, 1)
delta.add_transition(1, sigma.b, 2)
delta.add_transition(2, sigma.a, 2)
delta.add_transition(2, sigma.b, 1)

# Step 4: Create DFA
M = DFA(Q, sigma, delta)

# Step 5: Test DFA
input_string = "abbab"
print(M.accepts(input_string))  # Output: True
```

---

### **2. Working with State Sets**

```python
from theory_of_computation import StateSet

Q = StateSet(5)  # Define a state set with 5 states

# Set the start and accepting states
Q.set_start_state(0)
Q.set_accepting_states([3, 4])

# Access states
print(Q.start_state)  # Output: q0 (start)
print(Q)  # Output: {q0 (start), q1, q2, q3 (accept), q4 (accept)}
```

---

### **3. Defining and Using Alphabet Sets**

```python
from theory_of_computation import AlphabetSet

sigma = AlphabetSet("abc")  # Define an alphabet set with 'a', 'b', 'c'
sigma.add("d")  # Add a symbol
sigma.remove("a")  # Remove a symbol
print(sigma.contains("b"))  # Output: True
```

---

### **4. Defining Transition Functions**

```python
from theory_of_computation import AlphabetSet, TransitionFunction

sigma = AlphabetSet("ab")
delta = TransitionFunction(sigma)

# Define transitions
delta.add_transition(0, sigma.a, 1)
delta.add_transition(0, sigma.b, 0)
delta.add_transition(1, sigma.b, 2)

print(delta)
# Output:
# q0 -> a -> q1
# q0 -> b -> q0
# q1 -> b -> q2
```

---

## **Testing**

Run unit tests to ensure functionality:

```bash
python -m unittest discover tests/
```

---

## **Documentation**

### Classes Overview:
1. **`StateSet`**: Represents the set of states in an automaton.
2. **`AlphabetSet`**: Represents the alphabet used by the automaton.
3. **`TransitionFunction`**: Defines transitions between states.
4. **`DFA`**: Represents a deterministic finite automaton.

For detailed API usage, refer to the inline documentation in the source code.

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit changes with clear descriptions.
4. Submit a pull request for review.
