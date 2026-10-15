# Python Iterators and Generators — Complete Guide from Basic to Advanced

## 1. Introduction

In Python, we frequently work with lists, tuples, strings, dictionaries, and sets.

Example:

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
```

The `for` loop gets one element at a time and executes its body.

But have you ever wondered:

- How does Python know which element comes next?
- How does Python know when to stop?
- Can we retrieve values without using a `for` loop?
- Can we create our own objects that produce values one by one?
- Can we generate values without storing them all in a list?

Python answers these questions through **iteration, iterators, and generators**.

We will learn these concepts in the following order:

1. Iteration
2. Iterables
3. Iterators
4. `iter()` and `next()`
5. Internal execution of `for` loops
6. Iterator exhaustion
7. Custom iterator classes
8. Generators and `yield`
9. Generator execution and suspended state
10. Generator expressions
11. Memory efficiency and lazy evaluation
12. Generator methods
13. Advanced generator patterns
14. Practical programs and exercises

---

# PART 1: ITERATION AND ITERABLES

## 2. What Is Iteration?

**Iteration means accessing or processing elements one at a time.**

Example:

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

The loop processes `10`, then `20`, then `30`.

Each repetition of the loop is called an iteration.

### Example 2: Iterating over a string

```python
name = "TEJA"

for character in name:
    print(character)
```

Output:

```text
T
E
J
A
```

Python processes each character individually.

### Example 3: Iterating over a tuple

```python
colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)
```

Output:

```text
Red
Green
Blue
```

### Example 4: Iterating over a dictionary

```python
student = {
    "name": "Teja",
    "age": 21,
    "course": "Python"
}

for key in student:
    print(key)
```

Output:

```text
name
age
course
```

By default, iterating over a dictionary produces its keys.

To get values:

```python
for value in student.values():
    print(value)
```

Output:

```text
Teja
21
Python
```

To get keys and values:

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Teja
age : 21
course : Python
```

### Main point

Iteration is the process of visiting elements one at a time. Python's iterator protocol defines how objects provide those elements.

---

## 3. What Is an Iterable?

An **iterable is an object from which Python can obtain an iterator**.

Common examples include:

- Lists
- Tuples
- Strings
- Dictionaries
- Sets
- Ranges
- Files
- Generator objects

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
```

Here:

- `numbers` is an iterable.
- `iter(numbers)` obtains an iterator.
- `iterator` refers to that iterator.

### Example 1: List

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

### Example 2: String

```python
word = "Python"

for character in word:
    print(character)
```

### Example 3: Range

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

### Example 4: Set

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

The set's iteration order is not guaranteed to be a particular numerical order.

### Example 5: Dictionary

```python
student = {"name": "Teja", "age": 21}

for item in student.items():
    print(item)
```

Output:

```text
('name', 'Teja')
('age', 21)
```

### How can we check whether an object is iterable?

A useful practical test is to call `iter()`:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(iterator)
```

Python creates a list iterator. Its displayed representation can vary.

If an object cannot provide an iterator, calling `iter()` normally raises `TypeError`.

For example:

```python
number = 100

iter(number)
```

This raises a `TypeError` because an integer is not iterable.

**Important:** An iterable does not necessarily have an iteration position of its own. A list can provide a new iterator, and each iterator maintains its own progress.

---

## 4. The Difference Between Iterable and Iterator

This is one of the most important concepts in this topic.

| Iterable | Iterator |
|---|---|
| Can provide an iterator | Produces the next value |
| Usually used as the source of iteration | Keeps track of its iteration state |
| Examples: list, tuple, string | Examples: list iterator, generator |
| Commonly provides `__iter__()` | Provides `__iter__()` and `__next__()` |
| Can often create multiple independent iterators | Usually advances through one sequence of values |

Consider:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(numbers)
```

Output:

```text
10
20
[10, 20, 30]
```

The iterator advances, but the list remains unchanged.

### Visual understanding

```text
Iterable: numbers
+----------------------+
| 10 | 20 | 30         |
+----------------------+
          |
          | iter(numbers)
          v
Iterator
current progress: before 10
          |
          | next(iterator)
          v
returns 10
progress moves forward
          |
          | next(iterator)
          v
returns 20
progress moves forward
          |
          | next(iterator)
          v
returns 30
```

The iterator remembers which value should come next. The list does not need to be modified.

### Example: Two iterators from one list

```python
numbers = [10, 20, 30]

first = iter(numbers)
second = iter(numbers)

print(next(first))
print(next(first))
print(next(second))
```

Output:

```text
10
20
10
```

Why?

- `first` has returned `10` and `20`.
- `second` has returned only `10`.
- The iterators have independent progress.

This is different from using the same iterator twice.

---

## 5. The `iter()` Function

The `iter()` function obtains an iterator from an iterable.

### Syntax

```python
iter(iterable)
```

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
```

Output:

```text
10
```

### Example 2: String iterator

```python
name = "ABC"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
A
B
C
```

### Example 3: Dictionary iterator

```python
student = {"name": "Teja", "age": 21}

iterator = iter(student)

print(next(iterator))
print(next(iterator))
```

Output:

```text
name
age
```

Dictionary iteration produces keys by default.

### Example 4: Range iterator

```python
iterator = iter(range(1, 4))

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
1
2
3
```

### A subtle point

Calling `iter()` on an ordinary iterable such as a list creates a new iterator. Calling `iter()` on an iterator normally returns that same iterator.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(iter(numbers) is iterator)
print(iter(iterator) is iterator)
```

Output:

```text
False
True
```

The first comparison is false because a new list iterator is created. The second is true because the iterator returns itself.

---

## 6. The `next()` Function

The `next()` function asks an iterator for its next value.

### Syntax

```python
next(iterator)
```

Example:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

Every call advances the same iterator.

### Example: Retrieve values one by one

```python
numbers = [100, 200, 300, 400]
iterator = iter(numbers)

first = next(iterator)
second = next(iterator)

print(first)
print(second)
```

Output:

```text
100
200
```

The remaining values are still available from the iterator.

```python
print(next(iterator))
print(next(iterator))
```

Output:

```text
300
400
```

### What happens when values are finished?

```python
numbers = [10, 20]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

The first two calls return `10` and `20`. The third call raises:

```text
StopIteration
```

More precisely, Python raises the `StopIteration` exception. The full traceback and wording may vary.

This exception signals that the iterator has no more values.

### Using the default argument

You can supply a default value:

```python
numbers = [10, 20]
iterator = iter(numbers)

print(next(iterator, "Finished"))
print(next(iterator, "Finished"))
print(next(iterator, "Finished"))
```

Output:

```text
10
20
Finished
```

When the iterator is exhausted, `next(iterator, "Finished")` returns the default instead of raising `StopIteration`.

This is useful when you want to retrieve a value without handling that exception explicitly.

---

## 7. How Does a `for` Loop Work Internally?

Consider:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Conceptually, Python does something similar to the following:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
    except StopIteration:
        break

    print(number)
```

Output:

```text
10
20
30
```

This is a conceptual equivalent that illustrates the iterator protocol.

### Step-by-step execution

Initially:

```text
numbers = [10, 20, 30]
iterator = iter(numbers)
```

**First iteration**

```text
next(iterator) returns 10
number = 10
print(number)
```

Output:

```text
10
```

**Second iteration**

```text
next(iterator) returns 20
number = 20
print(number)
```

Output:

```text
20
```

**Third iteration**

```text
next(iterator) returns 30
number = 30
print(number)
```

Output:

```text
30
```

**Fourth attempt**

```text
next(iterator)
    |
    v
StopIteration
    |
    v
Loop stops
```

The `for` loop handles normal iterator exhaustion automatically. You usually do not need to catch `StopIteration` yourself.

---

## 8. Iterator Exhaustion and Reusability

An iterator generally moves forward. Once it is exhausted, it does not automatically restart.

Example:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(list(iterator))
print(list(iterator))
```

Output:

```text
[1, 2, 3]
[]
```

The first call consumes the iterator. The second call finds no values left.

### Reusing the iterable

```python
numbers = [1, 2, 3]

print(list(numbers))
print(list(numbers))
```

Output:

```text
[1, 2, 3]
[1, 2, 3]
```

The list can provide a fresh iterator each time.

### Important distinction

- Iterable: often reusable by obtaining a new iterator.
- Iterator: usually a one-pass object whose state advances.

This is common behavior, not a guarantee that every possible iterable is reusable. Some iterable objects may represent changing data or have special behavior.

### Practical example

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

for value in iterator:
    print(value)

for value in iterator:
    print(value)
```

Only the first loop prints values. The second loop prints nothing because the iterator has already been exhausted.

---

## 9. Common Built-in Iterables

### 9.1 `range()`

```python
for number in range(1, 6):
    print(number)
```

`range` provides an iterable sequence of integers without constructing a list containing every integer.

### 9.2 `enumerate()`

```python
names = ["Teja", "Ravi", "Sita"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 Teja
1 Ravi
2 Sita
```

`enumerate()` produces pairs containing an index and a value.

Start counting from one:

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

Output:

```text
1 Teja
2 Ravi
3 Sita
```

### 9.3 `zip()`

```python
names = ["Teja", "Ravi"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```text
Teja 90
Ravi 85
```

`zip()` produces tuples by combining corresponding elements. By default, it stops when the shortest input iterable is exhausted.

### 9.4 `map()`

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6]
```

In Python 3, `map()` returns an iterator-like object that computes results as they are consumed.

### 9.5 `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6]
```

`filter()` produces the elements that satisfy the condition.

These built-ins are useful because many Python operations use iteration behind the scenes.

---

# PART 2: CUSTOM ITERATORS

## 10. Understanding the Iterator Protocol

Python's iterator protocol defines two important methods:

- `__iter__()`
- `__next__()`

An iterator's `__iter__()` method returns the iterator itself.

Its `__next__()` method returns the next value or raises `StopIteration` when finished.

You rarely need to call these methods directly. Use `iter()` and `next()` in ordinary code.

### Example

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(iterator.__iter__() is iterator)
```

Output:

```text
True
```

The iterator returns itself from `__iter__()`.

---

## 11. Creating a Custom Iterator Class

Suppose we want an object that generates the numbers `1`, `2`, and `3`.

We can implement the iterator protocol ourselves.

```python
class Counter:

    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 3:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


counter = Counter()

for number in counter:
    print(number)
```

Output:

```text
1
2
3
```

### Understanding each method

**`__init__()`**

```python
def __init__(self):
    self.current = 1
```

When `Counter()` creates an object, its current value starts at `1`.

**`__iter__()`**

```python
def __iter__(self):
    return self
```

This object is its own iterator, so it returns itself.

**`__next__()`**

```python
def __next__(self):
    if self.current > 3:
        raise StopIteration

    value = self.current
    self.current += 1
    return value
```

This method:

1. Checks whether the sequence is finished.
2. Saves the current number.
3. Advances the stored number.
4. Returns the saved number.

When `current` becomes `4`, the method raises `StopIteration`.

### Why store `current` in `self`?

Because the object must remember its state between calls.

A local variable created inside `__next__()` would normally be recreated each time the method is called. An instance attribute persists between calls.

---

## 12. Custom Iterator That Generates Even Numbers

```python
class EvenNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 2
        return value


for number in EvenNumbers(10):
    print(number)
```

Output:

```text
2
4
6
8
10
```

### How it works

Initially:

```text
current = 2
limit = 10
```

Each call returns the current even number and adds two.

When `current` becomes `12`, the condition `current > limit` is true and iteration ends.

---

## 13. Custom Iterator for a Range

```python
class NumberRange:

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


for number in NumberRange(2, 6):
    print(number)
```

Output:

```text
2
3
4
5
```

The stop value is exclusive, just like `range(2, 6)`.

### A limitation of this design

The `NumberRange` object is also its iterator. Once iteration is exhausted, iterating over the same object again will not restart it.

If you want an iterable that can create a fresh iterator each time, a common design is to separate the iterable from the iterator. Generators often make that easier.

---

# PART 3: GENERATORS

## 14. What Is a Generator?

A **generator is a convenient way to create an iterator**.

A generator function uses `yield` to produce values one at a time.

Example:

```python
def numbers():
    yield 10
    yield 20
    yield 30


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
10
20
30
```

The object stored in `gen` is a generator object. It implements the iterator protocol.

### Why use a generator?

With a custom iterator class, we manually manage state using attributes such as `self.current`.

With a generator function, Python preserves the local variables and execution position while the generator is suspended. This often makes the code much simpler.

---

## 15. Understanding `yield`

The `yield` keyword produces a value and suspends the generator.

Example:

```python
def demo():
    yield 10
    yield 20


gen = demo()

print(next(gen))
print(next(gen))
```

Output:

```text
10
20
```

Compare `yield` with `return`.

### Using `return`

```python
def example():
    return 10
    return 20


print(example())
```

Output:

```text
10
```

The first `return` ends the function, so the second is never reached.

### Using `yield`

```python
def example():
    yield 10
    yield 20


gen = example()

print(next(gen))
print(next(gen))
```

Output:

```text
10
20
```

The first `yield` pauses the generator rather than finishing it.

The next call resumes execution after the previous `yield`.

---

## 16. A Generator Function Does Not Run Immediately

Consider:

```python
def demo():
    print("Function started")
    yield 100
    print("Function resumed")
    yield 200


gen = demo()

print("Generator created")
```

Output:

```text
Generator created
```

Why did `"Function started"` not appear?

Calling a generator function creates a generator object but does not execute the function body immediately.

Now advance the generator:

```python
print(next(gen))
```

Additional output:

```text
Function started
100
```

Advance it again:

```python
print(next(gen))
```

Additional output:

```text
Function resumed
200
```

The generator begins when it is first advanced and pauses at each `yield`.

---

## 17. Understanding Generator State

Consider this program:

```python
def demo():
    number = 10

    print("Before first yield")
    yield number

    number += 10

    print("Before second yield")
    yield number

    number += 10

    print("Finished calculation")
    yield number


gen = demo()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
Before first yield
10
Before second yield
20
Finished calculation
30
```

### What is preserved?

When a generator pauses, Python preserves the state needed to resume it, including:

- Its current execution position.
- Relevant local variables.
- Its active execution context.

When the next value is requested, the generator resumes from its suspended point.

The variable `number` does not restart at `10` on every call. The generator continues from its previous state.

---

## 18. Generator with a `for` Loop

```python
def generate_numbers(n):
    for number in range(1, n + 1):
        yield number


for value in generate_numbers(5):
    print(value)
```

Output:

```text
1
2
3
4
5
```

The generator produces one value per iteration.

### Generate squares

```python
def squares(n):
    for number in range(1, n + 1):
        yield number ** 2


print(list(squares(5)))
```

Output:

```text
[1, 4, 9, 16, 25]
```

The generator itself does not build the list. The call to `list()` consumes the generator and collects the results.

### Generate odd numbers

```python
def odd_numbers(limit):
    for number in range(1, limit + 1, 2):
        yield number


print(list(odd_numbers(10)))
```

Output:

```text
[1, 3, 5, 7, 9]
```

---

## 19. Generator Expressions

A generator expression is a compact way to create a generator.

### List comprehension

```python
squares = [x * x for x in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

The comprehension builds a list containing all the results.

### Generator expression

```python
squares = (x * x for x in range(1, 6))

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

The generator expression produces values as they are requested.

### Syntax comparison

```python
[x * x for x in range(5)]   # List comprehension

(x * x for x in range(5))   # Generator expression
```

The square brackets create a list. The parentheses create a generator expression.

### More examples

Squares of even numbers:

```python
result = (x * x for x in range(1, 11) if x % 2 == 0)

print(list(result))
```

Output:

```text
[4, 16, 36, 64, 100]
```

Uppercase strings:

```python
names = ["teja", "ravi", "sita"]

result = (name.upper() for name in names)

print(list(result))
```

Output:

```text
['TEJA', 'RAVI', 'SITA']
```

---

## 20. Generator Versus List Comprehension

| Feature | List comprehension | Generator expression |
|---|---|---|
| Syntax | `[expression for item in iterable]` | `(expression for item in iterable)` |
| Result | List | Generator object |
| Evaluation | Builds all list elements | Produces elements as consumed |
| Reuse | List can be iterated repeatedly | Generator is normally exhausted after one pass |
| Memory | Stores the resulting elements | Avoids storing all resulting elements together |
| Access by index | Supported | Not directly supported |

Example:

```python
numbers_list = [x * 2 for x in range(5)]
numbers_gen = (x * 2 for x in range(5))

print(numbers_list)
print(next(numbers_gen))
```

Output:

```text
[0, 2, 4, 6, 8]
0
```

Use a list when you need all results available for repeated access or indexing. Use a generator when producing values lazily is useful.

---

## 21. Lazy Evaluation

Lazy evaluation means delaying a computation until its result is requested.

Example:

```python
def numbers():
    print("Generating 1")
    yield 1

    print("Generating 2")
    yield 2

    print("Generating 3")
    yield 3


gen = numbers()

print("Generator created")
print(next(gen))
print("Requesting next value")
print(next(gen))
```

Output:

```text
Generator created
Generating 1
1
Requesting next value
Generating 2
2
```

Notice that `"Generating 3"` does not appear because the third value has not been requested.

### Why is lazy evaluation useful?

Imagine processing a large data source.

Instead of building a complete list of millions of transformed records, a generator can calculate each record only when the next record is needed.

This can reduce memory usage and avoid work for values that are never consumed.

---

## 22. Memory Efficiency: List Versus Generator

Example:

```python
numbers = [x for x in range(1_000_000)]
```

This creates a list containing one million integer objects' references and the associated list storage. Integers may also occupy memory depending on how they are represented and shared.

Compare:

```python
numbers = (x for x in range(1_000_000))
```

This creates a generator expression. It does not create a list containing one million resulting integers in advance.

### Important clarification

A generator does not automatically make every program memory-efficient.

For example:

```python
numbers = list(x for x in range(1_000_000))
```

This consumes the generator and creates a list of all results.

Similarly:

```python
numbers = list(range(1_000_000))
```

also creates a list.

A generator helps when values are consumed progressively rather than all being collected.

### Measuring approximate memory

```python
import sys

numbers_list = [x for x in range(1000)]
numbers_gen = (x for x in range(1000))

print(sys.getsizeof(numbers_list))
print(sys.getsizeof(numbers_gen))
```

The numbers depend on the Python implementation and environment. The measurement does not include every object indirectly referenced by the list or generator, so it is not a complete comparison of total memory usage.

---

## 23. Generator Exhaustion

Example:

```python
def numbers():
    yield 10
    yield 20
    yield 30


gen = numbers()

print(list(gen))
print(list(gen))
```

Output:

```text
[10, 20, 30]
[]
```

The first `list(gen)` consumes all values. The second sees an exhausted generator.

To start again:

```python
gen = numbers()

print(list(gen))
```

Output:

```text
[10, 20, 30]
```

Calling the generator function again creates a new generator object.

### Example: Partial consumption

```python
gen = (x for x in range(1, 6))

print(next(gen))
print(list(gen))
```

Output:

```text
1
[2, 3, 4, 5]
```

The first value is consumed separately. The list receives the remaining values.

---

# PART 4: PRACTICAL GENERATOR PROGRAMS

## 24. Generate Fibonacci Numbers

The Fibonacci sequence begins with `0` and `1`. Each following number is the sum of the previous two.

```python
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(10)))
```

Output:

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Execution

Initially:

```text
a = 0
b = 1
```

The first `yield` returns `0`. The assignment updates the values to `a = 1`, `b = 1`.

The next yield returns `1`. The update produces `a = 1`, `b = 2`.

The sequence continues in the same way.

The generator stores only the current pair rather than constructing a complete list of Fibonacci numbers.

---

## 25. Generate Prime Numbers

```python
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def primes(limit):
    for number in range(2, limit + 1):
        if is_prime(number):
            yield number


print(list(primes(30)))
```

Output:

```text
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

The `primes()` generator checks each number and yields only prime numbers.

This implementation is easy to understand but is not the most efficient prime-generation algorithm for very large limits.

---

## 26. Generate Multiplication Table Values

```python
def multiplication_table(number):
    for multiplier in range(1, 11):
        yield f"{number} x {multiplier} = {number * multiplier}"


for line in multiplication_table(5):
    print(line)
```

Output:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

Each line is produced only when the loop requests it.

---

## 27. Generate Even Numbers from a List

```python
def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


values = [10, 15, 20, 25, 30, 35]

print(list(even_numbers(values)))
```

Output:

```text
[10, 20, 30]
```

The generator processes the input one element at a time and yields only even numbers.

---

## 28. Generate Words from a Sentence

```python
def words(sentence):
    for word in sentence.split():
        yield word


sentence = "Python is easy to learn"

for word in words(sentence):
    print(word)
```

Output:

```text
Python
is
easy
to
learn
```

This is a simple example of processing text progressively. Note that `sentence.split()` itself constructs a list of words; a more advanced streaming parser would be needed if the entire sentence were too large to store.

---

## 29. Read a File Using a Generator

```python
def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


for line in read_lines("student.txt"):
    print(line)
```

The generator yields one line at a time.

### Important resource detail

The file remains open while the generator is suspended inside the `with` block. It closes when the generator reaches the end or the generator is properly closed.

If a caller stops early and needs prompt cleanup, it can explicitly close the generator or use `contextlib.closing()` around the generator when appropriate.

For example:

```python
from contextlib import closing

with closing(read_lines("student.txt")) as lines:
    for line in lines:
        print(line)
        break
```

This closes the generator when the `with` block exits, allowing the generator's `with open(...)` block to clean up the file.

---

## 30. A Simple Data Processing Pipeline

Generators can be combined to process data in stages.

```python
def numbers(limit):
    for number in range(1, limit + 1):
        yield number


def even_numbers(values):
    for value in values:
        if value % 2 == 0:
            yield value


def squares(values):
    for value in values:
        yield value * value


result = squares(even_numbers(numbers(10)))

print(list(result))
```

Output:

```text
[4, 16, 36, 64, 100]
```

### What happens?

1. `numbers(10)` produces numbers from `1` to `10`.
2. `even_numbers()` consumes those numbers and yields even values.
3. `squares()` consumes the even values and yields their squares.
4. `list()` consumes the final generator and collects the results.

The stages are connected without constructing a separate list at every step.

---

# PART 5: ADVANCED GENERATOR FEATURES

## 31. `yield from`

The `yield from` statement delegates iteration to another iterable or iterator.

Example:

```python
def first():
    yield 10
    yield 20


def second():
    yield from first()
    yield 30


print(list(second()))
```

Output:

```text
[10, 20, 30]
```

This is similar to:

```python
def second():
    for value in first():
        yield value

    yield 30
```

### Combining multiple iterables

```python
def combined():
    yield from [1, 2, 3]
    yield from (4, 5)
    yield from range(6, 8)


print(list(combined()))
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7]
```

### Returning a value from a subgenerator

A generator can return a final value. When delegated using `yield from`, the delegating generator can capture that return value.

```python
def subgenerator():
    yield 10
    return "Finished"


def main_generator():
    result = yield from subgenerator()
    yield result


print(list(main_generator()))
```

Output:

```text
[10, 'Finished']
```

The subgenerator yields `10` and then finishes with a return value of `"Finished"`. The `yield from` expression evaluates to that final return value.

This is an advanced feature, so focus first on the ordinary use of `yield from` to delegate iteration.

---

## 32. The `send()` Method

Generators can receive values from their callers using `send()`.

Example:

```python
def receiver():
    value = yield "Ready"
    yield f"Received: {value}"


gen = receiver()

print(next(gen))
print(gen.send(100))
```

Output:

```text
Ready
Received: 100
```

### Step-by-step execution

**First call:**

```python
next(gen)
```

The generator starts and reaches:

```python
value = yield "Ready"
```

It yields `"Ready"` and pauses.

**Second call:**

```python
gen.send(100)
```

The value `100` is sent into the suspended `yield` expression.

Conceptually:

```text
yield "Ready"
       |
       | send(100)
       v
yield expression evaluates to 100
       |
       v
value = 100
       |
       v
yield "Received: 100"
```

### Important rule

You cannot normally send a non-`None` value into a generator that has not started.

Start it first:

```python
gen = receiver()
next(gen)
gen.send(100)
```

For a newly created generator, use `next(gen)` or `gen.send(None)` to reach its first suspension point.

---

## 33. A Generator That Accumulates Values

```python
def accumulator():
    total = 0

    while True:
        number = yield total
        total += number


gen = accumulator()

print(next(gen))
print(gen.send(10))
print(gen.send(20))
print(gen.send(5))
```

Output:

```text
0
10
30
35
```

### Execution

Initially, `total = 0`.

The first `next()` advances the generator to `yield total` and returns `0`.

When `send(10)` is called, the suspended `yield` expression evaluates to `10`. The generator assigns it to `number` and updates the total to `10`.

The next `send(20)` updates the total to `30`.

The next `send(5)` updates it to `35`.

This is useful for understanding two-way communication with a generator.

---

## 34. The `throw()` Method

The `throw()` method raises an exception inside a suspended generator.

Example:

```python
def demo():
    try:
        yield 10
    except ValueError:
        yield "ValueError handled"


gen = demo()

print(next(gen))
print(gen.throw(ValueError("Invalid value")))
```

Output:

```text
10
ValueError handled
```

### How it works

1. `next(gen)` advances the generator to `yield 10`.
2. The generator pauses.
3. `throw()` raises `ValueError` at the suspended point.
4. The generator's `except ValueError` block catches it.
5. The generator yields `"ValueError handled"`.

If the exception is not caught inside the generator, it propagates to the caller.

---

## 35. The `close()` Method

The `close()` method requests termination of a generator.

It injects `GeneratorExit` at the generator's suspended point.

Example:

```python
def demo():
    try:
        yield 10
        yield 20
    finally:
        print("Cleanup executed")


gen = demo()

print(next(gen))
gen.close()
```

Output:

```text
10
Cleanup executed
```

The generator's `finally` block runs during closure.

Generators should not yield a new value while handling `GeneratorExit`; doing so causes a `RuntimeError`.

Use `close()` when you need to stop a generator before it naturally reaches the end, especially if it manages resources.

---

## 36. Generator Return Values

A generator can use `return` to stop iteration.

```python
def demo():
    yield 10
    yield 20
    return


gen = demo()

print(next(gen))
print(next(gen))
print(next(gen, "Finished"))
```

Output:

```text
10
20
Finished
```

After the `return`, the generator is exhausted.

A generator's return value is carried by the `StopIteration` exception raised when it finishes, rather than being yielded as another ordinary value.

Example:

```python
def demo():
    yield 10
    return 99


gen = demo()

print(next(gen))

try:
    next(gen)
except StopIteration as error:
    print("Return value:", error.value)
```

Output:

```text
10
Return value: 99
```

The `99` is the generator's completion value. It is not a normal yielded element.

---

## 37. The `itertools` Module

Python's `itertools` module provides tools for efficient iterator-based programming.

### 37.1 `count()`

Produces an arithmetic sequence.

```python
from itertools import count

for number in count(10, 2):
    if number > 16:
        break

    print(number)
```

Output:

```text
10
12
14
16
```

`count()` continues indefinitely unless you stop consuming it.

### 37.2 `cycle()`

Repeats values from an iterable indefinitely.

```python
from itertools import cycle

colors = cycle(["Red", "Green", "Blue"])

for _ in range(5):
    print(next(colors))
```

Output:

```text
Red
Green
Blue
Red
Green
```

Be careful with very large or infinite sources because `cycle()` stores the source values it needs to repeat.

### 37.3 `islice()`

Consumes only a selected portion of an iterable.

```python
from itertools import islice

numbers = (x * x for x in count(1))

print(list(islice(numbers, 5)))
```

Output:

```text
[1, 4, 9, 16, 25]
```

`islice()` is useful for taking a limited number of values from a potentially large or infinite iterator.

### 37.4 `chain()`

Combines multiple iterables sequentially.

```python
from itertools import chain

result = chain([1, 2], [3, 4], [5, 6])

print(list(result))
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

These utilities can simplify many iterator and generator programs.

---

# PART 6: COMMON ERRORS AND IMPORTANT DETAILS

## 38. Error: Calling `next()` on an Iterable

Incorrect:

```python
numbers = [10, 20, 30]

print(next(numbers))
```

This raises `TypeError` because the list is iterable but is not itself an iterator.

Correct:

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
```

Output:

```text
10
```

---

## 39. Error: Calling `next()` After Exhaustion

```python
numbers = iter([1, 2])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

The third call raises `StopIteration`.

Use a `for` loop when you want Python to handle the normal end of iteration.

Alternatively:

```python
numbers = iter([1, 2])

while True:
    value = next(numbers, None)

    if value is None:
        break

    print(value)
```

Output:

```text
1
2
```

This works for these values because `None` is not a possible element in the example. In general, if `None` could be a legitimate value, use a unique sentinel object instead of `None`.

---

## 40. Error: Expecting a Generator to Restart

Incorrect expectation:

```python
gen = (x for x in range(3))

print(list(gen))
print(list(gen))
```

Output:

```text
[0, 1, 2]
[]
```

Create a new generator object when you need to iterate again.

---

## 41. Error: Converting an Infinite Generator to a List

```python
def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1
```

Do not do this:

```python
# list(infinite_numbers())
```

The generator never finishes, so `list()` keeps trying to collect values until resources are exhausted or execution is interrupted.

Consume only the required values:

```python
from itertools import islice

print(list(islice(infinite_numbers(), 5)))
```

Output:

```text
[1, 2, 3, 4, 5]
```

---

## 42. Generator Exceptions and `StopIteration`

When a generator finishes normally, Python signals the end of iteration.

Inside a generator, do not manually raise `StopIteration` to indicate completion. Use `return` or let the function reach its end.

Correct:

```python
def numbers():
    yield 1
    yield 2
    return
```

Raising `StopIteration` directly from inside a generator is transformed into `RuntimeError` under modern Python generator semantics.

The iterator protocol still uses `StopIteration` to communicate that an iterator is exhausted. The important distinction is that a generator function should finish normally rather than manually raise that exception.

---

## 43. Generator Scope and Variable State

Consider:

```python
def counter():
    count = 0

    while count < 3:
        count += 1
        yield count


gen = counter()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
1
2
3
```

The local variable `count` retains its state while the generator is suspended.

This is one of the main benefits of generators compared with manually managing iterator state in a class.

---

# PART 7: PRACTICE PROGRAMS

## 44. Beginner Practice

### Question 1: Convert a list into an iterator

Expected result:

```text
10
20
30
```

### Question 2: Print every character using an iterator

Input:

```text
Python
```

Expected result:

```text
P
y
t
h
o
n
```

### Question 3: Generate numbers from 1 to N

For `N = 5`, expected result:

```text
1
2
3
4
5
```

### Question 4: Generate even numbers

For a limit of `10`, expected result:

```text
2
4
6
8
10
```

### Question 5: Generate squares

For a limit of `5`, expected result:

```text
1
4
9
16
25
```

---

## 45. Intermediate Practice

### Question 6: Create a custom countdown iterator

For a starting number of `5`, expected result:

```text
5
4
3
2
1
```

### Question 7: Generate Fibonacci numbers

For seven values, expected result:

```text
0
1
1
2
3
5
8
```

### Question 8: Generate prime numbers

For a limit of `20`, expected result:

```text
2
3
5
7
11
13
17
19
```

### Question 9: Use a generator expression to find cubes

Expected result:

```text
[1, 8, 27, 64, 125]
```

### Question 10: Read a file line by line using a generator

The generator should yield one line at a time rather than collecting all lines into a list.

---

## 46. Advanced Practice

### Question 11: Create an infinite counter

Produce values indefinitely, but consume only the first ten.

### Question 12: Create an accumulator using `send()`

The generator should maintain a running total as values are sent to it.

### Question 13: Handle an exception using `throw()`

Write a generator that catches `ValueError` and yields a suitable message.

### Question 14: Combine generators using `yield from`

Combine two generators into a single output sequence.

### Question 15: Build a lazy processing pipeline

Create one generator that produces numbers, another that filters even numbers, and another that squares the results.

### Question 16: Explain the output

```python
def demo():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")


gen = demo()

print("D")
print(next(gen))
print("E")
print(next(gen))
```

Expected output:

```text
D
A
10
E
B
20
```

The `"C"` message is not printed because the generator has not been advanced again.

---

# PART 8: QUICK REVISION

## 47. Important Differences

### Iterable versus iterator

An iterable provides an iterator. An iterator produces the next value and tracks progress.

### Iterator versus generator

An iterator follows the iterator protocol. A generator is a type of iterator created using generator machinery, commonly with `yield`.

### `return` versus `yield`

`return` ends a function or generator. `yield` produces a value and suspends a generator so it can resume later.

### List comprehension versus generator expression

A list comprehension creates a list of results. A generator expression produces results lazily as they are consumed.

### `iter()` versus `next()`

`iter()` obtains an iterator. `next()` requests the next value from an iterator.

---

## 48. Important Methods and Functions

| Function or method | Purpose |
|---|---|
| `iter(obj)` | Obtains an iterator |
| `next(it)` | Gets the next value |
| `next(it, default)` | Gets the next value or a default |
| `__iter__()` | Iterator protocol method |
| `__next__()` | Produces the next value |
| `yield` | Produces a value and suspends a generator |
| `yield from` | Delegates iteration |
| `send(value)` | Sends a value into a suspended generator |
| `throw(error)` | Raises an exception inside a suspended generator |
| `close()` | Requests generator termination |
| `itertools.count()` | Produces an arithmetic sequence |
| `itertools.cycle()` | Repeats values |
| `itertools.islice()` | Takes a selected portion of an iterable |
| `itertools.chain()` | Combines iterables sequentially |

---

## 49. Final Summary

Remember these fundamental points:

1. **Iteration** means processing values one at a time.
2. An **iterable** can provide an iterator.
3. An **iterator** produces the next value and tracks progress.
4. `iter()` obtains an iterator.
5. `next()` requests the next value.
6. `StopIteration` signals the end of an iterator.
7. A **generator** is a convenient way to create an iterator.
8. `yield` produces a value and suspends generator execution.
9. Generators preserve their state between requests.
10. Generator expressions provide lazy value generation.
11. Generators can reduce memory use when values are consumed progressively.
12. `yield from`, `send()`, `throw()`, and `close()` support advanced generator behavior.

The most important practical lesson is this: **use a list when you need all results available at once; use a generator when producing values one at a time is more suitable.**

Understanding iterators and generators will help you write clearer Python loops, process files efficiently, and build lazy data-processing pipelines.