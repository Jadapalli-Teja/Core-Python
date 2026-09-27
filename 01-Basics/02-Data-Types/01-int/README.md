1. What is an Integer?

An integer (int) is a whole number without a decimal part.

It can be:

Positive → 10, 25, 100
Negative → -10, -25
Zero → 0
age = 21
temperature = -5
count = 0

The type of all these values is int.

2. Creating Integer Objects

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

We don't need to write:

int age = 21

Python determines the type automatically.

3. Integer Literals

Python allows integers to be written in different number systems.

Decimal

This is the normal number system we use.

num = 25
print(num)

# Output:
# 25
Binary

Binary uses only 0 and 1.

We write binary numbers using 0b or 0B.

num = 0b1010
print(num)

# Output:
# 10

0b1010 means decimal 10.

Octal

Octal uses digits from 0 to 7.

We write octal numbers using 0o or 0O.

num = 0o17
print(num)

# Output:
# 15
Hexadecimal

Hexadecimal uses:

0-9 and A-F

We write hexadecimal numbers using 0x or 0X.

num = 0x1A
print(num)

# Output:
# 26

So:

0b1010 → 10
0o17   → 15
0x1A   → 26

The value is stored as an integer; these are simply different ways of writing integer literals.

4. Underscores in Integers

Python allows _ inside large numbers to make them easier to read.

salary = 1_00_000
population = 1_40_00_000

print(salary)
print(population)

# Output:
# 100000
# 14000000

The underscore has no effect on the value.

100000

and

1_00_000

represent the same integer value.

5. Python Integers Can Be Very Large

Python integers are not restricted to a fixed size like some other programming languages.

num = 999999999999999999999999999999999999

print(num)

# Output:
# 999999999999999999999999999999999999

Python can automatically handle large integers, limited mainly by available memory.

6. Arithmetic Operations with Integers

Integers can be used with arithmetic operators.

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

Important:

/ → normal division → returns float
// → floor division
% → remainder
** → power

For example:

10 // 3
# 3

10 % 3
# 1
7. Converting Other Values to Integer

We can use the int() function to convert certain values into integers.

a = int(10.8)
b = int("25")

print(a)
print(b)

# Output:
# 10
# 25

Notice:

int(10.8)

does not round the number.

It removes the decimal part.

10.8 → 10
10.9 → 10
-10.8 → -10
8. Checking Whether a Value is an Integer

We can use type():

num = 25

print(type(num))

# Output:
# <class 'int'>

We can also use isinstance():

num = 25

print(isinstance(num, int))

# Output:
# True

isinstance() is useful when we want to check whether an object belongs to a particular type or class.

9. Important Points About int
int represents whole numbers.
Integers can be positive, negative, or zero.
Python integers can grow very large.
/ produces a float, even when both operands are integers.
// performs floor division.
% gives the remainder.
** is used for exponentiation.
int() can convert suitable values to integers.
Binary, octal, and hexadecimal literals are still represented as integers.
Simple way to remember
int
 ↓
Whole numbers
 ↓
10, -10, 0, 100
 ↓
Can be used for calculations