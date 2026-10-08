# Input and Output in Python

Input and Output are used to communicate between the **user and the Python program**.

- **Input** → taking data from the user.
- **Output** → displaying information to the user.

Python mainly provides:

```python
input()
print()
```

---

# 1. What is Input?

**Input** means taking data from the user while the program is running.

Python uses the `input()` function to take input.

### Syntax

```python
input()
```

Example:

```python
name = input()

print(name)
```

If the user enters:

```text
Teja
```

Output:

```text
Teja
```

---

# 2. How `input()` Works

Consider:

```python
name = input("Enter your name: ")
```

Execution happens like this:

```text
Program starts
     ↓
input() executes
     ↓
Message is displayed
     ↓
Program waits for user
     ↓
User enters data
     ↓
input() receives the data
     ↓
input() returns the data as str
     ↓
Value is stored in name
```

Example:

```python
name = input("Enter your name: ")

print(name)
```

Input:

```text
Teja
```

Output:

```text
Enter your name: Teja
Teja
```

---

# 3. Important Point: `input()` Always Returns a String

This is one of the most important things to remember.

Even if the user enters a number, `input()` returns it as a `str`.

Example:

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

Input:

```text
21
```

Output:

```text
21
<class 'str'>
```

The value looks like a number, but Python received:

```python
"21"
```

not:

```python
21
```

---

# 4. Why Type Conversion is Needed

Suppose we write:

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

Input:

```text
10
20
```

Output:

```text
1020
```

Why?

Because:

```python
a = "10"
b = "20"
```

Therefore:

```python
"10" + "20"
```

means string concatenation.

---

# 5. Taking Integer Input

Use `int()` to convert the input into an integer.

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

Input:

```text
21
```

Output:

```text
21
<class 'int'>
```

Now arithmetic operations work normally.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

Input:

```text
10
20
```

Output:

```text
30
```

---

# 6. Taking Float Input

Use `float()`.

```python
price = float(input("Enter price: "))

print(price)
print(type(price))
```

Input:

```text
99.50
```

Output:

```text
99.5
<class 'float'>
```

---

# 7. Taking Boolean Input

Be careful when converting input to `bool`.

```python
value = bool(input("Enter something: "))

print(value)
```

If the user enters:

```text
False
```

the result is:

```python
True
```

Why?

Because:

```python
bool("False")
```

is `True`.

Any **non-empty string** is truthy.

```python
bool("hello")   # True
bool("False")   # True
bool("0")       # True
bool("")        # False
```

So `bool(input())` should not be used when you want the user to enter the words `"True"` or `"False"`.

---

# 8. Taking Multiple Inputs

There are several ways to take multiple inputs.

## Method 1: Separate `input()` Calls

```python
name = input("Enter name: ")
age = int(input("Enter age: "))

print(name)
print(age)
```

---

# 9. Multiple Values Using `split()`

Suppose the user enters:

```text
10 20 30
```

We can use:

```python
numbers = input().split()

print(numbers)
```

Output:

```text
['10', '20', '30']
```

Important:

`split()` produces strings.

So:

```python
input().split()
```

gives:

```python
['10', '20', '30']
```

not:

```python
[10, 20, 30]
```

---

# 10. Taking Multiple Integer Inputs

Use `map()` with `int`.

```python
a, b, c = map(int, input().split())

print(a)
print(b)
print(c)
```

Input:

```text
10 20 30
```

Output:

```text
10
20
30
```

Internally:

```text
input()
   ↓
"10 20 30"
   ↓
split()
   ↓
["10", "20", "30"]
   ↓
map(int, ...)
   ↓
10, 20, 30
   ↓
unpacking
   ↓
a = 10
b = 20
c = 30
```

---

# 11. Taking Multiple Values into a List

```python
numbers = list(map(int, input().split()))

print(numbers)
```

Input:

```text
10 20 30 40
```

Output:

```text
[10, 20, 30, 40]
```

This pattern is very common in coding problems:

```python
list(map(int, input().split()))
```

---

# 12. `print()` Function

`print()` is used to display output.

### Syntax

```python
print(value)
```

Example:

```python
print("Hello")
print(100)
print(10 + 20)
```

Output:

```text
Hello
100
30
```

---

# 13. Printing Multiple Values

```python
name = "Teja"
age = 21

print(name, age)
```

Output:

```text
Teja 21
```

By default, `print()` separates multiple values using a space.

---

# 14. `sep` Parameter

`sep` means **separator**.

Default:

```python
sep = " "
```

Example:

```python
print(10, 20, 30)
```

Output:

```text
10 20 30
```

Using `sep`:

```python
print(10, 20, 30, sep="-")
```

Output:

```text
10-20-30
```

Another example:

```python
print("2026", "10", "09", sep="/")
```

Output:

```text
2026/10/09
```

---

# 15. `end` Parameter

By default, `print()` moves to the next line.

This is because:

```python
end = "\n"
```

Example:

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

Using `end`:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Another example:

```python
print("Python", end="-")
print("Programming")
```

Output:

```text
Python-Programming
```

---

# 16. `sep` and `end` Together

```python
print(10, 20, 30, sep=":", end="!")
```

Output:

```text
10:20:30!
```

---

# 17. Printing Different Data Types

`print()` can display different data types.

```python
print(10)
print(10.5)
print("Python")
print(True)
print([1, 2, 3])
print((10, 20))
print({1, 2, 3})
print({"name": "Teja"})
print(None)
```

---

# 18. Printing Expressions

`print()` can evaluate expressions before displaying the result.

```python
print(10 + 20)
print(10 * 5)
print(20 / 4)
print(2 ** 3)
```

Output:

```text
30
50
5.0
8
```

---

# 19. Taking Input and Performing Calculation

Example:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum:", sum)
```

Input:

```text
10
20
```

Output:

```text
Sum: 30
```

---

# 20. Basic Input Programs

## Program 1: Add Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
```

---

## Program 2: Find Difference

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Difference:", a - b)
```

---

## Program 3: Find Product

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Product:", a * b)
```

---

## Program 4: Find Average

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

average = (a + b) / 2

print("Average:", average)
```

---

# 21. String Input

```python
name = input("Enter your name: ")

print("Hello", name)
```

Input:

```text
Teja
```

Output:

```text
Hello Teja
```

---

# 22. Character Input

Python does not have a separate `char` data type.

A single character is simply a string of length 1.

```python
ch = input("Enter a character: ")

print(ch)
print(type(ch))
```

Input:

```text
A
```

Output:

```text
A
<class 'str'>
```

We can check:

```python
print(len(ch))
```

Output:

```text
1
```

---

# 23. Input with Spaces

`input()` reads the complete line until Enter is pressed.

```python
sentence = input("Enter a sentence: ")

print(sentence)
```

Input:

```text
Python is easy to learn
```

Output:

```text
Python is easy to learn
```

The spaces are included in the string.

---

# 24. `input()` Does Not Automatically Convert Data

This:

```python
age = input()
```

does not mean:

```python
age = int(input())
```

They are different.

```python
age = input()
```

Result:

```python
str
```

Whereas:

```python
age = int(input())
```

Result:

```python
int
```

---

# 25. Type Conversion During Input

Common patterns:

```python
int(input())
float(input())
str(input())
```

For multiple values:

```python
map(int, input().split())
map(float, input().split())
```

Examples:

```python
age = int(input())
price = float(input())
name = input()
```

---

# 26. Formatted Output

We often need to combine variables with text.

There are several ways.

---

## Method 1: Comma in `print()`

```python
name = "Teja"
age = 21

print("Name:", name)
print("Age:", age)
```

Output:

```text
Name: Teja
Age: 21
```

---

# 27. String Concatenation

```python
name = "Teja"

print("Hello " + name)
```

Output:

```text
Hello Teja
```

But different data types cannot normally be concatenated directly.

This causes an error:

```python
age = 21

print("Age: " + age)
```

Because:

```text
str + int
```

is not allowed.

Convert it:

```python
print("Age: " + str(age))
```

---

# 28. f-Strings

f-strings are one of the easiest ways to format output.

```python
name = "Teja"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Teja and I am 21 years old.
```

Expressions can also be used:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

---

# 29. Number Formatting with f-Strings

```python
price = 99.56789

print(f"{price:.2f}")
```

Output:

```text
99.57
```

`.2f` means:

```text
2 digits after decimal
```

---

# 30. Escape Characters

Escape characters begin with `\`.

### New line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab

```python
print("Hello\tWorld")
```

Output:

```text
Hello    World
```

### Double quote

```python
print("He said \"Hello\"")
```

Output:

```text
He said "Hello"
```

### Backslash

```python
print("C:\\Users\\Teja")
```

Output:

```text
C:\Users\Teja
```

---

# 31. Raw Strings

Raw strings treat backslashes mostly as normal characters.

Use:

```python
r"string"
```

Example:

```python
path = r"C:\Users\Teja\Python"

print(path)
```

Output:

```text
C:\Users\Teja\Python
```

Raw strings are useful for Windows paths and regular expressions.

---

# 32. `print()` Return Value

An important concept:

```python
result = print("Hello")

print(result)
```

Output:

```text
Hello
None
```

Why?

Because `print()` displays the value but returns:

```python
None
```

Therefore:

```python
result is None
```

is `True`.

---

# 33. `input()` Return Value

`input()` returns the text entered by the user.

Example:

```python
value = input("Enter something: ")

print(type(value))
```

Whatever the user enters, the type is:

```text
<class 'str'>
```

unless we explicitly convert it.

---

# 34. Important Difference Between `input()` and `print()`

| Function | Purpose | Return |
|---|---|---|
| `input()` | Takes user input | `str` |
| `print()` | Displays output | `None` |

Remember:

```text
input()  → gets data
print()  → displays data
```

---

# 35. Common Input Pattern in Coding Problems

A very common pattern is:

```python
n = int(input())
```

For multiple integers:

```python
a, b = map(int, input().split())
```

For a list of integers:

```python
numbers = list(map(int, input().split()))
```

These three patterns are extremely important for coding practice.

---

# 36. Input with Multiple Data Types

Suppose input is:

```text
Teja 21 8.43
```

We can do:

```python
name, age, cgpa = input().split()

age = int(age)
cgpa = float(cgpa)

print(name)
print(age)
print(cgpa)
```

Output:

```text
Teja
21
8
.43
```

Actually, the output is:

```text
Teja
21
8.43
```

---

# 37. `split()` and `map()` Together

Consider:

```python
a, b, c = map(int, input().split())
```

Break it down:

### Step 1

```python
input()
```

User enters:

```text
10 20 30
```

Result:

```python
"10 20 30"
```

### Step 2

```python
.split()
```

Result:

```python
["10", "20", "30"]
```

### Step 3

```python
map(int, ...)
```

Converts them to integers:

```text
10
20
30
```

### Step 4

Unpacking:

```python
a = 10
b = 20
c = 30
```

This is why the following works:

```python
a, b, c = map(int, input().split())
```

---

# 38. Taking an Unknown Number of Inputs

If we don't know how many numbers the user will enter:

```python
numbers = list(map(int, input().split()))

print(numbers)
```

Input:

```text
10 20 30 40 50
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 39. Taking Input for a List

```python
numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)
```

Input:

```text
5 10 15 20
```

Output:

```text
[5, 10, 15, 20]
```

---

# 40. Taking Input for a Tuple

```python
numbers = tuple(map(int, input().split()))

print(numbers)
```

Input:

```text
10 20 30
```

Output:

```text
(10, 20, 30)
```

---

# 41. Taking Input for a Set

```python
numbers = set(map(int, input().split()))

print(numbers)
```

Input:

```text
10 20 10 30
```

Possible output:

```text
{10, 20, 30}
```

Duplicates are removed because a set stores unique elements.

---

# 42. Taking Input for a Dictionary

A simple approach is:

```python
name = input("Enter name: ")
age = int(input("Enter age: "))

student = {
    "name": name,
    "age": age
}

print(student)
```

Output:

```text
{'name': 'Teja', 'age': 21}
```

---

# 43. Practical Programs

## Program 1: Calculate Area of Circle

```python
radius = float(input("Enter radius: "))

area = 3.14 * radius ** 2

print("Area:", area)
```

---

## Program 2: Calculate Simple Interest

```python
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time) / 100

print("Simple Interest:", si)
```

---

## Program 3: Swap Two Numbers

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("a =", a)
print("b =", b)
```

---

## Program 4: Convert Celsius to Fahrenheit

```python
celsius = float(input("Enter Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)
```

---

## Program 5: Calculate Total and Average

```python
a = int(input("Enter first mark: "))
b = int(input("Enter second mark: "))
c = int(input("Enter third mark: "))

total = a + b + c
average = total / 3

print("Total:", total)
print("Average:", average)
```

---

# 44. Important Difference: `print()` vs `return`

`print()` displays a value.

```python
def test():
    print(10)
```

`return` sends a value back from a function.

```python
def test():
    return 10
```

Example:

```python
x = test()

print(x)
```

Output:

```text
10
```

This topic becomes more important when learning Functions.

---

# 45. Common Mistakes

### Mistake 1: Forgetting Type Conversion

Wrong:

```python
a = input()
b = input()

print(a + b)
```

If input is:

```text
10
20
```

result:

```text
1020
```

Correct:

```python
a = int(input())
b = int(input())

print(a + b)
```

Result:

```text
30
```

---

### Mistake 2: Trying to Concatenate String and Integer

Wrong:

```python
age = 21

print("Age: " + age)
```

Correct:

```python
print("Age: " + str(age))
```

Or better:

```python
print(f"Age: {age}")
```

---

### Mistake 3: Expecting `input()` to Return an Integer

```python
age = input()
```

does not create an integer.

Use:

```python
age = int(input())
```

---

### Mistake 4: Using `bool(input())` for `"True"` / `"False"`

```python
bool("False")
```

returns:

```text
True
```

because `"False"` is a non-empty string.

---

### Mistake 5: Wrong Number of Variables

```python
a, b = input().split()
```

If the user enters:

```text
10 20 30
```

there are three values but only two variables.

This causes:

```text
ValueError
```

---

# 46. Important Patterns to Remember

### Single integer

```python
n = int(input())
```

### Single float

```python
n = float(input())
```

### Two integers

```python
a, b = map(int, input().split())
```

### Multiple integers

```python
a, b, c = map(int, input().split())
```

### List of integers

```python
numbers = list(map(int, input().split()))
```

### List of strings

```python
words = input().split()
```

### Tuple of integers

```python
numbers = tuple(map(int, input().split()))
```

### Set of integers

```python
numbers = set(map(int, input().split()))
```

---

# 47. Quick Revision

```text
input()
    ↓
always returns str
    ↓
type conversion when required
    ↓
int()
float()
bool()
...
```

For multiple values:

```text
input()
   ↓
split()
   ↓
map()
   ↓
list / tuple / unpacking
```

Example:

```python
numbers = list(map(int, input().split()))
```

Output:

```text
input → split → convert → list
```

---

# 48. Important Functions

| Function | Purpose |
|---|---|
| `input()` | Takes user input |
| `print()` | Displays output |
| `int()` | Converts to integer |
| `float()` | Converts to float |
| `str()` | Converts to string |
| `bool()` | Converts to boolean |
| `split()` | Splits a string |
| `map()` | Applies a function to values |
| `list()` | Creates a list |
| `tuple()` | Creates a tuple |
| `set()` | Creates a set |

---

# 49. Final Mental Model

Remember Input/Output like this:

```text
                 USER
                  │
                  │ enters data
                  ↓
              input()
                  │
                  ↓
                 str
                  │
          ┌───────┴────────┐
          ↓                ↓
       convert          use as str
          │
    ┌─────┼─────┐
    ↓     ↓     ↓
   int  float  bool
          │
          ↓
       PROCESS
          │
          ↓
       print()
          │
          ↓
        OUTPUT
          │
          ↓
         USER
```

The most important rule is:

> **`input()` takes data from the user and always returns a string. `print()` displays data to the user and returns `None`.**

### One-line definition

**Input is the process of receiving data from the user, while output is the process of displaying information produced by the program.**