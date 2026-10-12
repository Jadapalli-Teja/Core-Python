# Python Exception Handling — From Basics to Advanced

## 1. What Is Exception Handling?

Before understanding exception handling, we need to understand what happens when a Python program encounters a problem.

Consider this program:

```python
a = 10
b = 0

result = a / b

print(result)
print("Program completed")
```

What do you think will happen?

Python executes the first two assignments successfully:

```python
a = 10
b = 0
```

Next, Python evaluates:

```python
result = a / b
```

But `b` is zero. Ordinary division by zero is not allowed, so Python raises an exception named `ZeroDivisionError`.

The program stops at that point because the exception is not handled.

The last two statements do not execute.

### What is exception handling?

**Exception handling is a way to respond to errors that occur while a program is running, instead of allowing an unhandled exception to terminate the normal flow of the program.**

We can handle the previous example using `try` and `except`.

```python
a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program completed")
```

Output:

```text
Cannot divide by zero
Program completed
```

Now the program handles the division failure and continues after the exception-handling statement.

### Remember

Exception handling does not make an invalid operation valid. It gives us a way to respond when the operation fails.

---

## 2. What Is an Exception?

An exception is an object that represents a condition that interrupts the normal execution of Python code.

For example:

```python
number = int("hello")
```

Python cannot convert `"hello"` into an integer, so it raises a `ValueError`.

The exception class tells us the category of the problem.

| Exception | Simple meaning |
|---|---|
| `ZeroDivisionError` | An invalid division or modulo operation involving zero |
| `ValueError` | The value is unsuitable for the requested operation |
| `TypeError` | An object has an inappropriate type for an operation |
| `NameError` | A name cannot be found |
| `IndexError` | A sequence index is outside the valid range |
| `KeyError` | A dictionary key is missing |
| `AttributeError` | An object does not provide the requested attribute |
| `FileNotFoundError` | A requested file cannot be found |
| `ModuleNotFoundError` | A requested module cannot be found |

We will examine these exceptions individually later.

## 3. Errors vs Exceptions

Python problems can be understood in three broad categories.

### 3.1 Syntax errors

A syntax error occurs when Python cannot parse the source code correctly.

Example:

```python
if 10 > 5
    print("Greater")
```

The colon is missing after the condition.

Correct code:

```python
if 10 > 5:
    print("Greater")
```

A malformed `try` statement cannot handle its own syntax error because Python must parse the code before executing it.

### 3.2 Runtime exceptions

A runtime exception occurs while Python is executing code.

Example:

```python
print(10 / 0)
```

The syntax is correct, but the operation raises `ZeroDivisionError`.

### 3.3 Logical errors

A logical error occurs when the program runs but produces the wrong result.

```python
length = 10
width = 5

area = length + width
print(area)
```

Output:

```text
15
```

The program runs, but the formula is incorrect.

Correct code:

```python
area = length * width
print(area)
```

Output:

```text
50
```

Exception handling does not automatically fix logical errors.

---

## 4. Why Do We Need Exception Handling?

Imagine asking a user to enter their age.

```python
age = int(input("Enter your age: "))
print(age)
```

If the user enters:

```text
twenty
```

Python raises `ValueError`, because the text cannot be converted into an integer.

We can handle this situation:

```python
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter your age as a whole number")
```

Possible output:

```text
Enter your age: twenty
Please enter your age as a whole number
```

Exception handling is useful when:

- Users enter invalid data.
- A file does not exist.
- A network operation fails.
- A database operation raises an exception.
- A calculation receives invalid values.
- A dependency is unavailable.
- A program needs to clean up resources after a failure.

The goal is not to catch every possible error. The goal is to handle failures that the program can meaningfully recover from or report.

---

# PART 1 — TRY AND EXCEPT

## 5. Understanding the `try` Block

A `try` block contains statements that may raise exceptions.

Syntax:

```python
try:
    # Code that may raise an exception
    pass
except SomeException:
    # Code that handles that exception
    pass
```

Example:

```python
try:
    number = int("100")
    print(number)
except ValueError:
    print("Conversion failed")
```

Output:

```text
100
```

No exception occurs, so the `except` block is skipped.

Now change the value:

```python
try:
    number = int("hello")
    print(number)
except ValueError:
    print("Conversion failed")
```

Output:

```text
Conversion failed
```

### Important rule

If an exception occurs inside the `try` block, Python skips the remaining statements in that `try` suite and looks for a matching exception handler.

---

## 6. Understanding the `except` Block

The `except` block handles a matching exception.

Consider:

```python
try:
    print("Statement 1")
    print(10 / 0)
    print("Statement 2")
except ZeroDivisionError:
    print("Exception handled")
print("Statement 3")
```

Output:

```text
Statement 1
Exception handled
Statement 3
```

### Step-by-step execution

**Step 1:** Python enters the `try` block.

**Step 2:** It prints `Statement 1`.

**Step 3:** Python evaluates `10 / 0`.

**Step 4:** The division raises `ZeroDivisionError`.

**Step 5:** Python immediately stops executing the remaining statements in the `try` suite.

Therefore, this statement is skipped:

```python
print("Statement 2")
```

**Step 6:** Python searches for a handler matching `ZeroDivisionError`.

**Step 7:** The matching `except` block executes.

**Step 8:** After the handler finishes, Python continues after the entire `try` statement and prints `Statement 3`.

This is the basic execution process behind exception handling.

---

## 7. Handling Different Exceptions Separately

Consider this program:

```python
number = int(input("Enter a number: "))
print(100 / number)
```

There are two possible problems:

1. The user enters text that cannot be converted to an integer.
2. The user enters zero, causing division by zero.

These problems have different exception types.

We can handle them separately:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("The number cannot be zero")
```

For input `abc`:

```text
Enter a number: abc
Please enter a valid integer
```

For input `0`:

```text
Enter a number: 0
The number cannot be zero
```

For input `5`:

```text
Enter a number: 5
20.0
```

### Why use separate handlers?

Because each handler can respond appropriately to a different problem.

If we use one generic message for every failure, the user may not understand what went wrong.

---

## 8. Handling Multiple Exceptions in One Block

If different exceptions require the same response, we can handle them using a tuple.

Syntax:

```python
except (ExceptionType1, ExceptionType2):
    pass
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except (ValueError, ZeroDivisionError):
    print("Enter a valid, non-zero integer")
```

Both `ValueError` and `ZeroDivisionError` use the same handler.

Use this approach when the same response is suitable for all listed exceptions.

---

## 9. Catching an Exception Using `as`

Sometimes we want to know the exception message.

We can use `as` to bind the exception object to a variable.

```python
try:
    number = int("hello")

except ValueError as error:
    print("Exception type:", type(error).__name__)
    print("Exception message:", error)
```

Output:

```text
Exception type: ValueError
Exception message: invalid literal for int() with base 10: 'hello'
```

Here:

```python
except ValueError as error:
```

means that the caught exception object is available through the name `error` inside the handler.

The exact wording of an exception message can vary between Python versions.

### Why is `as` useful?

It allows us to:

- Display a useful error message.
- Log details for debugging.
- Inspect the exception type.
- Preserve or re-raise the exception.
- Access exception attributes when available.

---

## 10. The Difference Between `ValueError` and `TypeError`

These exceptions are frequently confused.

### `ValueError`

The operation receives a suitable general type, but the value is invalid for the operation.

```python
number = int("hello")
```

The input is a string, which `int()` accepts in principle, but the string contents are not a valid integer representation.

### `TypeError`

The operation receives an object of an inappropriate type.

```python
print(10 + "20")
```

Python does not automatically add an integer and a string.

### Comparison

| Code | Exception | Reason |
|---|---|---|
| `int("hello")` | `ValueError` | The string cannot be converted to an integer |
| `10 + "20"` | `TypeError` | These operands cannot be added using `+` |
| `[10, 20][5]` | `IndexError` | The index is outside the valid sequence range |
| `{"name": "Ravi"}["age"]` | `KeyError` | The dictionary has no `"age"` key |
| `10 / 0` | `ZeroDivisionError` | Division by zero |

---

# PART 2 — ELSE AND FINALLY

## 11. Understanding the `else` Block

The `else` block executes when the `try` suite finishes without raising an exception.

Syntax:

```python
try:
    # Risky operation
    pass
except SomeException:
    # Handle failure
    pass
else:
    # Runs if try finishes normally
    pass
```

Example:

```python
try:
    number = int("50")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")
    print("Number:", number)
```

Output:

```text
Conversion successful
Number: 50
```

The conversion succeeds, so the `else` block executes.

Now change the value:

```python
try:
    number = int("hello")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")
```

Output:

```text
Invalid number
```

The `else` block is skipped.

### Why not put everything inside `try`?

Suppose we want to catch only invalid number conversions.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    print("Square:", number ** 2)
```

The conversion is the operation we expect might fail. The square calculation depends on successful conversion.

Keeping them separate makes the program's intention clearer.

**Important:** An exception raised inside `else` is not caught by the `except` clauses belonging to the same `try` statement.

---

## 12. Understanding the `finally` Block

The `finally` block is commonly used for cleanup that should happen as control leaves the `try` statement.

Example:

```python
try:
    print("Program started")
    number = 10 / 0

except ZeroDivisionError:
    print("Division failed")

finally:
    print("Cleanup completed")
```

Output:

```text
Program started
Division failed
Cleanup completed
```

The `finally` block executes after the exception handler.

### What if no exception occurs?

```python
try:
    print(10 / 2)

finally:
    print("Finally executed")
```

Output:

```text
5.0
Finally executed
```

### What if the exception is not handled?

```python
try:
    print(10 / 0)

finally:
    print("Finally executed")
```

The `finally` block runs, and then the unhandled `ZeroDivisionError` continues propagating.

### When is `finally` useful?

It is useful for cleanup tasks, such as releasing a resource or performing a final action.

However, for resources such as files, Python's `with` statement is usually a simpler and safer option.

**Important:** `finally` normally runs during ordinary exception and return handling, but it cannot guarantee cleanup if the process is forcibly terminated or certain fatal failures occur.

---

## 13. Using `try`, `except`, `else`, and `finally` Together

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter an integer")

except ZeroDivisionError:
    print("Zero is not allowed")

else:
    print("Result:", result)

finally:
    print("Program finished")
```

For input `4`:

```text
Enter a number: 4
Result: 25.0
Program finished
```

For input `abc`:

```text
Enter a number: abc
Please enter an integer
Program finished
```

For input `0`:

```text
Enter a number: 0
Zero is not allowed
Program finished
```

### Remember the order

- `try`: execute the risky operation.
- `except`: handle a matching exception.
- `else`: execute if `try` finishes normally.
- `finally`: perform final actions as control leaves the statement.

---

# PART 3 — RAISING EXCEPTIONS

## 14. What Is the `raise` Statement?

So far, Python has raised exceptions for us.

Sometimes, however, our own program must report an invalid condition.

That is where `raise` is useful.

Syntax:

```python
raise ExceptionType("Error message")
```

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Python raises `ValueError` with the message supplied.

### Why do we use `raise`?

Consider a function that withdraws money from an account.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount
```

The function refuses invalid operations instead of silently returning a misleading result.

Example:

```python
print(withdraw(1000, 300))
```

Output:

```text
700
```

But:

```python
print(withdraw(1000, 1500))
```

raises `ValueError`.

A caller can then decide how to handle that failure.

---

## 15. Raising an Exception and Handling It

We can raise an exception and catch it at another level.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")

    return "Eligible"

try:
    print(check_age(16))

except ValueError as error:
    print("Registration failed:", error)
```

Output:

```text
Registration failed: Age must be at least 18
```

### Execution process

1. Python calls `check_age(16)`.
2. The condition `age < 18` is true.
3. The function raises `ValueError`.
4. The function stops executing normally.
5. Python searches outward for a matching handler.
6. The surrounding `except ValueError` matches.
7. The handler prints the error message.

This is a common pattern: a function reports a failure, and the caller decides what to do about it.

---

## 16. Re-raising an Exception

Sometimes we catch an exception to log it or perform a small action, but we still want the original failure to reach the caller.

Use a bare `raise` inside the handler.

```python
try:
    number = int("abc")

except ValueError:
    print("Logging the conversion failure")
    raise
```

The message is printed, but the `ValueError` is raised again.

A bare `raise` preserves the currently handled exception and its traceback.

Compare this with:

```python
raise ValueError("Conversion failed")
```

That statement raises a new `ValueError` with a new message.

Use bare `raise` when the intention is to re-raise the original exception.

---

# PART 4 — CUSTOM EXCEPTIONS

## 17. What Is a Custom Exception?

A custom exception is an exception class created for a particular application.

Python already provides many built-in exceptions, but sometimes they do not clearly describe a domain-specific failure.

For example, a banking application may need:

- `InsufficientBalanceError`
- `InvalidAccountError`
- `TransactionFailedError`

We can define our own exception classes.

```python
class InvalidAgeError(Exception):
    pass
```

Here:

- `InvalidAgeError` is the custom exception class.
- `Exception` is its parent class.
- `pass` means the class body contains no additional implementation.

Now use it:

```python
def register(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")

    return "Registration successful"

try:
    print(register(16))

except InvalidAgeError as error:
    print(error)
```

Output:

```text
Age must be at least 18
```

### Why inherit from `Exception`?

Most application-specific exceptions should inherit from `Exception`, directly or through an appropriate custom base class.

This allows ordinary application handlers such as:

```python
except Exception:
```

to catch them, if that handler is appropriate.

Do not normally inherit custom application exceptions directly from `BaseException`.

---

## 18. Custom Exceptions with Additional Information

A custom exception can store useful information about the failure.

```python
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Balance {balance} is insufficient for withdrawal {amount}"
        )
```

Use it:

```python
try:
    raise InsufficientBalanceError(500, 800)

except InsufficientBalanceError as error:
    print(error)
    print("Available balance:", error.balance)
    print("Requested amount:", error.amount)
```

Output:

```text
Balance 500 is insufficient for withdrawal 800
Available balance: 500
Requested amount: 800
```

### Why is this useful?

The exception communicates both the reason for the failure and relevant data.

Custom exceptions should be designed around useful error information, not created merely to replace every built-in exception.

---

# PART 5 — EXCEPTION CHAINING

## 19. What Is Exception Chaining?

Exception chaining occurs when a new exception is raised while handling another exception, preserving the relationship between the failures.

Suppose we try to convert a string into an integer:

```python
int("hello")
```

Python raises `ValueError`.

But imagine that our application is reading a configuration value. Rather than exposing only a low-level conversion error, we want to report:

`ConfigurationError: Invalid configuration value`

We can raise a higher-level exception while preserving the original cause.

```python
class ConfigurationError(Exception):
    pass

try:
    int("hello")

except ValueError as error:
    raise ConfigurationError("Invalid configuration value") from error
```

Python displays the original `ValueError` and the new `ConfigurationError`, together with the relationship between them.

### What does `from error` mean?

```python
raise NewException("message") from error
```

It explicitly sets the original exception as the cause of the new exception.

The new exception's `__cause__` refers to the original exception.

### Step-by-step

1. `int("hello")` raises `ValueError`.
2. Python enters the `except ValueError as error` handler.
3. `error` refers to the original exception object.
4. The `raise ... from error` statement creates and raises a new exception.
5. The new exception is reported with the original exception as its explicit cause.

### Why use exception chaining?

It allows an application to provide a meaningful high-level error while preserving the lower-level reason for debugging.

---

## 20. Implicit Exception Chaining

Explicit chaining uses:

```python
raise NewException("message") from original_error
```

But Python can also preserve exception context automatically.

Example:

```python
try:
    int("hello")

except ValueError:
    raise RuntimeError("Unable to process the value")
```

The `RuntimeError` was raised while handling the `ValueError`.

Python records that relationship as the new exception's context, available through `__context__`.

### Explicit vs implicit chaining

| Feature | Explicit chaining | Implicit chaining |
|---|---|---|
| Syntax | `raise NewError() from error` | Raise a new exception while handling another |
| Relationship | Original exception is the explicit cause | Previous exception is the context |
| Main attributes | `__cause__` and `__context__` | `__context__` |
| Purpose | Explicitly state why the new error was raised | Preserve the surrounding exception context |

## 21. What Does `raise ... from None` Mean?

Sometimes an application wants to replace a low-level exception with a simpler message without displaying the previous exception context in the normal traceback.

Example:

```python
try:
    int("hello")

except ValueError:
    raise RuntimeError("Invalid configuration") from None
```

This suppresses normal display of the previous exception context.

It does not necessarily erase the original exception from the exception object's context attribute.

Use this only when hiding the low-level context is intentional. During debugging, preserving the original failure is often helpful.

---

# PART 6 — EXCEPTION PROPAGATION

## 22. What Is Exception Propagation?

Exception propagation means an exception moves outward through function calls until a matching handler is found.

Consider:

```python
def third():
    return 10 / 0

def second():
    return third()

def first():
    return second()

try:
    first()

except ZeroDivisionError:
    print("Division failed")
```

Output:

```text
Division failed
```

### Understand the process

**Step 1:** The main program calls `first()`.

**Step 2:** `first()` calls `second()`.

**Step 3:** `second()` calls `third()`.

**Step 4:** `third()` evaluates `10 / 0`.

**Step 5:** `ZeroDivisionError` is raised.

**Step 6:** `third()` has no matching handler, so the exception propagates to `second()`.

**Step 7:** `second()` has no matching handler, so it propagates to `first()`.

**Step 8:** The exception reaches the surrounding `try` statement.

**Step 9:** `except ZeroDivisionError` matches, and Python prints `Division failed`.

### Why is propagation useful?

Low-level functions can report failures without deciding how the whole application should respond.

A higher-level caller can decide whether to retry, display an error, log the problem, or stop the operation.

---

## 23. What Is a Traceback?

A traceback shows the sequence of function calls leading to an exception.

Example:

```python
def first():
    second()

def second():
    third()

def third():
    print(10 / 0)

first()
```

The traceback shows the call path through `first()`, `second()`, and `third()`, ending at the division that raises `ZeroDivisionError`.

A traceback helps you identify:

- The exception type.
- The error message.
- The line where the failure occurred.
- The sequence of calls leading to the failure.

### Exception vs traceback

An exception represents the failure.

A traceback records the execution path associated with the exception.

They are related, but they are not the same thing.

---

# PART 7 — THE EXCEPTION HIERARCHY

## 24. How Are Exceptions Organized?

Python's built-in exceptions are arranged in a class hierarchy.

A simplified diagram:

```text
BaseException
├── KeyboardInterrupt
├── SystemExit
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── AssertionError
    ├── AttributeError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── NameError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    ├── RuntimeError
    │   └── RecursionError
    ├── TypeError
    ├── ValueError
    └── SyntaxError
```

This is a simplified hierarchy; Python defines additional exception classes and relationships.

### Why does the hierarchy matter?

Because catching a parent exception also catches its subclasses.

Example:

```python
try:
    print(10 / 0)

except ArithmeticError:
    print("Arithmetic problem")
```

Output:

```text
Arithmetic problem
```

`ZeroDivisionError` is a subclass of `ArithmeticError`.

### `Exception` vs `BaseException`

Most ordinary application exceptions inherit from `Exception`.

`KeyboardInterrupt`, `SystemExit`, and `GeneratorExit` inherit directly from `BaseException`.

That is why ordinary application code should generally catch `Exception` or a more specific class instead of catching `BaseException`.

---

# PART 8 — OTHER IMPORTANT CONCEPTS

## 25. The `assert` Statement

An assertion checks an assumption about the program.

Syntax:

```python
assert condition
```

Or:

```python
assert condition, "Message"
```

Example:

```python
age = 20

assert age >= 18, "Age must be at least 18"

print("Eligible")
```

Output:

```text
Eligible
```

If the condition is false, Python raises `AssertionError`.

```python
age = 15

assert age >= 18, "Age must be at least 18"
```

### When should assertions be used?

Assertions are useful for development checks, internal assumptions, and tests.

They should not be the only way to validate user input or enforce essential business rules because Python can disable assertions with optimization options such as `-O`.

Use explicit checks and suitable exceptions for essential validation.

---

## 26. Exception Handling Inside Loops

The location of the handler changes the behavior of the program.

### Handler inside the loop

```python
values = ["10", "abc", "30"]

for value in values:
    try:
        print(int(value))

    except ValueError:
        print("Invalid value:", value)
```

Output:

```text
10
Invalid value: abc
30
```

The loop continues after the invalid value.

### Handler outside the loop

```python
values = ["10", "abc", "30"]

try:
    for value in values:
        print(int(value))

except ValueError:
    print("A value could not be converted")
```

Output:

```text
10
A value could not be converted
```

The loop stops when the invalid value raises an exception.

**Lesson:** Place the handler at the level where you want to recover.

---

## 27. Exception Handling and Files

File operations may fail because a file is missing, permission is denied, or another input/output problem occurs.

Example:

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("The file does not exist")

else:
    print(content)
```

The code handles a missing file. If another unexpected exception occurs, it is not silently swallowed.

### Why use `with`?

The `with` statement manages the file's lifetime. When the file has been successfully opened, it is closed automatically as control leaves the `with` block, including when an exception occurs during reading.

Resource management and exception handling are complementary:

- `with` manages the resource.
- `try` and `except` respond to selected failures.

---

## 28. Common Exception-Handling Mistakes

### Mistake 1: Catching everything

Avoid:

```python
try:
    risky_operation()
except:
    pass
```

This can hide bugs and catch control-flow exceptions that should normally be allowed to propagate.

### Mistake 2: Using the wrong exception type

If you expect integer conversion to fail, handle `ValueError` rather than catching an unrelated exception.

### Mistake 3: Putting too much code in `try`

A large `try` suite may catch an exception from an operation you did not intend to handle.

Keep the risky section focused.

### Mistake 4: Forgetting that code after a failing statement is skipped

```python
try:
    print(10 / 0)
    print("Next")
except ZeroDivisionError:
    print("Handled")
```

`Next` is not printed.

### Mistake 5: Assuming `else` catches errors

Exceptions raised inside `else` are not caught by the sibling `except` handlers of the same `try` statement.

### Mistake 6: Using `assert` for important input validation

Assertions can be disabled. Use explicit validation instead.

### Mistake 7: Returning `None` for every failure

A return value and an exception have different meanings. Choose a consistent contract for the function.

### Mistake 8: Raising a new exception without preserving the original cause

When translating one exception into another, consider using `raise NewError(...) from error` so the original failure remains available.

### Mistake 9: Returning from `finally`

A `return` in `finally` can override a previous return or suppress a pending exception.

### Mistake 10: Catching an exception too early

Handle an exception where the program has enough information to respond appropriately.

---

# PART 9 — COMPLETE PRACTICAL PROGRAMS

## 29. Program: Safe Integer Input

```python
while True:
    try:
        number = int(input("Enter an integer: "))

    except ValueError:
        print("Invalid input. Try again.")

    else:
        print("You entered:", number)
        break
```

This program continues asking until a valid integer is entered.

## 30. Program: Check Positive Age

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age < 18:
        return "Not eligible"

    return "Eligible"

try:
    age = int(input("Enter age: "))
    print(validate_age(age))

except ValueError as error:
    print("Invalid age:", error)
```

This program combines input conversion, validation, and exception handling.

## 31. Program: Custom Exception for Bank Withdrawal

```python
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    return balance - amount

try:
    remaining = withdraw(1000, 1500)
    print("Remaining balance:", remaining)

except ValueError as error:
    print("Invalid amount:", error)

except InsufficientBalanceError as error:
    print("Transaction failed:", error)
```

Output:

```text
Transaction failed: Insufficient balance
```

The custom exception identifies a specific business failure.

## 32. Program: Preserve an Original Exception

```python
class InvalidAgeError(Exception):
    pass

def parse_age(value):
    try:
        age = int(value)

    except ValueError as error:
        raise InvalidAgeError(
            "Age must be a whole number"
        ) from error

    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

    return age

try:
    print(parse_age("abc"))

except InvalidAgeError as error:
    print(error)
    print("Original exception:", type(error.__cause__).__name__)
```

Output:

```text
Age must be a whole number
Original exception: ValueError
```

This demonstrates exception chaining.

---

# PART 10 — PRACTICE QUESTIONS

## 33. Concept Questions

1. What is an exception?
2. What is the difference between syntax errors, runtime exceptions, and logical errors?
3. Why do we use exception handling?
4. What happens when an exception is raised inside a `try` block?
5. What is the difference between `ValueError` and `TypeError`?
6. What is the purpose of the `as` keyword in an exception handler?
7. Why should specific exception handlers appear before broader ones?
8. What is the difference between `else` and `finally`?
9. What does `raise` do?
10. What is the difference between `raise` and a bare `raise` inside a handler?
11. What is a custom exception?
12. What is exception propagation?
13. What is a traceback?
14. What is exception chaining?
15. What is the difference between `__cause__` and `__context__`?
16. Why should we avoid catching `BaseException` in ordinary application code?
17. What are the limitations of `assert`?
18. Why can a handler inside a loop behave differently from one outside the loop?

## 34. Programming Exercises

1. Handle division by zero.
2. Convert user input to an integer safely.
3. Handle invalid dictionary keys.
4. Handle a missing file.
5. Use multiple `except` blocks.
6. Use `try`, `except`, `else`, and `finally` together.
7. Create an `InvalidAgeError`.
8. Create an `InsufficientBalanceError`.
9. Demonstrate exception propagation through three functions.
10. Use `raise ... from ...` to preserve an original exception.
11. Process a list while continuing after invalid values.
12. Write a calculator that handles invalid input and division by zero.
13. Explain the traceback produced by an unhandled exception.
14. Write a program that logs a failure and re-raises the original exception.

---

# 35. Final Revision

| Concept | Main purpose |
|---|---|
| `try` | Encloses code that may fail |
| `except` | Handles a matching exception |
| `else` | Runs when `try` completes normally |
| `finally` | Performs cleanup or final actions |
| `raise` | Raises an exception explicitly |
| Bare `raise` | Re-raises the current exception |
| Custom exception | Represents an application-specific failure |
| `raise ... from ...` | Preserves an explicit exception cause |
| `assert` | Checks an internal assumption |
| Propagation | Moves an unhandled exception outward |
| Traceback | Shows the execution path leading to a failure |
| `Exception` | Base class for most application exceptions |
| `BaseException` | Root of the built-in exception hierarchy |

## Final Understanding

When Python encounters a problem during execution, it may raise an exception.

Python then looks for a matching handler. If it finds one, the handler executes. If no handler matches, the exception propagates outward and may eventually terminate the program with a traceback.

Good exception handling means understanding the failure, catching the right exception, and responding at the correct level without hiding unexpected problems.
