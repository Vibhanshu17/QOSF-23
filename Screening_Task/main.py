""" Imports """
import numpy as np
from qiskit import QuantumCircuit


""" Helper Functions """
# convert to binary
def num_to_bitstring(x):
    return bin(x)[2:]


# encode numbers into quantum circuit
def build_circuit(A, B):
    bit_A = num_to_bitstring(A)
    bit_B = num_to_bitstring(B)
    
    # Uncomment below lines to see the binary representation
    # print("bit_A {}".format(bit_A))
    # print("bit_B {}".format(bit_B))
    
    # no. of qubits required to encode each number
    n = max(len(bit_A), len(bit_B))
    
    qc = QuantumCircuit(3*n + 1, 1)
    
    """ Encode numbers into the circuit """
    for i, bit in enumerate(bit_A):
        if bit == '1': qc.x(i)
    for i, bit in enumerate(bit_B):
        if bit == '1': qc.x(n+i)
        
    qc.barrier()
    
    """ Check for equality """
    for i in range(2*n):
        qc.cx(i, 2*n + i%n)
        
    for i in range(n):
        qc.x(2*n + i)
    
    qc.mct(list(range(2*n, 3*n)), 3*n)
    
    qc.barrier()
    
    """ Measurement """
    qc.measure(3*n, 0)
    
    return qc


def compare(A, B):
    # quantum circuit to compare 2 numbers
    qc = build_circuit(A, B)
    
    """ Simulate measurement results """
    backend = Aer.get_backend("qasm_simulator")
    result = backend.run(qc, shots=1024).result()
    counts = result.get_counts()
    
    return (counts['1'] >= 1000 if '1' in counts.keys() else 0)
    
    
def is_rectangle (A, B, C, D):
    if compare(A, B) and compare(C, D): return 1
    elif compare(A, C) and compare(B, D): return 1
    elif compare(A, D) and compare(B, C): return 1

    return 0
    
if __name__ == "__main__":
    A = is_rectangle(5, 6, 6, 5)
    print(A)
    
    A = is_rectangle(50, 72, 72, 60)
    print(A)
    
    A = is_rectangle(7, 7, 3, 2)
    print(A)
