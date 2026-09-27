# Python Float (`float`)

## 1. What is a Float?

- A float represents a number that contains a fractional/decimal part.
- Floats can be positive, negative, or zero.
- The type of a floating-point object is `float`.

Examples:

```python
price = 99.50
temperature = 36.5
cgpa = 8.43
negative = -10.5
zero = 0.0

print(type(price))
print(type(cgpa))

Output:

<class 'float'>
<class 'float'>

Examples of floats:

10.5
-2.75
8.43
0.0
2. Integer vs Float

A number with .0 is still a float.

x = 10
y = 10.0

print(type(x))
print(type(y))

Output:

<class 'int'>
<class 'float'>

So:

10   → int
10.0 → float

The numerical value is the same, but the data types are different.

3. Creating Float Values

We can create a float simply by writing a decimal number.

price = 99.50
cgpa = 8.43

print(price)
print(cgpa)

Output:

99.5
8.43

Python removes unnecessary trailing zeros when displaying the value.

For example:

x = 99.50

print(x)

Output:

99.5
4. Positive, Negative and Zero Floats

A float can be positive, negative, or zero.

a = 10.5
b = -10.5
c = 0.0

print(a)
print(b)
print(c)

Output:

10.5
-10.5
0.0
5. Scientific Notation

Python allows floating-point numbers to be written using scientific notation.

We use e or E.

x = 2e3

print(x)

Output:

2000.0

Here:

2e3
= 2 × 10³
= 2000.0

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
6. Float Arithmetic

Floats support normal arithmetic operations.

a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

Output:

13.0
8.0
26.25
4.2

Important operators:

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Remainder
**  Power
7. Floor Division with Floats

// can also be used with floating-point numbers.

print(10.5 // 2)

# Output:
# 5.0

Notice that the result is:

5.0

not:

5

because the operation involves floats.

For negative values, floor division still goes toward negative infinity:

print(-10.5 // 2)

# Output:
# -6.0
8. Modulus with Floats

The % operator can also be used with floats.

print(10.5 % 3)

# Output:
# 1.5

Because:

10.5 = 3 × 3 + 1.5

So the remainder is 1.5.

9. Integer and Float Together

Python allows integers and floats to be used in the same arithmetic expression.

a = 10
b = 2.5

result = a + b

print(result)
print(type(result))

Output:

12.5
<class 'float'>

Generally:

int + float → float
int - float → float
int * float → float
10. Converting to Float

The float() function can convert suitable values into floats.

Integer to Float
x = float(10)

print(x)
print(type(x))

Output:

10.0
<class 'float'>
String to Float
x = float("25.5")

print(x)
print(type(x))

Output:

25.5
<class 'float'>

The string must contain a valid numeric representation.

11. Float to Integer

We can use int() to convert a float into an integer.

x = 10.8

print(int(x))

# Output:
# 10

Important:

int() does not round the number.

It removes the fractional part toward zero.

10.8  → 10
10.2  → 10
-10.8 → -10
-10.2 → -10

For rounding, Python provides functions such as round().

print(round(10.8))
print(round(10.2))

# Output:
# 11
# 10

So:

int()   → removes fractional part
round() → rounds the value
12. Floating-Point Precision

One of the most important things to understand about floats is that many decimal numbers cannot be represented exactly in binary floating-point format.

For example:

print(0.1 + 0.2)

Output:

0.30000000000000004

We might expect:

0.3

but the result contains a tiny representation difference.

This happens because computers store floating-point values using binary representation, and values such as 0.1 and 0.2 cannot be represented exactly in that format.

This is a limitation of floating-point representation, not an error in Python's addition.

13. Comparing Floating-Point Values

Because of floating-point precision, direct comparison can sometimes give unexpected results.

print(0.1 + 0.2 == 0.3)

# Output:
# False

When comparing calculated floating-point values, math.isclose() can be useful.

import math

result = 0.1 + 0.2

print(math.isclose(result, 0.3))

# Output:
# True
14. Special Float Values

Python floats can represent special values such as infinity and NaN.

Positive Infinity
x = float("inf")

print(x)

# Output:
# inf
Negative Infinity
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

NaN has special comparison behavior:

x = float("nan")

print(x == x)

# Output:
# False
15. Checking the Type

We can use type():

x = 10.5

print(type(x))

# Output:
# <class 'float'>

We can also use isinstance():

x = 10.5

print(isinstance(x, float))

# Output:
# True
16. Floats are Immutable

Float objects are immutable.

This means an existing float object cannot be changed.

x = 10.5

x = x + 2.5

print(x)

# Output:
# 13.0

The original float object is not modified. Python creates/uses another float value and makes x refer to it.

So:

Immutable object
       ↓
Existing value cannot be changed
       ↓
A new value is created when needed
17. Floats are Hashable

Float objects are hashable, so they can generally be used as:

Dictionary keys
Set elements

Example:

data = {
    8.43: "CGPA"
}

print(data[8.43])

# Output:
# CGPA

They can also be stored in a set:

numbers = {1.5, 2.5, 3.5}

print(numbers)

# Output:
# {1.5, 2.5, 3.5}
18. Comparing Floats

Floats support comparison operators.

a = 10.5
b = 20.5

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

Output:

False
True
True
False
True
False

The result of a comparison is a Boolean value.

float comparison
       ↓
True / False
       ↓
bool
19. float and Boolean Values

Since bool is a subclass of int, Boolean values can participate in arithmetic involving floats.

print(True + 2.5)
print(False + 2.5)

Output:

3.5
2.5

Conceptually:

True  → 1
False → 0
20. Important Points
float represents floating-point numbers.
Floats can be positive, negative, or zero.
10 is an int, while 10.0 is a float.
Scientific notation can be used with floats.
/ produces a floating-point result.
// performs floor division.
% returns the remainder.
float() converts suitable values to floats.
int() removes the fractional part; it does not round.
round() can be used when rounding is required.
Floating-point numbers have limited precision.
0.1 + 0.2 demonstrates floating-point representation limitations.
math.isclose() can be useful for comparing calculated float values.
Floats can represent inf, -inf, and nan.
Float objects are immutable.
Floats are hashable.
type() and isinstance() can be used to check the type.
Quick Revision
float
│
├── Decimal / fractional values
│   ├── 10.5
│   ├── -2.75
│   └── 8.43
│
├── Scientific notation
│   ├── 2e3
│   └── 2.5e-3
│
├── Arithmetic
│   ├── +
│   ├── -
│   ├── *
│   ├── /
│   ├── //
│   ├── %
│   └── **
│
├── Conversion
│   ├── float()
│   └── int()
│
├── Special values
│   ├── inf
│   ├── -inf
│   └── nan
│
├── Immutable
└── Hashable