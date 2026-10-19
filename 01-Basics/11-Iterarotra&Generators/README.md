
# Python Iterators and Generators — Complete Guide

## 1. Introduction

In Python, iterators and generators allow us to process values one at a time.

They are useful when working with lists, strings, files, large datasets, and sequences of values.

By learning iterators and generators, we can understand how Python's `for` loop works internally and how to generate values without storing every value in memory.

### Learning Objectives

After completing this topic, you will understand:

- Iterable, iterator, and generator.
- `iter()` and `next()`.
- The iterator protocol.
- `__iter__()` and `__next__()`.
- Custom iterator classes.
- Generator functions and `yield`.
- `yield` versus `return`.
- Generator execution and preserved state.
- `StopIteration`.
- `yield from`, `send()`, `throw()`, and `close()`.
- Memory efficiency and lazy evaluation.
- Practical examples and interview questions.

---

## 2. What Is an Iterable?

An iterable is an object from which Python can obtain an iterator.

Examples:

```python
numbers = [10, 20, 30]       # List
name = "PYTHON"              # String
values = (10, 20, 30)        # Tuple
unique = {10, 20, 30}        # Set
student = {"name": "Ravi"}   # Dictionary
sequence = range(5)          # Range
```

We can use a `for` loop with an iterable.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
```

A list is iterable, but a list is not itself an iterator.

---

## 3. What Is an Iterator?

An iterator is an object that returns values one at a time and remembers its current position.

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
10
20
30
```

### Internal Execution

Initially:

```python
numbers = [10, 20, 30]
it = iter(numbers)
```

The `iter()` function creates a list iterator.

First call:

```python
next(it)
```

Returns `10`.

Second call:

```python
next(it)
```

Returns `20`.

Third call:

```python
next(it)
```

Returns `30`.

The iterator remembers its position between calls.

### Important Point

Calling `iter(numbers)` does not return the first value. It returns an iterator object.

---

## 4. The `iter()` Function

The `iter()` function obtains an iterator from an iterable.

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
```

Output:

```text
10
```

### Calling `iter()` on an Iterator

```python
numbers = [10, 20, 30]

it = iter(numbers)
it2 = iter(it)

print(it is it2)
```

Output:

```text
True
```

Why?

An iterator is already an iterator. Calling `iter(it)` returns the same object.

It does not reset the iterator.

### Calling `iter()` on a List

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(iter(numbers) is numbers)
```

Output:

```text
False
```

Why?

The list and its iterator are two different objects.

---

## 5. The `next()` Function

The `next()` function requests the next value from an iterator.

Example:

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
```

Output:

```text
10
20
```

Each call advances the iterator.

### What Happens When an Iterator Is Exhausted?

```python
it = iter([1, 2])

print(next(it))
print(next(it))
print(next(it))
```

The first two calls return `1` and `2`.

The third call raises:

```text
StopIteration
```

`StopIteration` indicates that no more values are available.

### Using a Default Value

```python
it = iter([1, 2])

print(next(it, "Finished"))
print(next(it, "Finished"))
print(next(it, "Finished"))
```

Output:

```text
1
2
Finished
```

When the iterator is exhausted, `next(iterator, default)` returns the default value instead of raising `StopIteration`.

---

## 6. The Iterator Protocol

Python's iterator protocol uses two important methods.

### `__iter__()`

Returns an iterator.

For an iterator that is also its own iterable, it returns `self`.

### `__next__()`

Returns the next value.

When no values remain, it raises `StopIteration`.

These methods are used when creating custom iterators.

---

## 7. Creating a Custom Iterator

A custom iterator is commonly implemented using a class.

Example: Print numbers from 1 to 3.

```python
class Numbers:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 3:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


it = Numbers()

print(next(it))
print(next(it))
print(next(it))
```

Output:

```text
1
2
3
```

### Understanding the Code

#### Step 1: `__init__()`

```python
def __init__(self):
    self.current = 1
```

Initializes the current number to `1`.

#### Step 2: `__iter__()`

```python
def __iter__(self):
    return self
```

Returns the iterator object itself.

#### Step 3: `__next__()`

```python
def __next__(self):
    if self.current <= 3:
        value = self.current
        self.current += 1
        return value

    raise StopIteration
```

Checks whether another number is available.

If available, it returns the current number and increments it.

Otherwise, it raises `StopIteration`.

### State Tracking

| Call | Current Before | Returned | Current After |
|---|---:|---:|---:|
| 1 | 1 | 1 | 2 |
| 2 | 2 | 2 | 3 |
| 3 | 3 | 3 | 4 |
| 4 | 4 | StopIteration | 4 |

The variable `self.current` preserves the iterator's state.

---

## 8. Custom Iterator: Numbers from 1 to N

```python
class Numbers:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


n = int(input("Enter N: "))

for number in Numbers(n):
    print(number)
```

Example input:

```text
5
```

Output:

```text
1
2
3
4
5
```

---

## 9. Custom Iterator: Numbers from N to 1

```python
class Countdown:
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value

        raise StopIteration


for number in Countdown(5):
    print(number)
```

Output:

```text
5
4
3
2
1
```

The iterator decreases the current number after returning each value.

---

## 10. Custom Iterator: Even Numbers from a List

```python
class EvenNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1

            if value % 2 == 0:
                return value

        raise StopIteration


numbers = [1, 2, 3, 4, 5, 6]

for number in EvenNumbers(numbers):
    print(number)
```

Output:

```text
2
4
6
```

The `while` loop skips odd numbers until it finds an even number.

When no matching values remain, the iterator raises `StopIteration`.

---

## 11. Custom Iterator: Reverse a String

```python
class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            char = self.text[self.index]
            self.index -= 1
            return char

        raise StopIteration


for char in ReverseString("PYTHON"):
    print(char)
```

Output:

```text
N
O
H
T
Y
P
```

The index begins at the last character and decreases after each value.

---

## 12. Separate Iterable and Iterator Classes

An iterable can create a new iterator each time `iter()` is called.

This allows independent iterations.

```python
class NumberIterator:
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 3:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


class Numbers:
    def __iter__(self):
        return NumberIterator()


values = Numbers()

it1 = iter(values)
it2 = iter(values)

print(next(it1))
print(next(it1))
print(next(it2))
print(next(it1))
```

Output:

```text
1
2
1
3
```

Why?

`it1` and `it2` are separate iterator objects. Each has its own `current` variable.

---

# PART 2: GENERATORS

## 13. What Is a Generator?

A generator is a special kind of iterator.

A common way to create a generator is to define a function containing the `yield` keyword.

Example:

```python
def numbers():
    yield 10
    yield 20
    yield 30


g = numbers()

print(next(g))
print(next(g))
print(next(g))
```

Output:

```text
10
20
30
```

A generator produces values one at a time and remembers where it paused.

### Important Point

Calling a generator function creates a generator object.

The function body does not execute until the generator is advanced, usually using `next()` or a `for` loop.

---

## 14. Understanding `yield`

The `yield` keyword produces a value and pauses the generator.

Example:

```python
def demo():
    yield 10
    yield 20
    yield 30
```

Execution:

```python
g = demo()
```

Creates the generator object without executing the body.

```python
next(g)
```

Starts the function, produces `10`, and pauses.

```python
next(g)
```

Resumes after the first `yield`, produces `20`, and pauses.

```python
next(g)
```

Resumes again and produces `30`.

### Example with Print Statements

```python
def demo():
    print("A")
    yield 1

    print("B")
    yield 2


g = demo()

print("X")
print(next(g))
print("Y")
print(next(g))
```

Output:

```text
X
A
1
Y
B
2
```

The generator executes only when a value is requested.

---

## 15. Generator Execution and Preserved State

```python
def demo():
    x = 10
    yield x

    x = x + 5
    yield x


g = demo()

print(next(g))
print(next(g))
```

Output:

```text
10
15
```

Execution:

1. The first `next()` starts the function.
2. `x` becomes `10`.
3. The first `yield` produces `10`.
4. The generator pauses.
5. The second `next()` resumes execution.
6. `x` becomes `15`.
7. The second `yield` produces `15`.

Python preserves the local variables and execution position across each yield.

---

## 16. `yield` Versus `return`

### `yield`

- Produces a value.
- Pauses the generator.
- Allows execution to resume later.

### `return`

- Ends the function.
- In a generator, ends the generator.
- An optional value is carried by `StopIteration`.

Example:

```python
def demo():
    yield 10
    yield 20
    return
    yield 30


for value in demo():
    print(value)
```

Output:

```text
10
20
```

The `return` ends the generator, so `yield 30` is never executed.

### Generator Return Value

```python
def demo():
    yield 5
    return 100


g = demo()

print(next(g))

try:
    next(g)
except StopIteration as error:
    print(error.value)
```

Output:

```text
5
100
```

The value `100` is not yielded as a normal value. It is accessible through `StopIteration.value`.

---

## 17. Generators with Loops

```python
def numbers():
    for n in range(1, 4):
        yield n


for number in numbers():
    print(number)
```

Output:

```text
1
2
3
```

The loop advances `n`. Each `yield` produces one value and pauses the generator.

---

## 18. Generators with Conditions

Example: Yield only even numbers.

```python
def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


for number in even_numbers([1, 2, 3, 4, 5, 6]):
    print(number)
```

Output:

```text
2
4
6
```

Only values that satisfy the condition are yielded.

### Generator That Produces Vowels

```python
def vowels(text):
    for char in text:
        if char.lower() in "aeiou":
            yield char


print(list(vowels("Hello Python")))
```

Output:

```text
['e', 'o', 'o']
```

The `list()` function consumes the generator and collects its values into a list.

---

## 19. Infinite Generators

An infinite generator can continue producing values indefinitely.

```python
def count_forever():
    number = 1

    while True:
        yield number
        number += 1


g = count_forever()

print(next(g))
print(next(g))
print(next(g))
```

Output:

```text
1
2
3
```

The generator produces one value whenever requested.

### Stopping with `break`

```python
for number in count_forever():
    print(number)

    if number == 5:
        break
```

Output:

```text
1
2
3
4
5
```

Without a stopping condition, the loop would keep requesting values.

---

## 20. Generator Arguments

Generators can accept function arguments.

```python
def multiples(number):
    yield number
    yield number * 2
    yield number * 3


for value in multiples(4):
    print(value)
```

Output:

```text
4
8
12
```

The argument remains available throughout generator execution.

---

## 21. `yield from`

The `yield from` statement delegates yielding to another iterable or generator.

### Using `yield`

```python
def demo():
    yield [1, 2, 3]


print(list(demo()))
```

Output:

```text
[[1, 2, 3]]
```

The entire list is yielded as one value.

### Using `yield from`

```python
def demo():
    yield from [1, 2, 3]


print(list(demo()))
```

Output:

```text
[1, 2, 3]
```

Each element is yielded separately.

### Delegating to Another Generator

```python
def first():
    yield 1
    yield 2


def combined():
    yield from first()
    yield 3


print(list(combined()))
```

Output:

```text
[1, 2, 3]
```

After the delegated generator finishes, execution continues after the `yield from` statement.

---

## 22. The `send()` Method

The `send()` method sends a value into a paused generator.

```python
def demo():
    received = yield 10
    yield received


g = demo()

print(next(g))
print(g.send(50))
```

Output:

```text
10
50
```

Explanation:

1. `next(g)` starts the generator.
2. `yield 10` produces `10` and pauses.
3. `g.send(50)` resumes the generator.
4. The paused `yield` expression evaluates to `50`.
5. The generator yields `50`.

A generator must be started before sending it a non-`None` value.

---

## 23. The `throw()` Method

The `throw()` method raises an exception at the generator's paused position.

```python
def demo():
    try:
        yield 10
    except ValueError:
        yield 99


g = demo()

print(next(g))
print(g.throw(ValueError))
```

Output:

```text
10
99
```

The exception is caught by the `except` block, which yields `99`.

If the exception is not handled, it propagates to the caller and the generator normally closes.

---

## 24. The `close()` Method

The `close()` method requests that a generator stop.

```python
def demo():
    yield 10
    yield 20


g = demo()

print(next(g))
g.close()
```

Output:

```text
10
```

After closing the generator, another `next(g)` raises `StopIteration`.

### Cleanup with `finally`

```python
def demo():
    try:
        yield 10
        yield 20
    finally:
        print("Cleanup")


g = demo()

print(next(g))
g.close()
```

Output:

```text
10
Cleanup
```

The `finally` block runs when the generator is closed while paused inside the `try` block.

---

## 25. Generator Expressions

A generator expression creates a generator using a compact expression.

```python
squares = (n * n for n in range(1, 4))

print(next(squares))
print(next(squares))
print(next(squares))
```

Output:

```text
1
4
9
```

The parentheses create a generator expression.

Generator expressions are useful, but beginners should first understand generator functions and `yield`.

---

## 26. Iterator Versus Generator

| Feature | Custom Iterator | Generator |
|---|---|---|
| Common creation method | Class | Function containing `yield` |
| `__iter__()` | Usually implemented | Provided automatically |
| `__next__()` | Implemented by us | Provided automatically |
| State management | Usually explicit attributes | Python preserves execution state |
| Stopping | Raise `StopIteration` | Finishes automatically |
| Amount of code | Usually more | Usually less |
| Control | Full custom object behavior | Convenient step-by-step production |

A generator is an iterator, but not every iterator is a generator.

For example:

```python
it = iter([10, 20, 30])
```

This creates a list iterator, not a generator.

---

## 27. List Versus Iterator Versus Generator

| Feature | List | Iterator | Generator |
|---|---|---|---|
| Stores all output values | Yes | Not necessarily | Usually produces values on demand |
| Supports `next()` directly | No | Yes | Yes |
| Supports indexing | Yes | Generally no | No |
| Can be exhausted | List itself is not consumed | Yes | Yes |
| Can easily revisit values | Yes | No, create a new iterator | No, create a new generator |
| Typical purpose | Store and reuse values | Iterate through existing data | Produce values lazily |

### Example: List

```python
values = [10, 20, 30]
print(values[1])
```

Output:

```text
20
```

### Example: Iterator

```python
values = [10, 20, 30]
it = iter(values)

print(next(it))
```

Output:

```text
10
```

### Example: Generator

```python
def values():
    yield 10
    yield 20
    yield 30


g = values()
print(next(g))
```

Output:

```text
10
```

---

## 28. Memory and Lazy Evaluation

Generators can be memory-efficient because they produce values when requested.

### List: Store All Values

```python
squares = [n * n for n in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

The list stores all five values.

### Generator: Produce Values on Demand

```python
def squares():
    for n in range(1, 6):
        yield n * n


g = squares()

print(next(g))
print(next(g))
```

Output:

```text
1
4
```

Only the requested values are produced so far.

Generators are often useful for large datasets, but they are not automatically faster in every situation. A list may be better when you need indexing or repeated access to all values.

---

## 29. Practical Example: Cumulative Sum

For `[1, 2, 3]`, the cumulative sums are `1, 3, 6`.

```python
def cumulative_sum(numbers):
    total = 0

    for number in numbers:
        total += number
        yield total


print(list(cumulative_sum([1, 2, 3])))
```

Output:

```text
[1, 3, 6]
```

The variable `total` remembers the running sum.

---

## 30. Practical Example: Running Maximum

For `[3, 1, 4, 2]`, the running maximum is `3, 3, 4, 4`.

```python
def running_maximum(numbers):
    maximum = None

    for number in numbers:
        if maximum is None or number > maximum:
            maximum = number

        yield maximum


print(list(running_maximum([3, 1, 4, 2])))
```

Output:

```text
[3, 3, 4, 4]
```

The generator remembers the largest value seen so far.

---

## 31. Practical Example: Digits of an Integer

```python
def digits(number):
    for char in str(abs(number)):
        yield int(char)


print(list(digits(5832)))
```

Output:

```text
[5, 8, 3, 2]
```

The integer is converted to a string so its digits can be processed from left to right.

---

## 32. Practical Example: Reading a File

Files are iterable. Python can read a file one line at a time.

```python
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

This is useful for large files because the program does not need to load every line into a list first.

The `with` statement closes the file when the block ends.

---

## 33. Common Mistakes

### Mistake 1: Calling `next()` on a list

Incorrect:

```python
numbers = [1, 2, 3]
# next(numbers)
```

A list is iterable but is not itself an iterator.

Correct:

```python
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))
```

### Mistake 2: Thinking `iter()` returns the first value

```python
it = iter([10, 20, 30])
```

This creates an iterator. It does not return `10`.

Use `next(it)` to obtain the first value.

### Mistake 3: Expecting a generator function to execute immediately

```python
def demo():
    print("Started")
    yield 10


g = demo()
```

Nothing is printed yet.

```python
print(next(g))
```

Output:

```text
Started
10
```

### Mistake 4: Reusing an exhausted generator

```python
g = (n for n in [1, 2, 3])

print(list(g))
print(list(g))
```

Output:

```text
[1, 2, 3]
[]
```

The first call consumes the generator. The second call finds no remaining values.

### Mistake 5: Forgetting `StopIteration`

A custom iterator must raise `StopIteration` when no values remain.

### Mistake 6: Confusing `yield` with `return`

`yield` produces a value and pauses.

`return` ends the generator.

### Mistake 7: Assuming `break` always closes a generator

`break` stops the loop, but it does not necessarily close a generator stored in another variable. Call `close()` explicitly when deterministic generator cleanup is required.

---

## 34. When Should We Use Each?

### Use a List When:

- You need to store all values.
- You need indexing.
- You want to revisit the values many times.

### Use an Iterator When:

- You want to retrieve values one at a time.
- You are consuming an existing iterable.
- You need custom iteration behavior.

### Use a Custom Iterator Class When:

- You need explicit control over the iterator's state.
- You need a specialized iterator object.
- Each iteration should have independent state.

### Use a Generator When:

- You want to produce values step by step.
- You want to avoid storing every generated value.
- You want concise code using `yield`.
- You are processing large files or streams of values.

---

## 35. Practice Exercises

### Beginner

1. Create a custom iterator that returns numbers from 1 to N.
2. Create a custom iterator that returns numbers from N to 1.
3. Create a custom iterator that returns even numbers from a list.
4. Print every character of a string using `iter()` and `next()`.
5. Write a generator that yields 10, 20, and 30.

### Intermediate

6. Create a generator that yields the first N even numbers.
7. Create a generator that yields vowels from a string.
8. Create a generator that yields cumulative sums.
9. Create a custom iterator that returns list elements with their indexes without `enumerate()`.
10. Create a custom iterator that returns characters at even indexes.

### Advanced

11. Create a generator that yields running maximum values.
12. Create an infinite counter and stop after five values.
13. Combine two generators using `yield from`.
14. Use `send()` to send a value into a paused generator.
15. Handle a `ValueError` sent using `throw()`.
16. Use `try/finally` and `close()` to demonstrate cleanup.
17. Compare two independent iterators created from the same iterable.
18. Predict output involving `print()`, `yield`, and `return`.

---

## 36. Quick Revision

| Concept | Meaning |
|---|---|
| Iterable | An object from which an iterator can be obtained |
| Iterator | An object that returns values one at a time |
| Generator | A particular kind of iterator |
| `iter()` | Obtains an iterator |
| `next()` | Requests the next value |
| `__iter__()` | Returns an iterator |
| `__next__()` | Returns the next value or raises `StopIteration` |
| `yield` | Produces a value and pauses |
| `return` | Ends a function or generator |
| `yield from` | Delegates yielding to another iterable |
| `send()` | Sends a value into a paused generator |
| `throw()` | Raises an exception at the paused generator position |
| `close()` | Requests generator termination |
| `StopIteration` | Signals that iteration has finished |
| Lazy evaluation | Values are produced when requested |

### Three Most Important Rules

1. An iterable can provide an iterator.
2. An iterator remembers its current position and returns the next value.
3. A generator is an iterator that can be written conveniently using `yield`.

**Recommended learning order:** First master `iter()`, `next()`, and the iterator protocol. Then practise custom iterator classes. Finally, learn generator functions, `yield`, and advanced generator methods.
