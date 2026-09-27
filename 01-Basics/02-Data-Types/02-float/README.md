1. What is a Float?

A float represents numbers that contain a fractional/decimal part.

Examples:

price = 99.50
temperature = 36.5
cgpa = 8.43

Their type is float.

cgpa = 8.43

print(type(cgpa))

# Output:
# <class 'float'>

A float can also represent whole-number-looking values when written with .0:

x = 10.0

print(type(x))

# Output:
# <class 'float'>

Notice the difference:

x = 10
y = 10.0

print(type(x))
print(type(y))

# Output:
# <class 'int'>
# <class 'float'>

So 10 and 10.0 have the same numerical value, but they are different types.

2. Positive and Negative Floats

A float can be positive, negative, or zero.

a = 10.5
b = -10.5
c = 0.0

print(a)
print(b)
print(c)

# Output:
# 10.5
# -10.5
# 0.0
3. Scientific Notation

Python allows floats to be written using scientific notation.

We use e or E.

x = 2e3

print(x)

# Output:
# 2000.0

Here:

2e3

means:

2 × 10³
= 2000

Another example:

x = 1.5e2

print(x)

# Output:
# 150.0

We can also represent very small numbers:

x = 2.5e-3

print(x)

# Output:
# 0.0025
4. Arithmetic Operations with Floats

Floats can be used with normal arithmetic operators.

a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Output:
# 13.0
# 8.0
# 26.25
# 4.2

The result is generally a float when floating-point values are involved.

5. Float and Integer Together

Python allows arithmetic between int and float.

a = 10
b = 2.5

result = a + b

print(result)
print(type(result))

# Output:
# 12.5
# <class 'float'>

Here:

int + float → float

Similarly:

result = 10 * 2.5

print(result)

# Output:
# 25.0
6. Converting to Float

We can use float() to convert suitable values into a floating-point number.

Integer → Float
x = float(10)

print(x)
print(type(x))

# Output:
# 10.0
# <class 'float'>
String → Float
x = float("25.5")

print(x)

# Output:
# 25.5

But the string must contain a valid numeric representation.

float("25.5")   # valid

while:

float("hello")  # ValueError
7. Converting Float to Integer

We can use int() to convert a float into an integer.

x = 10.8

print(int(x))

# Output:
# 10

Python does not round the value.

It removes the fractional part.

10.8 → 10
10.2 → 10
-10.8 → -10

This is called truncation toward zero.

8. The Important 0.1 + 0.2 Problem

One of the most important things to understand about floats is floating-point precision.

You might expect:

print(0.1 + 0.2)

to produce:

0.3

But Python gives:

0.30000000000000004

Why?

Computers store floating-point numbers using a binary representation. Many decimal fractions, including 0.1 and 0.2, cannot be represented exactly in that binary format.

So the computer stores very close approximations.

For example, conceptually:

0.1 → very close to 0.1
0.2 → very close to 0.2

When they are added, the tiny representation difference can become visible:

result = 0.1 + 0.2

print(result)

# Output:
# 0.30000000000000004

This does not mean Python's addition is wrong.

It is a limitation of representing many decimal fractions in binary floating-point format.

9. Comparing Floats

Because of floating-point precision, directly comparing calculated floats can sometimes cause unexpected results.

For example:

print(0.1 + 0.2 == 0.3)

# Output:
# False

For situations where precision matters, Python provides tools such as math.isclose().

import math

print(math.isclose(0.1 + 0.2, 0.3))

# Output:
# True
10. Special Float Values

Python floats can also represent special values.

Infinity
x = float("inf")

print(x)

# Output:
# inf

Negative infinity:

x = float("-inf")

print(x)

# Output:
# -inf
NaN

NaN means Not a Number.

x = float("nan")

print(x)

# Output:
# nan

NaN has some special comparison behavior:

x = float("nan")

print(x == x)

# Output:
# False
11. Checking Whether a Value is a Float

Using type():

x = 10.5

print(type(x))

# Output:
# <class 'float'>

Using isinstance():

x = 10.5

print(isinstance(x, float))

# Output:
# True
12. Important Points
float represents floating-point numbers.
Floats can be positive, negative, or zero.
10 is an int, while 10.0 is a float.
Floats can be written using scientific notation.
float() converts suitable values to floats.
int() removes the fractional part; it does not round.
Floating-point numbers have limited precision.
0.1 + 0.2 demonstrates floating-point representation issues.
math.isclose() can be useful when comparing calculated floating-point values.
Python floats can represent inf, -inf, and nan.
Simple way to remember
float
  ↓
Numbers with fractional/decimal values
  ↓
10.5
-2.75
8.43
0.001