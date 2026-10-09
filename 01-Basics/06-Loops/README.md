# Loops in Python

## 1. What is a Loop?

A loop is used to execute a block of code repeatedly.

Normally, Python executes statements one after another. When we need to perform the same task multiple times, we can use a loop instead of writing the same code repeatedly.

Example without a loop:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Output:

```text
1
2
3
4
5
```

The same program can be written using a loop:

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

Both programs produce the same output, but the loop version is shorter and easier to maintain.

**Important:** A loop repeats a block of code while iterating over a sequence or while a condition remains true.

---

## 2. Why Do We Need Loops?

Loops are useful when we need to:

- Print numbers from 1 to 100.
- Calculate the sum of numbers.
- Display multiplication tables.
- Traverse strings, lists, tuples, sets, and dictionaries.
- Find maximum or minimum values.
- Count occurrences of elements.
- Perform repeated calculations.
- Solve pattern-printing problems.
- Process records from files or databases.

For example, printing 1,000 numbers manually would require many statements. A loop can do the same job with only a few lines.

---

## 3. Types of Loops in Python

Python provides two main loop statements:

1. `for` loop
2. `while` loop

Other important loop-related statements are:

- `break`
- `continue`
- `pass`

We can also use nested loops, where one loop is placed inside another loop.

---

# Part 1: The `for` Loop

## 4. What Is a `for` Loop?

A `for` loop iterates over the items of an iterable, such as a string, list, tuple, set, dictionary, or range.

### Syntax

```python
for variable in iterable:
    statement
```

Here:

- `for` starts the loop.
- `variable` receives the current item.
- `in` connects the variable to the iterable.
- `iterable` supplies items one at a time.
- The indented statements form the loop body.

Example:

```python
for i in range(1, 4):
    print(i)
```

Output:

```text
1
2
3
```

---

## 5. How a `for` Loop Executes

Consider:

```python
for i in range(1, 4):
    print(i)
```

`range(1, 4)` produces the values `1`, `2`, and `3`.

Execution:

| Iteration | Value of `i` | Output |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |

The execution flow is:

```text
Start loop
    ↓
Get next value from range
    ↓
Assign value to i
    ↓
Execute print(i)
    ↓
Get next value
    ↓
No more values?
    ├── No → Repeat
    └── Yes → Exit loop
```

The loop body executes once for each item.

---

## 6. The `range()` Function

`range()` is commonly used with `for` loops to generate a sequence of integers.

It does not create a list of all those integers immediately. It represents a range of values that can be iterated over.

### Form 1: `range(stop)`

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

The starting value defaults to `0`, and the stop value is excluded.

### Form 2: `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
```

Output:

```text
2
3
4
5
```

### Form 3: `range(start, stop, step)`

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

The `step` determines how much the value changes each time.

### Negative step

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

**Important points:**

- The stop value is excluded.
- The step cannot be zero.
- A positive step normally counts upward.
- A negative step normally counts downward.
- The start, stop, and step must be integers.

---

## 7. Printing Numbers

### Print numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

### Print even numbers from 2 to 20

```python
for i in range(2, 21, 2):
    print(i)
```

### Print odd numbers from 1 to 19

```python
for i in range(1, 20, 2):
    print(i)
```

### Print numbers in reverse order

```python
for i in range(10, 0, -1):
    print(i)
```

---

## 8. Using a `for` Loop with a String

A string is iterable. A loop can process its characters one by one.

```python
name = "PYTHON"

for ch in name:
    print(ch)
```

Output:

```text
P
Y
T
H
O
N
```

Execution:

```text
name = "PYTHON"
       ↓
First character  → P
Second character → Y
Third character  → T
Fourth character → H
Fifth character  → O
Sixth character  → N
       ↓
Loop ends
```

Example: count vowels.

```python
text = "education"
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print(count)
```

Output:

```text
5
```

The variable `count` increases whenever the current character is a vowel.

---

## 9. Using a `for` Loop with a List

A list stores multiple items and is iterable.

```python
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)
```

Output:

```text
10
20
30
40
```

### Calculate the sum of list elements

```python
numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print(total)
```

Output:

```text
100
```

Step-by-step:

| Current number | Previous total | New total |
|---:|---:|---:|
| 10 | 0 | 10 |
| 20 | 10 | 30 |
| 30 | 30 | 60 |
| 40 | 60 | 100 |

The statement:

```python
total += num
```

is equivalent to:

```python
total = total + num
```

---

## 10. Using a `for` Loop with a Dictionary

By default, iterating over a dictionary gives its keys.

```python
student = {
    "name": "Teja",
    "age": 21,
    "marks": 85
}

for key in student:
    print(key)
```

Output:

```text
name
age
marks
```

### Iterate over values

```python
for value in student.values():
    print(value)
```

### Iterate over keys and values

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Teja
age 21
marks 85
```

---

## 11. The `enumerate()` Function

When iterating over a sequence, sometimes we need both the index and the value.

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 apple
1 banana
2 mango
```

To start the index from `1`:

```python
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Output:

```text
1 apple
2 banana
3 mango
```

`enumerate()` is generally clearer than manually maintaining an index counter.

---

# Part 2: The `while` Loop

## 12. What Is a `while` Loop?

A `while` loop repeats a block of code as long as its condition evaluates to true.

### Syntax

```python
while condition:
    statement
```

Example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

Unlike a `for` loop over a range, a `while` loop is controlled by a condition.

---

## 13. How a `while` Loop Executes

Consider:

```python
i = 1

while i <= 3:
    print(i)
    i += 1
```

Execution:

| Step | Value of `i` before check | Condition `i <= 3` | Action |
|---|---:|---|---|
| 1 | 1 | True | Print 1, then set `i = 2` |
| 2 | 2 | True | Print 2, then set `i = 3` |
| 3 | 3 | True | Print 3, then set `i = 4` |
| 4 | 4 | False | Exit loop |

Output:

```text
1
2
3
```

The important point is that Python checks the condition before each iteration.

---

## 14. Why Must We Update the Variable?

Consider:

```python
i = 1

while i <= 5:
    print(i)
```

This produces:

```text
1
1
1
1
...
```

The loop never finishes because `i` remains `1`, so the condition remains true.

Correct version:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Always check whether a `while` loop can eventually reach a false condition or exit using a control statement.

---

## 15. A `while` Loop May Execute Zero Times

If the condition is false at the beginning, the body does not execute.

```python
i = 10

while i < 5:
    print(i)
```

Output:

```text
```

There is no output because `10 < 5` is false.

This is called a **zero-iteration loop**.

---

## 16. Practical `while` Loop Programs

### Print numbers from 1 to 10

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

### Print even numbers from 2 to 10

```python
i = 2

while i <= 10:
    print(i)
    i += 2
```

### Countdown

```python
i = 5

while i >= 1:
    print(i)
    i -= 1

print("Go!")
```

Output:

```text
5
4
3
2
1
Go!
```

### Sum of numbers from 1 to `n`

```python
n = int(input("Enter n: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum:", total)
```

Input:

```text
5
```

Output:

```text
Sum: 15
```

---

# Part 3: `for` Loop vs `while` Loop

## 17. Main Differences

| `for` loop | `while` loop |
|---|---|
| Iterates over an iterable | Repeats while a condition is true |
| Commonly used for sequences and collections | Commonly used for condition-controlled repetition |
| Often needs less manual counter management | Often requires manual condition updates |
| Can iterate over strings, lists, tuples, dictionaries, and ranges | Can also process these, but usually needs explicit control |
| Usually ends when the iterable is exhausted | Ends when the condition becomes false or control exits |

Both loops can solve many of the same problems.

Example using `for`:

```python
for i in range(1, 6):
    print(i)
```

Equivalent using `while`:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# Part 4: Loop Control Statements

## 18. The `break` Statement

`break` immediately terminates the nearest enclosing loop.

Example:

```python
for i in range(1, 10):
    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

Execution:

```text
i = 1 → print
i = 2 → print
i = 3 → print
i = 4 → print
i = 5 → break
         ↓
      Exit loop
```

When `i == 5`, Python exits the loop without printing `5`.

### Find a number and stop

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for num in numbers:
    if num == target:
        print("Found")
        break
```

Output:

```text
Found
```

---

## 19. The `continue` Statement

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

Execution:

```text
i = 1 → print 1
i = 2 → print 2
i = 3 → continue; skip print
i = 4 → print 4
i = 5 → print 5
```

The loop does not terminate at `3`. Only that iteration's remaining body is skipped.

### Print only odd numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
5
7
9
```

---

## 20. `break` vs `continue`

| `break` | `continue` |
|---|---|
| Terminates the nearest enclosing loop | Skips the current iteration |
| No more iterations of that loop occur | The next iteration may occur |
| Useful when a result is found or a stop condition is met | Useful when certain items should be skipped |

Remember:

```text
break     → exit loop
continue  → skip current iteration
```

---

## 21. The `pass` Statement

`pass` does nothing. It is used when Python requires a statement but you want to leave the block empty temporarily.

```python
for i in range(1, 4):
    pass

print("Loop completed")
```

Output:

```text
Loop completed
```

Unlike `break` and `continue`, `pass` does not alter the loop's execution flow.

---

# Part 5: Nested Loops

## 22. What Is a Nested Loop?

A nested loop is a loop inside another loop.

Example:

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

Output:

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

The outer loop controls `i`. For every value of `i`, the inner loop runs through all its values of `j`.

---

## 23. Nested Loop Execution

For:

```python
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)
```

Execution:

```text
Outer loop: i = 1
    Inner loop:
        j = 1 → print(1, 1)
        j = 2 → print(1, 2)
        j = 3 → print(1, 3)

Outer loop: i = 2
    Inner loop:
        j = 1 → print(2, 1)
        j = 2 → print(2, 2)
        j = 3 → print(2, 3)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

The inner loop completes all its iterations for each iteration of the outer loop.

---

## 24. How Many Times Does a Nested Loop Execute?

```python
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
```

The outer loop executes `3` times.

The inner loop executes `4` times for every outer iteration.

Total executions of the inner body:

\[
3 \times 4 = 12
\]

For two simple nested loops with fixed iteration counts, multiply their iteration counts to find the total number of inner-body executions.

---

# Part 6: Pattern Programs

## 25. Square Pattern

```python
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
```

Output:

```text
* * * *
* * * *
* * * *
* * * *
```

Explanation:

- The outer loop controls the rows.
- The inner loop prints four stars in each row.
- `end=" "` keeps stars on the same line.
- The empty `print()` moves to the next line.

---

## 26. Right-Angled Triangle

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output:

```text
*
* *
* * *
* * * *
```

The number of stars increases with each row.

| Row (`i`) | Number of stars |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |

---

## 27. Inverted Triangle

```python
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output:

```text
* * * *
* * *
* *
*
```

The outer loop decreases from `4` to `1`.

---

## 28. Number Triangle

```python
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
```

The inner loop prints numbers from `1` through the current row number.

---

## 29. Repeated Number Triangle

```python
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
```

Output:

```text
1
2 2
3 3 3
4 4 4 4
```

Here, the printed value is `i`, not `j`.

---

# Part 7: Important Loop Programs

## 30. Sum of Numbers from 1 to `n`

```python
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)
```

Input:

```text
5
```

Output:

```text
Sum: 15
```

For `n = 5`:

\[
1 + 2 + 3 + 4 + 5 = 15
\]

---

## 31. Factorial of a Number

The factorial of a non-negative integer \(n\) is the product of all integers from `1` through `n`.

\[
n! = 1 \times 2 \times 3 \times \cdots \times n
\]

By definition:

\[
0! = 1
\]

Program:

```python
n = int(input("Enter a non-negative integer: "))
factorial = 1

if n < 0:
    print("Factorial is not defined for negative integers")
else:
    for i in range(1, n + 1):
        factorial *= i

    print("Factorial:", factorial)
```

Input:

```text
5
```

Output:

```text
Factorial: 120
```

---

## 32. Multiplication Table

```python
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

Input:

```text
5
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

---

## 33. Count Digits in an Integer

For a positive integer, repeatedly divide by `10` using floor division to remove its last digit.

```python
n = int(input("Enter an integer: "))
number = abs(n)
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10
        count += 1

print("Digits:", count)
```

Input:

```text
12345
```

Output:

```text
Digits: 5
```

`abs()` allows the program to count digits of negative integers too. The minus sign is not counted as a digit.

---

## 34. Reverse an Integer

```python
n = int(input("Enter an integer: "))
number = abs(n)
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if n < 0:
    reverse = -reverse

print("Reverse:", reverse)
```

Input:

```text
1234
```

Output:

```text
Reverse: 4321
```

The key operations are:

- `number % 10` gets the last digit.
- `reverse * 10 + digit` appends that digit to the reversed number.
- `number // 10` removes the last digit.

Note: leading zeros in a reversed number are not preserved when the result is stored as an integer.

---

## 35. Check Whether a Number Is Prime

A prime number is an integer greater than `1` with exactly two positive divisors: `1` and itself.

```python
n = int(input("Enter a number: "))

if n < 2:
    print("Not prime")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")
```

Input:

```text
17
```

Output:

```text
Prime
```

Why do we only check up to the square root?

If a number has a factor greater than its square root, it must also have a corresponding factor smaller than its square root. Therefore, checking up to the square root is sufficient.

---

## 36. Fibonacci Series

The Fibonacci sequence begins with `0` and `1`. Each subsequent value is the sum of the previous two.

```python
n = int(input("How many terms? "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

Input:

```text
7
```

Output:

```text
0 1 1 2 3 5 8
```

---

## 37. Find the Largest Element in a List

```python
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
```

Output:

```text
Largest: 89
```

The variable `largest` keeps track of the largest value found so far.

This example assumes that the list is non-empty.

---

## 38. Count Even and Odd Numbers

```python
numbers = [10, 15, 20, 25, 30, 35]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)
```

Output:

```text
Even: 3
Odd: 3
```

---

# Part 8: Loop `else`

## 39. The `else` Block in a Loop

Python supports `else` with both `for` and `while` loops.

The `else` block runs when the loop finishes normally, without being terminated by `break`.

Example:

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
Loop completed
```

### What happens when `break` is used?

```python
for i in range(5):
    if i == 3:
        break

    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
```

The `else` block does not execute because the loop was terminated by `break`.

**Important:** A loop's `else` is not the same as an `if-else`. It indicates normal loop completion, not whether an `if` condition was false.

---

## 40. Practical Use of Loop `else`: Prime Search

```python
n = int(input("Enter a number: "))

if n < 2:
    print("Not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
```

If a divisor is found, `break` stops the loop. If no divisor is found and the loop completes normally, the `else` block prints `"Prime"`.

---

# Part 9: Common Loop Mistakes

## 41. Off-by-One Errors

Wrong:

```python
for i in range(1, 5):
    print(i)
```

This prints `1` through `4`, not `5`.

Correct:

```python
for i in range(1, 6):
    print(i)
```

Remember that `range()` excludes the stop value.

## 42. Infinite `while` Loops

Wrong:

```python
i = 1

while i <= 5:
    print(i)
```

The value of `i` never changes.

Correct:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

## 43. Incorrect Indentation

Wrong:

```python
for i in range(3):
print(i)
```

Correct:

```python
for i in range(3):
    print(i)
```

## 44. Confusing `break` and `continue`

- `break` terminates the nearest enclosing loop.
- `continue` skips the current iteration.
- `pass` does nothing.

## 45. Accidentally Resetting an Accumulator

Wrong:

```python
numbers = [10, 20, 30]

for num in numbers:
    total = 0
    total += num

print(total)
```

Output:

```text
30
```

The total is reset during every iteration.

Correct:

```python
numbers = [10, 20, 30]
total = 0

for num in numbers:
    total += num

print(total)
```

Output:

```text
60
```

Initialize counters and totals **before** the loop when you want to accumulate results across iterations.

---

# Part 10: Time Complexity of Loops

## 46. One Loop

```python
for i in range(n):
    print(i)
```

The body executes approximately `n` times.

Time complexity: \(O(n)\), assuming the body performs constant-time work.

## 47. Two Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The inner body executes \(n \times n\) times.

Time complexity: \(O(n^2)\).

## 48. Consecutive Loops

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Each loop executes `n` times, for approximately `2n` total iterations.

Time complexity: \(O(n)\), because constant factors are ignored in Big-O notation.

## 49. Repeated Halving

```python
while n > 1:
    n //= 2
```

The value of `n` is approximately halved each time.

Time complexity: \(O(\log n)\) for positive integer `n`.

These are common patterns in coding interviews.

---

# Part 11: Practice Problems

Try solving these without looking at the solutions first.

### Beginner

1. Print numbers from `1` to `50`.
2. Print all even numbers from `1` to `100`.
3. Find the sum of numbers from `1` to `n`.
4. Print the multiplication table of a number.
5. Count the digits of an integer.
6. Reverse an integer.
7. Find the factorial of a number.
8. Count vowels in a string.
9. Find the largest element in a list.
10. Count even and odd elements in a list.

### Intermediate

11. Check whether a number is prime.
12. Print all prime numbers in a given range.
13. Generate the Fibonacci series.
14. Check whether an integer is a palindrome.
15. Calculate the sum of digits of an integer.
16. Find the second-largest distinct element in a list.
17. Remove duplicates from a list while preserving order.
18. Count the frequency of each character in a string.
19. Print a right-angled star triangle.
20. Print an inverted number triangle.

### Loop control and nested loops

21. Print numbers from `1` to `20`, skipping multiples of `3`.
22. Search a list and stop as soon as the target is found.
23. Print all pairs from two lists.
24. Print a square star pattern.
25. Print a multiplication table from `1` to `10`.

---

# Final Quick Revision

| Concept | Main purpose |
|---|---|
| `for` | Iterates over an iterable |
| `while` | Repeats while a condition is true |
| `range()` | Represents a range of integers |
| `break` | Exits the nearest enclosing loop |
| `continue` | Skips the current iteration |
| `pass` | Does nothing |
| Nested loop | Places one loop inside another |
| Loop `else` | Runs after normal completion without `break` |
| `enumerate()` | Provides index and value |
| `+=` | Updates an accumulator or counter |

## Final mental model

```text
for loop:
Iterable → next item → execute body → repeat → finish

while loop:
Check condition → execute body → check again → finish when false

break:
Exit loop immediately

continue:
Skip the rest of this iteration

pass:
Do nothing

Nested loops:
The inner loop runs for each iteration of the outer loop
```

**One-line definition:** A loop is a control-flow structure that repeatedly executes a block of code by iterating over an iterable or checking a condition.