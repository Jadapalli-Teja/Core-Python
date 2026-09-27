1. What is a Complex Number?

A complex number contains two parts:

real part + imaginary part

In Python, the imaginary part is written using j.

Example:

z = 3 + 4j

Here:

3 → real part
4 → imaginary part
j → imaginary unit

You can check its type:

z = 3 + 4j

print(type(z))

# Output:
# <class 'complex'>
2. Creating Complex Numbers

We can directly write a complex number using j.

a = 2 + 3j
b = 5 - 2j
c = 4j

print(a)
print(b)
print(c)

# Output:
# (2+3j)
# (5-2j)
# 4j

A number like:

4j

has:

Real part      → 0
Imaginary part → 4
3. Real and Imaginary Parts

Python provides .real and .imag to access the two parts.

z = 3 + 4j

print(z.real)
print(z.imag)

# Output:
# 3.0
# 4.0

Notice that even though we wrote 3 and 4, Python returns them as floats:

3.0
4.0
4. Complex Numbers Can Be Created Using complex()

Python provides the complex() function.

z = complex(3, 4)

print(z)

# Output:
# (3+4j)

The syntax is:

complex(real, imaginary)

For example:

z = complex(10, 5)

print(z)

# Output:
# (10+5j)

We can also create a complex number with only the real part:

z = complex(10)

print(z)

# Output:
# (10+0j)
5. Arithmetic Operations

Complex numbers support basic arithmetic operations.

Addition
a = 2 + 3j
b = 4 + 5j

print(a + b)

# Output:
# (6+8j)

Real parts are added together, and imaginary parts are added together.

(2 + 3j) + (4 + 5j)
= (2 + 4) + (3 + 5)j
= 6 + 8j
Subtraction
a = 5 + 6j
b = 2 + 3j

print(a - b)

# Output:
# (3+3j)
Multiplication
a = 2 + 3j
b = 4 + 5j

print(a * b)

# Output:
# (-7+22j)

The important rule is:

j² = -1

So:

(2 + 3j)(4 + 5j)

= 8 + 10j + 12j + 15j²
= 8 + 22j - 15
= -7 + 22j
6. Division

Complex numbers can also be divided.

a = 2 + 3j
b = 1 + 2j

print(a / b)

# Output:
# (1.6-0.2j)

Python handles the complex-number calculation automatically.

7. Conjugate

A complex number's conjugate changes the sign of its imaginary part.

3 + 4j

has conjugate:

3 - 4j

Python provides .conjugate():

z = 3 + 4j

print(z.conjugate())

# Output:
# (3-4j)
8. Magnitude

The magnitude of a complex number can be found using abs().

For:

3 + 4j

the magnitude is:

√(3² + 4²)
= √25
= 5

Python:

z = 3 + 4j

print(abs(z))

# Output:
# 5.0
9. Complex Numbers Are Immutable

Complex objects are immutable.

Once a complex object is created, its value cannot be changed.

z = 3 + 4j

z = z + 2

print(z)

# Output:
# (5+4j)

Here, Python does not modify the existing complex object.

Instead, a new complex value is created and z is made to refer to it.

10. Important Points
Complex numbers contain a real part and an imaginary part.
Python uses j for the imaginary part.
Example: 3 + 4j
.real gives the real part.
.imag gives the imaginary part.
complex() can create complex numbers.
Complex numbers support +, -, *, and /.
.conjugate() returns the conjugate.
abs() gives the magnitude.
Complex numbers are immutable.
j² = -1.
Simple way to remember
3 + 4j
│   │
│   └── Imaginary part
└────── Real part