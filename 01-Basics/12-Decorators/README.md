# Python Decorators — Basic to Advanced

## 1. What Is a Decorator?

A decorator is a function that adds or changes the behavior of another function without directly modifying its original code.

Consider this function:

```python
def greet():
    print("Hello!")


greet()
```

Output:

```text
Hello!
```

Suppose we want to print a message before and after `greet()` runs.

One way is to modify the original function:

```python
def greet():
    print("Starting function")
    print("Hello!")
    print("Function finished")


greet()
```

Output:

```text
Starting function
Hello!
Function finished
```

But what if we have 100 functions and want to add the same behavior to all of them?

We would have to modify many functions.

Decorators help us reuse this behavior without changing each function's original code.

---

## 2. Understanding Functions as Objects

Before learning decorators, we must understand that functions are objects in Python.

This means we can assign functions to variables, pass them as arguments, and return them from other functions.

### Example 1: Assign a function to a variable

```python
def greet():
    print("Hello!")


message = greet

message()
```

Output:

```text
Hello!
```

Notice:

```python
message = greet
```

There are no parentheses after `greet`.

We are assigning a reference to the function object to `message`. We are not calling the function at that point.

Compare:

```python
message = greet
```

This assigns the function object.

```python
message = greet()
```

This calls the function immediately and assigns its return value to `message`.

Because `greet()` does not explicitly return anything, it returns `None`.

### Example 2: Pass a function to another function

```python
def greet():
    print("Hello!")


def execute(function):
    function()


execute(greet)
```

Output:

```text
Hello!
```

Step by step:

1. `greet` refers to the function object.
2. `execute(greet)` passes that object as an argument.
3. The parameter `function` refers to the same function object.
4. `function()` calls `greet()`.

This ability is important because a decorator receives another function and builds additional behavior around it.

---

## 3. Returning a Function from Another Function

A function can return another function.

```python
def outer():
    def inner():
        print("Inside inner function")

    return inner


result = outer()
result()
```

Output:

```text
Inside inner function
```

### Step-by-step execution

When `outer()` runs:

1. Python creates the local function `inner`.
2. `outer()` returns the `inner` function object.
3. The variable `result` refers to that function object.
4. `result()` calls the returned function.

Remember the difference:

```python
return inner
```

Returns the function object.

```python
return inner()
```

Calls `inner()` and returns its result.

This distinction is essential for understanding decorators.

---

## 4. Your First Decorator Without `@` Syntax

Let's create a decorator manually.

```python
def decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper


def greet():
    print("Hello!")


greet = decorator(greet)

greet()
```

Output:

```text
Before function
Hello!
After function
```

This is the fundamental structure of a decorator.

### Understand every line

The decorator:

```python
def decorator(function):
```

receives another function as its argument.

The inner function:

```python
def wrapper():
```

contains the additional behavior.

The line:

```python
function()
```

calls the original function.

Finally:

```python
return wrapper
```

returns the wrapper function without calling it.

Then:

```python
greet = decorator(greet)
```

passes the original `greet` function to the decorator and assigns the returned wrapper function to `greet`.

When we call:

```python
greet()
```

we are calling the wrapper, which calls the original function between two messages.

### Visual execution

```text
Original greet function
        |
        v
decorator(greet)
        |
        v
wrapper function returned
        |
        v
greet now refers to wrapper
        |
        v
greet()
        |
        v
Before function
        |
        v
Original greet()
        |
        v
After function
```

The original function's code was not modified.

---

## 5. Using the `@` Decorator Syntax

Python provides shorter syntax for applying decorators.

Instead of:

```python
def greet():
    print("Hello!")


greet = decorator(greet)
```

Write:

```python
@decorator
def greet():
    print("Hello!")


greet()
```

Output:

```text
Before function
Hello!
After function
```

The syntax:

```python
@decorator
def greet():
    ...
```

is approximately equivalent to:

```python
def greet():
    ...


greet = decorator(greet)
```

The decorator is applied when the function definition is executed, typically during module import or program execution.

The function body itself does not run merely because the decorator is applied.

---

## 6. Why Is the Inner Function Called `wrapper`?

The name `wrapper` is a common convention, not a special Python keyword.

It refers to a function that wraps another function with additional behavior.

Example:

```python
def decorator(function):
    def wrapper():
        print("Starting...")
        function()
        print("Finished...")

    return wrapper
```

You could name it `inner`, `new_function`, or something else. The behavior matters, not the name.

A wrapper can perform actions before and after the original function, validate arguments, measure execution time, check permissions, log calls, and much more.

---

## 7. The Problem with a Wrapper That Accepts No Arguments

Consider:

```python
def decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(10, 20)
```

This raises a `TypeError`.

Why?

The wrapper accepts no parameters:

```python
def wrapper():
```

But the call provides two arguments:

```python
add(10, 20)
```

After decoration, `add` refers to `wrapper`, so Python tries to pass two arguments to a function that accepts none.

We need a more flexible wrapper.

---

## 8. Understanding `*args` and `**kwargs`

Decorators commonly use `*args` and `**kwargs` to forward arguments.

### `*args`

Collects extra positional arguments into a tuple.

```python
def show(*args):
    print(args)


show(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

### `**kwargs`

Collects extra keyword arguments into a dictionary.

```python
def show(**kwargs):
    print(kwargs)


show(name="Teja", age=21)
```

Output:

```text
{'name': 'Teja', 'age': 21}
```

### Using both

```python
def show(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


show(10, 20, name="Teja", age=21)
```

Output:

```text
Positional: (10, 20)
Keyword: {'name': 'Teja', 'age': 21}
```

A wrapper can use the same pattern to accept and forward a wide variety of arguments.

---

## 9. A Decorator That Supports Arguments

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Before function
After function
30
```

### Step-by-step execution

**Step 1:** Python defines `add`.

**Step 2:** The decorator receives the original `add` function.

**Step 3:** The decorator returns `wrapper`.

**Step 4:** The name `add` now refers to `wrapper`.

**Step 5:** `add(10, 20)` calls `wrapper(10, 20)`.

**Step 6:** `args` becomes `(10, 20)` and `kwargs` becomes `{}`.

**Step 7:** `function(*args, **kwargs)` calls the original `add(10, 20)`.

**Step 8:** The original function returns `30`.

**Step 9:** The wrapper stores `30` in `result`, prints the ending message, and returns `30`.

**Step 10:** `print(add(10, 20))` displays `30`.

### Why return the result?

Without:

```python
return result
```

the wrapper would return `None`, even if the original function returned a value.

For a general-purpose decorator, preserving the original return value is usually important.

---

## 10. Decorators with Positional Arguments

```python
def log_calls(function):
    def wrapper(*args, **kwargs):
        print("Function called:", function.__name__)
        print("Arguments:", args)

        return function(*args, **kwargs)

    return wrapper


@log_calls
def multiply(a, b):
    return a * b


print(multiply(4, 5))
```

Output:

```text
Function called: multiply
Arguments: (4, 5)
20
```

The decorator logs the call before invoking the original function.

---

## 11. Decorators with Keyword Arguments

```python
def log_calls(function):
    def wrapper(*args, **kwargs):
        print("Function:", function.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

        return function(*args, **kwargs)

    return wrapper


@log_calls
def student(name, age):
    print(name, age)


student(name="Teja", age=21)
```

Output:

```text
Function: student
Positional arguments: ()
Keyword arguments: {'name': 'Teja', 'age': 21}
Teja 21
```

The wrapper receives the keyword arguments and passes them to the original function.

---

## 12. Decorators and Return Values

A decorator should usually preserve the original function's return value.

Incorrect example:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(2, 3))
```

Output:

```text
None
```

Why?

The original function returns `5`, but the wrapper discards it.

Correct example:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(2, 3))
```

Output:

```text
5
```

The wrapper returns the original function's result.

---

## 13. Decorators and Exceptions

A decorator can observe exceptions raised by the original function.

```python
def log_errors(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as error:
            print("An error occurred:", error)
            raise

    return wrapper


@log_errors
def divide(a, b):
    return a / b


print(divide(10, 2))
```

Output:

```text
5.0
```

If we call:

```python
divide(10, 0)
```

the decorator prints an error message and re-raises the exception.

The bare `raise` preserves the current exception rather than silently hiding the error.

A decorator should not catch and suppress exceptions unless that behavior is specifically intended.

---

## 14. Understanding Closures

Closures are an important concept behind many decorators.

A closure occurs when an inner function remembers variables from the enclosing function's scope, even after the enclosing function has returned.

Example:

```python
def outer():
    message = "Hello from outer"

    def inner():
        print(message)

    return inner


function = outer()
function()
```

Output:

```text
Hello from outer
```

The function `inner` still has access to `message`.

### Why does this work?

1. `outer()` creates the local variable `message`.
2. `outer()` defines `inner`.
3. `outer()` returns `inner`.
4. `outer()` finishes.
5. `function()` calls the returned inner function.
6. `inner` can still access `message`.

Python preserves the necessary enclosing-scope information for the closure.

### How closures help decorators

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before")
        return function(*args, **kwargs)

    return wrapper
```

The `wrapper` function remembers the `function` variable from the enclosing `decorator` call.

That is why the wrapper can call the original function after `decorator()` has returned.

---

## 15. Inspecting a Closure

Python exposes closure information through the `__closure__` attribute when a function has closure cells.

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner


function = outer()

print(function.__closure__)
```

The output shows a tuple of closure cells, but the exact representation is implementation-dependent.

You can inspect their contents:

```python
for cell in function.__closure__:
    print(cell.cell_contents)
```

Output:

```text
Hello
```

Not every function has a closure. For functions without captured variables, `__closure__` may be `None`.

---

## 16. Decorator Factory: A Decorator That Accepts Its Own Arguments

So far, our decorators receive the function being decorated.

What if we want to configure the decorator itself?

For example:

```python
@repeat(3)
def greet():
    print("Hello")
```

We want `greet()` to print `"Hello"` three times.

We need a decorator factory.

```python
def repeat(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")


greet()
```

Output:

```text
Hello
Hello
Hello
```

### Three layers explained

**Layer 1: `repeat(times)`**

Receives the decorator configuration, such as `3`.

**Layer 2: `decorator(function)`**

Receives the function that will be decorated.

**Layer 3: `wrapper(*args, **kwargs)`**

Runs when the decorated function is called.

### Equivalent expansion

```python
def greet():
    print("Hello")


greet = repeat(3)(greet)
```

The call `repeat(3)` returns a decorator. That decorator receives `greet` and returns the wrapper.

This is the pattern for decorators that accept their own settings.

---

## 17. Another Decorator Factory Example: Add a Prefix

```python
def prefix(text):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(text)
            return function(*args, **kwargs)

        return wrapper

    return decorator


@prefix("Welcome!")
def greet(name):
    print("Hello", name)


greet("Teja")
```

Output:

```text
Welcome!
Hello Teja
```

The text `"Welcome!"` is remembered by the wrapper through a closure.

---

## 18. A Timing Decorator

Decorators are often used to measure function execution time.

```python
import time


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            return function(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print("Execution time:", end - start, "seconds")

    return wrapper


@timer
def calculate():
    total = 0

    for number in range(1_000_000):
        total += number

    return total


print("Total:", calculate())
```

Example output:

```text
Execution time: 0.04 seconds
Total: 499999500000
```

The exact execution time depends on the computer, environment, and workload.

`time.perf_counter()` is suitable for measuring elapsed time.

The `finally` block ensures timing is reported even if the wrapped function raises an exception.

---

## 19. A Decorator for Access Control

A decorator can check whether a function should be allowed to run.

```python
def require_admin(function):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print("Access denied")
            return None

        return function(user, *args, **kwargs)

    return wrapper


@require_admin
def delete_record(user, record_id):
    print("Record deleted:", record_id)


delete_record("guest", 101)
delete_record("admin", 101)
```

Output:

```text
Access denied
Record deleted: 101
```

This is a demonstration of the pattern, not a secure authentication system. Real authorization should use a trustworthy identity and permission system rather than a hard-coded string.

---

## 20. Stacking Multiple Decorators

Python allows more than one decorator on a function.

```python
def first(function):
    def wrapper(*args, **kwargs):
        print("First: before")
        result = function(*args, **kwargs)
        print("First: after")
        return result

    return wrapper


def second(function):
    def wrapper(*args, **kwargs):
        print("Second: before")
        result = function(*args, **kwargs)
        print("Second: after")
        return result

    return wrapper


@first
@second
def greet():
    print("Hello")


greet()
```

Output:

```text
First: before
Second: before
Hello
Second: after
First: after
```

### Why this order?

The decorators are applied from the bottom upward.

```python
@first
@second
def greet():
    print("Hello")
```

is equivalent to:

```python
greet = first(second(greet))
```

When called, the outer `first` wrapper runs first, then the `second` wrapper, then the original function. Control returns in the reverse order.

---

## 21. The `functools.wraps` Decorator

A wrapper function normally has its own name and metadata.

Example:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@decorator
def greet():
    """Display a greeting."""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
wrapper
None
```

The decorated function has lost the original name and docstring from the perspective of these attributes.

Python provides `functools.wraps` to preserve important metadata.

Correct example:

```python
from functools import wraps


def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@decorator
def greet():
    """Display a greeting."""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Display a greeting.
```

### Why use `@wraps(function)`?

It copies important metadata from the original function to the wrapper, including its name and docstring, and sets `__wrapped__` to refer to the original function.

This helps debugging, documentation tools, and introspection.

**Best practice:** Use `@wraps(function)` in most general-purpose function decorators.

---

## 22. A Complete Logging Decorator

```python
from functools import wraps


def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        print("Arguments:", args, kwargs)

        result = function(*args, **kwargs)

        print(f"{function.__name__} finished")

        return result

    return wrapper


@log_calls
def add(a, b):
    return a + b


print("Result:", add(10, 20))
```

Output:

```text
Calling add
Arguments: (10, 20) {}
add finished
Result: 30
```

This decorator logs the function call, forwards its arguments, preserves the return value, and retains the original function's metadata.

---

## 23. Decorating Functions That Return Collections

Decorators can work with functions returning lists, tuples, dictionaries, or other objects.

```python
from functools import wraps


def show_result(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print("Result:", result)
        return result

    return wrapper


@show_result
def get_numbers():
    return [10, 20, 30]


numbers = get_numbers()
print(numbers)
```

Output:

```text
Result: [10, 20, 30]
[10, 20, 30]
```

The list is returned unchanged.

---

## 24. Decorators with Default Arguments

```python
from functools import wraps


def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling", function.__name__)
        return function(*args, **kwargs)

    return wrapper


@log_calls
def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Teja")
```

Output:

```text
Calling greet
Hello Guest
Calling greet
Hello Teja
```

Because the wrapper forwards `*args` and `**kwargs`, the original function can use its default argument normally.

---

## 25. Decorators and Function Attributes

Functions are objects, so they can have attributes.

```python
def greet():
    print("Hello")


greet.language = "English"

print(greet.language)
```

Output:

```text
English
```

A decorator can attach attributes to a wrapper, but it is important to distinguish attributes belonging to the wrapper from attributes belonging to the original function.

The `functools.wraps` decorator helps preserve standard metadata, but it does not automatically make every arbitrary attribute on the original function behave as though it were physically stored on the wrapper.

---

## 26. Class-Based Decorators

A decorator does not have to be a function. A callable object can also be used as a decorator.

An object is callable when its class implements `__call__()`.

```python
from functools import update_wrapper


class Logger:

    def __init__(self, function):
        self.function = function
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        print("Function called")
        return self.function(*args, **kwargs)


@Logger
def greet(name):
    print("Hello", name)


greet("Teja")
```

Output:

```text
Function called
Hello Teja
```

Here:

1. `Logger(greet)` creates an object.
2. `update_wrapper()` copies important metadata.
3. The decorated name refers to that object.
4. Calling `greet("Teja")` invokes the object's `__call__()` method.

Class-based decorators are useful when the decorator needs to maintain state across calls.

---

## 27. Stateful Decorator: Count Function Calls

```python
from functools import wraps


def count_calls(function):
    calls = 0

    @wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1

        print("Call number:", calls)

        return function(*args, **kwargs)

    return wrapper


@count_calls
def greet():
    print("Hello")


greet()
greet()
greet()
```

Output:

```text
Call number: 1
Hello
Call number: 2
Hello
Call number: 3
Hello
```

The `calls` variable belongs to the enclosing `count_calls()` call.

The `nonlocal` statement allows the wrapper to modify that enclosing variable.

Without `nonlocal calls`, assigning to `calls` inside `wrapper()` would make it a local variable and cause an error when the code tried to read it before assigning a value.

---

## 28. Decorator for Validating Arguments

```python
from functools import wraps


def positive_numbers(function):
    @wraps(function)
    def wrapper(a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Both numbers must be positive")

        return function(a, b)

    return wrapper


@positive_numbers
def multiply(a, b):
    return a * b


print(multiply(5, 4))
```

Output:

```text
20
```

Calling `multiply(-5, 4)` raises `ValueError`.

This decorator is specialized for functions that accept two comparable numeric arguments. For a general-purpose decorator, `*args` and `**kwargs` are more flexible.

---

## 29. Decorator for Caching Results

Caching stores a result so a repeated call can reuse it.

Python provides `functools.cache` and `functools.lru_cache` for common memoization use cases.

Example:

```python
from functools import cache


@cache
def square(number):
    print("Calculating...")
    return number * number


print(square(5))
print(square(5))
print(square(6))
```

Output:

```text
Calculating...
25
25
Calculating...
36
```

The second call to `square(5)` reuses the cached result, so `"Calculating..."` is not printed again.

Caching is most useful when repeated calls with the same arguments can safely reuse the same result.

The arguments must be hashable for `cache` and `lru_cache`, and cached results may need invalidation if the underlying data can change.

---

## 30. Built-in and Standard Library Decorators

Python uses decorators in many places.

### `@property`

Lets a method be accessed like an attribute.

```python
class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2


circle = Circle(5)

print(circle.area)
```

Output:

```text
78.53975
```

### `@staticmethod`

Defines a method that does not automatically receive the instance or class as its first argument.

```python
class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b


print(MathOperations.add(10, 20))
```

Output:

```text
30
```

### `@classmethod`

Defines a method that receives the class as its first argument.

```python
class Student:

    school = "ABC College"

    @classmethod
    def show_school(cls):
        return cls.school


print(Student.show_school())
```

Output:

```text
ABC College
```

These decorators are built into Python's object model and are widely used in classes.

---

## 31. Common Decorator Mistakes

### Mistake 1: Calling the function instead of passing it

Incorrect:

```python
greet = decorator(greet())
```

This calls `greet()` immediately and passes its return value to the decorator.

Usually, you want:

```python
greet = decorator(greet)
```

### Mistake 2: Forgetting to return the wrapper

Incorrect:

```python
def decorator(function):
    def wrapper():
        function()
```

Because the decorator does not return `wrapper`, the decorated name becomes `None`.

Correct:

```python
def decorator(function):
    def wrapper():
        function()

    return wrapper
```

### Mistake 3: Forgetting to return the original result

Incorrect:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper
```

The wrapper returns `None`.

Correct:

```python
def decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

### Mistake 4: Not accepting arguments

A wrapper defined as `wrapper()` cannot accept arbitrary positional and keyword arguments.

Use `wrapper(*args, **kwargs)` when the decorator must support general function signatures.

### Mistake 5: Forgetting `functools.wraps`

Without `@wraps(function)`, the wrapper's name and docstring generally replace the original function's metadata.

### Mistake 6: Catching exceptions and silently hiding them

A decorator that suppresses errors can make debugging difficult. Only suppress exceptions when it is an intentional part of the design.

### Mistake 7: Confusing decorator arguments with function arguments

In:

```python
@repeat(3)
def greet(name):
    print(name)
```

`3` configures the decorator. A value such as `"Teja"` is an argument passed to the decorated function when it is called.

---

## 32. Practice Questions

### Beginner

1. Create a decorator that prints `"Before"` and `"After"` around a function.
2. Create a decorator that prints the function name.
3. Create a decorator that supports positional arguments.
4. Create a decorator that preserves the original return value.
5. Explain the difference between `return inner` and `return inner()`.

### Intermediate

6. Create a decorator that counts function calls.
7. Create a decorator factory that repeats a function a specified number of times.
8. Create a decorator that measures execution time.
9. Create a decorator that catches and logs an exception before re-raising it.
10. Use `functools.wraps` and inspect `__name__` and `__doc__`.
11. Stack two decorators and explain the execution order.
12. Create a decorator that validates two positive numbers.

### Advanced

13. Create a class-based decorator using `__call__()`.
14. Create a decorator that caches function results.
15. Use `@property` to calculate a value from an object's attributes.
16. Explain how a closure preserves variables after the outer function returns.
17. Build a decorator factory that accepts a configurable message.
18. Explain how `@decorator` expands into an assignment.

---

## 33. Quick Revision

| Concept | Meaning |
|---|---|
| Decorator | Adds behavior around a function or another callable |
| Wrapper | Function that calls or surrounds another function |
| `@decorator` | Syntax for applying a decorator |
| `*args` | Collects positional arguments |
| `**kwargs` | Collects keyword arguments |
| Closure | Inner function retains access to enclosing variables |
| Decorator factory | Function that creates and returns a decorator |
| `functools.wraps` | Preserves important original-function metadata |
| `nonlocal` | Allows modification of a variable in an enclosing function scope |
| `__call__()` | Makes an instance callable |
| `@property` | Exposes a method through attribute access |
| `@staticmethod` | Defines a static method |
| `@classmethod` | Defines a method that receives the class |
| `@cache` | Caches function results |
| `@lru_cache` | Caches results with a configurable maximum size |

## 34. Final Understanding

Remember these points:

1. Functions are objects in Python.
2. Functions can be passed to and returned from other functions.
3. A decorator receives a callable and returns a callable.
4. A wrapper adds behavior around the original function.
5. `*args` and `**kwargs` allow flexible argument forwarding.
6. Returning the original function's result preserves its return behavior.
7. Closures allow wrappers to remember the original function and other configuration.
8. Decorator factories make configurable decorators possible.
9. `functools.wraps` preserves important metadata.
10. Decorators are useful for logging, timing, validation, caching, and access control.

**The core pattern to remember is:**

```python
from functools import wraps


def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Additional behavior before the function
        result = function(*args, **kwargs)
        # Additional behavior after the function
        return result

    return wrapper
```

Once you understand this pattern, many Python decorators become much easier to read and write.