# Python Float (`float`)

## 1. What is a Float?

- A float represents a number that contains a fractional/decimal part.
- Floats can be positive, negative, or zero.
- The type of a floating-point object is `float`.

Examples:

```python
10.5
3.14
0.5
-2.75
100.0
```

Example:

```python
price = 99.99
temperature = 36.5
percentage = 92.5

print(price)
print(temperature)
print(percentage)
```

Output:

```text
99.99
36.5
92.5
```

All three values are `float`.

---

# 2. Checking the Type

Use `type()` to check whether a value is a float.

```python
x = 10.5

print(type(x))
```

Output:

```text
<class 'float'>
```

Example:

```python
print(type(10.5))
print(type(3.14))
print(type(-2.5))
```

Output:

```text
<class 'float'>
<class 'float'>
<class 'float'>
```

---

# 3. Creating Float Values

A float can be created by writing a number with a decimal point.

```python
a = 10.5
b = 20.75
c = -5.25
d = 0.0
```

All of these are `float`.

```python
print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

Output:

```text
<class 'float'>
<class 'float'>
<class 'float'>
<class 'float'>
```

---

# 4. Float Can Be Positive, Negative or Zero

### Positive float

```python
x = 10.5
```

### Negative float

```python
x = -10.5
```

### Zero float

```python
x = 0.0
```

All are `float`.

```python
print(type(10.5))
print(type(-10.5))
print(type(0.0))
```

Output:

```text
<class 'float'>
<class 'float'>
<class 'float'>
```

---

# 5. `10` vs `10.0`

This is an important difference.

```python
a = 10
b = 10.0

print(type(a))
print(type(b))
```

Output:

```text
<class 'int'>
<class 'float'>
```

Even though both represent the value `10` mathematically:

```text
10   → int
10.0 → float
```

The decimal point makes `10.0` a float.

---

# 6. Float is Immutable

`float` objects are **immutable**.

This means an existing float object cannot be modified.

Example:

```python
x = 10.5

x = x + 2.5

print(x)
```

Output:

```text
13.0
```

It may look like `10.5` was changed.

But conceptually:

```text
Before:

x ───→ 10.5


After:

x ───→ 13.0
```

The original float object was not modified.

The variable `x` was made to refer to another value.

---

# 7. Reassigning a Float

Although float objects are immutable, variables can be reassigned.

```python
x = 10.5

x = 20.5

print(x)
```

Output:

```text
20.5
```

Remember:

> Immutable means the object cannot be modified. It does not mean the variable cannot be reassigned.

---

# 8. Arithmetic Operations with Floats

Floats support arithmetic operations.

```python
a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Example output:

```text
13.0
8.0
26.25
4.2
4.0
0.5
...
```

The exact result of exponentiation depends on the values.

---

# 9. Addition

```python
a = 10.5
b = 5.5

print(a + b)
```

Output:

```text
16.0
```

---

# 10. Subtraction

```python
a = 10.5
b = 3.5

print(a - b)
```

Output:

```text
7.0
```

---

# 11. Multiplication

```python
a = 2.5
b = 4

print(a * b)
```

Output:

```text
10.0
```

Notice that the result is a float.

---

# 12. Division

The `/` operator produces a float.

```python
print(10 / 2)
```

Output:

```text
5.0
```

Even though both operands are integers:

```text
10 → int
2  → int
```

the result of `/` is:

```text
5.0 → float
```

---

# 13. Floor Division with Float

`//` performs floor division.

```python
print(10.5 // 2)
```

Output:

```text
5.0
```

The result can still be a float when a float operand is involved.

Another example:

```python
print(7.5 // 2.0)
```

Output:

```text
3.0
```

### Important

Floor division means:

> Take the floor of the mathematical division result.

For negative values:

```python
print(-7.5 // 2)
```

Output:

```text
-4.0
```

Because:

```text
-7.5 / 2 = -3.75
```

and:

```text
floor(-3.75) = -4
```

---

# 14. Modulus `%`

The `%` operator gives the remainder.

```python
print(10.5 % 3)
```

Output:

```text
1.5
```

Because:

```text
10.5 = 3 × 3 + 1.5
```

So:

```text
Quotient  = 3
Remainder = 1.5
```

---

# 15. Power `**`

The `**` operator performs exponentiation.

```python
print(2.5 ** 2)
```

Output:

```text
6.25
```

Another example:

```python
print(4.0 ** 3)
```

Output:

```text
64.0
```

---

# 16. Float and Integer Arithmetic

When an integer and float are used together, the result is generally a float.

```python
a = 10
b = 2.5

result = a + b

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

Examples:

```python
print(10 + 2.5)
print(10 - 2.5)
print(10 * 2.5)
print(10 / 2)
```

Results:

```text
12.5
7.5
25.0
5.0
```

---

# 17. Converting Integer to Float

Use `float()`.

```python
x = 10

y = float(x)

print(y)
print(type(y))
```

Output:

```text
10.0
<class 'float'>
```

So:

```text
10 → 10.0
```

---

# 18. Converting String to Float

A numeric string can be converted to a float.

```python
x = float("10.5")

print(x)
print(type(x))
```

Output:

```text
10.5
<class 'float'>
```

Another example:

```python
price = float("99.99")

print(price)
```

Output:

```text
99.99
```

---

# 19. Converting Integer String to Float

Even an integer-looking string can be converted to float.

```python
x = float("10")

print(x)
```

Output:

```text
10.0
```

So:

```text
"10" → 10.0
```

---

# 20. Invalid String Conversion

A string that does not represent a valid number cannot normally be converted to float.

```python
x = float("hello")
```

This raises:

```text
ValueError
```

Similarly:

```python
float("10abc")
```

raises `ValueError`.

---

# 21. Converting Float to Integer

Use `int()`.

```python
x = 10.9

y = int(x)

print(y)
```

Output:

```text
10
```

Important:

> `int()` does not round the float. It truncates the fractional part toward zero.

Examples:

```python
print(int(10.9))
print(int(10.1))
print(int(-10.9))
print(int(-10.1))
```

Output:

```text
10
10
-10
-10
```

---

# 22. `round()` vs `int()`

These two are different.

### `int()`

Removes the fractional part.

```python
print(int(10.9))
```

Output:

```text
10
```

### `round()`

Rounds according to Python's rounding rules.

```python
print(round(10.9))
```

Output:

```text
11
```

Example:

```python
print(int(5.8))
print(round(5.8))
```

Output:

```text
5
6
```

---

# 23. Python's `round()` and `.5`

Python uses **round half to even** in the common case.

```python
print(round(10.5))
print(round(11.5))
```

Output:

```text
10
12
```

Why?

```text
10.5 → nearest even number = 10
11.5 → nearest even number = 12
```

This is an important behavior to know when working with `round()`.

---

# 24. Float to String

Use `str()`.

```python
x = 10.5

y = str(x)

print(y)
print(type(y))
```

Output:

```text
10.5
<class 'str'>
```

So:

```text
10.5 → float
"10.5" → string
```

---

# 25. Float to Boolean

Use `bool()`.

```python
print(bool(10.5))
print(bool(-2.5))
print(bool(0.0))
```

Output:

```text
True
True
False
```

The rule is:

```text
0.0 → False
any non-zero float → True
```

---

# 26. Float Truthiness

Floats can be used directly in conditions.

```python
if 10.5:
    print("True")
```

Output:

```text
True
```

But:

```python
if 0.0:
    print("True")
else:
    print("False")
```

Output:

```text
False
```

Remember:

```text
0.0       → False
10.5      → True
-10.5     → True
0.0001    → True
```

---

# 27. Comparison Operators

Floats can be compared using:

```text
>
<
>=
<=
==
!=
```

Example:

```python
a = 10.5
b = 20.5

print(a < b)
print(a > b)
print(a == b)
print(a != b)
```

Output:

```text
True
False
False
True
```

Comparison results are `bool`.

```python
result = 10.5 > 5.5

print(result)
print(type(result))
```

Output:

```text
True
<class 'bool'>
```

---

# 28. Float Equality Can Be Tricky

This is one of the most important concepts about floating-point numbers.

Consider:

```python
print(0.1 + 0.2 == 0.3)
```

The result is:

```text
False
```

This may look surprising.

Why?

Because many decimal fractions cannot be represented exactly using binary floating-point representation.

Python may internally represent these values approximately.

Conceptually:

```text
0.1 + 0.2
```

may be stored close to:

```text
0.30000000000000004
```

Therefore:

```python
0.1 + 0.2 == 0.3
```

can be `False`.

---

# 29. Why Floating-Point Precision Exists

Computers store floating-point numbers using a binary representation.

Binary can represent some values exactly, but many decimal fractions cannot be represented exactly.

For example:

```text
0.5
```

can be represented exactly in binary.

But values such as:

```text
0.1
0.2
0.3
```

generally cannot be represented exactly using ordinary binary floating-point representation.

Therefore, small rounding errors can occur.

---

# 30. Comparing Floats Safely

Instead of directly comparing calculated floating-point values, use a tolerance when appropriate.

Example:

```python
a = 0.1 + 0.2
b = 0.3

if abs(a - b) < 0.000001:
    print("Approximately equal")
```

Output:

```text
Approximately equal
```

Python also provides `math.isclose()`.

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))
```

Output:

```text
True
```

This is generally better for approximate floating-point comparisons.

---

# 31. Float Precision

A Python `float` normally uses a double-precision floating-point representation.

In typical Python implementations, this corresponds to the C `double` type.

It provides roughly:

```text
15–17 significant decimal digits
```

of precision.

Example:

```python
x = 1.2345678901234567

print(x)
```

You should not assume that every decimal digit you write can be stored exactly.

---

# 32. Very Large Float Values

Floats can represent very large values.

```python
x = 1.5e10

print(x)
```

Output:

```text
15000000000.0
```

The notation:

```text
1.5e10
```

means:

```text
1.5 × 10¹⁰
```

---

# 33. Scientific Notation

Python supports scientific notation.

Example:

```python
x = 2.5e3

print(x)
```

Output:

```text
2500.0
```

Because:

```text
2.5 × 10³ = 2500
```

Another example:

```python
x = 4.2e-3

print(x)
```

Output:

```text
0.0042
```

Because:

```text
4.2 × 10⁻³ = 0.0042
```

---

# 34. `e` in Float Values

The general form is:

```text
number e exponent
```

Examples:

```python
1e3
2.5e4
3.2e-2
```

Meaning:

```text
1e3   = 1 × 10³
2.5e4 = 2.5 × 10⁴
3.2e-2 = 3.2 × 10⁻²
```

These are floats.

```python
print(type(1e3))
```

Output:

```text
<class 'float'>
```

---

# 35. Special Float Values

Python floats can represent special values such as:

```text
inf
-inf
nan
```

These can be created using `float()`.

### Positive infinity

```python
x = float("inf")

print(x)
```

Output:

```text
inf
```

### Negative infinity

```python
x = float("-inf")

print(x)
```

Output:

```text
-inf
```

### NaN

```python
x = float("nan")

print(x)
```

Output:

```text
nan
```

`nan` means:

> Not a Number.

---

# 36. Checking Infinity and NaN

Use the `math` module.

```python
import math

x = float("inf")

print(math.isinf(x))
```

Output:

```text
True
```

For NaN:

```python
import math

x = float("nan")

print(math.isnan(x))
```

Output:

```text
True
```

---

# 37. Important Property of `nan`

`nan` behaves differently from ordinary numbers.

```python
x = float("nan")

print(x == x)
```

Output:

```text
False
```

This is an important special behavior.

For checking NaN, use:

```python
import math

math.isnan(x)
```

rather than:

```python
x == float("nan")
```

---

# 38. Infinity Operations

Example:

```python
x = float("inf")

print(x > 1000000)
```

Output:

```text
True
```

Positive infinity is greater than any finite number.

Similarly:

```python
x = float("-inf")

print(x < -1000000)
```

Output:

```text
True
```

---

# 39. `math` Functions with Floats

The `math` module provides many useful functions.

```python
import math
```

### Square root

```python
print(math.sqrt(25.0))
```

Output:

```text
5.0
```

### Ceiling

```python
print(math.ceil(10.2))
```

Output:

```text
11
```

### Floor

```python
print(math.floor(10.8))
```

Output:

```text
10
```

---

# 40. `math.floor()` vs `int()`

For positive numbers they can look similar:

```python
print(int(10.8))
print(math.floor(10.8))
```

Output:

```text
10
10
```

But with negative numbers they differ:

```python
print(int(-10.8))
print(math.floor(-10.8))
```

Output:

```text
-10
-11
```

Why?

```text
int(-10.8)        → truncates toward zero
math.floor(-10.8) → moves toward negative infinity
```

---

# 41. Float and `abs()`

`abs()` returns the absolute value.

```python
print(abs(-10.5))
```

Output:

```text
10.5
```

Example:

```python
temperature = -5.5

print(abs(temperature))
```

Output:

```text
5.5
```

---

# 42. Float and `pow()`

```python
print(pow(2.5, 2))
```

Output:

```text
6.25
```

Equivalent to:

```python
print(2.5 ** 2)
```

---

# 43. Float and `round()`

You can specify the number of decimal places.

```python
x = 10.56789

print(round(x, 2))
```

Output:

```text
10.57
```

Another example:

```python
price = 99.999

print(round(price, 2))
```

Output:

```text
100.0
```

---

# 44. Formatting Floats

You can control how a float is displayed.

Using an f-string:

```python
price = 99.98765

print(f"{price:.2f}")
```

Output:

```text
99.99
```

Here:

```text
.2f
```

means:

> Display the number with 2 digits after the decimal point.

Examples:

```python
x = 10.5

print(f"{x:.1f}")
print(f"{x:.2f}")
print(f"{x:.3f}")
```

Output:

```text
10.5
10.50
10.500
```

---

# 45. Formatting Does Not Change the Original Type

Example:

```python
x = 10.5

formatted = f"{x:.2f}"

print(formatted)
print(type(formatted))
```

Output:

```text
10.50
<class 'str'>
```

The formatted result is a string.

The original `x` is still a float.

---

# 46. Float Input from User

`input()` always returns a string.

Example:

```python
price = input("Enter price: ")

print(type(price))
```

If the user enters:

```text
99.99
```

the type is:

```text
<class 'str'>
```

To get a float:

```python
price = float(input("Enter price: "))

print(type(price))
```

Now the type is:

```text
<class 'float'>
```

---

# 47. Practical Example: Average Marks

```python
marks1 = 80
marks2 = 90
marks3 = 85

average = (marks1 + marks2 + marks3) / 3

print(average)
```

Output:

```text
85.0
```

---

# 48. Practical Example: Simple Interest

Formula:

```text
SI = (P × R × T) / 100
```

Python:

```python
p = 10000
r = 5.5
t = 2

si = (p * r * t) / 100

print(si)
```

Output:

```text
1100.0
```

---

# 49. Practical Example: Temperature Conversion

Celsius to Fahrenheit:

```text
F = (C × 9/5) + 32
```

Python:

```python
celsius = 37.5

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)
```

Output:

```text
99.5
```

---

# 50. Practical Example: Calculate Percentage

```python
obtained = 450
total = 500

percentage = (obtained / total) * 100

print(percentage)
```

Output:

```text
90.0
```

---

# 51. Practical Example: Calculate Area of Circle

Formula:

```text
Area = π × r²
```

Python:

```python
import math

radius = 5.5

area = math.pi * radius ** 2

print(area)
```

Output will be approximately:

```text
95.03317777109125
```

For displaying two decimal places:

```python
print(f"{area:.2f}")
```

Output:

```text
95.03
```

---

# 52. Float and Lists

Floats can be stored inside lists.

```python
prices = [10.5, 20.75, 30.25]

print(prices)
```

Output:

```text
[10.5, 20.75, 30.25]
```

A list can contain different data types:

```python
data = [10, 10.5, "Python", True]

print(data)
```

---

# 53. Float as Dictionary Value

Floats can be dictionary values.

```python
student = {
    "name": "Teja",
    "percentage": 85.5
}

print(student["percentage"])
```

Output:

```text
85.5
```

Floats can also be dictionary keys because they are hashable.

```python
data = {
    10.5: "Python"
}

print(data[10.5])
```

Output:

```text
Python
```

---

# 54. Float is Hashable

A float is hashable.

```python
x = 10.5

print(hash(x))
```

Because floats are hashable, they can be used as:

```text
Dictionary keys ✔
Set elements ✔
```

Example:

```python
numbers = {10.5, 20.5, 30.5}

print(numbers)
```

---

# 55. Float and `is`

Like integers, don't use `is` to compare float values.

Use:

```python
a == b
```

for value comparison.

Example:

```python
a = 10.5
b = 10.5

print(a == b)
```

The important concept is:

```text
== → compares values
is → compares object identity
```

---

# 56. Float and `bool`

Float values can be converted to boolean.

```python
print(bool(0.0))
print(bool(1.5))
print(bool(-1.5))
```

Output:

```text
False
True
True
```

Rule:

```text
0.0        → False
non-zero   → True
```

---

# 57. Float vs Integer

| Feature | `int` | `float` |
|---|---|---|
| Example | `10` | `10.5` |
| Decimal point | No | Usually yes |
| Fractional values | No | Yes |
| Mutable | No | No |
| Hashable | Yes | Yes |
| Dictionary key | Yes | Yes |
| Set element | Yes | Yes |
| Precision issue | Generally exact for integer values | Floating-point precision can occur |
| Division `/` | Produces float | Produces float |

---

# 58. Float vs String

```python
a = 10.5
b = "10.5"
```

They are different:

```text
10.5   → float
"10.5" → str
```

Therefore:

```python
print(a + 2.5)
```

works.

But:

```python
print(b + 2.5)
```

raises:

```text
TypeError
```

Convert the string first:

```python
b = float("10.5")

print(b + 2.5)
```

Output:

```text
13.0
```

---

# 59. Important Float Characteristics

Remember these points:

```text
1. float represents floating-point numbers.
2. Floats can represent fractional values.
3. float is immutable.
4. float is hashable.
5. Floats can be dictionary keys.
6. Floats can be set elements.
7. / returns a float.
8. // performs floor division.
9. % returns the remainder.
10. ** performs exponentiation.
11. float() converts compatible values to float.
12. 0.0 is falsy.
13. Non-zero floats are truthy.
14. Floating-point precision can cause small errors.
15. math.isclose() can be used for approximate comparisons.
16. inf, -inf and nan are special float values.
17. f-string formatting produces a string.
```

---

# 60. Common Mistakes

### Mistake 1: Confusing `10` and `10.0`

```text
10   → int
10.0 → float
```

---

### Mistake 2: Expecting `int()` to round

```python
int(10.9)
```

returns:

```text
10
```

not:

```text
11
```

---

### Mistake 3: Directly comparing calculated floats

Avoid relying on:

```python
0.1 + 0.2 == 0.3
```

when exact decimal equality is important.

Use an appropriate tolerance or:

```python
math.isclose()
```

---

### Mistake 4: Forgetting `input()` returns string

```python
price = input()
```

gives a string.

Use:

```python
price = float(input())
```

when a floating-point value is required.

---

### Mistake 5: Thinking formatting keeps the result as float

```python
x = f"{10.5:.2f}"
```

`x` is a string:

```text
<class 'str'>
```

---

### Mistake 6: Confusing `int()` with `math.floor()`

For negative values:

```python
int(-10.8)        # -10
math.floor(-10.8) # -11
```

They are not the same operation.

---

# 61. Important Float Functions

| Function | Purpose | Example |
|---|---|---|
| `float()` | Convert to float | `float("10.5")` |
| `int()` | Convert to integer | `int(10.5)` |
| `str()` | Convert to string | `str(10.5)` |
| `bool()` | Convert to Boolean | `bool(10.5)` |
| `abs()` | Absolute value | `abs(-10.5)` |
| `round()` | Round value | `round(10.56, 1)` |
| `pow()` | Power | `pow(2.5, 2)` |
| `type()` | Check type | `type(10.5)` |
| `isinstance()` | Check instance | `isinstance(10.5, float)` |
| `hash()` | Get hash | `hash(10.5)` |

---

# 62. Useful `math` Functions

```python
import math
```

| Function | Purpose |
|---|---|
| `math.sqrt()` | Square root |
| `math.ceil()` | Round upward |
| `math.floor()` | Round downward |
| `math.isclose()` | Compare approximately |
| `math.isinf()` | Check infinity |
| `math.isnan()` | Check NaN |
| `math.pi` | Value of π |
| `math.e` | Euler's number |

---

# 63. Quick Revision

```text
float
│
├── Floating-point number
│
├── Examples
│   ├── 10.5
│   ├── 3.14
│   ├── -2.5
│   └── 0.0
│
├── Immutable
│
├── Hashable
│
├── /  → float
├── // → floor division
├── %  → remainder
├── ** → power
│
├── 0.0      → False
├── non-zero → True
│
└── Floating-point precision
    └── use math.isclose() when appropriate
```

---

# 64. One-Line Definition

> **`float` is an immutable Python data type used to represent floating-point numbers, including fractional and decimal values.**

---

# 65. Final Example

```python
price = 99.99
quantity = 2

total = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
print("Type:", type(total))

print(f"Formatted Total: {total:.2f}")
```

Output:

```text
Price: 99.99
Quantity: 2
Total: 199.98
Type: <class 'float'>
Formatted Total: 199.98
```

### Final Mental Model

```text
float
  ↓
Decimal / fractional values
  ↓
Immutable
  ↓
Hashable
  ↓
Supports arithmetic
  ↓
Can have floating-point precision issues
  ↓
Useful for measurements,
percentages, averages, prices,
scientific calculations, etc.
```