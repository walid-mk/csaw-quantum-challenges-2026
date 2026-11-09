# QAML: background and setup

This short introduction prepares you for the tools and vocabulary used in
quantum machine learning. No previous quantum programming experience is required.
Allow about **30–45 minutes**, plus installation time.

## The essential ideas

**Machine learning** uses adjustable parameters to map numerical inputs to
predictions. A *loss* measures how far a prediction is from its desired outcome.
A *gradient* describes how a small parameter change affects that loss.

**Quantum machine learning** can use a parameterized quantum circuit as one part
of that calculation. Classical software prepares numerical inputs, the circuit
transforms a quantum state, and measurements return numbers for further processing.
This combination is often called a *hybrid quantum–classical model*.

**Quantum adversarial machine learning (QAML)** studies the reliability and
security of these learning systems. For preparation, focus on understanding the
computation and checking measurements carefully. Specialist security methods and
advanced quantum algorithms are not needed for this introduction.

You only need a few quantum terms:

- A **qubit** is a two-level quantum system. A simulator represents its state
  numerically; measurement outcomes have probabilities.
- A **gate** transforms that state. A rotation gate has an angle that controls
  the transformation; numerical features can be represented by such angles.
- An **expectation value** is the average associated with a measurement. A
  noiseless simulator can calculate it analytically rather than sampling shots.

Be comfortable with Python functions, imports, arrays and basic vector arithmetic.
Know that an array's **shape**, **dtype** and **value range** are separate properties.
For example, `(4, 3)` describes four rows of three numbers; it does not specify
their precision or units. Keep training and evaluation data conceptually separate,
and record package versions and random seeds when comparing results.

## Set up the software

You need **Python 3.11**, **Git**, a text editor and a GitHub account. A CPU is
sufficient; no GPU, quantum hardware account or paid service is required.
The libraries are NumPy for arrays, PyTorch for tensors and automatic gradients,
and PennyLane for simulated quantum circuits.

The supplied dependency file uses the versions verified on the organizer's
**Linux x86-64 CPU environment**. Other operating systems and processors have not
been verified. If you use macOS, Windows or ARM, contact `#help-desk` early for a
compatible environment; do not spend preparation time guessing replacement pins.

On the supported Linux environment:

```bash
git clone https://github.com/walid-mk/csaw-quantum-challenges-2026.git
cd csaw-quantum-challenges-2026/preparation/qaml
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-cpu.lock
python -m pip check
python environment_check.py
```

A virtual environment keeps these packages separate from other Python projects.
Use this pinned file rather than upgrading packages individually. The Python
documentation explains [virtual environments](https://docs.python.org/3.11/library/venv.html).

## A small example

The environment check contains this single-qubit calculation:

```python
import pennylane as qml
import torch

device = qml.device("default.qubit", wires=1)

@qml.qnode(device, interface="torch", diff_method="backprop")
def circuit(angle):
    qml.RX(angle, wires=0)
    return qml.expval(qml.PauliZ(0))

angle = torch.tensor(0.5, dtype=torch.float64, requires_grad=True)
value = circuit(angle)
value.backward()
print(round(value.item(), 4), round(angle.grad.item(), 4))
```

Expected output: approximately **`0.8776 -0.4794`**. The first number is the
measurement expectation; the second is its derivative with respect to the angle.
This is a generic calculus-and-circuit example, with no dataset, trained model or
challenge-specific configuration. PennyLane's [PyTorch interface guide](https://docs.pennylane.ai/en/stable/introduction/interfaces/torch.html)
explains how the two libraries connect.

You are ready when you can activate the environment, run the check and explain
what its two numbers mean. If installation fails, share your operating system,
processor type, Python version and relevant error in `#help-desk`; remove any
credentials or personal paths first. You do not need to install additional quantum
frameworks or study advanced quantum algorithms before the event.
