"""Generic QML environment check: one qubit, no data and no trained model."""
import math

import numpy as np
import pennylane as qml
import torch


device = qml.device('default.qubit', wires=1)


@qml.qnode(device, interface='torch', diff_method='backprop')
def circuit(angle):
    qml.RX(angle, wires=0)
    return qml.expval(qml.PauliZ(0))


def main():
    angle = torch.tensor(0.5, dtype=torch.float64, requires_grad=True)
    value = circuit(angle)
    value.backward()
    assert math.isclose(value.item(), math.cos(0.5), abs_tol=1e-10)
    assert angle.grad is not None
    assert math.isclose(angle.grad.item(), -math.sin(0.5), abs_tol=1e-10)
    print(f'NumPy {np.__version__}; PyTorch {torch.__version__}; PennyLane {qml.__version__}')
    print(f'Expectation: {value.item():.4f}; derivative: {angle.grad.item():.4f}')
    print('Environment check passed. No dataset or trained model was used.')


if __name__ == '__main__':
    main()
