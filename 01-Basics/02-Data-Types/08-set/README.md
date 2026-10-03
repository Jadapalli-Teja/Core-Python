# Python Sets

A set is an unordered, mutable collection of unique elements in Python.

Sets are created mainly using `{}` or the `set()` constructor.

---

## 1. What is a Set?

A set stores multiple elements, but it does not allow duplicate values.

```python
numbers = {10, 20, 30, 40}

print(numbers)

Output:

{10, 20, 30, 40}

A set has three important properties:

Set
 ↓
Unordered
 ↓
Unique elements
 ↓
Mutable
2. Creating a Set

A set can be created using curly braces {}.

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

Output:

{10, 20, 30, 40}
<class 'set'>
3. Duplicate Values Are Removed

Sets automatically remove duplicate values.

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

Output:

{10, 20, 30, 40}

The duplicate values 10 and 20 occur only once.

4. Empty Set

This is an important point.

empty = {}

This does not create an empty set.

It creates an empty dictionary.

empty = {}

print(type(empty))

Output:

<class 'dict'>

To create an empty set, use:

empty = set()

print(empty)
print(type(empty))

Output:

set()
<class 'set'>
5. Using set()

Python provides the set() constructor.

numbers = set([10, 20, 30])

print(numbers)

Output:

{10, 20, 30}

set() can convert an iterable into a set.

6. List to Set
numbers = [10, 20, 10, 30, 20]

result = set(numbers)

print(result)

Output:

{10, 20, 30}

This is commonly used to remove duplicate values from a list.

7. Tuple to Set
numbers = (10, 20, 10, 30)

result = set(numbers)

print(result)

Output:

{10, 20, 30}
8. String to Set

A string can be converted into a set.

text = "hello"

result = set(text)

print(result)

The result contains unique characters.

The order should not be relied upon.

9. Dictionary to Set

When a dictionary is passed to set(), its keys are used.

student = {
    "name": "Teja",
    "age": 21
}

result = set(student)

print(result)

Output contains:

{'name', 'age'}
10. Set Elements Must Be Hashable

Set elements must be hashable.

These can be stored in a set:

numbers = {10, 20, 30}

Strings can also be stored:

names = {"Teja", "Ravi", "Kiran"}

But a list cannot be a set element:

numbers = {[10, 20]}

This produces:

TypeError

because lists are mutable and unhashable.

11. Different Data Types in a Set

A set can contain different hashable data types.

data = {10, 3.14, "Python", True}

print(data)

The exact display order may vary.

12. Set is Unordered

Sets do not provide positional ordering like lists and tuples.

numbers = {10, 20, 30, 40}

You should not depend on the displayed order.

Therefore, indexing is not supported.

numbers[0]

This produces an error.

A set does not have:

set[0]
set[1]
set[-1]
13. Set Does Not Support Indexing

This is different from lists and tuples.

numbers = {10, 20, 30}

print(numbers[0])

This produces:

TypeError

Use membership operators instead:

print(20 in numbers)
14. Set is Mutable

A set itself can be modified.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

Output contains:

{10, 20, 30, 40}

The set object was modified.

15. add()

add() adds one element to a set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

Output:

{10, 20, 30, 40}
16. Adding an Existing Element

Adding an element that already exists does not create a duplicate.

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)

Output:

{10, 20, 30}
17. update()

update() adds multiple elements.

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)

Output:

{10, 20, 30, 40, 50}

Unlike add(), update() accepts an iterable.

18. add() vs update()
add()

Adds one element.

numbers.add(40)
update()

Adds multiple elements from an iterable.

numbers.update([40, 50, 60])

Important:

numbers = {10, 20}

numbers.add((30, 40))

This adds the tuple as one element.

But:

numbers = {10, 20}

numbers.update((30, 40))

This adds 30 and 40 separately.

19. remove()

remove() deletes an element.

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

Output contains:

{10, 30}

If the element does not exist, remove() raises:

KeyError
20. discard()

discard() also removes an element.

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)

The important difference is:

remove()  → error if element does not exist
discard() → no error if element does not exist

Example:

numbers = {10, 20, 30}

numbers.discard(100)

print(numbers)

No error occurs.

21. pop()

pop() removes and returns an arbitrary set element.

numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)

The exact element removed should not be relied upon.

Unlike a list:

list.pop(index)

set pop() does not accept an index.

22. clear()

clear() removes all elements.

numbers = {10, 20, 30}

numbers.clear()

print(numbers)

Output:

set()
23. del With Set

You can delete the entire set variable.

numbers = {10, 20, 30}

del numbers

But individual elements should be removed using:

remove()
discard()
pop()
24. Membership

Membership checking is one of the main uses of sets.

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 in numbers)

Output:

True
False

Sets are especially useful for fast membership checking.

Average-case complexity:

x in set → O(1)
25. not in
numbers = {10, 20, 30}

print(50 not in numbers)
print(20 not in numbers)

Output:

True
False
26. Set Union

Union combines elements from both sets.

Use:

|

Example:

a = {10, 20, 30}
b = {30, 40, 50}

result = a | b

print(result)

Output:

{10, 20, 30, 40, 50}

Duplicates are automatically removed.

27. union()

The same operation can be performed using union().

a = {10, 20, 30}
b = {30, 40, 50}

result = a.union(b)

print(result)

Output:

{10, 20, 30, 40, 50}

union() creates a new set.

28. Set Intersection

Intersection returns elements common to both sets.

Use:

&

Example:

a = {10, 20, 30}
b = {20, 30, 40}

result = a & b

print(result)

Output:

{20, 30}
29. intersection()

The same operation can be performed using intersection().

a = {10, 20, 30}
b = {20, 30, 40}

result = a.intersection(b)

print(result)

Output:

{20, 30}
30. Set Difference

Difference returns elements present in the first set but not the second.

Use:

-

Example:

a = {10, 20, 30}
b = {20, 30, 40}

result = a - b

print(result)

Output:

{10}

The order matters.

a - b

is not necessarily the same as:

b - a
31. difference()

The same operation can be performed using difference().

a = {10, 20, 30}
b = {20, 30, 40}

result = a.difference(b)

print(result)

Output:

{10}
32. Symmetric Difference

Symmetric difference returns elements that belong to either set, but not both.

Use:

^

Example:

a = {10, 20, 30}
b = {20, 30, 40}

result = a ^ b

print(result)

Output:

{10, 40}
33. symmetric_difference()
a = {10, 20, 30}
b = {20, 30, 40}

result = a.symmetric_difference(b)

print(result)

Output:

{10, 40}
34. Subset

A set is a subset if all of its elements are present in another set.

Use:

<=

Example:

a = {10, 20}
b = {10, 20, 30, 40}

print(a <= b)

Output:

True

You can also use:

a.issubset(b)
35. Proper Subset

Use < to check whether a set is a proper subset.

a = {10, 20}
b = {10, 20, 30}

print(a < b)

Output:

True

A proper subset must be smaller than the other set.

36. Superset

A set is a superset if it contains all elements of another set.

Use:

>=

Example:

a = {10, 20, 30, 40}
b = {10, 20}

print(a >= b)

Output:

True

You can also use:

a.issuperset(b)
37. Proper Superset

Use > to check for a proper superset.

a = {10, 20, 30}
b = {10, 20}

print(a > b)

Output:

True
38. Disjoint Sets

Two sets are disjoint if they have no common elements.

a = {10, 20}
b = {30, 40}

print(a.isdisjoint(b))

Output:

True

If they have a common element:

a = {10, 20}
b = {20, 30}

print(a.isdisjoint(b))

Output:

False
39. Set Operation Summary

For:

a = {1, 2, 3}
b = {3, 4, 5}
Operation	Operator	Result
Union	a | b	{1,2,3,4,5}
Intersection	a & b	{3}
Difference	a - b	{1,2}
Difference	b - a	{4,5}
Symmetric difference	a ^ b	{1,2,4,5}
40. Iterating Through a Set

A set can be used in a for loop.

numbers = {10, 20, 30}

for number in numbers:
    print(number)

The order should not be relied upon.

41. len() With Set

len() returns the number of unique elements.

numbers = {10, 20, 30, 40}

print(len(numbers))

Output:

4
42. Set Cannot Contain a List

This is invalid:

numbers = {[10, 20], [30, 40]}

It produces:

TypeError

because lists are unhashable.

43. Set Can Contain a Tuple

A tuple containing hashable elements can be stored inside a set.

points = {(10, 20), (30, 40)}

print(points)

This works because tuples containing integers are hashable.

44. Set Cannot Contain a Dictionary

Dictionaries are mutable and unhashable.

data = {{"name": "Teja"}}

This produces:

TypeError
45. Set of Boolean and Integer Values

An important Python behavior:

data = {True, 1, False, 0}

print(data)

True and 1 are considered equal.

Similarly:

False == 0
True == 1

Therefore they do not behave as four completely separate set elements.

46. set() With a String

set() breaks a string into unique characters.

text = "banana"

result = set(text)

print(result)

The result contains:

{'b', 'a', 'n'}

Order may vary.

47. Removing Duplicates From a List

One common use of a set is removing duplicates.

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)

The values become unique.

However, the original order should not be relied upon.

48. Set vs List
Feature	Set	List
Ordered	No	Yes
Mutable	Yes	Yes
Duplicates	No	Yes
Indexing	No	Yes
Slicing	No	Yes
add()	Yes	No
append()	No	Yes
Fast membership	Yes	Slower generally
Union	Yes	No
Intersection	Yes	No
Difference	Yes	No
49. Set vs Tuple
Feature	Set	Tuple
Ordered	No	Yes
Mutable	Yes	No
Duplicates	No	Yes
Indexing	No	Yes
Slicing	No	Yes
Hashable	Yes	If all elements are hashable
add()	Yes	No
count()	No	Yes
index()	No	Yes
50. Set Time Complexity

Average-case complexity:

Operation	Time Complexity
Add	O(1)
Remove	O(1)
Discard	O(1)
Membership	O(1)
Length	O(1)
Union	O(n + m)
Intersection	O(min(n, m))
Difference	O(n)
Iteration	O(n)

Worst-case hash-table behavior can differ, but these are the usual average-case complexities.

51. Important Set Properties

A set is:

Unordered
Mutable
Collection of unique elements
Not indexable
Not sliceable
Iterable
Hash-based
Supports fast membership testing
Supports union
Supports intersection
Supports difference
Supports symmetric difference
Supports subset and superset operations
Can contain only hashable elements
Does not allow duplicate elements
52. Quick Revision
Set
 ↓
Unordered collection
 ↓
Unique elements
 ↓
Mutable
 ↓
Created using {}
 ↓
Empty set → set()
 ↓
No indexing
 ↓
No slicing
 ↓
Fast membership checking
 ↓
Supports add(), update()
 ↓
Supports remove(), discard(), pop(), clear()
 ↓
Supports union
 ↓
Supports intersection
 ↓
Supports difference
 ↓
Supports symmetric difference
Important Examples
{}                  # Empty dictionary

set()               # Empty set

{10, 20, 30}        # Set

set([10, 20, 10])   # List → Set

set("hello")        # String → Set

a | b               # Union

a & b               # Intersection

a - b               # Difference

a ^ b               # Symmetric difference
Most Important Point

A set stores unique hashable elements and is mainly useful when you need fast membership checking or mathematical set operations.