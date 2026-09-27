## 1. What is a Data Type?

- A data type tells us what kind of value an object represents.
- Different types of data behave differently in Python.
- Python provides many built-in data types.

Example:

```python
age = 21
name = "Teja"
cgpa = 8.43
is_student = True

Here:

21 → int
"Teja" → str
8.43 → float
True → bool

We can check the type using type().

print(type(age))
print(type(name))
print(type(cgpa))
print(type(is_student))

Output:

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
2. Why Do We Need Data Types?

Different types support different operations.

Example with integers:

a = 10
b = 20

print(a + b)

Output:

30

Here + performs addition.

Example with strings:

a = "10"
b = "20"

print(a + b)

Output:

1020

Here + joins the strings.

So the same operator can behave differently depending on the data type.

int + int
    ↓
Addition

str + str
    ↓
Concatenation
3. Python is Dynamically Typed

Python is a dynamically typed language.

This means:

We don't have to declare the type of a variable before assigning a value.
Python determines the type from the object assigned to the name.
The same name can refer to objects of different types at different times.

Example:

x = 10
print(type(x))

x = "Python"
print(type(x))

x = 10.5
print(type(x))

Output:

<class 'int'>
<class 'str'>
<class 'float'>

The name x first refers to an integer object, then a string object, and then a float object.

x → 10       → int

x → "Python" → str

x → 10.5     → float
Important Point

The type belongs to the object, not permanently to the variable name.

4. Variable, Object and Data Type

These three concepts are different.

Consider:

age = 21

Here:

age → name
21 → object
int → type of the object

Conceptually:

age
 ↓
21
 ↓
int

A simple way to remember:

Name → Object → Type

This concept is important when learning:

References
Mutable and immutable objects
Shallow copy
Deep copy
Memory management
Classes and objects
5. Everything in Python is an Object

In Python, values are represented as objects.

Examples:

10
10.5
"Python"
[10, 20, 30]
True

All of these are objects.

Their types are:

10             → int
10.5           → float
"Python"       → str
[10, 20, 30]   → list
True           → bool

Python also treats functions, classes and many other things as objects.

6. type() Function

The type() function is used to find the type of an object.

Syntax
type(object)

Example:

x = 10

print(type(x))

Output:

<class 'int'>

More examples:

print(type(10))
print(type(10.5))
print(type("Python"))
print(type(True))
print(type([1, 2, 3]))

Output:

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'list'>
7. isinstance()

isinstance() is used to check whether an object belongs to a particular type or class.

Syntax
isinstance(object, type)

Example:

age = 21

print(isinstance(age, int))
print(isinstance(age, str))

Output:

True
False
Difference
type()
    ↓
Tells the type of an object

isinstance()
    ↓
Checks whether the object belongs to a type

isinstance() becomes especially useful when working with inheritance.

8. Strong Typing

Python is dynamically typed and strongly typed.

Strong typing means Python does not freely mix incompatible types.

Example:

x = "10"
y = 5

print(x + y)

This produces a TypeError.

Why?

Because:

"10" → str
5    → int

We can explicitly convert the string:

x = "10"
y = 5

print(int(x) + y)

Output:

15

So:

Dynamic typing → type does not need to be declared beforehand.
Strong typing → incompatible types are not automatically mixed in arbitrary operations.
9. Object Identity

Every object has an identity during its lifetime.

The id() function can be used to obtain an object's identity.

Example:

x = 10

print(id(x))

Output will be a number similar to:

140735...

The exact number can be different between executions.

For now, remember:

Object
├── Value
├── Type
└── Identity

Object identity becomes important when working with references and the is operator.

10. == vs is

These operators are different.

==

Checks whether two objects have equal values.

is

Checks whether two names refer to the same object.

Example:

a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)

Output:

True
False

Why?

Both lists contain the same values:

[10, 20]

So:

a == b

is True.

But they are different list objects.

So:

a is b-

is False.

11. References

Consider:

a = [10, 20]
b = a

Here b refers to the same list object as a.

Conceptually:

a ──────┐
        ↓
      [10, 20]
        ↑
b ──────┘

Therefore:

print(a == b)
print(a is b)

Output:

True
True

This becomes very important when learning mutable objects and copying.

12. Main Built-in Data Types

Python provides many built-in data types.

Numeric Types
int
float
complex
Boolean Type
bool
Sequence Types
str
list
tuple
range
Set Types
set
frozenset
Mapping Type
dict
Special Type
NoneType
Binary Types
bytes
bytearray
memoryview
13. Data Type Examples
Type	Example
int	10
float	10.5
complex	3 + 4j
bool	True
str	"Python"
list	[10, 20, 30]
tuple	(10, 20, 30)
range	range(5)
set	{10, 20, 30}
frozenset	frozenset({10, 20})
dict	{"name": "Teja"}
NoneType	None
bytes	b"Python"
bytearray	bytearray(b"Python")
memoryview	memoryview(b"Python")
14. Important Properties of Data Types

When studying a data type, we should understand more than just its definition.

Mutable or Immutable

Can the object be changed after it is created?

Examples:

list  → Mutable
tuple → Immutable
str   → Immutable

We will study this separately in detail.

Ordered or Unordered

Does the collection maintain an order?

Examples:

list  → Ordered
tuple → Ordered
str   → Ordered

Sets are not sequence types and do not support positional indexing.

Allows Duplicates

Some collections allow duplicate values.

numbers = [10, 10, 20]

Lists allow duplicates.

A set stores unique elements:

numbers = {10, 10, 20}

print(numbers)

Output:

{10, 20}
Supports Indexing

Some types allow accessing elements using positions.

Example:

name = "Python"

print(name[0])

Output:

P

Lists, tuples and strings support indexing.

Sets do not support indexing.

Hashable or Unhashable

Some objects can be hashed and can be used as dictionary keys or set elements.

Examples:

int   → Hashable
str   → Hashable
list  → Unhashable

We will study this separately.

15. Type Conversion

Type conversion means converting an object from one type to another.

Example:

x = "100"

y = int(x)

print(y)
print(type(y))

Output:

100
<class 'int'>

Python provides functions such as:

int()
float()
str()
bool()
list()
tuple()
set()
dict()

Type conversion can be:

Implicit conversion
Explicit conversion

We will study both in detail.

16. Mutable and Immutable Types

One of the most important concepts in Python is whether an object can be changed after creation.

Mutable

The object can be changed.

Examples:

list
set
dict
bytearray
Immutable

The object cannot be changed after creation.

Examples:

int
float
complex
bool
str
tuple
frozenset
bytes

We will study why these objects are mutable or immutable, rather than simply memorizing the list.

17. Complete Data Type Learning Order

We will study the types in this order:

int
float
complex
bool
str
list
tuple
range
set
frozenset
dict
NoneType
bytes
bytearray
memoryview

After studying them, we will cover:

Type conversion
Mutable vs immutable
Hashable vs unhashable
Ordered vs unordered
Indexing and slicing
Equality vs identity
type() vs isinstance()
Important differences between data types
Practice questions



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