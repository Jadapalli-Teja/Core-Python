# Python Boolean (`bool`)

## 1. What is Boolean?

- Boolean represents a logical value.
- Python has only two Boolean values:
  - `True`
  - `False`
- The type of these values is `bool`.

Example:

```python
a = True
b = False

print(type(a))
print(type(b))

Output:

<class 'bool'>
<class 'bool'>
2. True and False

Boolean values must start with a capital letter.

x = True
y = False

print(x)
print(y)

Output:

True
False

These are not Boolean values:

true
false

Python treats them as names/variables rather than the Boolean values True and False.

3. Boolean Values from Comparisons

Comparison operators produce Boolean results.

print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
print(10 >= 10)
print(5 <= 3)

Output:

True
False
True
False
True
False

Common comparison operators:

>    Greater than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
==   Equal to
!=   Not equal to
4. Boolean Expressions

An expression that produces True or False is called a Boolean expression.

age = 21

result = age >= 18

print(result)
print(type(result))

Output:

True
<class 'bool'>
5. Boolean with if

Boolean expressions are commonly used in conditions.

age = 21

if age >= 18:
    print("Adult")

Output:

Adult

The expression:

age >= 18

produces True, so the if block runs.

6. bool() Function

bool() converts a value into a Boolean value.

print(bool(1))
print(bool(0))

Output:

True
False

The result depends on whether the value is truthy or falsy.

7. Truthy and Falsy Values

Python evaluates many objects as either truthy or falsy when they are used in conditions.

Common falsy values
False
None
0
0.0
0j
""
[]
()
{}
set()

Example:

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))

Output:

False
False
False
False
False
False
False
Common truthy values

Non-zero numbers and non-empty objects are generally truthy.

print(bool(1))
print(bool(-10))
print(bool("Python"))
print(bool([1, 2]))
print(bool({"name": "Teja"}))

Output:

True
True
True
True
True
8. Empty vs Non-Empty Collections

An empty collection is generally falsy.

print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

Output:

False
False
False
False

A non-empty collection is generally truthy.

print(bool([1, 2]))
print(bool((1, 2)))
print(bool({"a": 1}))
print(bool({1, 2}))

Output:

True
True
True
True
9. Boolean Operators

Python provides three main logical operators:

and
or
not

They are commonly used to combine or reverse conditions.

10. and Operator

and is true when both conditions are true.

print(True and True)
print(True and False)
print(False and True)
print(False and False)

Output:

True
False
False
False

Example:

age = 21
marks = 75

print(age >= 18 and marks >= 60)

Output:

True
11. or Operator

or is true when at least one condition is true.

print(True or True)
print(True or False)
print(False or True)
print(False or False)

Output:

True
True
True
False

Example:

age = 16
has_permission = True

print(age >= 18 or has_permission)

Output:

True
12. not Operator

not reverses the truth value.

print(not True)
print(not False)

Output:

False
True

It also works with other values:

print(not 0)
print(not 10)
print(not "")
print(not "Python")

Output:

True
False
True
False
13. Truth Tables
and
A	B	A and B
True	True	True
True	False	False
False	True	False
False	False	False
or
A	B	A or B
True	True	True
True	False	True
False	True	True
False	False	False
not
A	not A
True	False
False	True
14. and and or Can Return Actual Values

An important Python behavior is that and and or do not always return True or False.

They can return one of their operands.

Example:

print(10 and 20)
print(0 and 20)

Output:

20
0

With or:

print(10 or 20)
print(0 or 20)

Output:

10
20

The result depends on the truthiness of the operands.

15. Short-Circuit Evaluation

and and or use short-circuit evaluation.

and

If the first value is falsy, Python does not need to evaluate the remaining expression.

x = 0

result = x and (10 / 0)

print(result)

Output:

0

The division is never evaluated because x is already falsy.

or

If the first value is truthy, Python does not need to evaluate the remaining expression.

x = 10

result = x > 5 or (10 / 0)

print(result)

Output:

True

The second expression is not evaluated.

16. Boolean Values in Arithmetic

In Python, bool is a subclass of int.

Therefore:

True  → 1
False → 0

in arithmetic contexts.

Example:

print(True + True)
print(True + False)
print(False + False)

Output:

2
1
0

More examples:

print(True * 5)
print(False * 5)
print(True - False)
print(False - True)

Output:

5
0
1
-1
17. bool is a Subclass of int

We can verify this using isinstance().

print(isinstance(True, int))
print(isinstance(False, int))

Output:

True
True

However, their actual types are different:

print(type(True))
print(type(1))

Output:

<class 'bool'>
<class 'int'>

So:

bool → subclass of int

but:

True → bool
1    → int
18. True == 1 and False == 0

Because Boolean values behave like 1 and 0 in comparisons:

print(True == 1)
print(False == 0)

Output:

True
True

But they still have different types.

19. Boolean with Strings

An empty string is falsy:

print(bool(""))

Output:

False

A non-empty string is truthy:

print(bool("Python"))

Output:

True

An important example:

print(bool("False"))

Output:

True

Why?

Because "False" is a non-empty string. Python checks whether the string is empty, not what text it contains.

20. Boolean with Numbers

For numbers:

0 → False
non-zero → True

Examples:

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(10.5))
print(bool(-2.5))

Output:

False
True
True
True
True
21. Boolean with None

None represents the absence of a value.

Its Boolean value is False.

x = None

print(bool(x))

Output:

False
22. sum() with Boolean Values

Because:

True  → 1
False → 0

we can use sum() with Boolean values.

values = [True, False, True, True]

print(sum(values))

Output:

3

Because:

True + False + True + True
  1  +   0   +  1  +  1
= 3

This can be useful for counting how many conditions are true.

23. Chained Comparisons

Python allows multiple comparisons to be written together.

Instead of:

age >= 18 and age <= 60

we can write:

18 <= age <= 60

Example:

age = 21

print(18 <= age <= 60)

Output:

True
24. Boolean Values with while

Boolean expressions are also used with loops.

count = 1

while count <= 3:
    print(count)
    count += 1

Output:

1
2
3

The condition:

count <= 3

produces either True or False.

25. Boolean Objects are Immutable

Boolean objects are immutable.

Python has only two Boolean values:

True
False

If we write:

x = True
x = False

we are not changing the True object.

We are simply making x refer to False.

26. Boolean Identity

True and False are singleton Boolean objects.

When we specifically want to check whether a value is the Boolean object True, is can be used:

value = True

print(value is True)

Output:

True

For normal conditions, however, simply use:

if value:
    print("True")
27. Important Points
bool represents logical values.
Python has two Boolean values: True and False.
The type of both is bool.
Comparison operators produce Boolean values.
bool() converts values to their truth value.
Zero, empty collections, empty strings, None, and False are commonly falsy.
Non-zero and non-empty values are generally truthy.
and, or, and not are logical operators.
and and or use short-circuit evaluation.
and and or can return actual operands.
bool is a subclass of int.
True behaves like 1 and False behaves like 0 in arithmetic.
True + True gives 2.
True == 1 is True.
type(True) is bool, not int.
Boolean objects are immutable.
Boolean values are commonly used with if and while.
sum() can be used to count True values.
Quick Revision
bool
│
├── True
└── False
      │
      ↓
Comparison results
      │
      ↓
   bool()

Falsy:
0, 0.0, 0j, "", [], (), {}, set(), None, False

Truthy:
Non-zero values
Non-empty objects

Logical operators:
and
or
not

True  → 1
False → 0

bool → subclass of int

True + True → 2
True == 1   → True

and / or
   ↓
Short-circuit evaluation
   ↓
Can return operands