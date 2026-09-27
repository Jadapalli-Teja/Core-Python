Python Boolean (bool)
1. What is a Boolean?

A Boolean represents a logical value.

Python has only two Boolean values:

True
False

They represent:

True → something is true
False → something is false

Example:

is_student = True
is_working = False

Here:

is_student → True
is_working → False

Boolean values are mainly used when Python needs to make a decision.

2. Type of Boolean Values

The type of True and False is bool.

print(type(True))
print(type(False))

Output:

<class 'bool'>
<class 'bool'>

So:

True  → bool
False → bool
3. True and False Are Python Keywords

Boolean values must be written with a capital first letter:

True
False

These are correct:

x = True
y = False

These are not Boolean values:

x = true
y = false

Python treats true and false as names/variables, not Boolean values.

4. Boolean Values from Comparisons

Comparison operators produce Boolean results.

For example:

print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)

Output:

True
False
True
False

Common comparison operators:

Operator	Meaning
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
==	Equal to
!=	Not equal to

Example:

age = 21

print(age >= 18)

Output:

True

The expression:

age >= 18

produces a Boolean value.

5. Boolean Expressions

An expression that produces True or False is called a Boolean expression.

age = 21

result = age >= 18

print(result)
print(type(result))

Output:

True
<class 'bool'>

The important idea is:

Expression
    ↓
True / False
    ↓
bool
6. Boolean Values in if

Boolean expressions are commonly used in conditional statements.

age = 21

if age >= 18:
    print("Adult")

Output:

Adult

Here:

age >= 18

produces:

True

Therefore the if block executes.

7. The bool() Function

Python provides the built-in bool() function.

It converts a value into a Boolean value.

print(bool(1))
print(bool(0))

Output:

True
False

The result depends on whether Python considers the value truthy or falsy.

8. Truthy and Falsy Values

Python does not require an expression to literally be True or False when used in a condition.

Many objects can be evaluated for their truth value.

For example:

if "Python":
    print("This runs")

A non-empty string is considered truthy.

On the other hand:

if "":
    print("This will not run")

An empty string is considered falsy.

9. Common Falsy Values

The following values are commonly considered falsy:

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

Examples:

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

Output:

False
False
False
False
False
False
False
False
False
False

An important point:

An empty collection is generally falsy, while a non-empty collection is generally truthy.

10. Common Truthy Values

Examples of truthy values:

print(bool(1))
print(bool(-1))
print(bool(10.5))
print(bool("Python"))
print(bool([1, 2]))
print(bool((1, 2)))
print(bool({"name": "Teja"}))
print(bool({1, 2}))

Output:

True
True
True
True
True
True
True
True

So a simple rule is:

Non-zero number → True
Non-empty object → True

and commonly:

Zero → False
Empty object → False
None → False
11. Boolean with not

not reverses the truth value.

print(not True)
print(not False)

Output:

False
True

With other values:

print(not 0)
print(not 10)
print(not "")
print(not "Python")

Output:

True
False
True
False

So:

not True  → False
not False → True
12. and Operator

The and operator is used when both conditions need to be satisfied.

For Boolean values:

print(True and True)
print(True and False)
print(False and True)
print(False and False)

Output:

True
False
False
False

The basic logical rule is:

True and True → True
Everything else → False

Example:

age = 21
has_id = True

print(age >= 18 and has_id)

Output:

True
13. or Operator

The or operator is used when at least one condition can be true.

print(True or True)
print(True or False)
print(False or True)
print(False or False)

Output:

True
True
True
False

The basic rule is:

False or False → False
Everything else → True
14. Truth Table
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
15. Important: and and or Don't Always Return True or False

This is a very important Python behavior.

Many beginners think:

10 and 20

must return:

True

But Python actually returns:

20

Example:

print(10 and 20)
print(0 and 20)

Output:

20
0

Similarly:

print(10 or 20)
print(0 or 20)

Output:

10
20

So and and or can return one of their operands, not necessarily a Boolean.

16. How and Works

The and operator evaluates values from left to right.

It stops as soon as it finds a falsy value.

Example:

print(10 and 20)

Both values are truthy.

Python reaches the last value and returns:

20

Another example:

print(0 and 20)

0 is falsy.

Python stops immediately and returns:

0

This behavior is called short-circuit evaluation.

17. How or Works

or also evaluates from left to right.

It stops as soon as it finds a truthy value.

print(10 or 20)

10 is truthy, so Python stops and returns:

10

But:

print(0 or 20)

0 is falsy, so Python checks the next value:

20

Therefore:

20
18. Short-Circuit Evaluation

Short-circuiting means Python may stop evaluating an expression before checking every part.

Example:

x = 10

result = x > 5 or x / 0

print(result)

Output:

True

Why doesn't this produce a division-by-zero error?

Because:

x > 5

is already True.

With or, Python doesn't need to evaluate the second part.

This is called short-circuit evaluation.

Similarly, with and, if the first value is falsy, Python can stop.

19. Boolean Values in Arithmetic

One of the most important Python-specific concepts is that bool is a subclass of int.

Therefore:

True

behaves like:

1

in arithmetic contexts.

And:

False

behaves like:

0

Example:

print(True + True)
print(True + False)
print(False + False)

Output:

2
1
0
20. More Boolean Arithmetic
print(True * 5)
print(False * 5)

print(True - False)
print(False - True)

Output:

5
0
1
-1

Conceptually:

True  → 1
False → 0
21. bool is a Subclass of int

We can verify this using isinstance():

print(isinstance(True, int))
print(isinstance(False, int))

Output:

True
True

This means:

bool
  ↓
subclass of
  ↓
int

But this does not mean that Boolean values have the type int.

Their actual type is still bool.

print(type(True))
print(type(1))

Output:

<class 'bool'>
<class 'int'>
22. True == 1

Because Boolean values behave like 1 and 0 in equality comparisons:

print(True == 1)
print(False == 0)

Output:

True
True

But:

print(type(True))
print(type(1))

still gives different types.

So:

True == 1

is True because their values compare equal.

But:

type(True) != type(1)

because their types are different.

23. == vs is with Boolean Values

Remember:

== → compares values
is → compares object identity

For example:

print(True == 1)

Output:

True

But:

print(True is 1)

should not be used to compare Boolean and integer values.

The important rule is:

Use == when you want to compare values. Use is when you specifically need to test object identity.

24. Boolean with Collections

The truth value of collections depends mainly on whether they contain elements.

Empty list
print(bool([]))

Output:

False
Non-empty list
print(bool([1, 2, 3]))

Output:

True

Similarly:

print(bool({}))
print(bool({"name": "Teja"}))

Output:

False
True
25. sum() with Boolean Values

Because:

True  → 1
False → 0

we can use Boolean values with sum().

values = [True, False, True, True]

print(sum(values))

Output:

3

Why?

True + False + True + True
  1  +   0   +  1  +  1
= 3

This can be useful when counting how many conditions are true.

26. Boolean Conversion of Strings

Strings have an important truth-value rule:

Empty string → False
Non-empty string → True

Example:

print(bool(""))
print(bool("Python"))
print(bool("False"))

Output:

False
True
True

Notice:

bool("False")

is:

True

because "False" is a non-empty string.

It does not matter that the text says "False".

27. Boolean Conversion of Numbers

For numbers:

0 → False
non-zero → True

Examples:

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(100))
print(bool(0.0))
print(bool(2.5))

Output:

False
True
True
True
False
True
28. Boolean Conversion of None

None represents the absence of a value.

Its Boolean value is False.

x = None

print(bool(x))

Output:

False
29. Boolean Expressions with Multiple Conditions

We can combine multiple conditions.

age = 21
marks = 75

result = age >= 18 and marks >= 60

print(result)

Output:

True

Both conditions are true.

Another example:

age = 16
has_permission = True

result = age >= 18 or has_permission

print(result)

Output:

True

At least one condition is true.

30. Chained Comparisons

Python allows us to write comparisons in a clean way.

Instead of:

age >= 18 and age <= 60

we can write:

18 <= age <= 60

Example:

age = 21

print(18 <= age <= 60)

Output:

True

Python evaluates this as a chained comparison.

31. Boolean Values and while

Boolean expressions are also commonly used with while.

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

keeps producing True or False.

32. Boolean Objects are Immutable

bool objects are immutable.

There are only two Boolean values:

True
False

You cannot modify the True object itself.

When a Boolean variable changes:

x = True
x = False

the variable is simply made to refer to another Boolean object.

33. Boolean and Identity

Python has Boolean singleton objects:

True
False

Therefore, when specifically checking whether something is the Boolean singleton True or False, is can be appropriate:

value = True

print(value is True)

# Output:
# True

For ordinary truth testing, however, prefer:

if value:
    ...

rather than unnecessarily comparing with True.

34. Common Mistakes
Mistake 1: Using lowercase true
x = true

This is not Python's Boolean value.

Use:

x = True
Mistake 2: Thinking "False" is false
print(bool("False"))

Output:

True

Because the string is not empty.

Mistake 3: Thinking 10 and 20 returns True
print(10 and 20)

Output:

20

and and or can return operands.

Mistake 4: Using is for normal value comparison

Use:

x == y

when comparing values.

Use:

x is y

when checking object identity.

35. Important Points
bool represents logical values.
Python has exactly two Boolean values: True and False.
The type of both is bool.
Comparisons normally produce Boolean results.
bool() converts objects to their truth value.
0, 0.0, 0j, "", empty collections, None, and False are falsy.
Most non-zero and non-empty values are truthy.
not reverses a truth value.
and requires both sides to be truthy when used as a logical condition.
or succeeds when at least one side is truthy.
and and or can return actual operands rather than True/False.
and and or use short-circuit evaluation.
bool is a subclass of int.
True behaves like 1 and False behaves like 0 in arithmetic.
True + True gives 2.
True == 1 is True.
type(True) is bool, not int.
Boolean values are immutable.
Boolean values are heavily used in if, while, comparisons, and logical expressions.
sum() can be used with Boolean values to count True values.
Quick Revision
bool
│
├── True
└── False

Comparison
    ↓
True / False

bool(value)
    ↓
Truth value

0 / "" / [] / {} / None
    ↓
False

Non-zero / non-empty values
    ↓
True

and → logical AND + short-circuit
or  → logical OR + short-circuit
not → reverses truth value

True  → 1
False → 0

bool → subclass of int