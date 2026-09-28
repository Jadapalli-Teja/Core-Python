# Python Integer (`int`)

## 1. What is an Integer?

- An integer represents a whole number without a decimal/fractional part.
- Integers can be positive, negative, or zero.
- The type of an integer object is `int`.

Examples:

```python
age = 21
marks = 95
temperature = -5
count = 0

print(type(age))
print(type(temperature))

Output:

<class 'int'>
<class 'int'>

Examples of integers:

10
-10
0
100
-250
2. Creating Integer Values

We can create an integer simply by assigning a whole number to a variable.

age = 21
marks = 95
balance = -500

print(age)
print(marks)
print(balance)

Output:

21
95
-500

Python automatically determines that these values are integers.

3. Integer Literals

A number written directly in Python code is called a literal.

For example:

x = 100

Here, 100 is an integer literal.

Python supports different ways of writing integer literals.

Decimal

This is the normal number system.

x = 25

print(x)

# Output:
# 25
Binary

Binary uses only 0 and 1.

Python uses 0b or 0B before a binary number.

x = 0b1010

print(x)

# Output:
# 10
Octal

Octal uses digits from 0 to 7.

Python uses 0o or 0O.

x = 0o17

print(x)

# Output:
# 15
Hexadecimal

Hexadecimal uses:

0 - 9
A - F

Python uses 0x or 0X.

x = 0x1A

print(x)

# Output:
# 26

So:

0b1010 → 10
0o17   → 15
0x1A   → 26

These are different representations of integer values.

4. Underscores in Integer Literals

Python allows underscores inside large numbers to make them easier to read.

salary = 1_00_000
population = 1_40_00_000

print(salary)
print(population)

Output:

100000
14000000

The underscore does not change the value.

100000
1_00_000

represent the same integer value.

5. Positive, Negative and Zero

An integer can be:

Positive
x = 25
Negative
x = -25
Zero
x = 0

All three are of type int.

6. Integer Arithmetic

Integers support normal arithmetic operations.

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

Output:

13
7
30
3.3333333333333335
3
1
1000

Important operators:

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus / Remainder
**  Exponentiation
7. / Always Produces a Float

Even when both operands are integers, / produces a float.

a = 10
b = 2

result = a / b

print(result)
print(type(result))

Output:

5.0
<class 'float'>

So:

10 / 2 → 5.0 → float

This is different from:

10 // 2

which gives:

5 → int
8. Floor Division //

// performs floor division.

print(10 // 3)

# Output:
# 3

For positive numbers:

10 / 3  → 3.333...
10 // 3 → 3

For negative numbers, floor division goes toward negative infinity.

print(-10 // 3)

# Output:
# -4

This is important because it is not simply truncation toward zero.

9. Modulus %

The % operator returns the remainder.

print(10 % 3)

# Output:
# 1

Because:

10 = 3 × 3 + 1

So the remainder is 1.

The modulus operator is commonly used to check whether a number is divisible by another number.

print(10 % 2)

# Output:
# 0

If the remainder is 0, the number is divisible by 2.

10. Exponentiation **

The ** operator is used for powers.

print(2 ** 3)

# Output:
# 8

Because:

2³ = 2 × 2 × 2 = 8

Another example:

print(5 ** 2)

# Output:
# 25
11. Integer and Float Together

Python allows integers and floats to participate in the same arithmetic expression.

a = 10
b = 2.5

result = a + b

print(result)
print(type(result))

Output:

12.5
<class 'float'>

Generally, when an integer is combined with a float in arithmetic, the result is a float.

int + float → float
int * float → float
12. Converting to Integer Using int()

The int() function can convert suitable values into integers.

Float to Integer
x = int(10.8)

print(x)

# Output:
# 10

int() does not round the value.

It removes the fractional part toward zero.

10.8  → 10
10.2  → 10
-10.8 → -10
String to Integer
x = int("25")

print(x)
print(type(x))

Output:

25
<class 'int'>

The string must contain a valid integer representation.

13. Converting Binary, Octal and Hexadecimal Strings

int() can also convert strings using a specified base.

print(int("1010", 2))
print(int("17", 8))
print(int("1A", 16))

Output:

10
15
26

Here:

2  → binary
8  → octal
16 → hexadecimal
14. Python Integers Can Be Very Large

Python integers can represent very large numbers.

x = 999999999999999999999999999999999999

print(x)

Python does not have the same fixed integer-size limitation that languages using fixed-width integer types commonly have.

The practical limit is mainly the memory available to the Python process.

15. Checking the Type

We can use type() to check the type of an integer.

x = 100

print(type(x))

# Output:
# <class 'int'>

We can also use isinstance().

x = 100

print(isinstance(x, int))

# Output:
# True
16. Integers Are Immutable

int objects are immutable.

This means an existing integer object cannot be changed.

For example:

x = 10

x = x + 5

print(x)

# Output:
# 15

It may look like the value 10 was changed to 15, but Python actually creates/uses an integer object representing 15 and makes x refer to it.

The original integer object representing 10 is not modified.

This is an important difference between immutable types and mutable types such as lists.

17. Integer Variables Can Be Reassigned

Although integer objects are immutable, a variable can be assigned a different integer.

x = 10
x = 20

print(x)

# Output:
# 20

Here the variable x changes what it refers to.

The integer object itself is not modified.

18. Boolean and Integer Relationship

In Python, bool is a subclass of int.

Therefore:

print(isinstance(True, int))
print(isinstance(False, int))

Output:

True
True

Boolean values behave like integers in some arithmetic situations:

print(True + True)
print(True + False)

Output:

2
1

Conceptually:

True  → 1
False → 0

But their types are still different:

print(type(True))
print(type(1))

Output:

<class 'bool'>
<class 'int'>
19. Integers are Hashable

Integers are hashable, which means they can be used as:

dictionary keys
elements of a set

Example:

student_marks = {
    101: 85,
    102: 90
}

print(student_marks[101])

# Output:
# 85

Here the integers 101 and 102 are used as dictionary keys.

We can also use integers in a set:

numbers = {10, 20, 30}

print(numbers)

# Output:
# {10, 20, 30}
20. Comparing Integers

Integers can be compared using comparison operators.

a = 10
b = 20

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

Comparison expressions produce Boolean values.

int comparison
      ↓
True / False
      ↓
bool
21. Integer Objects and id()

An integer is an object, so it has an identity.

We can use id() to get its identity.

x = 100

print(id(x))

The exact number returned by id() can vary between executions and Python implementations.

The important concept is that x refers to an integer object.

22. Important Points
int represents whole numbers.
Integers can be positive, negative, or zero.
Python supports decimal, binary, octal, and hexadecimal integer literals.
_ can be used to improve the readability of large integer literals.
/ returns a float.
// performs floor division.
% returns the remainder.
** performs exponentiation.
int() can convert suitable values to integers.
Converting a float with int() truncates toward zero; it does not round.
Python integers can represent very large values.
Integer objects are immutable.
Variables can still be reassigned to another integer.
bool is a subclass of int.
Integers are hashable.
Integers can be used as dictionary keys and set elements.
type() and isinstance() can be used to check integer types.
Quick Revision
int
│
├── Whole numbers
│   ├── Positive → 10
│   ├── Negative → -10
│   └── Zero → 0
│
├── Number systems
│   ├── Decimal → 25
│   ├── Binary → 0b1010
│   ├── Octal → 0o17
│   └── Hexadecimal → 0x1A
│
├── Arithmetic
│   ├── +  Addition
│   ├── -  Subtraction
│   ├── *  Multiplication
│   ├── /  Division → float
│   ├── // Floor division
│   ├── %  Remainder
│   └── ** Power
│
├── Immutable
├── Hashable
└── bool is a subclass of int