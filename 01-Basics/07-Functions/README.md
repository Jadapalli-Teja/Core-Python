# Functions in Python

## 1. What Is a Function?

A function is a reusable block of code that performs a particular task.

Instead of writing the same code repeatedly, we can write it once inside a function and call it whenever needed.

Example without a function:

```python
print(10 + 20)
print(10 + 20)
print(10 + 20)
```

Example using a function:

```python
def add():
    print(10 + 20)

add()
add()
add()
```

Output:

```text
30
30
30
```

Both programs produce the same output, but the function version avoids repeating the calculation code.

**Important:** Defining a function does not normally execute its body. The body runs when the function is called.

---

## 2. Why Do We Need Functions?

Functions help us to:

- Reuse code.
- Avoid unnecessary repetition.
- Divide large programs into smaller parts.
- Make code easier to read and maintain.
- Test individual parts of a program.
- Accept different inputs and produce different results.
- Organize program logic.

For example, a calculator can have separate functions for addition, subtraction, multiplication, and division.

---

## 3. Types of Functions in Python

Two basic categories are:

### Built-in functions

These are provided by Python.

Examples:

```python
print("Hello")
len("Python")
type(10)
max(10, 20, 30)
sum([10, 20, 30])
```

### User-defined functions

These are created by the programmer using `def` or `lambda`.

Example:

```python
def greet():
    print("Hello")

greet()
```

Python also supports methods, generator functions, asynchronous functions, and other specialized forms.

---

# Part 1: Defining and Calling Functions

## 4. The `def` Keyword

The `def` keyword is used to define a function.

### Syntax

```python
def function_name():
    statements
```

Example:

```python
def greet():
    print("Hello, Python!")

greet()
```

Output:

```text
Hello, Python!
```

Explanation:

- `def` starts the function definition.
- `greet` is the function name.
- `()` contains the parameter list, which is empty here.
- `:` marks the start of the function body.
- The indented statement belongs to the function.
- `greet()` calls the function.

---

## 5. Function Definition vs Function Call

Consider:

```python
def greet():
    print("Hello")

print("Before call")
greet()
print("After call")
```

Output:

```text
Before call
Hello
After call
```

Execution flow:

```text
Python reads the function definition
             ↓
Function body is not executed yet
             ↓
print("Before call")
             ↓
greet() is called
             ↓
Function body executes
             ↓
Control returns to the caller
             ↓
print("After call")
```

The function definition tells Python what the function does. The call requests its execution.

---

## 6. Calling a Function Multiple Times

```python
def greet():
    print("Welcome")

greet()
greet()
greet()
```

Output:

```text
Welcome
Welcome
Welcome
```

Each call executes the function body again.

---

## 7. Function Names

Function names should describe the task they perform.

Good examples:

```python
calculate_total()
find_largest()
check_prime()
display_menu()
```

Avoid unclear names such as:

```python
x()
abc()
do1()
```

Use lowercase words separated by underscores, following Python's usual naming convention.

---

# Part 2: Parameters and Arguments

## 8. What Is a Parameter?

A parameter is a name written in a function definition that receives a value when the function is called.

Example:

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a parameter.

## 9. What Is an Argument?

An argument is a value or expression supplied when calling a function.

```python
greet("Teja")
```

Here, `"Teja"` is an argument.

Output:

```text
Hello Teja
```

Remember:

```text
Function definition → parameter
Function call       → argument
```

---

## 10. Functions with One Parameter

```python
def square(number):
    print(number * number)

square(5)
square(8)
```

Output:

```text
25
64
```

The same function works with different arguments.

During the first call:

```text
number = 5
5 * 5 = 25
```

During the second call:

```text
number = 8
8 * 8 = 64
```

---

## 11. Functions with Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
add(100, 200)
```

Output:

```text
30
300
```

For the call:

```python
add(10, 20)
```

Python binds the arguments as:

```text
a = 10
b = 20
```

Then it evaluates:

```python
a + b
```

which produces `30`.

---

## 12. Positional Arguments

Positional arguments are matched to parameters by their position.

```python
def introduce(name, age):
    print(name, age)

introduce("Teja", 21)
```

Output:

```text
Teja 21
```

The first argument goes to `name`, and the second goes to `age`.

Changing the order changes the assignments:

```python
introduce(21, "Teja")
```

Output:

```text
21 Teja
```

Python does not automatically know which value is a name or an age.

---

## 13. Keyword Arguments

Keyword arguments identify parameters by name.

```python
def introduce(name, age):
    print(name, age)

introduce(age=21, name="Teja")
```

Output:

```text
Teja 21
```

The order of keyword arguments can differ from the order of parameters.

Keyword arguments are especially useful when a function has several parameters.

---

## 14. Mixing Positional and Keyword Arguments

This is valid:

```python
def student(name, age, course):
    print(name, age, course)

student("Teja", age=21, course="Python")
```

Output:

```text
Teja 21 Python
```

However, positional arguments cannot follow keyword arguments in a normal function call.

Invalid:

```python
student(name="Teja", 21, course="Python")
```

Correct:

```python
student("Teja", 21, course="Python")
```

or:

```python
student(name="Teja", age=21, course="Python")
```

---

## 15. Default Arguments

A default argument gives a parameter a value to use when no argument is supplied for it.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Teja")
```

Output:

```text
Hello Guest
Hello Teja
```

When `greet()` is called without an argument, `name` receives `"Guest"`.

When `greet("Teja")` is called, the supplied value is used instead.

### Default parameter ordering

Parameters with defaults normally follow parameters without defaults.

Valid:

```python
def student(name, age=21):
    print(name, age)
```

Invalid:

```python
def student(age=21, name):
    print(name, age)
```

The invalid definition places a required parameter after a default parameter.

---

## 16. Mutable Default Argument Trap

Avoid using a mutable object such as a list as a default value when you intend to create a new list on every call.

Problematic example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
```

Output:

```text
['apple']
['apple', 'banana']
```

Why?

The default list is created once when the function is defined and reused for calls that omit `items`.

A safer pattern is:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
```

Output:

```text
['apple']
['banana']
```

Now each call without an `items` argument gets a new list.

---

# Part 3: `return` vs `print()`

## 17. What Is `return`?

The `return` statement ends a function call and sends a value back to the caller.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

The function calculates the result and returns it. The caller stores the returned value in `result`.

---

## 18. Difference Between `print()` and `return`

### Using `print()`

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Why?

1. `print(a + b)` displays `30`.
2. The function reaches its end without a `return` statement.
3. Python returns `None` automatically.
4. Therefore, `result` contains `None`.

### Using `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

The returned value is available for later calculations.

**Remember:**

- `print()` displays information.
- `return` sends a value back to the caller.

---

## 19. Using a Returned Value in Another Calculation

```python
def square(n):
    return n * n

result = square(5)

print(result + 10)
```

Output:

```text
35
```

Execution:

```text
square(5)
    ↓
5 * 5
    ↓
return 25
    ↓
result = 25
    ↓
result + 10
    ↓
35
```

---

## 20. Returning Multiple Values

Python allows a function to return multiple values.

```python
def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(10, 4)

print(sum_result)
print(difference)
```

Output:

```text
14
6
```

Technically, the return expression creates a tuple:

```python
(a + b, a - b)
```

The caller unpacks the tuple into two variables.

---

## 21. A Function Without an Explicit `return`

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

```text
Hello
None
```

A function without an explicit return value returns `None`.

This is different from returning a value such as `0`, `False`, or an empty string.

---

## 22. Early Return

A function can return before reaching the end of its body.

```python
def check_number(n):
    if n < 0:
        return "Negative"

    return "Zero or positive"

print(check_number(-5))
print(check_number(10))
```

Output:

```text
Negative
Zero or positive
```

When `n < 0`, the first `return` immediately ends that function call.

---

# Part 4: Scope of Variables

## 23. What Is Scope?

Scope determines where a variable name can be accessed.

Common concepts include:

- Local scope
- Enclosing scope
- Global scope
- Built-in scope

Python generally resolves names using the **LEGB rule**:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches in that order when resolving a name.

---

## 24. Local Variables

A variable assigned inside a function is usually local to that function, unless a declaration such as `global` or `nonlocal` changes how the name is treated.

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Output:

```text
Hello
```

The name `message` is local to `greet()`.

Trying to access it outside the function causes a `NameError`:

```python
def greet():
    message = "Hello"

greet()
print(message)
```

---

## 25. Global Variables

A global variable is defined at module level.

```python
name = "Teja"

def greet():
    print(name)

greet()
print(name)
```

Output:

```text
Teja
Teja
```

The function can read the global variable because it does not define a local variable with the same name.

---

## 26. Local and Global Variables with the Same Name

```python
x = 100

def show():
    x = 20
    print(x)

show()
print(x)
```

Output:

```text
20
100
```

The assignment `x = 20` creates a local variable inside `show()`. It does not change the global `x`.

---

## 27. The `global` Keyword

Use `global` when a function needs to assign to a global variable.

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)
```

Output:

```text
2
```

Without `global`, an assignment such as `count += 1` would treat `count` as local and raise an `UnboundLocalError` because Python would try to read the local variable before it had been assigned.

In larger programs, returning a new value or using an object to hold state is often easier to maintain than modifying globals.

---

## 28. The `nonlocal` Keyword

`nonlocal` is used in a nested function to refer to a variable in the nearest enclosing function scope, excluding the global scope.

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    inner()

    print(count)

outer()
```

Output:

```text
2
```

Here:

- `count` belongs to `outer()`.
- `inner()` accesses that enclosing variable.
- `nonlocal count` allows `inner()` to reassign it.

---

# Part 5: `*args` and `**kwargs`

## 29. Variable-Length Arguments

Sometimes a function needs to accept a variable number of arguments.

Python provides:

- `*args` for extra positional arguments.
- `**kwargs` for extra keyword arguments.

The names `args` and `kwargs` are conventions. The `*` and `**` syntax is what matters.

---

## 30. Using `*args`

```python
def add(*args):
    print(args)

add(10, 20)
add(10, 20, 30, 40)
```

Output:

```text
(10, 20)
(10, 20, 30, 40)
```

Inside the function, `args` is a tuple containing the extra positional arguments.

### Calculate their sum

```python
def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10, 20))
print(add(10, 20, 30, 40))
```

Output:

```text
30
100
```

The loop works with any number of supplied positional arguments.

---

## 31. Using `**kwargs`

```python
def display(**kwargs):
    print(kwargs)

display(name="Teja", age=21)
```

Output:

```text
{'name': 'Teja', 'age': 21}
```

Inside the function, `kwargs` is a dictionary containing the extra keyword arguments.

### Example

```python
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

student(name="Teja", age=21, course="Python")
```

Output:

```text
name Teja
age 21
course Python
```

---

## 32. Using Normal Parameters with `*args` and `**kwargs`

```python
def display(name, *args, **kwargs):
    print("Name:", name)
    print("Extra positional:", args)
    print("Extra keyword:", kwargs)

display("Teja", 10, 20, age=21, course="Python")
```

Output:

```text
Name: Teja
Extra positional: (10, 20)
Extra keyword: {'age': 21, 'course': 'Python'}
```

The argument `"Teja"` is assigned to `name`. The remaining positional arguments go into `args`, and the extra keyword arguments go into `kwargs`.

---

# Part 6: Lambda Functions

## 33. What Is a Lambda Function?

A lambda function is a small anonymous function created using the `lambda` keyword.

Syntax:

```python
lambda parameters: expression
```

Example:

```python
square = lambda n: n * n

print(square(5))
```

Output:

```text
25
```

The expression's result is returned automatically.

This is similar to:

```python
def square(n):
    return n * n
```

Use `def` for most named functions, especially when they need multiple statements or clear documentation.

---

## 34. Lambda with Multiple Parameters

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Lambda functions can have multiple parameters, but the body is limited to a single expression.

---

## 35. Lambda with `sorted()`

```python
students = [
    ("Ravi", 80),
    ("Teja", 95),
    ("Kiran", 70)
]

result = sorted(students, key=lambda student: student[1])

print(result)
```

Output:

```text
[('Kiran', 70), ('Ravi', 80), ('Teja', 95)]
```

The `key` function tells `sorted()` to compare each tuple using its second element.

---

# Part 7: Recursion

## 36. What Is Recursion?

Recursion occurs when a function calls itself.

A recursive function needs:

1. A **base case** that stops the recursion.
2. A **recursive case** that moves the problem toward the base case.

Without a suitable base case, recursion may continue until Python raises a `RecursionError`.

---

## 37. Factorial Using Recursion

Mathematically:

\[
n! = n \times (n-1)!
\]

with:

\[
0! = 1
\]

Program:

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

### Step-by-step calls

```text
factorial(5)
    ↓
5 * factorial(4)
    ↓
5 * 4 * factorial(3)
    ↓
5 * 4 * 3 * factorial(2)
    ↓
5 * 4 * 3 * 2 * factorial(1)
    ↓
5 * 4 * 3 * 2 * 1 * factorial(0)
    ↓
factorial(0) returns 1
```

Now the calls return in reverse order:

```text
factorial(0) = 1
factorial(1) = 1 * 1 = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
factorial(5) = 5 * 24 = 120
```

For production-quality code, validate that the input is a non-negative integer.

---

## 38. Sum of Numbers Using Recursion

```python
def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)

print(sum_numbers(5))
```

Output:

```text
15
```

The function calculates:

```text
5 + 4 + 3 + 2 + 1 + 0
```

---

## 39. Recursion vs Iteration

| Recursion | Iteration |
|---|---|
| A function calls itself | A loop repeats statements |
| Needs a base case | Needs a loop termination condition |
| Uses function-call stack space | Often uses less additional stack space |
| Can be natural for tree and divide-and-conquer problems | Often simpler for straightforward repetition |

Python limits recursion depth to prevent unbounded recursive calls. For simple counting and accumulation, a loop is often more efficient.

---

# Part 8: Functions as Objects

## 40. Functions Are First-Class Objects

In Python, functions are objects. This means they can be:

- Assigned to variables.
- Passed as arguments.
- Returned from other functions.
- Stored in collections.

Example:

```python
def greet():
    print("Hello")

another_name = greet

another_name()
```

Output:

```text
Hello
```

Notice that `greet` without parentheses refers to the function object. `greet()` calls the function.

---

## 41. Passing a Function as an Argument

```python
def square(n):
    return n * n

def apply_function(function, value):
    return function(value)

print(apply_function(square, 5))
```

Output:

```text
25
```

Here, `square` is passed as a function object, and `apply_function()` calls it with the value `5`.

This pattern is useful for callbacks, sorting, and functional programming.

---

## 42. Returning a Function from Another Function

```python
def outer():
    def inner():
        return "Hello"

    return inner

function = outer()

print(function())
```

Output:

```text
Hello
```

`outer()` returns the function object `inner`. The final `function()` call executes it.

---

# Part 9: Docstrings and Type Hints

## 43. Docstrings

A docstring describes a function and its intended behavior.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(10, 20))
print(add.__doc__)
```

Output:

```text
30
Return the sum of two numbers.
```

Docstrings are useful for explaining purpose, parameters, return values, and assumptions.

---

## 44. Type Hints

Type hints describe the types expected for parameters and return values.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

Here:

- `a: int` suggests an integer parameter.
- `b: int` suggests an integer parameter.
- `-> int` suggests an integer return value.

Python does not normally enforce these annotations at runtime. They help developers, editors, and static type-checking tools.

---

# Part 10: Additional Important Concepts

## 45. Passing Mutable Objects to Functions

Python passes object references by assignment. A function parameter becomes a local name referring to the supplied object.

If the object is mutable, modifying it inside the function can affect the same object seen by the caller.

Example:

```python
def add_item(items):
    items.append(40)

numbers = [10, 20, 30]

add_item(numbers)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

The function modifies the existing list.

### Reassigning the parameter is different

```python
def change(items):
    items = [100, 200]

numbers = [10, 20, 30]

change(numbers)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

Reassigning the local parameter `items` does not reassign the caller's variable `numbers`.

---

## 46. Functions Can Call Other Functions

```python
def square(n):
    return n * n

def calculate(a, b):
    return square(a) + square(b)

print(calculate(3, 4))
```

Output:

```text
25
```

Execution:

```text
calculate(3, 4)
      ↓
square(3) + square(4)
      ↓
9 + 16
      ↓
25
```

Breaking a problem into smaller functions improves reuse and readability.

---

## 47. Function Annotations

Annotations can describe parameter and return types.

```python
def greet(name: str) -> str:
    return f"Hello {name}"

print(greet("Teja"))
print(greet.__annotations__)
```

Output:

```text
Hello Teja
{'name': <class 'str'>, 'return': <class 'str'>}
```

Annotations are metadata; they do not automatically validate arguments.

---

## 48. Positional-Only and Keyword-Only Parameters

Python allows function definitions to control how parameters may be supplied.

### Positional-only parameters

The `/` marks parameters before it as positional-only.

```python
def divide(a, b, /):
    return a / b

print(divide(10, 2))
```

Output:

```text
5.0
```

A call such as `divide(a=10, b=2)` is not allowed.

### Keyword-only parameters

The `*` marks parameters after it as keyword-only.

```python
def greet(name, *, message="Hello"):
    print(message, name)

greet("Teja", message="Welcome")
```

Output:

```text
Welcome Teja
```

A call such as `greet("Teja", "Welcome")` is not allowed because `message` must be passed by keyword.

---

# Part 11: Practical Programs

## 49. Check Even or Odd Using a Function

```python
def is_even(n):
    return n % 2 == 0

number = int(input("Enter a number: "))

if is_even(number):
    print("Even")
else:
    print("Odd")
```

Input:

```text
10
```

Output:

```text
Even
```

---

## 50. Find the Largest of Three Numbers

```python
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest(10, 25, 15))
```

Output:

```text
25
```

---

## 51. Check a Prime Number Using a Function

```python
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(17))
print(is_prime(20))
```

Output:

```text
True
False
```

---

## 52. Count Vowels Using a Function

```python
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

print(count_vowels("Education"))
```

Output:

```text
5
```

---

## 53. Calculate Factorial Using a Function

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))
```

Output:

```text
120
```

---

## 54. Simple Calculator Using Functions

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))
```

Output:

```text
15
5
50
2.0
Cannot divide by zero
```

Each function performs one task, making the calculator easier to understand and maintain.

---

# Part 12: Common Mistakes

## 55. Forgetting to Call the Function

```python
def greet():
    print("Hello")

greet
```

This references the function object but does not call it.

Correct:

```python
greet()
```

## 56. Forgetting to Return a Value

```python
def add(a, b):
    result = a + b

print(add(10, 20))
```

Output:

```text
None
```

Correct:

```python
def add(a, b):
    return a + b
```

## 57. Using a Local Variable Outside Its Scope

A local variable defined inside a function is not automatically accessible outside it.

Return the value when the caller needs it.

## 58. Wrong Number of Arguments

```python
def add(a, b):
    return a + b

add(10)
```

This raises `TypeError` because the required argument `b` is missing.

## 59. Confusing `function` with `function()`

```python
square
```

refers to the function object.

```python
square(5)
```

calls the function with the argument `5`.

## 60. Mutable Default Arguments

Avoid using a list or dictionary as a default when a fresh object is intended for every call. Use `None` and create the object inside the function.

---

# Part 13: Time Complexity of Functions

A function does not have one fixed time complexity. Its complexity depends on the operations it performs.

### Constant-time example

```python
def get_first(numbers):
    return numbers[0]
```

For a non-empty list, accessing the first element takes \(O(1)\) time.

### Linear-time example

```python
def display(numbers):
    for num in numbers:
        print(num)
```

For a list containing `n` elements, the loop performs `n` iterations: \(O(n)\).

### Nested-loop example

```python
def display_pairs(numbers):
    for a in numbers:
        for b in numbers:
            print(a, b)
```

For `n` elements, it processes `n × n` pairs: \(O(n^2)\).

The function definition itself does not determine the complexity; the work performed during its call does.

---

# Part 14: Practice Problems

Try these programs yourself.

### Beginner

1. Create a function that prints a welcome message.
2. Create a function that returns the sum of two numbers.
3. Create a function that calculates the square of a number.
4. Create a function that checks whether a number is even or odd.
5. Create a function that returns the largest of two numbers.
6. Create a function that calculates factorial.
7. Create a function that counts vowels in a string.
8. Create a function that reverses a string.
9. Create a function that returns the sum of a list.
10. Create a function that checks whether a number is prime.

### Intermediate

11. Write a function using `*args` to calculate a sum.
12. Write a function using `**kwargs` to display student details.
13. Write a recursive function for factorial.
14. Write a recursive function for the Fibonacci sequence.
15. Write a function that returns both the minimum and maximum values.
16. Write a function that removes duplicates while preserving order.
17. Write a function that counts the frequency of each character.
18. Write a function that accepts a function as an argument.
19. Write a function that sorts tuples based on their second element.
20. Write a calculator using separate functions for each operation.

---

# Final Quick Revision

| Concept | Meaning |
|---|---|
| `def` | Defines a function |
| Function call | Executes the function |
| Parameter | Name in the function definition |
| Argument | Value supplied in a function call |
| `return` | Ends the function call and sends back a value |
| `print()` | Displays output |
| Default argument | Value used when the argument is omitted |
| Keyword argument | Argument supplied using a parameter name |
| `*args` | Collects extra positional arguments into a tuple |
| `**kwargs` | Collects extra keyword arguments into a dictionary |
| Local scope | Names local to a function |
| Global scope | Names defined at module level |
| `global` | Allows assignment to a global name |
| `nonlocal` | Allows assignment to a name in an enclosing function scope |
| Lambda | Small anonymous function expression |
| Recursion | A function calling itself |
| Docstring | Documentation string for a function |
| Type hint | Annotation describing expected types |

## Final Mental Model

```text
Define function
      ↓
Call function
      ↓
Pass arguments
      ↓
Bind parameters
      ↓
Execute function body
      ↓
Return value (if any)
      ↓
Continue caller execution
```

**One-line definition:** A function is a reusable block of code that performs a task and can accept inputs, execute instructions, and optionally return a result.