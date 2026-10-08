# Conditional Statements in Python

Conditional statements are used when a program needs to **make a decision**.

The program checks a condition and decides which block of code should execute.

For example:

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Here Python checks:

```text
age >= 18
    ↓
True
    ↓
execute print()
```

If the condition is `False`, the code inside the `if` block is skipped.

---

# 1. Why Conditional Statements are Needed

Without conditions, a program would execute instructions sequentially.

But real programs need to make decisions.

Examples:

```text
If marks >= 40       → Pass
Otherwise            → Fail

If age >= 18         → Eligible
Otherwise             → Not eligible

If number is even    → Even
Otherwise             → Odd

If password matches  → Login
Otherwise             → Reject
```

Conditional statements allow Python to make these decisions.

---

# 2. What is a Condition?

A condition is an expression that produces either:

```python
True
```

or

```python
False
```

Examples:

```python
10 > 5
10 < 5
10 == 10
10 != 20
```

Results:

```python
10 > 5      # True
10 < 5      # False
10 == 10    # True
10 != 20    # True
```

So a condition is basically a **Boolean expression**.

---

# 3. Boolean Expressions

A Boolean expression produces a Boolean value.

Example:

```python
age = 21

age >= 18
```

Result:

```python
True
```

Another example:

```python
marks = 30

marks >= 40
```

Result:

```python
False
```

These expressions can be directly used inside `if`.

---

# 4. `if` Statement

The `if` statement executes a block of code when its condition is `True`.

### Syntax

```python
if condition:
    statement
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

---

# 5. How `if` Works Internally

Consider:

```python
age = 20

if age >= 18:
    print("Adult")
```

Python evaluates:

```text
age >= 18
    ↓
20 >= 18
    ↓
True
    ↓
execute if block
    ↓
print("Adult")
```

If:

```python
age = 15
```

then:

```text
15 >= 18
    ↓
False
    ↓
skip if block
```

---

# 6. Indentation

Python uses indentation to identify a block of code.

Correct:

```python
if age >= 18:
    print("Adult")
```

The spaces before `print()` are important.

Usually 4 spaces are used.

Incorrect:

```python
if age >= 18:
print("Adult")
```

This causes an indentation error.

---

# 7. Colon `:`

A colon is required after the condition.

Correct:

```python
if age >= 18:
    print("Adult")
```

Incorrect:

```python
if age >= 18
    print("Adult")
```

The colon tells Python that a block of code is starting.

---

# 8. `if` with Comparison Operators

Conditions commonly use comparison operators.

```python
a = 10
b = 20

if a < b:
    print("a is smaller")
```

Comparison operators:

```text
>     greater than
<     less than
>=    greater than or equal to
<=    less than or equal to
==    equal to
!=    not equal to
```

---

# 9. Simple `if` Programs

## Check Positive Number

```python
number = int(input("Enter number: "))

if number > 0:
    print("Positive")
```

---

## Check Even Number

```python
number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even")
```

Why?

For an even number:

```text
number % 2
    ↓
0
```

Therefore:

```python
number % 2 == 0
```

becomes `True`.

---

# 10. `if-else`

Sometimes we need two possible outcomes.

For this we use `if-else`.

### Syntax

```python
if condition:
    statement1
else:
    statement2
```

Example:

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

Output:

```text
Not eligible
```

---

# 11. How `if-else` Works

Example:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Evaluation:

```text
7 % 2
 ↓
1

1 == 0
 ↓
False

if block → skipped
 ↓
else block → executed
 ↓
Odd
```

---

# 12. `if-elif-else`

When there are more than two possibilities, use `elif`.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

Example:

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")
```

Output:

```text
B
```

---

# 13. Important Rule: `elif` is Checked Only When Previous Conditions Fail

Consider:

```python
marks = 85

if marks >= 40:
    print("Pass")
elif marks >= 80:
    print("Excellent")
```

Output:

```text
Pass
```

Why?

Python checks from top to bottom:

```text
marks >= 40
85 >= 40
    ↓
True
    ↓
execute if
    ↓
Pass
```

Python does **not** continue to the `elif`.

Therefore the order of conditions matters.

---

# 14. Correct Ordering of Conditions

For grading:

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")
```

Output:

```text
B
```

We start with the highest range.

---

# 15. What Happens If Conditions Are in the Wrong Order?

Wrong:

```python
marks = 85

if marks >= 40:
    print("D")
elif marks >= 75:
    print("B")
elif marks >= 90:
    print("A")
```

Output:

```text
D
```

Because:

```text
85 >= 40
    ↓
True
```

The first condition wins.

---

# 16. Multiple `elif`

You can have multiple `elif` blocks.

Example:

```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")
```

Python checks conditions from top to bottom.

The first `True` condition is executed.

---

# 17. Important Structure of `if-elif-else`

```text
if
 ↓
condition
 ↓
True? ─── Yes → execute block → stop
 ↓ No
elif
 ↓
condition
 ↓
True? ─── Yes → execute block → stop
 ↓ No
elif
 ↓
...
 ↓ No
else
 ↓
execute
```

Only **one block** of an `if-elif-else` chain is executed.

---

# 18. Nested `if`

An `if` statement inside another `if` statement is called a **nested if**.

Example:

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

Execution:

```text
age >= 18
   ↓
True
   ↓
check citizen
   ↓
True
   ↓
Eligible to vote
```

---

# 19. Nested `if-else`

```python
age = 20
citizen = False

if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Not a citizen")
else:
    print("Under age")
```

Output:

```text
Not a citizen
```

---

# 20. Nested Conditions vs Logical Operators

This:

```python
if age >= 18:
    if citizen:
        print("Eligible")
```

can often be written as:

```python
if age >= 18 and citizen:
    print("Eligible")
```

Both can represent the same logical requirement.

The second version is usually simpler when the conditions are independent Boolean checks.

---

# 21. `and` in Conditions

`and` requires both conditions to be true.

Example:

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

Evaluation:

```text
age >= 18
25 >= 18
   ↓
True

citizen
   ↓
True

True and True
   ↓
True
```

Output:

```text
Eligible
```

---

# 22. `and` Truth Table

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

Both must be `True`.

---

# 23. `or` in Conditions

`or` requires at least one condition to be true.

Example:

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

Evaluation:

```text
day == "Saturday"
    ↓
False

day == "Sunday"
    ↓
True

False or True
    ↓
True
```

Output:

```text
Weekend
```

---

# 24. `or` Truth Table

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

Only both `False` gives `False`.

---

# 25. `not` in Conditions

`not` reverses a Boolean value.

```python
not True
```

gives:

```python
False
```

and:

```python
not False
```

gives:

```python
True
```

Example:

```python
logged_in = False

if not logged_in:
    print("Please login")
```

Output:

```text
Please login
```

---

# 26. Complex Boolean Conditions

Consider:

```python
age = 25
citizen = True
has_id = True

if age >= 18 and citizen and has_id:
    print("Eligible")
```

Python evaluates:

```text
age >= 18
25 >= 18
   ↓
True

citizen
   ↓
True

has_id
   ↓
True

True and True and True
   ↓
True
```

Therefore:

```text
Eligible
```

---

# 27. Complex Condition with `and` and `or`

Consider:

```python
age = 17
permission = True

if age >= 18 or permission:
    print("Allowed")
```

Evaluation:

```text
age >= 18
17 >= 18
   ↓
False

permission
   ↓
True

False or True
   ↓
True
```

Output:

```text
Allowed
```

---

# 28. Precedence of Logical Operators

When a condition contains:

```python
not
and
or
```

Python follows this order:

```text
not
 ↓
and
 ↓
or
```

Example:

```python
True or False and False
```

First:

```text
False and False
    ↓
False
```

Then:

```text
True or False
    ↓
True
```

Therefore:

```python
True or False and False
```

is:

```python
True
```

---

# 29. Use Parentheses to Make Conditions Clear

Consider:

```python
if age >= 18 and citizen or permission:
    print("Allowed")
```

Python interprets it according to precedence.

For clarity, write:

```python
if (age >= 18 and citizen) or permission:
    print("Allowed")
```

Parentheses make the intended logic easier to understand.

---

# 30. Truthy and Falsy Values

Python does not require a condition to literally be `True` or `False`.

Many values can be used directly in `if`.

### Falsy values

Common falsy values:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

These behave like `False` in a condition.

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

Output:

```text
Name is empty
```

---

# 31. Truthy Values

Most non-empty and non-zero values are truthy.

Examples:

```python
1
-1
10
"Python"
[1, 2]
(10,)
{1, 2}
{"a": 1}
```

Example:

```python
name = "Teja"

if name:
    print("Name exists")
```

Output:

```text
Name exists
```

---

# 32. `if` with Strings

```python
name = input("Enter name: ")

if name == "Teja":
    print("Welcome Teja")
else:
    print("Unknown user")
```

We can also check whether a string is empty:

```python
name = input("Enter name: ")

if name:
    print("Name entered")
else:
    print("No name entered")
```

---

# 33. `if` with Lists

```python
numbers = [10, 20, 30]

if numbers:
    print("List is not empty")
```

Output:

```text
List is not empty
```

Empty list:

```python
numbers = []

if numbers:
    print("Not empty")
else:
    print("Empty")
```

Output:

```text
Empty
```

---

# 34. `if` with `None`

Use `is None` when checking for `None`.

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

Also:

```python
if value is not None:
    print(value)
```

---

# 35. Why `is None` is Preferred

Use:

```python
value is None
```

rather than:

```python
value == None
```

`is` checks object identity.

For `None`, the recommended style is:

```python
if value is None:
```

---

# 36. Chained Comparisons

Python allows comparisons to be chained.

Example:

```python
age = 25

if 18 <= age <= 60:
    print("Working age")
```

This is equivalent to:

```python
if age >= 18 and age <= 60:
    print("Working age")
```

Python effectively checks:

```text
18 <= age
AND
age <= 60
```

---

# 37. More Chained Comparison Examples

```python
if 10 < x < 100:
    print("x is between 10 and 100")
```

Equivalent to:

```python
if x > 10 and x < 100:
    print("x is between 10 and 100")
```

Another example:

```python
if 0 <= marks <= 100:
    print("Valid marks")
```

---

# 38. Conditional Expression / Ternary Operator

Python allows a short form of `if-else`.

### Normal form

```python
if age >= 18:
    result = "Adult"
else:
    result = "Minor"
```

### Conditional expression

```python
result = "Adult" if age >= 18 else "Minor"
```

Example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output:

```text
Adult
```

Structure:

```text
value_if_true if condition else value_if_false
```

---

# 39. Nested Conditional Expression

It is possible to write:

```python
result = "A" if marks >= 90 else "B" if marks >= 75 else "C"
```

But this can become difficult to read.

For multiple conditions, normal `if-elif-else` is usually clearer.

---

# 40. `if` with Membership Operators

The `in` operator can be used in conditions.

```python
name = "Teja"

if "T" in name:
    print("T exists")
```

Output:

```text
T exists
```

Example:

```python
numbers = [10, 20, 30]

if 20 in numbers:
    print("20 exists")
```

---

# 41. `if` with Dictionary

Dictionary membership checks keys by default.

```python
student = {
    "name": "Teja",
    "age": 21
}

if "age" in student:
    print("Age exists")
```

Output:

```text
Age exists
```

---

# 42. Important: `in` with Dictionary

This:

```python
"age" in student
```

checks keys.

It does not directly check values.

To check values:

```python
21 in student.values()
```

To check key-value pairs:

```python
("age", 21) in student.items()
```

---

# 43. Multiple Conditions: Detailed Example

Consider:

```python
age = 25
salary = 50000
experience = 2

if age >= 21 and salary >= 30000 and experience >= 1:
    print("Eligible")
else:
    print("Not eligible")
```

Step-by-step:

```text
age >= 21
25 >= 21
    ↓
True

salary >= 30000
50000 >= 30000
    ↓
True

experience >= 1
2 >= 1
    ↓
True
```

Then:

```text
True and True and True
        ↓
       True
```

Output:

```text
Eligible
```

---

# 44. Complex Condition Example

Consider:

```python
age = 17
has_permission = True
has_id = False

if (age >= 18 and has_id) or has_permission:
    print("Allowed")
else:
    print("Not allowed")
```

Evaluate the parentheses first:

```text
age >= 18
17 >= 18
    ↓
False

False and has_id
    ↓
False
```

Now:

```text
False or has_permission
False or True
    ↓
True
```

Output:

```text
Allowed
```

---

# 45. Short-Circuit Evaluation

Python sometimes does not evaluate every condition.

This is called **short-circuit evaluation**.

For `and`:

```python
False and something
```

Once Python sees the first `False`, the entire result must be false.

For `or`:

```python
True or something
```

Once Python sees the first `True`, the entire result must be true.

Example:

```python
x = 0

if x != 0 and 10 / x > 2:
    print("Yes")
```

Python first checks:

```text
x != 0
0 != 0
   ↓
False
```

Because the first condition is `False`, Python does not need to evaluate:

```python
10 / x
```

Therefore, no division-by-zero error occurs.

---

# 46. Practical Program: Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")
```

---

# 47. Practical Program: Largest of Three Numbers

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
```

---

# 48. Practical Program: Check Leap Year

A year is a leap year when:

```text
divisible by 400
OR
divisible by 4 but NOT divisible by 100
```

Program:

```python
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
```

This is a good example of a complex Boolean condition.

---

# 49. Practical Program: Positive, Negative or Zero

```python
number = int(input("Enter number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

# 50. Practical Program: Even or Odd

```python
number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 51. Practical Program: Valid Marks

```python
marks = int(input("Enter marks: "))

if 0 <= marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")
```

This uses a chained comparison.

---

# 52. Practical Program: Grade Calculator

```python
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Fail")
```

Notice that validation is performed before grading.

---

# 53. Practical Program: Voting Eligibility

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

---

# 54. Practical Program: Login Check

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

---

# 55. Practical Program: Divisible by 5 and 11

```python
number = int(input("Enter number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")
```

---

# 56. Practical Program: Vowel or Consonant

```python
ch = input("Enter character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

---

# 57. Practical Program: Check Character Type

```python
ch = input("Enter character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
```

---

# 58. Common Mistakes

## Mistake 1: Using `=` instead of `==`

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

Remember:

```text
=   assignment
==  comparison
```

---

## Mistake 2: Forgetting Colon

Wrong:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

## Mistake 3: Wrong Indentation

Wrong:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 4: Incorrect `and` / `or` Logic

Wrong:

```python
if age >= 18 or age <= 60:
```

This condition is true for almost every number.

If you want a range, use:

```python
if 18 <= age <= 60:
```

or:

```python
if age >= 18 and age <= 60:
```

---

## Mistake 5: Wrong `elif` Order

Wrong:

```python
if marks >= 40:
    print("Pass")
elif marks >= 90:
    print("A")
```

The `elif` will never be reached for marks `90` or above.

---

# 59. `if` vs `if-elif` vs Multiple `if`

### `if`

Used for one independent condition:

```python
if age >= 18:
    print("Adult")
```

### `if-elif-else`

Used when only one category should be selected:

```python
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

### Multiple `if`

Each condition is checked independently:

```python
if age >= 18:
    print("Adult")

if age >= 21:
    print("Can legally drink in some jurisdictions")
```

Both can execute.

This is different from `if-elif`.

---

# 60. Difference Between Multiple `if` and `if-elif`

Consider:

```python
number = 10

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")
```

Output:

```text
Positive
Even
```

Both conditions are checked.

But:

```python
number = 10

if number > 0:
    print("Positive")
elif number % 2 == 0:
    print("Even")
```

Output:

```text
Positive
```

Once the first condition is `True`, the `elif` is skipped.

---

# 61. `pass` in Conditional Statements

`pass` does nothing.

It can be used as a placeholder.

```python
age = 20

if age >= 18:
    pass
else:
    print("Minor")
```

`pass` is useful when the block is intentionally left empty while developing code.

---

# 62. Conditions with Functions

A function can return a Boolean value.

```python
def is_even(number):
    return number % 2 == 0

number = 10

if is_even(number):
    print("Even")
```

Output:

```text
Even
```

Here:

```python
is_even(number)
```

returns:

```python
True
```

so the `if` block executes.

---

# 63. Conditions with `any()` and `all()`

`any()` returns `True` if at least one value is truthy.

```python
values = [False, False, True]

if any(values):
    print("At least one is true")
```

`all()` returns `True` if every value is truthy.

```python
values = [True, True, True]

if all(values):
    print("All are true")
```

These become useful in more advanced programs.

---

# 64. Important Evaluation Rules

When Python evaluates a complex condition, remember:

```text
Parentheses
    ↓
Comparisons
    ↓
not
    ↓
and
    ↓
or
```

Example:

```python
if (age >= 18 and citizen) or permission:
```

First:

```text
(age >= 18 and citizen)
```

Then:

```text
result or permission
```

Parentheses should be used when they make the intended logic clearer.

---

# 65. Final Mental Model

Think of conditional statements as a decision-making system:

```text
             CONDITION
                 │
          ┌──────┴──────┐
          │             │
        True           False
          │             │
          ↓             ↓
    execute block    check next
                        │
                    elif / else
```

For `if-elif-else`:

```text
Condition 1
    │
    ├── True → execute → STOP
    │
    └── False
          ↓
      Condition 2
          │
          ├── True → execute → STOP
          │
          └── False
                ↓
              else
```

---

# 66. Quick Revision

### Basic `if`

```python
if condition:
    statement
```

### `if-else`

```python
if condition:
    statement
else:
    statement
```

### `if-elif-else`

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Logical operators

```text
not → reverses
and → both must be true
or  → at least one must be true
```

### Truthy/Falsy

```text
False
None
0
0.0
""
[]
()
{}
set()
```

are commonly falsy.

### Chained comparison

```python
18 <= age <= 60
```

### Conditional expression

```python
result = "Adult" if age >= 18 else "Minor"
```

### `None` check

```python
if value is None:
```

### Membership

```python
if value in collection:
```

---

# 67. One-Line Definition

**Conditional statements allow a Python program to make decisions by evaluating conditions and executing different blocks of code based on whether those conditions are true or false.**