from pyeda.inter import exprvars, Or, And, Not, Xor # Use pip install pyeda for this....

# Define Boolean variables, e.g., up to 6 inputs
x = exprvars('x', 6)  # Creates variables x[0], x[1], ..., x[5]

# Define gates using pyeda syntax
# You can combine gates to form complex expressions

# AND Gate: x1 AND x2
and_gate = x[0] & x[1]

# OR Gate: x1 OR x2
or_gate = x[0] | x[1]

# NOT Gate: NOT x1
not_gate = ~x[0]

# NAND Gate: x1 NAND x2
nand_gate = ~(x[0] & x[1])

# NOR Gate: x1 NOR x2
nor_gate = ~(x[0] | x[1])

# XOR Gate: x1 XOR x2
xor_gate = x[0] ^ x[1]

# XNOR Gate (XNOR is also called EQUIV): x1 XNOR x2
xnor_gate = ~(x[0] ^ x[1])  # Alternatively, x[0].eq(x[1])

# Example of a complex expression combining these gates
# e.g., ((x1 NOR x2) AND (NOT x3)) OR (x4 NAND x5)
complex_expr = (nor_gate & not_gate) | nand_gate

# Print the expression and its truth table
print("Complex expression:", complex_expr)
print("Truth table for the expression:")
print(complex_expr.truthtable())
