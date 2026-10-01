# Python Lists

A **list** is an ordered, mutable collection used to store multiple values in a single object.

Lists are created mainly using square brackets `[]` or the `list()` constructor.

---

## 1. What is a List?

A list can store multiple elements.

```python
numbers = [10, 20, 30, 40]

Here:

numbers → variable
[10, 20, 30, 40] → list object
10, 20, 30, 40 → elements

Check the type:

print(type(numbers))

Output:

<class 'list'>

A list can store multiple values in one object.

2. Creating a List Using []

The most common way to create a list is using square brackets.

numbers = [10, 20, 30]

names = ["Teja", "Ravi", "Kiran"]

marks = [85, 90, 78]

The values inside the square brackets are called elements or items.

3. Creating a List Using list()

Python also provides the built-in list() constructor.

numbers = list()

print(numbers)
print(type(numbers))

Output:

[]
<class 'list'>

list() creates an empty list when no argument is provided.

So:

[]

and:

list()

both create empty lists.

4. Creating a List From an Iterable

list() can also convert an iterable into a list.

For example, a string is iterable:

word = "Python"

letters = list(word)

print(letters)

Output:

['P', 'y', 't', 'h', 'o', 'n']

Each character becomes an element of the list.

5. list() With a Tuple

A tuple can also be converted into a list.

data = (10, 20, 30)

numbers = list(data)

print(numbers)

Output:

[10, 20, 30]

The original tuple is not changed.

A new list is created.

6. list() With a Set

A set can also be converted into a list.

data = {10, 20, 30}

numbers = list(data)

print(numbers)

The result is a list.

The order should not be relied upon because sets are unordered collections.

7. list() With a Dictionary

When a dictionary is passed to list(), its keys are converted into a list.

student = {
    "name": "Teja",
    "age": 21
}

result = list(student)

print(result)

Output:

['name', 'age']

Only the keys are produced.

To get the values:

print(list(student.values()))

To get key-value pairs:

print(list(student.items()))
8. list() With range()

range() is iterable, so it can be converted into a list.

numbers = list(range(1, 6))

print(numbers)

Output:

[1, 2, 3, 4, 5]

Another example:

numbers = list(range(0, 10, 2))

print(numbers)

Output:

[0, 2, 4, 6, 8]

This is a very common use of list().

9. Empty List

A list can contain zero elements.

items = []

print(items)
print(len(items))

Output:

[]
0

The following both create empty lists:

a = []
b = list()
10. Lists Can Store Different Data Types

A list can contain different types of objects.

data = [10, 3.14, "Python", True]

Here:

10 → int
3.14 → float
"Python" → str
True → bool

Example:

print(data)

Output:

[10, 3.14, 'Python', True]

Such a list can be called a heterogeneous list.

11. Lists Can Store Other Objects

A list can contain almost any Python object.

For example:

data = [
    10,
    "Python",
    [1, 2, 3],
    {"name": "Teja"},
    (10, 20)
]

A list can therefore contain other collections as elements.

12. Lists Allow Duplicate Values

Lists can contain duplicate elements.

numbers = [10, 20, 10, 30, 10]

print(numbers)

Output:

[10, 20, 10, 30, 10]

Python does not automatically remove duplicates from a list.

13. Lists Are Ordered

Lists preserve the order of their elements.

numbers = [30, 10, 20]

print(numbers)

Output:

[30, 10, 20]

The list does not automatically become:

[10, 20, 30]

unless you explicitly sort it.

14. Lists Are Mutable

One of the most important properties of lists is mutability.

Mutable means that the contents of an existing list can be changed.

numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)

Output:

[10, 200, 30]

The existing list was modified.

This is different from strings.

text = "Python"

# text[0] = "J"    # TypeError

String:

Immutable

List:

Mutable
15. List Indexing

Each element in a list has an index.

Indexes start from 0.

numbers = [10, 20, 30, 40]

Conceptually:

Element:   10   20   30   40
Index:      0    1    2    3

Example:

print(numbers[0])
print(numbers[2])
print(numbers[3])

Output:

10
30
40
16. Negative Indexing

Negative indexes start from -1.

Element:    10    20    30    40
Positive:    0     1     2     3
Negative:   -4    -3    -2    -1

Example:

numbers = [10, 20, 30, 40]

print(numbers[-1])
print(numbers[-2])

Output:

40
30

-1 always refers to the last element.

17. IndexError

If an index does not exist, Python raises IndexError.

numbers = [10, 20, 30]

print(numbers[5])

There is no index 5.

Python raises:

IndexError: list index out of range

The last valid positive index is:

len(list) - 1
18. List Slicing

Lists support slicing.

Syntax
list[start:stop]

The start index is included.

The stop index is excluded.

Example:

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

Output:

[20, 30, 40]
19. Slicing With Step

Syntax:

list[start:stop:step]

Example:

numbers = [10, 20, 30, 40, 50]

print(numbers[0:5:2])

Output:

[10, 30, 50]
20. Reversing a List Using Slicing
numbers = [10, 20, 30, 40]

print(numbers[::-1])

Output:

[40, 30, 20, 10]

Important:

numbers[::-1]

creates a reversed list.

It does not modify the original list.

21. Adding Elements Using append()

append() adds one element at the end.

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

Output:

[10, 20, 30, 40]
22. append() Adds the Object as One Element

This is important.

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

Output:

[1, 2, [3, 4]]

The entire [3, 4] list becomes one element.

The result has three elements:

1
2
[3, 4]
23. Adding Elements Using insert()

insert() adds an element at a specified index.

Syntax
list.insert(index, value)

Example:

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

Output:

[10, 15, 20, 30]

The element 15 was inserted at index 1.

24. Adding Multiple Elements Using extend()

extend() adds elements from another iterable.

numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)

Output:

[10, 20, 30, 40, 50]
25. append() vs extend()

This is a very important difference.

append()
numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

Result:

[1, 2, [3, 4]]
extend()
numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

Result:

[1, 2, 3, 4]

Remember:

append()  → adds one object
extend()  → adds elements from an iterable
26. List Concatenation Using +

Two lists can be joined using +.

a = [1, 2, 3]
b = [4, 5, 6]

result = a + b

print(result)

Output:

[1, 2, 3, 4, 5, 6]

This creates a new list.

The original lists are not modified.

27. + vs extend()

Both can combine lists, but they behave differently.

+
a = [1, 2]
b = [3, 4]

c = a + b

A new list is created.

extend()
a = [1, 2]
b = [3, 4]

a.extend(b)

The existing a is modified.

So:

+       → creates a new list
extend  → modifies the existing list
28. List Repetition

The * operator repeats a list.

numbers = [1, 2]

print(numbers * 3)

Output:

[1, 2, 1, 2, 1, 2]

It creates a new list.

29. Removing Elements Using remove()

remove() removes the first matching value.

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

Output:

[10, 30, 20]

Only the first 20 is removed.

If the value does not exist:

numbers.remove(100)

Python raises:

ValueError
30. Removing Elements Using pop()

pop() removes an element using its index and returns the removed element.

numbers = [10, 20, 30]

value = numbers.pop()

print(value)
print(numbers)

Output:

30
[10, 20]

Without an index, pop() removes the last element.

31. pop(index)

You can specify an index.

numbers = [10, 20, 30]

value = numbers.pop(1)

print(value)
print(numbers)

Output:

20
[10, 30]
32. remove() vs pop()

Important difference:

remove(value)
    ↓
removes by value
pop(index)
    ↓
removes by index
    ↓
returns removed element

Example:

numbers = [10, 20, 30]

numbers.remove(20)

removes the value 20.

But:

value = numbers.pop(1)

removes whatever is at index 1 and returns it.

33. Removing Everything Using clear()

clear() removes all elements from the existing list.

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

Output:

[]

The list object still exists; it is simply empty.

34. del With Lists

del can remove an element using its index.

numbers = [10, 20, 30]

del numbers[1]

print(numbers)

Output:

[10, 30]

del can also remove a slice:

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

Output:

[10, 50]
35. del vs remove() vs pop() vs clear()
Operation	Works with	Returns removed value?
remove(value)	Value	No
pop(index)	Index	Yes
del list[index]	Index	No
clear()	Entire list	No
36. Membership Operators

Use in and not in to check whether an element exists.

numbers = [10, 20, 30]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)

Output:

True
False
True
37. len() With Lists

len() returns the number of elements.

numbers = [10, 20, 30, 40]

print(len(numbers))

Output:

4

Remember:

Length = number of elements

Last index = length - 1
38. Iterating Through a List

A list can be iterated using a for loop.

numbers = [10, 20, 30]

for number in numbers:
    print(number)

Output:

10
20
30
39. Iterating Using Indexes

You can also use indexes.

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(i, numbers[i])

Output:

0 10
1 20
2 30
40. enumerate() With Lists

enumerate() provides both index and value.

names = ["Teja", "Ravi", "Kiran"]

for index, name in enumerate(names):
    print(index, name)

Output:

0 Teja
1 Ravi
2 Kiran
41. Nested Lists

A list can contain another list.

matrix = [
    [1, 2],
    [3, 4]
]

Access the first inner list:

print(matrix[0])

Output:

[1, 2]

Access an individual element:

print(matrix[0][1])

Output:

2

Here:

matrix[0]     → first inner list
matrix[0][1]  → second element of first inner list
42. Lists Can Have Different Levels of Nesting

Lists can contain lists inside lists.

data = [
    [1, 2],
    [3, [4, 5]]
]

Accessing:

print(data[1][1][0])

Output:

4
43. List Assignment Creates a Reference

Consider:

a = [10, 20, 30]
b = a

b does not create a new list.

Both variables refer to the same list object.

a ─────┐
       ↓
   [10, 20, 30]
       ↑
b ─────┘

Therefore:

a.append(40)

print(a)
print(b)

Output:

[10, 20, 30, 40]
[10, 20, 30, 40]

Changing the list through a is visible through b.

44. copy() Creates a Separate List

Use copy() when you want a separate list.

a = [10, 20, 30]

b = a.copy()

a.append(40)

print(a)
print(b)

Output:

[10, 20, 30, 40]
[10, 20, 30]

Now a and b are separate list objects.

45. list() Can Also Create a Shallow Copy

Another way to copy a list is:

a = [10, 20, 30]

b = list(a)

a.append(40)

print(a)
print(b)

Output:

[10, 20, 30, 40]
[10, 20, 30]

Both:

b = a.copy()

and:

b = list(a)

create a new outer list.

46. a = b vs copy() vs list()
Reference
b = a

Both refer to the same list.

Copy
b = a.copy()

Creates a new outer list.

list()
b = list(a)

Also creates a new outer list.

47. Shallow Copy

copy() and list() create shallow copies.

For a simple list:

a = [10, 20, 30]
b = a.copy()

this usually behaves exactly as expected.

But with nested mutable objects, the inner objects can still be shared.

Example:

a = [[1, 2], [3, 4]]

b = a.copy()

a[0].append(100)

print(a)
print(b)

Output:

[[1, 2, 100], [3, 4]]
[[1, 2, 100], [3, 4]]

Why?

The outer lists are different, but the inner lists are shared.

This is the meaning of a shallow copy.

48. Sorting a List

sort() sorts the existing list.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

Output:

[10, 20, 30, 40]

Descending order:

numbers.sort(reverse=True)

print(numbers)

Output:

[40, 30, 20, 10]
49. sort() Modifies the Original List

sort() changes the existing list.

numbers = [30, 10, 20]

result = numbers.sort()

print(numbers)
print(result)

Output:

[10, 20, 30]
None

This is important:

Many list methods that modify a list return None.

For example:

numbers.append(40)
numbers.sort()
numbers.reverse()
numbers.clear()

These methods modify the list rather than returning a new list.

50. sorted() vs sort()

sorted() is a built-in function.

It returns a new sorted list.

numbers = [30, 10, 20]

result = sorted(numbers)

print(result)
print(numbers)

Output:

[10, 20, 30]
[30, 10, 20]

The original list is unchanged.

Compare:

sort()
    ↓
modifies original list
    ↓
returns None
sorted()
    ↓
creates a new sorted list
    ↓
original remains unchanged
51. reverse() Method vs Reversed Slicing

Using:

numbers.reverse()

modifies the original list.

Using:

numbers[::-1]

creates a new reversed list.

Example:

numbers = [10, 20, 30]

result = numbers[::-1]

print(result)
print(numbers)

Output:

[30, 20, 10]
[10, 20, 30]
52. List Comprehension

List comprehension provides a concise way to create lists.

Example:

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

Output:

[1, 4, 9, 16, 25]

General form:

[expression for item in iterable]
53. List Comprehension With Condition
numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]

print(even)

Output:

[2, 4, 6]

General form:

[expression for item in iterable if condition]
54. List Unpacking

A list can be unpacked into variables.

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

Output:

10
20
30

The number of variables must normally match the number of elements.

55. Extended Unpacking

The * operator can collect multiple elements.

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

Output:

10
[20, 30, 40]
50

Here:

first  → 10
middle → [20, 30, 40]
last   → 50
56. Checking Whether an Object Is a List

Use type():

numbers = [10, 20, 30]

print(type(numbers))

Output:

<class 'list'>

You can also use isinstance():

print(isinstance(numbers, list))

Output:

True

isinstance() is generally more flexible when checking types.

57. Boolean Behavior of Lists

An empty list is considered False.

print(bool([]))

Output:

False

A non-empty list is considered True.

print(bool([10]))

Output:

True

So:

[]          → False
[10]        → True
[False]     → True
[""]        → True

The last two are important.

The list itself is non-empty, so it is truthy even if the element inside is falsy.

58. Lists in if

Because empty lists are falsy, you can write:

numbers = []

if numbers:
    print("List is not empty")
else:
    print("List is empty")

Output:

List is empty

This is commonly used in Python.

59. List Equality

Two lists are equal if their elements are equal and in the same order.

a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)

Output:

True

Order matters:

a = [10, 20, 30]
b = [30, 20, 10]

print(a == b)

Output:

False
60. List Identity

== checks values.

is checks whether two variables refer to the same object.

a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)

Output:

True
False

The values are equal, but they are different list objects.

Now:

a = [10, 20]
b = a

print(a == b)
print(a is b)

Output:

True
True

Both variables refer to the same object.

61. List Methods and Their Return Values

A very important point:

Many list methods modify the existing list and return None.

Examples:

numbers = [10, 20]

result = numbers.append(30)

print(result)

Output:

None

Similarly:

numbers.sort()
numbers.reverse()
numbers.extend([40, 50])
numbers.clear()

These modify the list.

Do not assume that every list method returns the modified list.

62. Important List Methods
Method	Purpose
append(x)	Adds x at the end
extend(iterable)	Adds elements from an iterable
insert(i, x)	Inserts x at index i
remove(x)	Removes first matching x
pop()	Removes and returns last element
pop(i)	Removes and returns element at index i
clear()	Removes all elements
index(x)	Returns index of first x
count(x)	Counts occurrences of x
sort()	Sorts the existing list
reverse()	Reverses the existing list
copy()	Creates a shallow copy
63. Important Characteristics of Lists

Python lists are:

Ordered
Mutable
Indexed
Sliceable
Iterable
Allow duplicate values
Can store different data types
Can contain nested collections
Dynamically sized
Can grow and shrink during execution
64. List vs String

Both strings and lists are sequences.

Both support:

Indexing
Negative indexing
Slicing
Iteration
len()
Membership testing

But they are different.

Feature	String	List
Stores	Characters	Objects/elements
Mutable	No	Yes
Ordered	Yes	Yes
Indexed	Yes	Yes
Duplicates	Yes	Yes
Different types	No	Yes
Created using	Quotes	[] / list()

Example:

text = "Python"
numbers = [10, 20, 30]
65. List vs Tuple

Lists and tuples can both store multiple values.

Feature	List	Tuple
Syntax	[]	()
Mutable	Yes	No
Ordered	Yes	Yes
Indexed	Yes	Yes
Duplicates	Yes	Yes
Different types	Yes	Yes

Example:

numbers_list = [10, 20, 30]
numbers_tuple = (10, 20, 30)

The main difference is mutability.

66. Quick Revision
List
  ↓
Ordered collection
  ↓
Created using [] or list()
  ↓
Can contain multiple elements
  ↓
Can contain different data types
  ↓
Allows duplicates
  ↓
Supports indexing
  ↓
Supports negative indexing
  ↓
Supports slicing
  ↓
Mutable
  ↓
Supports append / extend / insert
  ↓
Supports remove / pop / clear / del
  ↓
Supports iteration
  ↓
Supports nested lists
  ↓
Supports copying
  ↓
Supports list comprehension
  ↓
Supports unpacking
Most Important Concepts
list()
[]
Indexing
Negative indexing
Slicing
Mutability
append()
extend()
insert()
remove()
pop()
clear()
del
sort()
sorted()
reverse()
copy()
Shallow copy
Nested lists
List references
List comprehension
Unpacking
Membership
Truthiness