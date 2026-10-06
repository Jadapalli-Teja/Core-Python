# Python Integer (`int`)

## 1. What is an Integer?

- An integer represents a whole number without a decimal/fractional part.
- Integers can be positive, negative, or zero.
- The type of an integer object is `int`.


Examples:

```python
10
25
-10
0
1000
```

Python uses the `int` data type to store whole numbers.

```python
age = 21
marks = 95
temperature = -5
```

Here:

```text
age          → 21
marks        → 95
temperature  → -5
```

All three variables contain integers.

---

# 2. Creating Integers

We can create an integer simply by assigning a whole number to a variable.

```python
a = 10
b = 25
c = -50
d = 0

print(a)
print(b)
print(c)
print(d)
```

Output:

```text
10
25
-50
0
```

---

# 3. Checking the Type

Use `type()` to check the data type.

```python
x = 100

print(type(x))
```

Output:

```text
<class 'int'>
```

So:

```python
type(100)
```

returns:

```text
<class 'int'>
```

---

# 4. Checking Whether a Value is an Integer

We can use `isinstance()`.

```python
x = 100

print(isinstance(x, int))
```

Output:

```text
True
```

Example:

```python
x = 10.5

print(isinstance(x, int))
```

Output:

```text
False
```

### Difference

```python
type(x) == int
```

checks the exact type.

```python
isinstance(x, int)
```

checks whether the object is an instance of `int` (including subclasses).

---

# 5. Positive, Negative and Zero

Integers can be:

### Positive

```python
x = 25
```

### Negative

```python
x = -25
```

### Zero

```python
x = 0
```

All are `int`.

```python
print(type(25))
print(type(-25))
print(type(0))
```

Output:

```text
<class 'int'>
<class 'int'>
<class 'int'>
```

---

# 6. Integers Do Not Have a Decimal Point

These are integers:

```python
10
20
-50
0
```

These are **not** integers:

```python
10.0
20.5
-5.2
```

They are `float`.

```python
print(type(10))
print(type(10.0))
```

Output:

```text
<class 'int'>
<class 'float'>
```

Even though `10` and `10.0` represent the same mathematical value, Python stores them as different types.

---

# 7. Integer Can Be Very Large

Python integers do not have a small fixed limit like some languages.

For example:

```python
x = 999999999999999999999999999999999999999999
print(x)
```

Python can handle very large integers as long as the available memory is sufficient.

---

# 8. Integer is Immutable

`int` objects are **immutable**.

This means the value of an existing integer object cannot be changed.

For example:

```python
x = 10

x = x + 5

print(x)
```

Output:

```text
15
```

It may look like `10` was changed to `15`.

But internally, Python creates/uses an integer object representing `15` and makes `x` refer to it.

Conceptually:

```text
Before:

x ───→ 10

After x = x + 5:

x ───→ 15
```

The original integer `10` itself was not modified.

---

# 9. Integer Variables Can Be Reassigned

Although integers are immutable, a variable can be reassigned.

```python
x = 10

x = 20

print(x)
```

Output:

```text
20
```

Important:

> **Immutable object does not mean the variable cannot be reassigned.**

It means the existing object cannot be modified.

---

# 10. Arithmetic Operations on Integers

Python supports many arithmetic operators.

| Operator | Meaning | Example | Result |
|---|---|---:|---:|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333333335
3
1
1000
```

---

# 11. Addition `+`

The `+` operator performs addition.

```python
a = 10
b = 20

result = a + b

print(result)
```

Output:

```text
30
```

---

# 12. Subtraction `-`

```python
a = 20
b = 8

print(a - b)
```

Output:

```text
12
```

---

# 13. Multiplication `*`

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

# 14. Division `/`

The `/` operator always returns a `float`.

```python
result = 10 / 2

print(result)
print(type(result))
```

Output:

```text
5.0
<class 'float'>
```

Even though the division is exact, the result is `float`.

```python
10 / 2
```

gives:

```text
5.0
```

not:

```text
5
```

---

# 15. Floor Division `//`

Floor division returns the floor of the division result.

```python
print(10 // 3)
```

Output:

```text
3
```

Because:

```text
10 / 3 = 3.333...
```

Floor is:

```text
3
```

### Important with negative numbers

```python
print(-10 // 3)
```

Output:

```text
-4
```

Why?

```text
-10 / 3 = -3.333...
```

Floor means the greatest integer less than or equal to the result.

So:

```text
floor(-3.333...) = -4
```

---

# 16. Modulus `%`

The `%` operator gives the **remainder**.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 = 3 × 3 + 1
```

Therefore:

```text
Quotient = 3
Remainder = 1
```

### Common use

Checking whether a number is even:

```python
n = 10

if n % 2 == 0:
    print("Even")
```

Output:

```text
Even
```

---

# 17. Power `**`

The `**` operator is used for exponentiation.

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

Another example:

```python
print(5 ** 2)
```

Output:

```text
25
```

---

# 18. Comparison Operators with Integers

Integers can be compared using:

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
a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```

Output:

```text
False
True
False
True
```

Comparison results are `bool`.

```python
x = 10

result = x > 5

print(result)
print(type(result))
```

Output:

```text
True
<class 'bool'>
```

---

# 19. Assignment Operators

Python provides shorthand assignment operators.

```python
x = 10

x += 5
print(x)
```

Output:

```text
15
```

Common operators:

```text
+=
-=
*=
/=
//=
%=
**=
```

Example:

```python
x = 10

x += 5      # x = x + 5
x -= 2      # x = x - 2
x *= 2      # x = x * 2
x //= 3     # x = x // 3
```

---

# 20. Unary Plus and Minus

### Unary plus

```python
x = 10

print(+x)
```

Output:

```text
10
```

### Unary minus

```python
x = 10

print(-x)
```

Output:

```text
-10
```

Unary minus changes the sign.

---

# 21. Converting Other Values to Integer

We can use the `int()` function.

```python
x = int("100")

print(x)
print(type(x))
```

Output:

```text
100
<class 'int'>
```

---

# 22. String to Integer

A numeric string can be converted to an integer.

```python
x = int("25")

print(x + 5)
```

Output:

```text
30
```

Without conversion:

```python
x = "25"

print(x + 5)
```

This produces:

```text
TypeError
```

because `"25"` is a string, not an integer.

---

# 23. Float to Integer

A float can be converted using `int()`.

```python
x = int(10.9)

print(x)
```

Output:

```text
10
```

`int()` removes the fractional part. It does **not** round to the nearest integer.

Examples:

```python
print(int(10.9))
print(int(10.1))
print(int(-10.9))
```

Output:

```text
10
10
-10
```

So `int()` truncates toward zero.

---

# 24. Boolean to Integer

`bool` is closely related to integers in Python.

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

In Python:

```text
True  → 1
False → 0
```

Also:

```python
print(True == 1)
print(False == 0)
```

Output:

```text
True
True
```

---

# 25. Integer to Float

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

---

# 26. Integer to String

Use `str()`.

```python
x = 100

y = str(x)

print(y)
print(type(y))
```

Output:

```text
100
<class 'str'>
```

Remember:

```text
100  → int
"100" → str
```

They look similar when printed, but they are different types.

---

# 27. Integer and Boolean Relationship

In Python, `bool` is a subclass of `int`.

Conceptually:

```text
int
└── bool
```

You can check:

```python
print(isinstance(True, int))
```

Output:

```text
True
```

And:

```python
print(isinstance(False, int))
```

Output:

```text
True
```

But normally, think of:

```text
True  → Boolean
False → Boolean
```

rather than treating them as ordinary integers.

---

# 28. Integer and `bool` as Dictionary Keys

Because:

```python
True == 1
False == 0
```

they can refer to the same dictionary key.

Example:

```python
data = {
    1: "one",
    True: "true"
}

print(data)
```

The keys collide because:

```python
1 == True
```

This is an important Python behavior to understand.

---

# 29. Integer Hashability

Integers are **hashable**.

You can use an integer as:

- a dictionary key
- a set element

Example:

```python
data = {
    10: "Python",
    20: "Java"
}

print(data[10])
```

Output:

```text
Python
```

Set example:

```python
numbers = {10, 20, 30}

print(numbers)
```

Integers can be elements of a set because they are hashable.

---

# 30. `hash()` with Integers

You can call `hash()` on an integer.

```python
x = 100

print(hash(x))
```

Output:

```text
100
```

For integers, the hash is based on the integer value.

```python
print(hash(10))
print(hash(20))
```

Output:

```text
10
20
```

The important point is:

> Integers are hashable and therefore can be used as dictionary keys and set elements.

---

# 31. Integer Truthiness

Integers can be used in conditions.

Python considers:

```text
0 → False
non-zero integer → True
```

Example:

```python
if 10:
    print("True")
```

Output:

```text
True
```

Example:

```python
if 0:
    print("True")
else:
    print("False")
```

Output:

```text
False
```

Negative numbers are also truthy:

```python
if -10:
    print("True")
```

Output:

```text
True
```

So:

```text
0       → False
1       → True
-1      → True
100     → True
-100    → True
```

---

# 32. Integer with `and` and `or`

Python's `and` and `or` return operands, not necessarily `True` or `False`.

Example:

```python
print(10 and 20)
```

Output:

```text
20
```

Because both values are truthy, `and` returns the second value.

Example:

```python
print(0 and 20)
```

Output:

```text
0
```

Because `0` is falsy.

For `or`:

```python
print(10 or 20)
```

Output:

```text
10
```

Because `10` is already truthy.

---

# 33. Integer Comparison

Integers can be compared mathematically.

```python
a = 10
b = 20

print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
```

Output:

```text
True
False
True
False
False
True
```

---

# 34. Integer Equality vs Identity

`==` checks whether values are equal.

`is` checks whether two variables refer to the same object.

Example:

```python
a = 100
b = 100

print(a == b)
print(a is b)
```

`==` is the correct operator for comparing values.

Do not use:

```python
a is b
```

when your intention is simply to check whether two integers have the same value.

Use:

```python
a == b
```

---

# 35. Integer Literals in Different Bases

Python allows integer literals in different number systems.

### Decimal

```python
x = 10
```

### Binary

Prefix:

```text
0b
```

Example:

```python
x = 0b1010

print(x)
```

Output:

```text
10
```

### Octal

Prefix:

```text
0o
```

```python
x = 0o12

print(x)
```

Output:

```text
10
```

### Hexadecimal

Prefix:

```text
0x
```

```python
x = 0xA

print(x)
```

Output:

```text
10
```

So:

```text
0b1010 = 10
0o12   = 10
0xA    = 10
```

All are stored as Python integers.

---

# 36. Converting Decimal to Other Bases

Python provides built-in functions.

### Decimal to binary

```python
print(bin(10))
```

Output:

```text
0b1010
```

### Decimal to octal

```python
print(oct(10))
```

Output:

```text
0o12
```

### Decimal to hexadecimal

```python
print(hex(10))
```

Output:

```text
0xa
```

The returned values from `bin()`, `oct()`, and `hex()` are strings.

---

# 37. Underscores in Integer Literals

Python allows underscores to make large numbers easier to read.

```python
salary = 1_00_000

print(salary)
```

Output:

```text
100000
```

Another example:

```python
population = 1_000_000
```

The underscores are only for readability.

```python
1_000_000
```

has the same value as:

```python
1000000
```

---

# 38. Integer Division by Zero

Division by zero is not allowed.

```python
print(10 / 0)
```

This raises:

```text
ZeroDivisionError
```

Similarly:

```python
print(10 // 0)
print(10 % 0)
```

also raise `ZeroDivisionError`.

---

# 39. Arithmetic Expression Evaluation

Python follows operator precedence.

For example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Why?

Multiplication happens first:

```text
5 * 2 = 10

10 + 10 = 20
```

Use parentheses when you want to control the order:

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

Basic order to remember:

```text
()
**
*, /, //, %
+, -
```

---

# 40. Integer Functions

Some useful built-in functions work with integers.

### `abs()`

Returns the absolute value.

```python
print(abs(-10))
```

Output:

```text
10
```

---

### `pow()`

```python
print(pow(2, 3))
```

Output:

```text
8
```

Similar to:

```python
2 ** 3
```

---

### `divmod()`

Returns quotient and remainder together.

```python
result = divmod(10, 3)

print(result)
```

Output:

```text
(3, 1)
```

So:

```text
quotient  = 3
remainder = 1
```

---

### `round()`

```python
print(round(10.7))
```

Output:

```text
11
```

`round()` is mainly useful with floating-point values, but it can also accept integers.

---

# 41. `min()` and `max()`

```python
numbers = [10, 20, 5, 30]

print(min(numbers))
print(max(numbers))
```

Output:

```text
5
30
```

---

# 42. `sum()`

```python
numbers = [10, 20, 30]

print(sum(numbers))
```

Output:

```text
60
```

---

# 43. Integer in Loops

Integers are commonly used with loops.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

Here `i` takes integer values.

---

# 44. Integer with `range()`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

`range()` is commonly used when working with integer sequences.

---

# 45. Integer Input from User

`input()` always returns a string.

Example:

```python
age = input("Enter age: ")

print(type(age))
```

If the user enters:

```text
21
```

the type is still:

```text
<class 'str'>
```

To get an integer:

```python
age = int(input("Enter age: "))

print(type(age))
```

Now:

```text
<class 'int'>
```

This is extremely important in Python programs.

---

# 46. Practical Example: Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a + b

print("Sum:", result)
```

Example:

```text
Enter first number: 10
Enter second number: 20
Sum: 30
```

---

# 47. Practical Example: Even or Odd

```python
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Example:

```text
Enter a number: 10
Even
```

The logic is:

```text
n % 2 == 0
```

If the remainder is `0`, the number is even.

---

# 48. Practical Example: Positive, Negative or Zero

```python
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

---

# 49. Practical Example: Sum of Digits

```python
n = 1234
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)
```

Output:

```text
10
```

Because:

```text
1 + 2 + 3 + 4 = 10
```

Here:

```python
n % 10
```

gets the last digit.

And:

```python
n // 10
```

removes the last digit.

This is a very important integer programming technique.

---

# 50. Practical Example: Reverse a Number

```python
n = 1234
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)
```

Output:

```text
4321
```

Important operations:

```text
n % 10   → get last digit
n // 10  → remove last digit
```

---

# 51. Practical Example: Count Digits

```python
n = 12345
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)
```

Output:

```text
5
```

---

# 52. Integer vs Float

| Feature | `int` | `float` |
|---|---|---|
| Example | `10` | `10.5` |
| Decimal point | No | Yes |
| Whole number | Yes | Can represent fractional values |
| `/` result | Usually float | Float |
| Mutable | No | No |
| Hashable | Yes | Yes |

Example:

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

---

# 53. Integer vs String

```python
a = 100
b = "100"
```

They look similar when printed, but:

```text
a → int
b → str
```

Therefore:

```python
print(a + 10)
```

works:

```text
110
```

But:

```python
print(b + 10)
```

raises:

```text
TypeError
```

---

# 54. Integer Object and Variable

Consider:

```python
x = 10
```

It is better to think:

```text
x ─────→ integer object 10
```

The variable `x` is a **name/reference**.

The integer `10` is the **object**.

If:

```python
x = 20
```

then:

```text
x ─────→ integer object 20
```

The variable now refers to another object.

---

# 55. Integer Immutability Example

Consider:

```python
x = 10

x += 5
```

Conceptually:

```text
Before:

x ───→ 10

x += 5

After:

x ───→ 15
```

The integer object `10` was not modified.

This is why integers are called **immutable objects**.

---

# 56. Important Characteristics of `int`

Remember these points:

```text
1. int represents whole numbers.
2. It can be positive, negative or zero.
3. int is immutable.
4. Python integers can be very large.
5. int is hashable.
6. int can be used as a dictionary key.
7. int can be a set element.
8. / returns float.
9. // performs floor division.
10. % gives the remainder.
11. ** performs exponentiation.
12. int() converts compatible values to integers.
13. 0 is falsy.
14. Non-zero integers are truthy.
15. bool is a subclass of int.
```

---

# 57. Common Mistakes

### Mistake 1: Thinking `10.0` is an integer

```python
10.0
```

is:

```text
float
```

not `int`.

---

### Mistake 2: Expecting `/` to return an integer

```python
10 / 2
```

returns:

```text
5.0
```

Use:

```python
10 // 2
```

if you want floor division.

---

### Mistake 3: Thinking `int(10.9)` rounds

```python
int(10.9)
```

returns:

```text
10
```

It does not return `11`.

---

### Mistake 4: Forgetting `input()` returns string

```python
age = input()
```

`age` is a string.

Use:

```python
age = int(input())
```

when you need an integer.

---

### Mistake 5: Dividing by zero

```python
10 / 0
```

raises:

```text
ZeroDivisionError
```

---

### Mistake 6: Using `is` to compare integer values

Prefer:

```python
a == b
```

for value comparison.

---

# 58. Important Integer Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor division | `10 // 3` |
| `%` | Remainder | `10 % 3` |
| `**` | Power | `2 ** 3` |
| `==` | Equal | `10 == 10` |
| `!=` | Not equal | `10 != 20` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `10 < 20` |
| `>=` | Greater/equal | `10 >= 10` |
| `<=` | Less/equal | `10 <= 20` |

---

# 59. Useful Integer Functions

| Function | Purpose | Example |
|---|---|---|
| `int()` | Convert to integer | `int("10")` |
| `float()` | Convert to float | `float(10)` |
| `str()` | Convert to string | `str(10)` |
| `abs()` | Absolute value | `abs(-10)` |
| `pow()` | Power | `pow(2, 3)` |
| `divmod()` | Quotient + remainder | `divmod(10, 3)` |
| `bin()` | Binary representation | `bin(10)` |
| `oct()` | Octal representation | `oct(10)` |
| `hex()` | Hexadecimal representation | `hex(10)` |
| `type()` | Check type | `type(10)` |
| `isinstance()` | Check instance | `isinstance(10, int)` |

---

# 60. Quick Revision

```text
int
│
├── Whole numbers
│
├── Positive
│   └── 10
│
├── Negative
│   └── -10
│
├── Zero
│   └── 0
│
├── Immutable
│
├── Hashable
│
├── Dictionary key ✔
│
├── Set element ✔
│
├── /  → float
├── // → floor division
├── %  → remainder
└── ** → power
```

---

# 61. One-Line Definition

> **`int` is an immutable Python data type used to represent whole numbers without a decimal point, including positive numbers, negative numbers, and zero.**

---

# 62. Final Example

```python
age = 21
marks = 95
negative_number = -10
zero = 0

print(age)
print(type(age))

print(marks + 5)
print(10 // 3)
print(10 % 3)
print(2 ** 4)

if age >= 18:
    print("Adult")
```

Output:

```text
21
<class 'int'>
100
3
1
16
Adult
```

### Remember this mental model

```text
int
 ↓
Whole numbers
 ↓
Immutable
 ↓
Hashable
 ↓
Supports arithmetic
 ↓
Used heavily in calculations,
loops, indexing and problem solving
```