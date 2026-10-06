# Python `complex` Data Type

## 1. What is `complex`?

`complex` is a Python data type used to represent **complex numbers**.

A complex number has two parts:

```text
real part + imaginary part
```

The general form is:

```text
a + bj
```

where:

```text
a → real part
b → imaginary part
j → imaginary unit
```

Example:

```python
z = 3 + 4j

print(z)
```

Output:

```text
(3+4j)
```

Here:

```text
3 → real part
4 → imaginary part
```

---

# 2. Why is `j` Used?

In mathematics, the imaginary unit is commonly represented by `i`.

Mathematically:

```text
i = √-1
```

Python uses **`j`** instead of `i`.

So:

```text
3 + 4j
```

means:

```text
3 + 4i
```

in mathematical notation.

In Python:

```python
z = 3 + 4j
```

The `j` tells Python that `4` is the imaginary part.

---

# 3. Creating Complex Numbers

The simplest way is to write a real number followed by `j`.

```python
z = 3 + 4j

print(z)
```

Output:

```text
(3+4j)
```

More examples:

```python
a = 5 + 2j
b = -3 + 4j
c = 2 - 7j
d = 4j
```

All are complex numbers.

---

# 4. Checking the Type

Use `type()`.

```python
z = 3 + 4j

print(type(z))
```

Output:

```text
<class 'complex'>
```

Therefore:

```python
type(3 + 4j)
```

returns:

```text
<class 'complex'>
```

---

# 5. Real and Imaginary Parts

A complex number has:

```text
real part
imaginary part
```

Example:

```python
z = 3 + 4j
```

Here:

```text
Real part      = 3
Imaginary part = 4
```

Python provides:

```python
.real
.imag
```

to access them.

Example:

```python
z = 3 + 4j

print(z.real)
print(z.imag)
```

Output:

```text
3.0
4.0
```

Notice that the real and imaginary parts are returned as `float`.

---

# 6. `.real` Attribute

The `.real` attribute returns the real part.

```python
z = 10 + 5j

print(z.real)
```

Output:

```text
10.0
```

Another example:

```python
z = -7 + 3j

print(z.real)
```

Output:

```text
-7.0
```

---

# 7. `.imag` Attribute

The `.imag` attribute returns the imaginary part.

```python
z = 10 + 5j

print(z.imag)
```

Output:

```text
5.0
```

Example:

```python
z = 8 - 2j

print(z.imag)
```

Output:

```text
-2.0
```

---

# 8. Purely Real Complex Number

A complex number can have an imaginary part of zero.

```python
z = 5 + 0j

print(z)
print(z.real)
print(z.imag)
```

Output:

```text
(5+0j)
5.0
0.0
```

Although mathematically this is just `5`, Python considers:

```python
5 + 0j
```

a `complex`.

---

# 9. Purely Imaginary Complex Number

A complex number can have a real part of zero.

```python
z = 4j

print(z)
print(z.real)
print(z.imag)
```

Output:

```text
4j
0.0
4.0
```

So:

```text
4j
```

means:

```text
0 + 4j
```

---

# 10. Negative Imaginary Part

Python allows negative imaginary parts.

```python
z = 5 - 3j

print(z)
```

Output:

```text
(5-3j)
```

Here:

```text
Real part      = 5
Imaginary part = -3
```

Check:

```python
print(z.real)
print(z.imag)
```

Output:

```text
5.0
-3.0
```

---

# 11. Complex Number with Negative Real Part

```python
z = -5 + 3j

print(z)
```

Output:

```text
(-5+3j)
```

Here:

```text
Real part      = -5
Imaginary part = 3
```

---

# 12. Both Parts Can Be Negative

```python
z = -5 - 3j

print(z)
```

Output:

```text
(-5-3j)
```

So both components can be positive or negative.

---

# 13. Complex Number Using `complex()`

Python provides the built-in `complex()` function.

Basic form:

```python
complex(real, imaginary)
```

Example:

```python
z = complex(3, 4)

print(z)
```

Output:

```text
(3+4j)
```

This is equivalent to:

```python
z = 3 + 4j
```

---

# 14. `complex()` with Only One Argument

```python
z = complex(5)

print(z)
```

Output:

```text
(5+0j)
```

So:

```text
complex(5)
```

creates:

```text
5 + 0j
```

---

# 15. `complex()` with No Arguments

```python
z = complex()

print(z)
```

Output:

```text
0j
```

So:

```python
complex()
```

creates:

```text
0 + 0j
```

---

# 16. Creating Complex Numbers from Strings

A string representing a complex number can be passed to `complex()`.

```python
z = complex("3+4j")

print(z)
```

Output:

```text
(3+4j)
```

Another example:

```python
z = complex("5-2j")

print(z)
```

Output:

```text
(5-2j)
```

---

# 17. Invalid Complex String

The string must represent a valid complex number.

For example:

```python
z = complex("hello")
```

raises:

```text
ValueError
```

Similarly:

```python
complex("3+4")
```

does not mean a complex number in the same way as:

```python
complex("3+4j")
```

---

# 18. Complex Numbers Are Immutable

`complex` objects are **immutable**.

This means an existing complex object cannot be modified.

Example:

```python
z = 3 + 4j

z = z + 2 + 1j

print(z)
```

Output:

```text
(5+5j)
```

Conceptually:

```text
Before:

z ───→ 3 + 4j


After:

z ───→ 5 + 5j
```

The original complex object was not changed.

The variable was reassigned to another complex value.

---

# 19. Reassigning a Complex Variable

```python
z = 3 + 4j

z = 10 + 20j

print(z)
```

Output:

```text
(10+20j)
```

Again:

> Immutable object does not mean the variable cannot be reassigned.

---

# 20. Complex Addition

Complex numbers support addition.

Example:

```python
a = 3 + 4j
b = 2 + 5j

result = a + b

print(result)
```

Output:

```text
(5+9j)
```

Calculation:

```text
(3 + 4j) + (2 + 5j)

= (3 + 2) + (4 + 5)j

= 5 + 9j
```

---

# 21. Complex Subtraction

```python
a = 5 + 7j
b = 2 + 3j

print(a - b)
```

Output:

```text
(3+4j)
```

Calculation:

```text
(5 + 7j) - (2 + 3j)

= (5 - 2) + (7 - 3)j

= 3 + 4j
```

---

# 22. Complex Multiplication

Complex numbers can also be multiplied.

```python
a = 2 + 3j
b = 4 + 5j

print(a * b)
```

Output:

```text
(-7+22j)
```

Let's understand it:

```text
(2 + 3j)(4 + 5j)

= 8 + 10j + 12j + 15j²
```

Since:

```text
j² = -1
```

we get:

```text
= 8 + 22j - 15

= -7 + 22j
```

Therefore:

```text
(2 + 3j)(4 + 5j) = -7 + 22j
```

---

# 23. Important Rule: `j² = -1`

This is the most important mathematical property behind complex numbers.

```text
j² = -1
```

Therefore:

```text
j × j = -1
```

Example:

```python
z = 1j

print(z * z)
```

Output:

```text
(-1+0j)
```

Because:

```text
j × j = -1
```

---

# 24. Complex Division

Complex numbers also support division.

```python
a = 4 + 2j
b = 1 + 1j

print(a / b)
```

Output:

```text
(3-1j)
```

The mathematical process involves multiplying the numerator and denominator by the **complex conjugate** of the denominator.

For:

```text
1 + j
```

the conjugate is:

```text
1 - j
```

This removes the imaginary part from the denominator.

---

# 25. Complex Modulus

The magnitude or modulus of:

```text
a + bj
```

is:

```text
√(a² + b²)
```

Example:

```text
3 + 4j
```

Magnitude:

```text
√(3² + 4²)

= √(9 + 16)

= √25

= 5
```

Python provides:

```python
abs()
```

for this.

```python
z = 3 + 4j

print(abs(z))
```

Output:

```text
5.0
```

---

# 26. `abs()` with Complex Numbers

`abs()` returns the magnitude.

```python
z = 5 + 12j

print(abs(z))
```

Output:

```text
13.0
```

Because:

```text
√(5² + 12²)
= √169
= 13
```

The result is a `float`.

---

# 27. Complex Conjugate

The conjugate of:

```text
a + bj
```

is:

```text
a - bj
```

Example:

```text
3 + 4j
```

has conjugate:

```text
3 - 4j
```

Python provides the `.conjugate()` method.

```python
z = 3 + 4j

print(z.conjugate())
```

Output:

```text
(3-4j)
```

---

# 28. Another Conjugate Example

```python
z = 5 - 7j

print(z.conjugate())
```

Output:

```text
(5+7j)
```

The sign of the imaginary part changes.

```text
3 + 4j → 3 - 4j
3 - 4j → 3 + 4j
```

---

# 29. Complex Number and `type()`

```python
z = 3 + 4j

print(type(z))
```

Output:

```text
<class 'complex'>
```

The `complex` type is one of Python's built-in numeric types.

---

# 30. Checking with `isinstance()`

```python
z = 3 + 4j

print(isinstance(z, complex))
```

Output:

```text
True
```

Example:

```python
x = 10

print(isinstance(x, complex))
```

Output:

```text
False
```

---

# 31. Complex Numbers Are Numeric

Python's numeric types include:

```text
int
float
complex
```

Conceptually:

```text
Numbers
│
├── int
├── float
└── complex
```

Example:

```python
a = 10
b = 10.5
c = 3 + 4j

print(type(a))
print(type(b))
print(type(c))
```

---

# 32. Complex and Integer

Python can perform arithmetic between integers and complex numbers.

```python
z = 3 + 4j

print(z + 5)
```

Output:

```text
(8+4j)
```

The integer:

```text
5
```

is treated as:

```text
5 + 0j
```

---

# 33. Complex and Float

Floats can also participate in complex arithmetic.

```python
z = 3 + 4j

print(z + 2.5)
```

Output:

```text
(5.5+4j)
```

Conceptually:

```text
3 + 4j
+
2.5 + 0j
-----------
5.5 + 4j
```

---

# 34. Complex Numbers Do Not Support Ordering

This is an important difference between complex numbers and `int`/`float`.

You cannot normally use:

```text
>
<
>=
<=
```

between complex numbers.

For example:

```python
a = 3 + 4j
b = 2 + 5j

print(a > b)
```

raises:

```text
TypeError
```

Why?

Because complex numbers do not have a natural ordering like ordinary real numbers.

---

# 35. Equality Works with Complex Numbers

Although ordering does not work, equality comparison does.

```python
a = 3 + 4j
b = 3 + 4j

print(a == b)
```

Output:

```text
True
```

And:

```python
print(a != b)
```

Output:

```text
False
```

So:

```text
== → supported
!= → supported
<  → not supported
>  → not supported
<= → not supported
>= → not supported
```

---

# 36. Complex Numbers and `is`

Use `==` for value comparison.

```python
a = 3 + 4j
b = 3 + 4j

print(a == b)
```

`==` compares the values.

`is` checks whether two variables refer to the same object.

Therefore:

> Use `==` when comparing complex-number values.

---

# 37. Complex Numbers Are Hashable

Complex numbers are hashable.

You can check:

```python
z = 3 + 4j

print(hash(z))
```

This allows complex numbers to be used as:

- set elements
- dictionary keys

Example:

```python
numbers = {3 + 4j, 5 + 2j}

print(numbers)
```

---

# 38. Complex Number as Dictionary Key

```python
data = {
    3 + 4j: "Point A"
}

print(data[3 + 4j])
```

Output:

```text
Point A
```

Complex numbers are immutable and hashable, so they can be used as dictionary keys.

---

# 39. Complex Number in a Set

```python
numbers = {3 + 4j, 2 + 5j}

print(numbers)
```

A complex number can be a set element because it is hashable.

---

# 40. Complex Numbers Are Immutable and Hashable

These two properties are connected to how complex numbers can be used.

```text
complex
│
├── Immutable
│
└── Hashable
    │
    ├── Dictionary key ✔
    └── Set element ✔
```

---

# 41. Complex Number Truthiness

A complex number is considered:

```text
0 + 0j → False
anything else → True
```

Example:

```python
print(bool(0 + 0j))
print(bool(3 + 4j))
```

Output:

```text
False
True
```

Another example:

```python
if 3 + 4j:
    print("True")
```

Output:

```text
True
```

---

# 42. Zero Complex Number

The zero complex number is:

```text
0j
```

Example:

```python
z = 0j

print(z)
print(bool(z))
```

Output:

```text
0j
False
```

---

# 43. Complex Number with Only Imaginary Part

```python
z = 5j

print(z)
print(z.real)
print(z.imag)
```

Output:

```text
5j
0.0
5.0
```

Remember:

```text
5j = 0 + 5j
```

---

# 44. Complex Number with Only Real Part

```python
z = 5 + 0j

print(z)
```

Output:

```text
(5+0j)
```

The type is still:

```text
complex
```

```python
print(type(z))
```

Output:

```text
<class 'complex'>
```

---

# 45. Complex Number Conversion

Use `complex()` to convert compatible values.

### Integer

```python
print(complex(10))
```

Output:

```text
(10+0j)
```

### Float

```python
print(complex(10.5))
```

Output:

```text
(10.5+0j)
```

### String

```python
print(complex("3+4j"))
```

Output:

```text
(3+4j)
```

---

# 46. Converting Complex to Integer

You cannot directly convert a complex number to `int`.

For example:

```python
int(3 + 4j)
```

raises:

```text
TypeError
```

Why?

Because a complex number contains both a real and imaginary component, and Python does not automatically decide which information should be discarded.

---

# 47. Converting Complex to Float

Similarly:

```python
float(3 + 4j)
```

raises:

```text
TypeError
```

You must explicitly choose what you want.

For example:

```python
z = 3 + 4j

print(z.real)
```

Output:

```text
3.0
```

Or:

```python
print(z.imag)
```

Output:

```text
4.0
```

---

# 48. Complex Input from User

`input()` returns a string.

To create a complex number:

```python
z = complex(input("Enter complex number: "))

print(z)
```

If the user enters:

```text
3+4j
```

Output:

```text
(3+4j)
```

---

# 49. Practical Example: Real and Imaginary Parts

```python
z = 10 + 20j

real_part = z.real
imaginary_part = z.imag

print("Real:", real_part)
print("Imaginary:", imaginary_part)
```

Output:

```text
Real: 10.0
Imaginary: 20.0
```

---

# 50. Practical Example: Magnitude

```python
z = 3 + 4j

magnitude = abs(z)

print("Magnitude:", magnitude)
```

Output:

```text
Magnitude: 5.0
```

---

# 51. Practical Example: Conjugate

```python
z = 3 + 4j

print("Original:", z)
print("Conjugate:", z.conjugate())
```

Output:

```text
Original: (3+4j)
Conjugate: (3-4j)
```

---

# 52. Practical Example: Complex Arithmetic

```python
z1 = 3 + 4j
z2 = 2 + 5j

print("Addition:", z1 + z2)
print("Subtraction:", z1 - z2)
print("Multiplication:", z1 * z2)
print("Division:", z1 / z2)
```

Complex numbers are especially useful when calculations naturally involve both real and imaginary components.

---

# 53. Complex Numbers and Mathematical Representation

Consider:

```text
z = 3 + 4j
```

We can think of it as a point on a complex plane:

```text
                 Imaginary
                    ↑
                    |
                4   |       ● (3,4)
                    |
                    |
--------------------+----------------→ Real
                    |
                    |
```

The horizontal axis represents the **real part**.

The vertical axis represents the **imaginary part**.

So:

```text
3 + 4j
```

corresponds to:

```text
(real = 3, imaginary = 4)
```

---

# 54. Complex Number Magnitude

For:

```text
z = a + bj
```

the magnitude is:

```text
|z| = √(a² + b²)
```

For:

```text
z = 3 + 4j
```

we get:

```text
|z| = √(3² + 4²)

    = √25

    = 5
```

Python:

```python
z = 3 + 4j

print(abs(z))
```

Output:

```text
5.0
```

---

# 55. Complex Number Conjugate and Magnitude

For:

```text
z = a + bj
```

the conjugate is:

```text
a - bj
```

An important mathematical relationship is:

```text
z × conjugate(z) = |z|²
```

Example:

```text
z = 3 + 4j

conjugate(z) = 3 - 4j
```

Then:

```text
(3 + 4j)(3 - 4j)
```

becomes:

```text
9 - 16j²
```

Since:

```text
j² = -1
```

we get:

```text
9 + 16 = 25
```

And:

```text
|z|² = 5² = 25
```

---

# 56. Complex Number Methods and Attributes

Important things available on a complex object:

| Attribute/Method | Purpose |
|---|---|
| `.real` | Gets real part |
| `.imag` | Gets imaginary part |
| `.conjugate()` | Returns conjugate |
| `abs()` | Returns magnitude |
| `complex()` | Creates a complex number |
| `type()` | Checks type |
| `isinstance()` | Checks whether it is a complex instance |
| `hash()` | Gets hash value |

Example:

```python
z = 3 + 4j

print(z.real)
print(z.imag)
print(z.conjugate())
print(abs(z))
```

Output:

```text
3.0
4.0
(3-4j)
5.0
```

---

# 57. Complex vs Integer vs Float

| Feature | `int` | `float` | `complex` |
|---|---|---|---|
| Example | `10` | `10.5` | `3+4j` |
| Whole numbers | Yes | Can represent | Yes, as real part |
| Decimal values | No | Yes | Yes |
| Imaginary part | No | No | Yes |
| Immutable | Yes | Yes | Yes |
| Hashable | Yes | Yes | Yes |
| Ordering | Yes | Yes | No |
| Equality | Yes | Yes | Yes |
| Dictionary key | Yes | Yes | Yes |
| Set element | Yes | Yes | Yes |

---

# 58. Important Difference: `float` vs `complex`

A float has one numeric component:

```text
10.5
```

A complex number has two components:

```text
3 + 4j
```

So:

```text
float
│
└── one real value

complex
├── real part
└── imaginary part
```

---

# 59. Complex Number and Floating-Point Precision

The real and imaginary parts of Python complex numbers use floating-point representation.

Therefore, calculations involving complex numbers can also experience floating-point precision issues.

Example:

```python
z = 0.1 + 0.2j

print(z)
```

The components are floating-point values and therefore follow the same general floating-point representation rules.

---

# 60. Common Mistakes

### Mistake 1: Using `i` instead of `j`

Python uses:

```python
3 + 4j
```

not:

```python
3 + 4i
```

---

### Mistake 2: Forgetting that `j` is required

```python
3 + 4
```

is simply:

```text
7
```

It is not a complex number.

Use:

```python
3 + 4j
```

for a complex number.

---

### Mistake 3: Trying to use ordering operators

This is invalid:

```python
a = 3 + 4j
b = 2 + 5j

print(a > b)
```

Complex numbers do not support normal ordering.

---

### Mistake 4: Trying `int()` directly

```python
int(3 + 4j)
```

raises `TypeError`.

Use:

```python
z.real
```

or:

```python
z.imag
```

if you specifically need one component.

---

### Mistake 5: Confusing `.imag` with an imaginary number

```python
z = 3 + 4j

print(z.imag)
```

returns:

```text
4.0
```

It returns the **imaginary component**, not `4j`.

---

### Mistake 6: Forgetting `j² = -1`

This is fundamental when manually understanding complex arithmetic:

```text
j² = -1
```

---

# 61. Important Characteristics of `complex`

Remember these points:

```text
1. complex represents complex numbers.
2. General form is a + bj.
3. Python uses j for the imaginary unit.
4. A complex number has real and imaginary parts.
5. .real returns the real part.
6. .imag returns the imaginary part.
7. .conjugate() returns the conjugate.
8. abs() returns the magnitude.
9. complex is immutable.
10. complex is hashable.
11. Complex numbers can be dictionary keys.
12. Complex numbers can be set elements.
13. Equality comparison is supported.
14. Normal ordering is not supported.
15. int() cannot directly convert a complex number.
16. float() cannot directly convert a complex number.
17. 0j is falsy.
18. Non-zero complex numbers are truthy.
19. j² = -1.
20. Complex numbers are useful in scientific and engineering calculations.
```

---

# 62. Quick Revision

```text
complex
│
├── General form
│   └── a + bj
│
├── a
│   └── Real part
│
├── b
│   └── Imaginary part
│
├── j
│   └── Imaginary unit
│
├── .real
│   └── Real component
│
├── .imag
│   └── Imaginary component
│
├── .conjugate()
│   └── Conjugate
│
├── abs()
│   └── Magnitude
│
├── Immutable
│
├── Hashable
│
├── == → supported
│
└── <, >, <=, >= → not supported
```

---

# 63. One-Line Definition

> **`complex` is an immutable Python numeric data type used to represent numbers containing a real part and an imaginary part in the form `a + bj`.**

---

# 64. Final Example

```python
z = 3 + 4j

print("Complex Number:", z)
print("Type:", type(z))

print("Real Part:", z.real)
print("Imaginary Part:", z.imag)
print("Magnitude:", abs(z))
print("Conjugate:", z.conjugate())

print("Addition:", z + (2 + 5j))
print("Multiplication:", z * (2 + 5j))
```

Output:

```text
Complex Number: (3+4j)
Type: <class 'complex'>
Real Part: 3.0
Imaginary Part: 4.0
Magnitude: 5.0
Conjugate: (3-4j)
Addition: (5+9j)
Multiplication: (-14+23j)
```

### Final Mental Model

```text
Complex Number
      │
      ↓
   a + bj
   /     \
  /       \
Real     Imaginary
part       part
  │          │
  a          b
             ↓
            j
```

Think of:

```text
3 + 4j
```

as:

```text
Real part      → 3
Imaginary part → 4
Imaginary unit → j
Magnitude      → 5
Conjugate      → 3 - 4j
```