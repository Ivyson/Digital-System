from sympy import symbols
from sympy.logic.boolalg import truth_table, And, Nor

# Define up to 6 input variables
x1, x2, x3, x4, x5, x6 = symbols('x1 x2 x3 x4 x5 x6')
R = Nor(x1,x2)
S = And(x3,x4)
P = And(x3, R)
X = Nor(P, S)
expression = X

# Generate truth table
print("Truth table for the expression:", expression)
print("x1 | x2 | x3 | x4 | Output")
print("-" * 20)

# Target conditions to check
target1 = [1, 1, 1, 0]
target2 = [0, 1, 1, 1]
target3 = [1, 1, 0, 0]
target4 = [1, 0, 0, 0]
target5 = [0, 0, 1, 1]

# Loop through the truth table and print each row in a formatted way
for row in truth_table(expression, [x1, x2, x3, x4]):
    inputs = [int(val) for val in row[0]]  # Convert True/False to 1/0 (list of ints)
    output = 1 if row[1] else 0  # Convert output from True/False to 1/0

    # Check if the current inputs match any of the target conditions
    if inputs == target1:
        print(f"{inputs} |   {output} 1")
    if inputs == target2:
        print(f"{inputs} |   {output} 2")
    if inputs == target3:
        print(f"{inputs} |   {output} 3")
    if inputs == target4:
        print(f"{inputs} |   {output} 4")
    if inputs == target5:
        print(f"{inputs} |   {output} 5")