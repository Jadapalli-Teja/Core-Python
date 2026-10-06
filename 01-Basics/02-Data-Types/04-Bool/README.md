# Python Boolean (`bool`)

## 1. What is Boolean?

- Boolean represents a logical value.
- Python has only two Boolean values:
  - `True`
  - `False`
- The type of these values is `bool`.
Example:

```python
is_student = True
is_employee = False

print(is_student)
print(is_employee)
```

**Output:**
```text
True
False
```

Boolean values are mainly used in:

- Conditions
- Comparisons
- Decision making
- Loops
- Validation
- Flags
- Logical operations

---

# 2. Boolean Values

Python has only two Boolean values:

```python
True
False
```

They must start with a **capital letter**.

Correct:

```python
True
False
```

Incorrect:

```python
true
false
```

Python is case-sensitive.

```python
x = True
print(type(x))
```

**Output:**
```text
<class 'bool'>
```

---

# 3. Type of Boolean

Use `type()` to check the data type.

```python
print(type(True))
print(type(False))
```

**Output:**
```text
<class 'bool'>
<class 'bool'>
```

Therefore:

```text
True  → bool
False → bool
```

---

# 4. Creating Boolean Values

Boolean values can be directly assigned to variables.

```python
is_logged_in = True
is_admin = False
has_permission = True

print(is_logged_in)
print(is_admin)
print(has_permission)
```

**Output:**
```text
True
False
True
```

---

# 5. Boolean Values from Comparisons

Most comparison operations return a Boolean value.

Example:

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
```

**Output:**
```text
True
False
True
False
```

### Comparison operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal | `10 == 10` | `True` |
| `!=` | Not equal | `10 != 5` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal | `10 >= 10` | `True` |
| `<=` | Less than or equal | `5 <= 10` | `True` |

Example:

```python
age = 21

print(age >= 18)
```

**Output:**
```text
True
```

---

# 6. Boolean as a Result of Conditions

Boolean values are commonly used with `if`.

```python
age = 21

if age >= 18:
    print("Eligible")
```

**Output:**
```text
Eligible
```

The condition:

```python
age >= 18
```

produces:

```python
True
```

So Python executes the `if` block.

---

# 7. Boolean with `if-else`

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

**Output:**
```text
Not Eligible
```

Internally:

```text
age >= 18
   ↓
False
   ↓
else block
```

---

# 8. Boolean Conversion using `bool()`

Python provides the built-in function:

```python
bool()
```

It converts a value into `True` or `False`.

Example:

```python
print(bool(1))
print(bool(0))
```

**Output:**
```text
True
False
```

---

# 9. Truthy and Falsy Values

Python does not require a value to literally be `True` or `False` inside a condition.

Python checks whether the value is **truthy** or **falsy**.

### Falsy values

These values are considered `False`:

```python
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
range(0)
```

Example:

```python
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
print(bool(range(0)))
```

All produce:

```text
False
```

---

# 10. Truthy Values

Almost every other value is considered `True`.

Examples:

```python
print(bool(10))
print(bool(-10))
print(bool(3.14))
print(bool("Python"))
print(bool("False"))
print(bool([1, 2]))
print(bool((1, 2)))
print(bool({1, 2}))
print(bool({"name": "Teja"}))
```

**Output:**
```text
True
True
True
True
True
True
True
True
```

---

# 11. Important: `bool("False")` is True

This is a very common confusion.

```python
print(bool("False"))
```

Output:

```text
True
```

Why?

Because `"False"` is a **non-empty string**.

Python does not check the meaning of the word.

It checks whether the string is empty.

```python
bool("")
```

→ `False`

```python
bool("False")
```

→ `True`

Similarly:

```python
bool("0")
```

→ `True`

because `"0"` is also a non-empty string.

---

# 12. Empty vs Non-Empty Collections

For collections:

```text
Empty collection → False
Non-empty collection → True
```

Example:

```python
print(bool([]))
print(bool([0]))
```

Output:

```text
False
True
```

Notice:

```python
[0]
```

contains `0`, but the list itself is **not empty**.

Therefore:

```python
bool([0])
```

is:

```text
True
```

---

# 13. Boolean is a Subclass of Integer

One of the most important Python concepts is:

```python
bool
```

is a subclass of:

```python
int
```

You can check this using:

```python
print(isinstance(True, int))
print(isinstance(False, int))
```

**Output:**
```text
True
True
```

Python internally treats:

```text
True  → 1
False → 0
```

for numeric operations.

---

# 14. `True == 1`

```python
print(True == 1)
print(False == 0)
```

**Output:**
```text
True
True
```

Because:

```text
True  behaves like 1
False behaves like 0
```

But their types are different:

```python
print(type(True))
print(type(1))
```

**Output:**
```text
<class 'bool'>
<class 'int'>
```

So:

```text
True == 1
```

is `True`, but:

```text
type(True) == type(1)
```

is `False`.

---

# 15. Boolean in Arithmetic

Because `bool` is a subclass of `int`, Boolean values can participate in arithmetic.

```python
print(True + True)
print(True + False)
print(False + False)
```

**Output:**
```text
2
1
0
```

More examples:

```python
print(True * 5)
print(False * 5)
```

**Output:**
```text
5
0
```

Conceptually:

```text
True  → 1
False → 0
```

---

# 16. Counting True Values

This property is useful in Python programs.

```python
values = [True, False, True, True, False]

print(sum(values))
```

**Output:**
```text
3
```

Why?

```text
True  → 1
False → 0

1 + 0 + 1 + 1 + 0 = 3
```

So `sum()` can be used to count Boolean `True` values.

---

# 17. Boolean and `and`

The `and` operator is used when **both conditions** need to be satisfied.

Example:

```python
age = 21
has_id = True

print(age >= 18 and has_id)
```

**Output:**
```text
True
```

Both conditions are true:

```text
age >= 18 → True
has_id    → True

True and True → True
```

### Truth table for `and`

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# 18. Boolean and `or`

The `or` operator returns a truthy result when **at least one condition** is true.

```python
print(True or False)
print(False or True)
print(True or True)
print(False or False)
```

**Output:**
```text
True
True
True
False
```

### Truth table

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# 19. Boolean and `not`

`not` reverses the Boolean result.

```python
print(not True)
print(not False)
```

**Output:**
```text
False
True
```

Example:

```python
is_logged_in = True

print(not is_logged_in)
```

Output:

```text
False
```

---

# 20. Important: `and` and `or` Do Not Always Return `True` or `False`

This is an important Python concept.

Consider:

```python
print(10 and 20)
```

Output:

```text
20
```

Why?

Python's `and` returns one of its operands.

Similarly:

```python
print(10 or 20)
```

Output:

```text
10
```

So:

```text
and → returns an operand
or  → returns an operand
not → always returns bool
```

Example:

```python
print("" or "Python")
```

Output:

```text
Python
```

Because `""` is falsy, so Python evaluates the second operand.

---

# 21. Short-Circuit Evaluation

Python does not always evaluate every condition.

This is called **short-circuit evaluation**.

### `and`

If the first operand is falsy, Python stops.

```python
False and something
```

Python already knows the result cannot be truthy.

### `or`

If the first operand is truthy, Python stops.

```python
True or something
```

Python already knows the result.

Example:

```python
x = 0

print(x and 10)
```

Output:

```text
0
```

The second operand does not need to be evaluated.

---

# 22. `bool()` and `if` Use the Same Truthiness Concept

Example:

```python
value = []

if value:
    print("True")
else:
    print("False")
```

Output:

```text
False
```

This is effectively checking:

```python
bool(value)
```

So:

```python
if value:
```

can be understood as:

```python
if bool(value):
```

although Python normally performs the truth-value test directly.

---

# 23. Boolean with Strings

```python
name = "Teja"

if name:
    print("Name is available")
```

Output:

```text
Name is available
```

Because:

```python
bool("Teja")
```

is `True`.

But:

```python
name = ""

if name:
    print("Name is available")
else:
    print("Name is empty")
```

Output:

```text
Name is empty
```

---

# 24. Boolean with Lists

```python
numbers = [10, 20, 30]

if numbers:
    print("List is not empty")
```

Output:

```text
List is not empty
```

But:

```python
numbers = []

if numbers:
    print("List is not empty")
else:
    print("List is empty")
```

Output:

```text
List is empty
```

---

# 25. Boolean with Dictionaries

```python
student = {"name": "Teja"}

if student:
    print("Dictionary is not empty")
```

Output:

```text
Dictionary is not empty
```

Empty dictionary:

```python
student = {}

if student:
    print("Data exists")
else:
    print("Dictionary is empty")
```

Output:

```text
Dictionary is empty
```

---

# 26. Boolean with Numbers

```python
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(100))
```

Output:

```text
False
True
True
True
```

Important:

```text
0       → False
non-zero → True
```

This includes negative numbers.

```python
bool(-5)
```

→ `True`

---

# 27. Boolean with Floating-Point Numbers

```python
print(bool(0.0))
print(bool(0.1))
print(bool(-2.5))
```

Output:

```text
False
True
True
```

Again:

```text
0.0      → False
non-zero → True
```

---

# 28. Boolean with Complex Numbers

```python
print(bool(0j))
print(bool(2 + 3j))
```

Output:

```text
False
True
```

So:

```text
0j       → False
non-zero → True
```

---

# 29. Boolean and `None`

`None` represents the absence of a value.

```python
print(bool(None))
```

Output:

```text
False
```

Example:

```python
result = None

if result:
    print("Result exists")
else:
    print("No result")
```

Output:

```text
No result
```

---

# 30. Boolean Comparison with `None`

When specifically checking for `None`, use:

```python
is None
```

Example:

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

```python
is None
```

rather than:

```python
== None
```

for a `None` check.

---

# 31. Boolean and Equality

Comparison operators return Boolean values.

```python
a = 10
b = 20

result = a < b

print(result)
print(type(result))
```

Output:

```text
True
<class 'bool'>
```

So:

```python
result = a < b
```

stores a Boolean value.

---

# 32. Chained Comparisons

Python allows multiple comparisons in one expression.

```python
age = 21

print(18 <= age <= 60)
```

Output:

```text
True
```

This is equivalent to:

```python
18 <= age and age <= 60
```

Another example:

```python
x = 10

print(1 < x < 20)
```

Output:

```text
True
```

---

# 33. Boolean Variables as Flags

A Boolean variable is often called a **flag**.

Example:

```python
is_logged_in = True
```

The variable tells us whether something is enabled or disabled.

Common flag names:

```python
is_active = True
is_valid = False
is_available = True
is_completed = False
has_permission = True
```

This is a very common pattern in real programs.

---

# 34. Boolean in Validation

Example:

```python
age = 25

is_valid_age = age >= 18

print(is_valid_age)
```

Output:

```text
True
```

Here:

```python
is_valid_age
```

stores the result of a condition.

---

# 35. Practical Example: Even or Odd

```python
number = 10

is_even = number % 2 == 0

print(is_even)
```

Output:

```text
True
```

Explanation:

```text
10 % 2 → 0

0 == 0 → True
```

Therefore:

```python
is_even
```

contains:

```text
True
```

---

# 36. Practical Example: Age Eligibility

```python
age = 21

eligible = age >= 18

print(eligible)
```

Output:

```text
True
```

---

# 37. Practical Example: Password Validation

```python
password = "python123"

is_valid = len(password) >= 8

print(is_valid)
```

Output:

```text
True
```

---

# 38. Practical Example: Multiple Conditions

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

Both conditions must be satisfied.

---

# 39. Boolean with `any()`

`any()` returns `True` if **at least one** item is truthy.

```python
values = [False, False, True, False]

print(any(values))
```

Output:

```text
True
```

Because at least one value is `True`.

Example:

```python
values = [0, 0, 5, 0]

print(any(values))
```

Output:

```text
True
```

Because `5` is truthy.

---

# 40. Boolean with `all()`

`all()` returns `True` only when **every item** is truthy.

```python
values = [True, True, True]

print(all(values))
```

Output:

```text
True
```

But:

```python
values = [True, False, True]

print(all(values))
```

Output:

```text
False
```

---

# 41. Important Difference Between `any()` and `all()`

### `any()`

At least one should be truthy.

```python
any([False, True, False])
```

→ `True`

### `all()`

Every value should be truthy.

```python
all([True, True, True])
```

→ `True`

```python
all([True, False, True])
```

→ `False`

---

# 42. Boolean and `isinstance()`

You can check whether a value is Boolean:

```python
x = True

print(isinstance(x, bool))
```

Output:

```text
True
```

But remember:

```python
isinstance(True, int)
```

is also:

```text
True
```

because `bool` inherits from `int`.

---

# 43. Boolean Immutability

Boolean values are **immutable**.

You cannot change the Boolean object itself.

You can only make a variable refer to another value.

```python
x = True

x = False
```

Here Python does not modify `True`.

Instead:

```text
x → True
```

then:

```text
x → False
```

The variable is reassigned.

---

# 44. Boolean is Hashable

Boolean values are hashable.

```python
print(hash(True))
print(hash(False))
```

Typically:

```text
1
0
```

Because:

```text
True  → 1
False → 0
```

Therefore Boolean values can be used as:

- Dictionary keys
- Set elements

Example:

```python
data = {
    True: "Yes",
    False: "No"
}

print(data)
```

---

# 45. Important: Boolean Keys and Integer Keys

Because:

```python
True == 1
False == 0
```

they behave as the same key in dictionaries.

Example:

```python
data = {
    True: "Boolean",
    1: "Integer"
}

print(data)
```

The keys collide because:

```python
True == 1
```

So you should be careful when mixing Boolean and integer keys.

---

# 46. `==` vs `is` with Boolean

`==` checks **value equality**.

`is` checks **object identity**.

Example:

```python
x = True

print(x == True)
print(x is True)
```

Output:

```text
True
True
```

For normal conditions, prefer:

```python
if x:
```

instead of unnecessarily writing:

```python
if x == True:
```

Example:

```python
is_valid = True

if is_valid:
    print("Valid")
```

This is cleaner.

---

# 47. `if x` vs `if x == True`

Prefer:

```python
if x:
    print("Yes")
```

when you want to check whether `x` is truthy.

Example:

```python
numbers = [1, 2, 3]

if numbers:
    print("List has data")
```

Do not unnecessarily restrict it to an exact Boolean:

```python
if numbers == True:
```

because the list is not the Boolean value `True`.

---

# 48. Boolean Conversion Table

| Value | `bool(value)` |
|---|---:|
| `True` | `True` |
| `False` | `False` |
| `None` | `False` |
| `0` | `False` |
| `1` | `True` |
| `-1` | `True` |
| `0.0` | `False` |
| `2.5` | `True` |
| `0j` | `False` |
| `""` | `False` |
| `"Python"` | `True` |
| `"False"` | `True` |
| `[]` | `False` |
| `[1]` | `True` |
| `()` | `False` |
| `(1,)` | `True` |
| `{}` | `False` |
| `{"a": 1}` | `True` |
| `set()` | `False` |
| `{1}` | `True` |

---

# 49. Boolean Operator Summary

| Operator | Purpose | Example | Result |
|---|---|---|---|
| `and` | Both conditions | `True and False` | `False` |
| `or` | At least one | `True or False` | `True` |
| `not` | Reverse truth value | `not True` | `False` |

---

# 50. Operator Precedence with Boolean Operators

Boolean operators have different priorities.

Generally:

```text
not
 ↓
and
 ↓
or
```

Example:

```python
print(True or False and False)
```

`and` is evaluated before `or`.

So:

```text
False and False → False

True or False → True
```

Output:

```text
True
```

Use parentheses when you want to make the logic clear:

```python
print(True or (False and False))
```

---

# 51. Boolean in Loops

Boolean conditions are commonly used in loops.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

The condition:

```python
i <= 5
```

produces either:

```text
True
```

or:

```text
False
```

The loop continues while the condition is truthy.

---

# 52. Boolean and `while True`

A common pattern is:

```python
while True:
    print("Running")
    break
```

Here:

```python
True
```

makes the loop condition always truthy.

The `break` statement is used to stop the loop.

---

# 53. Boolean Functions

A function can return a Boolean value.

Example:

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))
```

Output:

```text
True
False
```

Functions beginning with names such as:

```text
is_...
has_...
can_...
```

often return Boolean values.

Examples:

```python
is_valid()
is_even()
has_permission()
can_access()
```

---

# 54. Boolean with User Input

`input()` always returns a string.

Example:

```python
answer = input("Do you agree? ")

print(type(answer))
```

Even if the user enters:

```text
True
```

the result is:

```text
<class 'str'>
```

It is not automatically Boolean.

---

# 55. Important Input Mistake

Do not do this:

```python
answer = bool(input("Enter True or False: "))
```

If the user enters:

```text
False
```

the result will actually be:

```text
True
```

because `"False"` is a non-empty string.

For real Boolean input, you need to explicitly interpret the user's text.

Example:

```python
answer = input("Enter yes/no: ").lower()

is_yes = answer == "yes"

print(is_yes)
```

If the user enters:

```text
yes
```

Output:

```text
True
```

---

# 56. Boolean and Strings

A Boolean value is different from a string containing Boolean-looking text.

```python
x = True
y = "True"

print(type(x))
print(type(y))
```

Output:

```text
<class 'bool'>
<class 'str'>
```

So:

```text
True   → Boolean
"True" → String
```

---

# 57. Boolean and Numbers

Similarly:

```python
x = True
y = 1

print(type(x))
print(type(y))
```

Output:

```text
<class 'bool'>
<class 'int'>
```

But:

```python
print(x == y)
```

gives:

```text
True
```

because Boolean is related to integer behavior.

---

# 58. Common Mistakes

### Mistake 1: Lowercase `true`

Wrong:

```python
x = true
```

Correct:

```python
x = True
```

---

### Mistake 2: Lowercase `false`

Wrong:

```python
x = false
```

Correct:

```python
x = False
```

---

### Mistake 3: Thinking `"False"` is False

```python
bool("False")
```

gives:

```text
True
```

because the string is not empty.

---

### Mistake 4: Thinking `"0"` is False

```python
bool("0")
```

gives:

```text
True
```

because `"0"` is a non-empty string.

---

### Mistake 5: Using `== True` unnecessarily

Instead of:

```python
if is_valid == True:
    print("Valid")
```

prefer:

```python
if is_valid:
    print("Valid")
```

---

### Mistake 6: Confusing `=` and `==`

`=` means assignment:

```python
x = True
```

`==` means comparison:

```python
x == True
```

---

### Mistake 7: Confusing `and` with `&`

These are different operators.

```python
and
```

is a logical operator.

```python
&
```

is a bitwise AND operator.

For Boolean conditions, normally use:

```python
and
```

---

# 59. Useful Built-in Functions with Boolean

| Function | Purpose |
|---|---|
| `bool()` | Convert value to Boolean |
| `type()` | Check type |
| `isinstance()` | Check whether value belongs to a type |
| `any()` | True if at least one item is truthy |
| `all()` | True if every item is truthy |
| `sum()` | Can count Boolean `True` values |
| `int()` | Convert Boolean to `1` or `0` |

Example:

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

---

# 60. Practical Program: Check Positive Number

```python
number = 10

is_positive = number > 0

print(is_positive)
```

Output:

```text
True
```

---

# 61. Practical Program: Check Adult

```python
age = 21

is_adult = age >= 18

print(is_adult)
```

Output:

```text
True
```

---

# 62. Practical Program: Check Even Number

```python
number = 20

is_even = number % 2 == 0

print(is_even)
```

Output:

```text
True
```

---

# 63. Practical Program: Check Empty String

```python
name = ""

is_empty = not name

print(is_empty)
```

Output:

```text
True
```

---

# 64. Practical Program: Check List

```python
numbers = [10, 20, 30]

if numbers:
    print("List contains elements")
else:
    print("List is empty")
```

Output:

```text
List contains elements
```

---

# 65. Practical Program: Count True Values

```python
results = [True, False, True, True, False]

count = sum(results)

print(count)
```

Output:

```text
3
```

---

# 66. Practical Program: Multiple Conditions

```python
age = 22
has_degree = True

eligible = age >= 18 and has_degree

print(eligible)
```

Output:

```text
True
```

---

# 67. Boolean vs Integer

| Feature | Boolean | Integer |
|---|---|---|
| Example | `True` | `10` |
| Type | `bool` | `int` |
| Main purpose | Logic | Whole numbers |
| Values | `True`, `False` | Many whole numbers |
| Numeric behavior | `True = 1`, `False = 0` | Numeric |
| Mutable? | No | No |
| Hashable? | Yes | Yes |

Important:

```python
True == 1
```

is `True`, but:

```python
type(True) == type(1)
```

is `False`.

---

# 68. Boolean vs String

| Feature | Boolean | String |
|---|---|---|
| Example | `True` | `"True"` |
| Type | `bool` | `str` |
| Quotes | No | Yes |
| Main purpose | Logic | Text |
| `bool()` | Already Boolean | Based on emptiness |

Example:

```python
True
```

is Boolean.

```python
"True"
```

is String.

---

# 69. Important Characteristics of `bool`

Python Boolean data type:

- Has only two values: `True` and `False`
- Is used for logical decisions
- Is a subclass of `int`
- `True` behaves numerically like `1`
- `False` behaves numerically like `0`
- Is immutable
- Is hashable
- Can be used as dictionary keys
- Can be used as set elements
- Is returned by comparison operations
- Works with `and`, `or`, and `not`
- Supports truth-value testing
- Works with `if`, `while`, and conditional expressions
- Can be created using `bool()`

---

# 70. Important Mental Model

Think of Boolean values as:

```text
              BOOLEAN
             /       \
          True       False
           ↓           ↓
           1           0
```

For conditions:

```text
Condition
    ↓
True / False
    ↓
Decision
```

Example:

```python
age >= 18
```

If age is 21:

```text
21 >= 18
     ↓
    True
     ↓
Execute if block
```

---

# 71. Quick Revision

```text
True / False
     ↓
   bool
```

### Truthiness

```text
0          → False
0.0        → False
0j         → False
""         → False
[]         → False
()         → False
{}         → False
set()      → False
None       → False
```

Most non-empty/non-zero values:

```text
→ True
```

### Important relationship

```text
True  == 1
False == 0
```

### Logical operators

```text
and → both conditions
or  → at least one condition
not → reverse
```

### Important behavior

```text
and → returns an operand
or  → returns an operand
not → returns bool
```

### Common Boolean checks

```python
if value:
if value is None:
if age >= 18:
if x == y:
```

---

# 72. One-Line Definition

> **Boolean (`bool`) is a Python data type that represents logical values as `True` or `False` and is mainly used for conditions, comparisons, decision making, and logical operations.**

---

# 73. Final Example

```python
age = 21
has_id = True
has_ticket = True

is_eligible = age >= 18 and has_id and has_ticket

print(is_eligible)
```

**Output:**
```text
True
```

The execution can be understood as:

```text
age >= 18
    ↓
  True

has_id
    ↓
  True

has_ticket
    ↓
  True

True and True and True
          ↓
        True
```

This is the basic idea behind how Boolean values are used in real Python programs.