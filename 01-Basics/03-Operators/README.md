# Python Operators

## 1. Introduction

When we write a Python program, we usually need to perform some kind of operation.

For example:

```python
a = 10
b = 5
```

We may want to:

- Add `a` and `b`
- Subtract `b` from `a`
- Check whether `a` is greater than `b`
- Check whether a value exists in a list
- Combine two conditions
- Change the value of a variable
- Work with binary numbers
- Check whether two variables refer to the same object

Python provides **operators** for all these tasks.

---

# 2. What is an Operator?

An **operator** is a symbol or keyword that tells Python to perform an operation.

Example:

```python
10 + 5
```

Here:

```text
10 + 5
↑  ↑  ↑
│  │  │
│  │  └── Operand
│  └───── Operator
└──────── Operand
```

`+` tells Python to add `10` and `5`.

Therefore:

```text
10 + 5 = 15
```

---

# 3. What is an Operand?

An **operand** is the value on which an operator works.

Example:

```python
10 + 5
```

There are two operands:

```text
10 → operand
5  → operand
```

and one operator:

```text
+ → operator
```

Another example:

```python
age > 18
```

Here:

```text
age → operand
>   → operator
18  → operand
```

---

# 4. Why are Operators Important?

Operators are used in almost every Python program.

### Example 1 — Calculate total price

```python
price = 100
quantity = 3

total = price * quantity

print(total)
```

Output:

```text
300
```

### Example 2 — Check age

```python
age = 21

print(age >= 18)
```

Output:

```text
True
```

### Example 3 — Check whether a number exists

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

### Example 4 — Combine conditions

```python
age = 21

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

All these examples use operators.

---

# 5. Categories of Python Operators

Python operators can be grouped into the following categories:

```text
Python Operators
│
├── 1. Arithmetic Operators
│
├── 2. Assignment Operators
│
├── 3. Comparison Operators
│
├── 4. Logical Operators
│
├── 5. Bitwise Operators
│
├── 6. Membership Operators
│
├── 7. Identity Operators
│
└── 8. Operator Precedence
```

We will understand each category in detail.

---

# 6. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

Python provides seven main arithmetic operators:

```text
+      Addition
-      Subtraction
*      Multiplication
/      Division
//     Floor Division
%      Modulus
**     Exponentiation
```

Example:

```python
a = 10
b = 3
```

Let's understand each one.

---

# 7. Addition Operator `+`

The `+` operator adds two values.

```python
a = 10
b = 5

result = a + b

print(result)
```

Output:

```text
15
```

Python evaluates:

```text
10 + 5
↓
15
```

---

## Addition with Different Numeric Types

### int + int

```python
print(10 + 5)
```

Output:

```text
15
```

Result:

```text
int
```

### int + float

```python
print(10 + 2.5)
```

Output:

```text
12.5
```

Result:

```text
float
```

### float + float

```python
print(2.5 + 1.5)
```

Output:

```text
4.0
```

---

# 8. Addition with Strings

The `+` operator does something different with strings.

```python
first = "Hello"
second = "Python"

print(first + second)
```

Output:

```text
HelloPython
```

Here `+` means:

> Concatenate (join) the strings.

We can add a space:

```python
print(first + " " + second)
```

Output:

```text
Hello Python
```

Therefore:

```text
number + number
        ↓
addition

string + string
        ↓
concatenation
```

---

# 9. String + Number

This is a common beginner mistake.

```python
age = 21

print("Age: " + age)
```

This produces:

```text
TypeError
```

Why?

Because:

```text
"Age: " → str
21      → int
```

Python does not automatically concatenate them using `+`.

Convert the number:

```python
print("Age: " + str(age))
```

Output:

```text
Age: 21
```

Or use an f-string:

```python
print(f"Age: {age}")
```

---

# 10. Addition with Lists

The `+` operator can concatenate lists.

```python
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

So:

```text
[1, 2] + [3, 4]
        ↓
[1, 2, 3, 4]
```

But:

```python
[1, 2] + (3, 4)
```

is not allowed because one is a list and the other is a tuple.

---

# 11. Subtraction Operator `-`

The `-` operator subtracts one number from another.

```python
a = 10
b = 3

print(a - b)
```

Output:

```text
7
```

Python evaluates:

```text
10 - 3
↓
7
```

Subtraction is normally used with numeric types.

---

# 12. Multiplication Operator `*`

The `*` operator performs multiplication.

```python
a = 10
b = 5

print(a * b)
```

Output:

```text
50
```

---

## Multiplication with Different Numeric Types

```python
print(10 * 2)
print(10 * 2.5)
print(2.5 * 2)
```

Output:

```text
20
25.0
5.0
```

---

# 13. Multiplication with Strings

`*` can also repeat a string.

```python
print("Python" * 3)
```

Output:

```text
PythonPythonPython
```

Here:

```text
string * integer
        ↓
repeat string
```

---

# 14. Multiplication with Lists

Lists can also be repeated.

```python
numbers = [1, 2, 3]

print(numbers * 2)
```

Output:

```text
[1, 2, 3, 1, 2, 3]
```

Important:

```text
"Hi" * 3
```

does not mean mathematical multiplication.

It means:

> Repeat `"Hi"` three times.

---

# 15. Division Operator `/`

The `/` operator performs normal division.

```python
print(10 / 2)
```

Output:

```text
5.0
```

Notice something important:

```text
10 → int
2  → int
```

but:

```text
10 / 2 → 5.0
```

The result is a `float`.

```python
result = 10 / 2

print(type(result))
```

Output:

```text
<class 'float'>
```

So:

```text
int / int → float
```

---

# 16. Division with a Remainder

```python
print(10 / 3)
```

Output:

```text
3.3333333333333335
```

Normal division gives the complete quotient as a floating-point value.

---

# 17. Division by Zero

This is invalid:

```python
print(10 / 0)
```

Python raises:

```text
ZeroDivisionError
```

The same problem occurs with:

```python
10 // 0
```

and:

```python
10 % 0
```

Remember:

> You cannot divide by zero in Python.

---

# 18. Floor Division `//`

Floor division divides two values and returns the **floor** of the result.

Example:

```python
print(10 // 3)
```

Normal division:

```text
10 / 3
↓
3.333...
```

Floor:

```text
3
```

Therefore:

```text
10 // 3
↓
3
```

---

# 19. `/` vs `//`

This is extremely important.

```python
print(10 / 3)
print(10 // 3)
```

Output:

```text
3.3333333333333335
3
```

Remember:

```text
/  → normal division

// → floor division
```

---

# 20. Floor Division with Negative Numbers

This is where many beginners become confused.

```python
print(-10 // 3)
```

Output:

```text
-4
```

Why not `-3`?

Because:

```text
-10 / 3
≈ -3.333
```

Floor means:

> Go toward negative infinity.

The numbers around `-3.333` are:

```text
-4   -3.333   -3
```

The floor is:

```text
-4
```

Therefore:

```text
-10 // 3 = -4
```

---

# 21. Modulus Operator `%`

The `%` operator gives the **remainder** after division.

Example:

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 ÷ 3

3 × 3 = 9
10 - 9 = 1
```

Therefore:

```text
10 % 3 = 1
```

---

# 22. Another Modulus Example

```python
print(20 % 4)
```

Output:

```text
0
```

Because 20 is completely divisible by 4.

This is very useful for checking whether a number is even or odd.

---

# 23. Even and Odd Numbers Using `%`

A number is even when its remainder after division by `2` is zero.

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

For an odd number:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

This is one of the most important practical uses of `%`.

---

# 24. Exponentiation Operator `**`

The `**` operator is used for powers.

Example:

```python
print(2 ** 3)
```

This means:

```text
2 × 2 × 2
```

Result:

```text
8
```

Therefore:

```text
2 ** 3 = 8
```

---

# 25. More Exponentiation Examples

```python
print(5 ** 2)
print(10 ** 2)
print(2 ** 5)
```

Output:

```text
25
100
32
```

Remember:

```text
5 ** 2
```

means:

> 5 raised to the power 2.

---

# 26. Square and Cube

### Square

```python
number = 5

print(number ** 2)
```

Output:

```text
25
```

### Cube

```python
number = 5

print(number ** 3)
```

Output:

```text
125
```

---

# 27. Unary Plus and Unary Minus

The `+` and `-` operators can also work with one operand.

Example:

```python
x = 10

print(-x)
print(+x)
```

Output:

```text
-10
10
```

Here `-x` means:

> Change the sign of `x`.

---

# 28. Arithmetic Operator Summary

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

# 29. Assignment Operators

Assignment operators are used to assign values to variables.

The most basic one is:

```text
=
```

Example:

```python
x = 10
```

Think of it as:

```text
10
 ↓
x
```

The value `10` is assigned to `x`.

---

# 30. `=` Does Not Mean Mathematical Equality

In mathematics:

```text
x = 10
```

can mean equality.

In programming, Python interprets:

```python
x = 10
```

as:

> Assign the value `10` to `x`.

To check equality, Python uses:

```text
==
```

Example:

```python
x = 10

print(x == 10)
```

Output:

```text
True
```

---

# 31. `+=`

`+=` adds a value to the existing variable.

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

This is equivalent to:

```python
x = x + 5
```

Step-by-step:

```text
x = 10

x += 5
↓
x = x + 5
↓
x = 10 + 5
↓
x = 15
```

---

# 32. `-=`

```python
x = 10

x -= 3

print(x)
```

Output:

```text
7
```

Equivalent to:

```python
x = x - 3
```

---

# 33. `*=`

```python
x = 10

x *= 3

print(x)
```

Output:

```text
30
```

Equivalent to:

```python
x = x * 3
```

---

# 34. `/=`

```python
x = 10

x /= 2

print(x)
```

Output:

```text
5.0
```

Equivalent to:

```python
x = x / 2
```

Notice the result becomes a float.

---

# 35. `//=`

```python
x = 10

x //= 3

print(x)
```

Output:

```text
3
```

Equivalent to:

```python
x = x // 3
```

---

# 36. `%=`

```python
x = 10

x %= 3

print(x)
```

Output:

```text
1
```

Equivalent to:

```python
x = x % 3
```

---

# 37. `**=`

```python
x = 2

x **= 3

print(x)
```

Output:

```text
8
```

Equivalent to:

```python
x = x ** 3
```

---

# 38. Assignment Operator Summary

```text
x = 10

x += 5     → x = x + 5
x -= 5     → x = x - 5
x *= 5     → x = x * 5
x /= 5     → x = x / 5
x //= 5    → x = x // 5
x %= 5     → x = x % 5
x **= 5    → x = x ** 5
```

---

# 39. Comparison Operators

Comparison operators compare two values.

They normally return:

```text
True
```

or:

```text
False
```

The operators are:

```text
==    Equal
!=    Not equal
>     Greater than
<     Less than
>=    Greater than or equal
<=    Less than or equal
```

---

# 40. Equal to `==`

```python
print(10 == 10)
```

Output:

```text
True
```

Python asks:

```text
Is 10 equal to 10?
```

Yes.

```python
print(10 == 5)
```

Output:

```text
False
```

---

# 41. Not Equal `!=`

```python
print(10 != 5)
```

Output:

```text
True
```

Python asks:

```text
Are 10 and 5 different?
```

Yes.

---

# 42. Greater Than `>`

```python
print(10 > 5)
```

Output:

```text
True
```

Because 10 is greater than 5.

---

# 43. Less Than `<`

```python
print(5 < 10)
```

Output:

```text
True
```

Because 5 is less than 10.

---

# 44. Greater Than or Equal `>=`

```python
print(10 >= 10)
print(10 >= 5)
```

Output:

```text
True
True
```

It is true when:

```text
greater
OR
equal
```

---

# 45. Less Than or Equal `<=`

```python
print(5 <= 5)
print(5 <= 10)
```

Output:

```text
True
True
```

It is true when:

```text
less
OR
equal
```

---

# 46. Comparison Operator Example

```python
marks = 75

print(marks >= 40)
```

Output:

```text
True
```

This can be used in a program:

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Pass
```

---

# 47. Comparing Different Numeric Types

Python can compare numeric types.

```python
print(10 == 10.0)
```

Output:

```text
True
```

Although:

```text
10     → int
10.0   → float
```

they represent the same numeric value.

---

# 48. Comparing Strings

Strings can also be compared.

```python
print("apple" == "apple")
```

Output:

```text
True
```

```python
print("apple" == "Apple")
```

Output:

```text
False
```

Python string comparison is case-sensitive.

---

# 49. Logical Operators

Logical operators are used mainly with conditions.

There are three:

```text
and
or
not
```

---

# 50. `and`

`and` combines two conditions.

For the basic Boolean case:

```text
True and True   → True
True and False  → False
False and True  → False
False and False → False
```

The result is true only when both conditions are true.

Example:

```python
age = 25

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

Both conditions are true:

```text
25 >= 18 → True

25 <= 60 → True
```

Therefore:

```text
True and True
↓
True
```

---

# 51. `or`

`or` is true when at least one condition is true.

```text
True or True   → True
True or False  → True
False or True  → True
False or False → False
```

Example:

```python
age = 15

print(age < 18 or age > 60)
```

Output:

```text
True
```

Because:

```text
15 < 18 → True
```

---

# 52. `not`

`not` reverses a Boolean truth value.

```python
print(not True)
print(not False)
```

Output:

```text
False
True
```

Think:

```text
True  → not → False
False → not → True
```

---

# 53. Important: `and` and `or` Return Operands

This is an important Python concept.

Beginners often think:

```python
10 and 20
```

must return:

```text
True
```

But Python actually returns:

```text
20
```

Example:

```python
print(10 and 20)
```

Output:

```text
20
```

Why?

Because both values are truthy, so Python returns the second operand.

Similarly:

```python
print(10 or 20)
```

Output:

```text
10
```

`or` returns the first truthy operand.

This behavior is very important in Python.

---

# 54. Short-Circuit Evaluation

Python does not always evaluate every part of a logical expression.

Example:

```python
False and something
```

Python already knows the whole expression must be false.

So it can stop.

Similarly:

```python
True or something
```

Python already knows the whole expression is true.

This is called **short-circuit evaluation**.

---

# 55. Bitwise Operators

Bitwise operators work on individual bits.

Operators:

```text
&     AND
|     OR
^     XOR
~     NOT
<<    Left Shift
>>    Right Shift
```

Before learning these, understand binary numbers.

---

# 56. Decimal and Binary

Normally we use decimal numbers:

```text
0 1 2 3 4 5 6 7 8 9
```

Computers work internally with binary:

```text
0 and 1
```

For example:

```text
5 = 101
```

because:

```text
1 × 4
0 × 2
1 × 1

= 5
```

And:

```text
3 = 011
```

---

# 57. Bitwise AND `&`

Example:

```python
print(5 & 3)
```

Convert to binary:

```text
5 = 101
3 = 011
```

Perform AND:

```text
  101
& 011
-----
  001
```

`001` is decimal `1`.

Therefore:

```text
5 & 3 = 1
```

---

# 58. Bitwise OR `|`

```python
print(5 | 3)
```

Binary:

```text
5 = 101
3 = 011
```

OR:

```text
  101
| 011
-----
  111
```

`111` is decimal `7`.

Therefore:

```text
5 | 3 = 7
```

---

# 59. Bitwise XOR `^`

XOR means:

```text
Same bits → 0
Different bits → 1
```

Example:

```text
  101
^ 011
-----
  110
```

`110` is decimal `6`.

Therefore:

```python
print(5 ^ 3)
```

Output:

```text
6
```

---

# 60. Bitwise NOT `~`

The `~` operator flips bits.

Example:

```python
print(~5)
```

Output:

```text
-6
```

This is initially confusing.

Python integers use signed integer representation, and the useful identity to remember is:

```text
~x = -(x + 1)
```

Therefore:

```text
~5
= -(5 + 1)
= -6
```

---

# 61. Left Shift `<<`

Left shift moves bits to the left.

Example:

```python
print(5 << 1)
```

Binary:

```text
5 = 101
```

Shift left by one:

```text
1010
```

`1010` is decimal `10`.

Therefore:

```text
5 << 1 = 10
```

For positive integers, shifting left by one is equivalent to multiplying by 2.

---

# 62. Right Shift `>>`

Right shift moves bits to the right.

```python
print(10 >> 1)
```

Binary:

```text
10 = 1010
```

Shift right:

```text
0101
```

`0101` is `5`.

Therefore:

```text
10 >> 1 = 5
```

For positive integers, shifting right by one is equivalent to integer division by 2.

---

# 63. Membership Operators

Membership operators answer:

> Does this value exist inside this object?

There are two:

```text
in
not in
```

---

# 64. `in` with String

```python
text = "Python"

print("Py" in text)
```

Output:

```text
True
```

Python searches inside the string.

```python
print("Java" in text)
```

Output:

```text
False
```

---

# 65. `in` with List

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

```python
print(50 in numbers)
```

Output:

```text
False
```

---

# 66. `in` with Tuple

```python
values = (10, 20, 30)

print(20 in values)
```

Output:

```text
True
```

---

# 67. `in` with Set

```python
values = {10, 20, 30}

print(20 in values)
```

Output:

```text
True
```

---

# 68. `in` with Dictionary

This is important.

```python
student = {
    "name": "Teja",
    "age": 21
}

print("name" in student)
```

Output:

```text
True
```

But:

```python
print("Teja" in student)
```

Output:

```text
False
```

Why?

Because membership on a dictionary checks **keys**.

```text
"name" → key
"age"  → key

"Teja" → value
21     → value
```

Therefore:

```text
"name" in student
↓
checks keys
```

---

# 69. `not in`

`not in` means:

> The value does not exist inside the object.

Example:

```python
numbers = [10, 20, 30]

print(50 not in numbers)
```

Output:

```text
True
```

---

# 70. Identity Operators

There are two identity operators:

```text
is
is not
```

They check **object identity**.

This is different from comparing values.

---

# 71. Understanding Objects First

Consider:

```python
a = [10, 20]
```

Python creates a list object.

Think of:

```text
a
↓
┌───────────┐
│ 10 │ 20   │
└───────────┘
```

Now:

```python
b = a
```

Python does not create another list.

Instead:

```text
a ───────┐
         ↓
      ┌───────────┐
      │ 10 │ 20   │
      └───────────┘
         ↑
         │
b ───────┘
```

Both `a` and `b` refer to the same object.

Therefore:

```python
print(a is b)
```

Output:

```text
True
```

---

# 72. `==` vs `is`

Now look at this:

```python
a = [10, 20]
b = [10, 20]
```

Python creates two separate lists:

```text
a ─────→ [10, 20]

b ─────→ [10, 20]
```

The values are equal:

```python
print(a == b)
```

Output:

```text
True
```

But they are different objects:

```python
print(a is b)
```

Output:

```text
False
```

Therefore:

```text
== → Do the values compare equal?

is → Are they the same object?
```

---

# 73. When Should `is` Be Used?

The most common use is checking for `None`.

Correct:

```python
value = None

if value is None:
    print("No value")
```

Output:

```text
No value
```

Use:

```text
is None
```

rather than:

```text
== None
```

for this purpose.

---

# 74. `is not`

`is not` checks whether two references do not refer to the same object.

Example:

```python
a = [1, 2]
b = [1, 2]

print(a is not b)
```

Output:

```text
True
```

They are different objects.

---

# 75. Operator Precedence

When Python sees multiple operators in one expression, it needs to know which operation happens first.

Example:

```python
result = 10 + 5 * 2
```

Python does not simply read from left to right.

It follows precedence rules.

First:

```text
5 * 2
```

Then:

```text
10 + 10
```

Therefore:

```text
20
```

---

# 76. Parentheses Have High Priority

Consider:

```python
10 + 5 * 2
```

Result:

```text
20
```

Now:

```python
(10 + 5) * 2
```

Result:

```text
30
```

Why?

Because parentheses tell Python:

> Do this operation first.

---

# 77. Basic Precedence Order

For normal beginner-to-intermediate expressions, remember:

```text
1. ( )                  Parentheses

2. **                   Exponentiation

3. +x, -x, ~x           Unary operators

4. *, /, //, %          Multiplication/Division

5. +, -                 Addition/Subtraction

6. <<, >>               Shifts

7. &                    Bitwise AND

8. ^                    Bitwise XOR

9. |                    Bitwise OR

10. Comparisons         < > <= >= == !=

11. not                 Logical NOT

12. and                 Logical AND

13. or                  Logical OR
```

Assignment happens at a lower precedence level.

---

# 78. Example of Multiple Operators

Consider:

```python
result = 10 + 2 * 3
```

Step 1:

```text
2 * 3 = 6
```

Step 2:

```text
10 + 6 = 16
```

Final:

```text
16
```

---

# 79. Example with Parentheses

```python
result = (10 + 2) * 3
```

Step 1:

```text
10 + 2 = 12
```

Step 2:

```text
12 * 3 = 36
```

Final:

```text
36
```

---

# 80. Unary Operators

A unary operator works with **one operand**.

Example:

```python
x = 10

print(-x)
```

Here:

```text
- → operator
x → operand
```

Another example:

```python
print(not True)
```

`not` has one operand:

```text
True
```

---

# 81. Binary Operators

A binary operator works with **two operands**.

Example:

```python
10 + 5
```

```text
10 → operand
+  → operator
5  → operand
```

Examples:

```text
10 + 5
10 - 5
10 * 5
10 > 5
10 == 5
```

---

# 82. Conditional Expression

Python also provides a short form of `if-else`.

Syntax:

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 21

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output:

```text
Adult
```

Understand it as:

```text
Is age >= 18?
      │
   ┌──┴──┐
 Yes     No
  │       │
Adult   Minor
```

This is called a **conditional expression**.

---

# 83. Important Type Behavior

Operators depend on the data types.

### int + int

```python
10 + 5
```

Result:

```text
15
```

### int + float

```python
10 + 2.5
```

Result:

```text
12.5
```

### str + str

```python
"Hello" + "World"
```

Result:

```text
HelloWorld
```

### list + list

```python
[1, 2] + [3, 4]
```

Result:

```text
[1, 2, 3, 4]
```

But:

```python
10 + "20"
```

causes:

```text
TypeError
```

Therefore:

> Always consider the data types of the operands before applying an operator.

---

# 84. Operators That Return Boolean Values

These operators normally produce `True` or `False`:

### Comparison

```text
== != > < >= <=
```

### Membership

```text
in
not in
```

### Identity

```text
is
is not
```

Example:

```python
print(10 > 5)
print(10 in [10, 20])
print(None is None)
```

Output:

```text
True
True
True
```

---

# 85. Common Beginner Confusions

## `=` vs `==`

```text
=   → assignment
==  → equality comparison
```

---

## `==` vs `is`

```text
==  → value equality
is  → object identity
```

---

## `/` vs `//`

```text
/   → normal division
//  → floor division
```

---

## `/` vs `%`

```text
/   → division result
%   → remainder
```

---

## `and` vs `&`

```text
and → logical AND
&   → bitwise AND
```

---

## `or` vs `|`

```text
or → logical OR
|  → bitwise OR
```

---

# 86. Complete Operator Table

| Category | Operators | Purpose |
|---|---|---|
| Arithmetic | `+ - * / // % **` | Mathematical operations |
| Assignment | `= += -= *= /= //= %= **=` | Assign/update values |
| Comparison | `== != > < >= <=` | Compare values |
| Logical | `and or not` | Work with conditions |
| Bitwise | `& \| ^ ~ << >>` | Work with bits |
| Membership | `in`, `not in` | Check membership |
| Identity | `is`, `is not` | Check object identity |

---

# 87. Complete Operator Map

```text
                         OPERATORS
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
   Arithmetic            Assignment           Comparison
       │                     │                     │
+ - * / // % **        = += -= *= ...       == != > < >= <=
       │
       │
       ├─────────────────────┐
       │                     │
    Logical               Bitwise
       │                     │
 and or not             & | ^ ~ << >>
       │
       ├─────────────────────┐
       │                     │
  Membership             Identity
       │                     │
 in / not in            is / is not
```

---

# 88. Real-World Example Combining Operators

Let's build a simple eligibility program.

```python
age = 21
has_id = True

eligible = age >= 18 and has_id

print(eligible)
```

Output:

```text
True
```

Let's understand it step by step.

### Step 1

```text
age >= 18
```

becomes:

```text
21 >= 18
```

Result:

```text
True
```

### Step 2

```text
has_id
```

is:

```text
True
```

### Step 3

```text
True and True
```

Result:

```text
True
```

So:

```text
eligible = True
```

This is how different operators work together.

---

# 89. Another Real-World Example

Calculate whether a student passed.

```python
marks = 75
attendance = 80

passed = marks >= 40 and attendance >= 75

print(passed)
```

Output:

```text
True
```

Here:

```text
marks >= 40
        ↓
      True

attendance >= 75
        ↓
      True

True and True
        ↓
      True
```

---

# 90. Operator Learning Order

We will learn your operators folder in this order:

```text
03-Operators
│
├── README.md
│
├── 01-Arithmetic-Operators
│   ├── README.md
│   └── arithmetic.py
│
├── 02-Assignment-Operators
│   ├── README.md
│   └── assignment.py
│
├── 03-Comparison-Operators
│   ├── README.md
│   └── comparison.py
│
├── 04-Logical-Operators
│   ├── README.md
│   └── logical.py
│
├── 05-Bitwise-Operators
│   ├── README.md
│   └── bitwise.py
│
├── 06-Membership-Operators
│   ├── README.md
│   └── membership.py
│
├── 07-Identity-Operators
│   ├── README.md
│   └── identity.py
│
└── 08-Operator-Precedence
    ├── README.md
    └── precedence.py
```

---

# Quick Revision

## Arithmetic

Used for calculations:

```text
+ - * / // % **
```

## Assignment

Used to assign/update:

```text
= += -= *= /= //= %= **=
```

## Comparison

Used to compare:

```text
== != > < >= <=
```

Normally returns:

```text
True / False
```

## Logical

Used to combine conditions:

```text
and or not
```

## Bitwise

Used to work with bits:

```text
& | ^ ~ << >>
```

## Membership

Used to check whether a value exists:

```text
in
not in
```

## Identity

Used to check whether two references point to the same object:

```text
is
is not
```

## Precedence

Determines which operation happens first.

---

# Most Important Things to Remember

```text
=       → assign a value

==      → compare values

is      → compare object identity

+       → addition / concatenation

*       → multiplication / repetition

/       → normal division

//      → floor division

%       → remainder

**      → power

and     → logical AND

or      → logical OR

not     → logical NOT

&       → bitwise AND

|       → bitwise OR

^       → bitwise XOR

~       → bitwise NOT

<<      → left shift

>>      → right shift

in      → membership

not in  → not a member

is      → same object

is not  → different object
```

---

# Final Definition

> **An operator is a symbol or keyword that tells Python to perform an operation on one or more operands.**

Operators are one of the most important foundations of Python because they are used in:

```text
Calculations
    ↓
Conditions
    ↓
Loops
    ↓
Functions
    ↓
Data structures
    ↓
Algorithms
    ↓
Real-world programs
```