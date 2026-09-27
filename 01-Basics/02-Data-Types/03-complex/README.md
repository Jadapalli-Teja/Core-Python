# Python Complex Number (`complex`)

## 1. What is a Complex Number?

- A complex number contains two parts:
  - Real part
  - Imaginary part
- Python uses `j` to represent the imaginary part.
- The type of a complex number is `complex`.

Example:

```python
z = 3 + 4j

print(z)
print(type(z))

Output:

(3+4j)
<class 'complex'>

Here:

3 → real part
4 → imaginary part
j → imaginary unit
2. Creating Complex Numbers

We can directly create a complex number using j.

a = 2 + 3j
b = 5 - 2j
c = 4j

print(a)
print(b)
print(c)

Output:

(2+3j)
(5-2j)
4j

If only the imaginary part is given:

c = 4j

then the real part is 0.

So:

4j → 0 + 4j
3. Real and Imaginary Parts

Python provides .real and .imag to access the two parts.

z = 3 + 4j

print(z.real)
print(z.imag)

Output:

3.0
4.0

Notice that Python returns the real and imaginary parts as float values.

4. Creating Complex Numbers Using complex()

Python provides the built-in complex() function.

Syntax:

complex(real, imaginary)

Example:

z = complex(3, 4)

print(z)

Output:

(3+4j)

We can also provide only the real part:

z = complex(10)

print(z)

Output:

(10+0j)
5. Complex Number with Negative Parts

Both the real and imaginary parts can be negative.

a = -3 + 4j
b = 3 - 4j
c = -3 - 4j

print(a)
print(b)
print(c)

Output:

(-3+4j)
(3-4j)
(-3-4j)
6. Addition

Complex numbers can be added by adding their real parts and imaginary parts separately.

a = 2 + 3j
b = 4 + 5j

print(a + b)

Output:

(6+8j)

Because:

(2 + 3j) + (4 + 5j)

= (2 + 4) + (3 + 5)j
= 6 + 8j
7. Subtraction

The real and imaginary parts are subtracted separately.

a = 5 + 6j
b = 2 + 3j

print(a - b)

Output:

(3+3j)
8. Multiplication

Complex numbers can be multiplied using normal algebra.

a = 2 + 3j
b = 4 + 5j

print(a * b)

Output:

(-7+22j)

The important rule is:

j² = -1

Therefore:

(2 + 3j)(4 + 5j)

= 8 + 10j + 12j + 15j²
= 8 + 22j - 15
= -7 + 22j
9. Division

Complex numbers also support division.

a = 2 + 3j
b = 1 + 2j

print(a / b)

Output:

(1.6-0.2j)

Python automatically performs the complex-number division.

10. Conjugate

The conjugate of a complex number is obtained by changing the sign of its imaginary part.

For example:

3 + 4j

has the conjugate:

3 - 4j

Python provides the conjugate() method.

z = 3 + 4j

print(z.conjugate())

Output:

(3-4j)
11. Magnitude of a Complex Number

The magnitude of:

a + bj

is:

√(a² + b²)

For:

3 + 4j

the magnitude is:

√(3² + 4²)
= √25
= 5

Python provides abs():

z = 3 + 4j

print(abs(z))

Output:

5.0
12. Complex Numbers and abs()

abs() can be used with different numeric types.

For a complex number:

z = 3 + 4j

print(abs(z))

Output:

5.0

The result is the magnitude, not the real or imaginary part.

13. Checking the Type

We can use type():

z = 3 + 4j

print(type(z))

Output:

<class 'complex'>

We can also use isinstance():

z = 3 + 4j

print(isinstance(z, complex))

Output:

True
14. Complex Numbers are Immutable

Complex objects are immutable.

This means an existing complex object cannot be changed.

For example:

z = 3 + 4j

z = z + 2

print(z)

Output:

(5+4j)

The original complex object was not modified.

Instead, a new complex value is created and z is made to refer to that value.

15. Complex Numbers and Comparison

Complex numbers support equality and inequality comparisons:

a = 3 + 4j
b = 3 + 4j

print(a == b)
print(a != b)

Output:

True
False

However, complex numbers do not support ordering comparisons such as:

a > b
a < b

For example:

3 + 4j > 2 + 3j

raises a TypeError.

Complex numbers do not have a natural ordering like ordinary real numbers.

16. Complex Numbers Cannot Be Converted Directly to int or float

A complex number cannot be directly converted to an integer or float.

For example:

x = 3 + 4j

int(x)

raises:

TypeError

Similarly:

float(x)

also raises:

TypeError

If we need a particular part, we can access it first:

x = 3 + 4j

print(int(x.real))
print(int(x.imag))

Output:

3
4
17. Complex Numbers and Arithmetic with Other Numeric Types

Complex numbers can be used with integers and floats.

z = 3 + 4j

print(z + 2)
print(z + 2.5)

Output:

(5+4j)
(5.5+4j)

The result remains a complex number.

18. Complex Numbers and bool

Since bool is related to integers, Boolean values can also participate in complex arithmetic.

z = 3 + 4j

print(z + True)
print(z + False)

Output:

(4+4j)
(3+4j)

Conceptually:

True  → 1
False → 0
19. Complex Numbers are Hashable

Complex numbers are immutable and hashable, so they can generally be used as:

Dictionary keys
Set elements

Example:

data = {
    3 + 4j: "complex number"
}

print(data[3 + 4j])

Output:

complex number

They can also be placed in a set:

numbers = {2 + 3j, 4 + 5j}

print(numbers)

The order displayed by a set should not be relied upon.

20. Complex Numbers in Python Use j

In mathematics, the imaginary unit is commonly written as:

i

Python uses:

j

So mathematically:

3 + 4i

is written in Python as:

3 + 4j

Do not write:

3 + 4i

because i is not Python's imaginary-number notation.

21. Important Points
complex represents complex numbers.
A complex number contains a real part and an imaginary part.
Python uses j for the imaginary part.
Example: 3 + 4j
.real returns the real part.
.imag returns the imaginary part.
complex() can create complex numbers.
Complex numbers support +, -, *, and /.
j² = -1.
conjugate() returns the conjugate.
abs() returns the magnitude.
Complex numbers are immutable.
Complex numbers support == and !=.
Complex numbers do not support <, >, <=, or >=.
Complex numbers cannot be directly converted to int or float.
Complex numbers can be used with integers and floats.
Complex numbers are hashable.
Python uses j, not i, for the imaginary part.
Quick Revision
complex
│
├── Real part
├── Imaginary part
│
├── Example
│   └── 3 + 4j
│
├── Access parts
│   ├── .real
│   └── .imag
│
├── Operations
│   ├── +
│   ├── -
│   ├── *
│   └── /
│
├── Special
│   ├── conjugate()
│   └── abs()
│
├── Immutable
├── Hashable
└── No ordering comparisons