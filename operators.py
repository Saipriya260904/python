a = 10
b = 5

# Arithmetic Operators
print(f'Arithmetic Operators:')
print(f'a + b = {a + b}')  # Addition
print(f'a - b = {a - b}')  # Subtraction
print(f'a * b = {a * b}')  # Multiplication
print(f'a / b = {a / b}')  # Division
print(f'a % b = {a % b}')  # Modulus
print(f'a ** b = {a ** b}') # Exponentiation
print(f'a // b = {a // b}') # Floor Division

# Comparison Operators
print(f'\nComparison Operators:')
print(f'a == b: {a == b}')  # Equal to
print(f'a != b: {a != b}')  # Not equal to
print(f'a > b: {a > b}')    # Greater than
print(f'a < b: {a < b}')    # Less than
print(f'a >= b: {a >= b}')  # Greater than or equal to
print(f'a <= b: {a <= b}')  # Less than or equal to

# Logical Operators
print(f'\nLogical Operators:')
print(f'a > b and a != b: {a > b and a != b}') # Logical AND
print(f'a > b or a == b: {a > b or a == b}')  # Logical OR
print(f'not(a > b): {not(a > b)}')             # Logical NOT

# Assignment Operators
print(f'\nAssignment Operators:')
c = a  # Simple Assignment
print(f'c = a: {c}')
c += b  # Addition Assignment
print(f'c += b: {c}')
c -= b  # Subtraction Assignment
print(f'c -= b: {c}')
c *= b  # Multiplication Assignment
print(f'c *= b: {c}')
c /= b  # Division Assignment
print(f'c /= b: {c}')
c %= b  # Modulus Assignment
print(f'c %= b: {c}')
c **= b # Exponentiation Assignment
print(f'c **= b: {c}')
c //= b # Floor Division Assignment
print(f'c //= b: {c}')

# Bitwise Operators
print(f'\nBitwise Operators:')
print(f'a & b = {a & b}')  # Bitwise AND
print(f'a | b = {a | b}')  # Bitwise OR
print(f'a ^ b = {a ^ b}')  # Bitwise XOR
print(f'~a = {~a}')        # Bitwise NOT
print(f'a << 1 = {a << 1}') # Bitwise Left Shift
print(f'a >> 1 = {a >> 1}') # Bitwise Right Shift
