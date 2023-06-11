# QOSF-23

#### Task 2: Is rectangle?  
Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).  
If any such rectangle exist return 1 else return 0.

#### Solution:
We compare each pair of numbers to see if they can form a rectangle.  
There are 3 possibilities: [(A, B), (C, D)], [(A, C), (B, D)], [(A, D), (B, C)]

The ``` compare() ``` circuit is divided into 3 parts:
* Encoding: encode the numbers into quantum circuit
* Operation: We apply quantum gates to check if the numbers are equal
* Measurement: Finally, the measurement of 0 => equal and 1 => unequal


Quantum Circuit (qc) has 2 * n qubits for encoding (n qubits for each number),  
n qubits to apply operations and finally 1 qubit and 1 classical bit to take measurement.
