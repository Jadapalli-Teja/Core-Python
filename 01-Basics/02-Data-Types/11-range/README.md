# Range in Python

`range` is a built-in Python type used to represent a sequence of integers.

It is commonly used with loops.

```python
numbers = range(5)

print(numbers)

# Output:
# range(0, 5)
```

A `range` object does not immediately store all the numbers as a list. It represents the sequence using:

```text
start
stop
step
```

---

## 1. Creating a Range

The simplest form is:

```python
r = range(5)

print(r)

# Output:
# range(0, 5)
```

It represents:

```text
0 1 2 3 4
```

The stop value `5` is **not included**.

---

## 2. `range(stop)`

When one argument is given:

```python
range(stop)
```

Python assumes:

```text
start = 0
step = 1
```

Example:

```python
r = range(5)

print(list(r))

# Output:
# [0, 1, 2, 3, 4]
```

---

## 3. `range(start, stop)`

Two arguments can be provided:

```python
range(start, stop)
```

Example:

```python
r = range(2, 7)

print(list(r))

# Output:
# [2, 3, 4, 5, 6]
```

Again, `stop` is excluded.

---

## 4. `range(start, stop, step)`

Three arguments:

```python
range(start, stop, step)
```

Example:

```python
r = range(2, 10, 2)

print(list(r))

# Output:
# [2, 4, 6, 8]
```

Here:

```text
start = 2
stop  = 10
step  = 2
```

---

## 5. Default Start

With one argument:

```python
range(5)
```

is equivalent to:

```python
range(0, 5)
```

Example:

```python
print(list(range(5)))
print(list(range(0, 5)))

# Output:
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
```

---

## 6. Default Step

If step is not provided, it is `1`.

```python
range(2, 6)
```

is equivalent to:

```python
range(2, 6, 1)
```

---

## 7. Stop Value Is Excluded

This is one of the most important properties of `range`.

```python
print(list(range(1, 5)))

# Output:
# [1, 2, 3, 4]
```

`5` is not included.

So:

```text
range(1, 5)
```

means:

```text
1 <= number < 5
```

---

## 8. Positive Step

A positive step moves forward.

```python
print(list(range(1, 10, 2)))

# Output:
# [1, 3, 5, 7, 9]
```

---

## 9. Negative Step

A negative step moves backward.

```python
print(list(range(10, 0, -2)))

# Output:
# [10, 8, 6, 4, 2]
```

---

## 10. Counting Backwards

```python
print(list(range(5, 0, -1)))

# Output:
# [5, 4, 3, 2, 1]
```

Notice that `0` is excluded.

---

## 11. Step Cannot Be Zero

This is invalid:

```python
range(1, 10, 0)
```

It raises:

```text
ValueError
```

because the step cannot be zero.

---

# Range and Loops

## 12. Using Range with `for`

One of the most common uses of `range()` is with loops.

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

---

## 13. Loop from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

Output:

```text
1
2
3
4
5
6
7
8
9
10
```

---

## 14. Even Numbers

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

---

## 15. Odd Numbers

```python
for i in range(1, 11, 2):
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

# Converting Range

## 16. Range to List

A range object can be converted into a list.

```python
r = range(5)

print(list(r))

# Output:
# [0, 1, 2, 3, 4]
```

---

## 17. Range to Tuple

```python
r = range(5)

print(tuple(r))

# Output:
# (0, 1, 2, 3, 4)
```

---

## 18. Range to Set

```python
r = range(5)

print(set(r))

# Output:
# {0, 1, 2, 3, 4}
```

Set order should not be relied upon.

---

## 19. Range from Negative Numbers

```python
r = range(-5, 0)

print(list(r))

# Output:
# [-5, -4, -3, -2, -1]
```

---

## 20. Range with Negative Start and Positive Step

```python
r = range(-5, 6, 2)

print(list(r))

# Output:
# [-5, -3, -1, 1, 3, 5]
```

---

# Accessing Range Elements

## 21. Indexing

A range supports indexing.

```python
r = range(10, 20)

print(r[0])

# Output:
# 10
```

---

## 22. Positive Indexing

```python
r = range(10, 20)

print(r[2])

# Output:
# 12
```

---

## 23. Negative Indexing

```python
r = range(10, 20)

print(r[-1])

# Output:
# 19
```

---

## 24. Another Negative Index

```python
r = range(10, 20)

print(r[-2])

# Output:
# 18
```

---

## 25. Index Out of Range

```python
r = range(5)

print(r[5])
```

This raises:

```text
IndexError
```

Valid indexes are:

```text
0 1 2 3 4
```

---

# Slicing Range

## 26. Range Slicing

Range supports slicing.

```python
r = range(10)

print(r[2:7])

# Output:
# range(2, 7)
```

The result is another `range` object.

---

## 27. Convert Sliced Range to List

```python
r = range(10)

print(list(r[2:7]))

# Output:
# [2, 3, 4, 5, 6]
```

---

## 28. Slicing with Step

```python
r = range(10)

print(list(r[1:8:2]))

# Output:
# [1, 3, 5, 7]
```

---

## 29. Reverse a Range Using Slicing

```python
r = range(10)

print(list(r[::-1]))

# Output:
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

# Length and Membership

## 30. `len()` with Range

```python
r = range(5)

print(len(r))

# Output:
# 5
```

---

## 31. Length with Start and Stop

```python
r = range(2, 8)

print(len(r))

# Output:
# 6
```

The values are:

```text
2 3 4 5 6 7
```

---

## 32. Membership Using `in`

```python
r = range(1, 10)

print(5 in r)

# Output:
# True
```

---

## 33. Value Not Present

```python
r = range(1, 10)

print(10 in r)

# Output:
# False
```

---

## 34. Membership with Step

```python
r = range(2, 11, 2)

print(6 in r)
print(7 in r)

# Output:
# True
# False
```

---

# Range Properties

## 35. `type()`

```python
r = range(5)

print(type(r))

# Output:
# <class 'range'>
```

---

## 36. `isinstance()`

```python
r = range(5)

print(isinstance(r, range))

# Output:
# True
```

---

## 37. Range Is Iterable

You can loop through a range.

```python
r = range(3)

for value in r:
    print(value)
```

Output:

```text
0
1
2
```

---

## 38. Range Is Not a List

```python
r = range(5)

print(type(r))
print(type(list(r)))

# Output:
# <class 'range'>
# <class 'list'>
```

`range()` creates a range object, not a list.

---

# Range Memory Behavior

## 39. Range Does Not Store Every Number Like a List

Consider:

```python
r = range(1000000000)
```

This does not create a list containing one billion integers.

The range object stores enough information to generate the sequence:

```text
start
stop
step
```

This makes `range` memory efficient.

---

## 40. Range vs List

```python
r = range(1000000)
numbers = list(range(1000000))
```

`r` is a range object.

`numbers` contains all the generated elements in a list.

Therefore, range is usually preferred when you only need to iterate through numbers.

---

# Range Equality

## 41. Equal Ranges

Two range objects can represent the same sequence.

```python
a = range(5)
b = range(0, 5, 1)

print(a == b)

# Output:
# True
```

They represent the same sequence:

```text
0 1 2 3 4
```

---

## 42. Different Ranges

```python
a = range(5)
b = range(1, 5)

print(a == b)

# Output:
# False
```

Their sequences are different.

---

# Range Conversion

## 43. Converting a Range to a String

```python
r = range(5)

print(str(r))

# Output:
# range(0, 5)
```

This does not convert the range into `"01234"`.

It produces its range representation.

---

## 44. Converting String to Range

You cannot directly do:

```python
range("5")
```

This raises a `TypeError`.

Convert the string to an integer first:

```python
r = range(int("5"))

print(list(r))

# Output:
# [0, 1, 2, 3, 4]
```

---

# Practical Examples

## 45. Print Numbers from 1 to 100

```python
for i in range(1, 101):
    print(i)
```

---

## 46. Sum of Numbers

```python
total = 0

for i in range(1, 11):
    total += i

print(total)

# Output:
# 55
```

---

## 47. Multiplication Table

```python
number = 5

for i in range(1, 11):
    print(number, "*", i, "=", number * i)
```

Output:

```text
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
...
5 * 10 = 50
```

---

## 48. Countdown

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

---

## 49. Sum of Even Numbers

```python
total = 0

for i in range(2, 11, 2):
    total += i

print(total)

# Output:
# 30
```

---

## 50. Generate Squares

```python
for i in range(1, 6):
    print(i * i)
```

Output:

```text
1
4
9
16
25
```

---

# Important Points

1. `range` is a built-in Python type.
2. It represents a sequence of integers.
3. `range()` is commonly used with `for` loops.
4. `range(stop)` starts from `0`.
5. The default step is `1`.
6. The stop value is always excluded.
7. A negative step can be used for reverse sequences.
8. Step cannot be `0`.
9. Range supports indexing.
10. Range supports negative indexing.
11. Range supports slicing.
12. Range supports `len()`.
13. Range supports membership testing using `in`.
14. `range()` creates a range object, not a list.
15. Range is memory efficient because it does not store every generated integer as a list.
16. `list(range(...))` creates an actual list.
17. `tuple(range(...))` creates a tuple.
18. A range can have positive or negative start values.
19. A range can use a negative step.
20. `range` objects are immutable.
21. Range values cannot be changed individually.
22. `range` is especially useful for counting and iteration.

---

# Range vs List

| Feature | Range | List |
|---|---|---|
| Type | `range` | `list` |
| Mutable | No | Yes |
| Stores generated elements | No, represents sequence | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| `in` | Yes | Yes |
| Memory efficient for large sequences | Yes | No |
| Can contain arbitrary values | No, integers only | Yes |
| Common use | Loops/counting | General collection |

---

# Time Complexity

For a range object:

| Operation | Complexity |
|---|---:|
| Indexing | O(1) |
| `len()` | O(1) |
| Membership | O(1) |
| Slicing | O(1) |
| Creating range | O(1) |

The important point is that creating a range does not create all its values.

---

# Quick Revision

```text
range(start, stop, step)

            ↓
        start
            ↓
        stop excluded
            ↓
          step
```

Examples:

```python
range(5)
# 0 1 2 3 4

range(2, 6)
# 2 3 4 5

range(2, 10, 2)
# 2 4 6 8

range(10, 0, -2)
# 10 8 6 4 2
```

The most important rule:

```text
range(start, stop, step)
                  ↑
          STOP IS EXCLUDED
```