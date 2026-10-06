# Bytearray (`bytearray`) Data Type in Python

## 1. What is Bytearray?

The **`bytearray`** data type is used to store a sequence of bytes, just like `bytes`.

The main difference is:

```text
bytes     → Immutable
bytearray → Mutable
```

A `bytearray` contains integer values from:

```text
0 to 255
```

Example:

```python
data = bytearray(b"Python")

print(data)
```

**Output:**

```text
bytearray(b'Python')
```

A `bytearray` is mainly useful when binary data needs to be **modified after it is created**.

It is commonly used with:

- Binary files
- Network data
- Protocols
- Data processing
- Low-level programming
- Mutable binary buffers

---

# 2. What is a Byte?

A byte contains **8 bits**.

```text
1 byte = 8 bits
```

The possible values of one byte are:

```text
0 to 255
```

For example:

```text
0
1
2
...
254
255
```

Therefore, a `bytearray` can contain values only in this range.

Example:

```python
data = bytearray([65, 66, 67])

print(data)
```

**Output:**

```text
bytearray(b'ABC')
```

Because:

```text
65 → A
66 → B
67 → C
```

---

# 3. Creating a Bytearray

There are several ways to create a `bytearray`.

### Using a bytes object

```python
data = bytearray(b"Python")

print(data)
```

Output:

```text
bytearray(b'Python')
```

---

### Using a list of integers

```python
data = bytearray([65, 66, 67])

print(data)
```

Output:

```text
bytearray(b'ABC')
```

---

### Using `bytearray()`

```python
data = bytearray()

print(data)
```

Output:

```text
bytearray(b'')
```

This creates an empty bytearray.

---

# 4. Type of Bytearray

Use `type()`:

```python
data = bytearray(b"Python")

print(type(data))
```

Output:

```text
<class 'bytearray'>
```

Using `isinstance()`:

```python
print(isinstance(data, bytearray))
```

Output:

```text
True
```

---

# 5. Bytearray Literal

Unlike `bytes`, Python does **not** have a special literal such as:

```python
b"Python"
```

for directly creating a bytearray.

This:

```python
b"Python"
```

creates a `bytes` object.

To create a bytearray:

```python
bytearray(b"Python")
```

Example:

```python
data = bytearray(b"Python")

print(type(data))
```

Output:

```text
<class 'bytearray'>
```

---

# 6. Bytearray Contains Integer Values

A bytearray stores byte values from `0` to `255`.

Example:

```python
data = bytearray([65, 66, 67])

print(data[0])
print(data[1])
print(data[2])
```

Output:

```text
65
66
67
```

So internally:

```text
bytearray(b"ABC")
        ↓
[65, 66, 67]
```

---

# 7. ASCII and Bytearray

For common English characters, byte values correspond to ASCII values.

Example:

```python
data = bytearray(b"ABC")

print(data[0])
print(data[1])
print(data[2])
```

Output:

```text
65
66
67
```

Some common values:

| Character | Value |
|---|---:|
| `A` | 65 |
| `B` | 66 |
| `C` | 67 |
| `a` | 97 |
| `b` | 98 |
| `0` | 48 |
| `1` | 49 |
| Space | 32 |

---

# 8. The Most Important Feature: Mutable

The biggest difference between `bytes` and `bytearray` is **mutability**.

A bytearray can be modified after creation.

Example:

```python
data = bytearray(b"Python")

data[0] = 74

print(data)
```

Output:

```text
bytearray(b'Jython')
```

Why?

Originally:

```text
P → 80
```

We changed the first byte to:

```text
74 → J
```

Therefore:

```text
Python
  ↓
Jython
```

---

# 9. Modifying Individual Bytes

You can change any individual byte using its index.

```python
data = bytearray(b"ABC")

data[0] = 88
data[1] = 89
data[2] = 90

print(data)
```

Output:

```text
bytearray(b'XYZ')
```

Because:

```text
88 → X
89 → Y
90 → Z
```

---

# 10. Valid Values When Modifying

When assigning a value to a bytearray element, the value must be between:

```text
0 and 255
```

Valid:

```python
data = bytearray(b"ABC")

data[0] = 100

print(data)
```

Output:

```text
bytearray(b'dBC')
```

Invalid:

```python
data[0] = 256
```

This raises:

```text
ValueError
```

Similarly:

```python
data[0] = -1
```

also raises:

```text
ValueError
```

So remember:

```text
0 <= byte value <= 255
```

---

# 11. Bytes vs Bytearray

This is one of the most important interview concepts.

### `bytes`

```python
data = b"ABC"
```

Immutable.

You cannot do:

```python
data[0] = 90
```

It raises `TypeError`.

### `bytearray`

```python
data = bytearray(b"ABC")
```

Mutable.

You can do:

```python
data[0] = 90
```

Result:

```text
bytearray(b'ZBC')
```

### Main difference

```text
bytes
   ↓
Immutable

bytearray
   ↓
Mutable
```

---

# 12. Reassignment vs Modification

Remember the difference.

### Reassignment

```python
data = bytearray(b"Python")

data = bytearray(b"Java")
```

The variable now refers to another object.

### Modification

```python
data = bytearray(b"Python")

data[0] = 74
```

The existing bytearray itself is changed.

This is possible because bytearray is mutable.

---

# 13. Indexing

Bytearray supports indexing.

```python
data = bytearray(b"Python")

print(data[0])
print(data[1])
print(data[2])
```

Output:

```text
80
121
116
```

Remember:

```text
bytearray indexing → integer
```

Not a one-character bytearray.

---

# 14. Positive Indexing

For:

```python
data = bytearray(b"Python")
```

indexes are:

```text
Character: P   y   t   h   o   n
Index:     0   1   2   3   4   5
```

Example:

```python
print(data[0])
print(data[5])
```

Output:

```text
80
110
```

---

# 15. Negative Indexing

Bytearray supports negative indexing.

```python
data = bytearray(b"Python")

print(data[-1])
print(data[-2])
```

Output:

```text
110
111
```

Because:

```text
n → 110
o → 111
```

Index structure:

```text
 P    y    t    h    o    n
 0    1    2    3    4    5
-6   -5   -4   -3   -2   -1
```

---

# 16. Slicing

Bytearray supports slicing.

```python
data = bytearray(b"Python")

print(data[0:3])
```

Output:

```text
bytearray(b'Pyt')
```

Another example:

```python
print(data[2:5])
```

Output:

```text
bytearray(b'tho')
```

---

# 17. Slice Returns a New Bytearray

Example:

```python
data = bytearray(b"Python")

part = data[0:3]

print(part)
print(type(part))
```

Output:

```text
bytearray(b'Pyt')
<class 'bytearray'>
```

The result of slicing a bytearray is another `bytearray`.

---

# 18. Slicing with Step

```python
data = bytearray(b"Python")

print(data[::2])
```

Output:

```text
bytearray(b'Pto')
```

Indexes used:

```text
0 → P
2 → t
4 → o
```

---

# 19. Reverse Bytearray

Use a negative step:

```python
data = bytearray(b"Python")

print(data[::-1])
```

Output:

```text
bytearray(b'nohtyP')
```

---

# 20. Length

Use `len()`:

```python
data = bytearray(b"Python")

print(len(data))
```

Output:

```text
6
```

The result represents the number of bytes.

---

# 21. Empty Bytearray

You can create an empty bytearray:

```python
data = bytearray()

print(data)
print(len(data))
```

Output:

```text
bytearray(b'')
0
```

You can also write:

```python
data = bytearray(b"")
```

Both represent an empty bytearray.

---

# 22. Bytearray Truthiness

An empty bytearray is falsy:

```python
data = bytearray()

print(bool(data))
```

Output:

```text
False
```

A non-empty bytearray is truthy:

```python
data = bytearray(b"Python")

print(bool(data))
```

Output:

```text
True
```

Therefore:

```text
bytearray()        → False
bytearray(b"ABC")  → True
```

---

# 23. Adding Data Using `append()`

Because bytearray is mutable, you can add bytes.

```python
data = bytearray(b"ABC")

data.append(68)

print(data)
```

Output:

```text
bytearray(b'ABCD')
```

Because:

```text
68 → D
```

---

# 24. `append()` Accepts Only One Byte

The value must be from:

```text
0 to 255
```

Example:

```python
data = bytearray()

data.append(65)

print(data)
```

Output:

```text
bytearray(b'A')
```

Invalid:

```python
data.append(256)
```

raises:

```text
ValueError
```

---

# 25. Adding Multiple Bytes Using `extend()`

Use `extend()` to add multiple bytes.

```python
data = bytearray(b"ABC")

data.extend([68, 69, 70])

print(data)
```

Output:

```text
bytearray(b'ABCDEF')
```

Because:

```text
68 → D
69 → E
70 → F
```

---

# 26. `append()` vs `extend()`

This is important.

### `append()`

Adds **one byte**.

```python
data.append(68)
```

### `extend()`

Adds **multiple bytes**.

```python
data.extend([68, 69, 70])
```

Think:

```text
append  → one
extend  → many
```

---

# 27. Insert

You can insert a byte at a specific position.

```python
data = bytearray(b"AC")

data.insert(1, 66)

print(data)
```

Output:

```text
bytearray(b'ABC')
```

Because:

```text
66 → B
```

The original:

```text
A C
```

becomes:

```text
A B C
```

---

# 28. Remove

You can remove a specific byte value using `remove()`.

```python
data = bytearray(b"ABC")

data.remove(66)

print(data)
```

Output:

```text
bytearray(b'AC')
```

Because:

```text
66 → B
```

was removed.

---

# 29. Pop

`pop()` removes and returns a byte.

```python
data = bytearray(b"ABC")

value = data.pop()

print(value)
print(data)
```

Output:

```text
67
bytearray(b'AB')
```

The last byte was:

```text
C → 67
```

---

# 30. Pop at a Specific Index

```python
data = bytearray(b"ABC")

value = data.pop(0)

print(value)
print(data)
```

Output:

```text
65
bytearray(b'BC')
```

---

# 31. Clear

`clear()` removes all bytes.

```python
data = bytearray(b"Python")

data.clear()

print(data)
```

Output:

```text
bytearray(b'')
```

The bytearray object remains, but its contents are removed.

---

# 32. Delete Using `del`

You can delete a particular byte.

```python
data = bytearray(b"ABC")

del data[1]

print(data)
```

Output:

```text
bytearray(b'AC')
```

You can also delete a range:

```python
data = bytearray(b"Python")

del data[1:4]

print(data)
```

Output:

```text
bytearray(b'Pon')
```

---

# 33. Replace Bytes

`bytearray` provides `replace()`.

```python
data = bytearray(b"Python Python")

result = data.replace(b"Python", b"Java")

print(result)
```

Output:

```text
bytearray(b'Java Java')
```

Unlike direct indexing, `replace()` returns a new bytearray rather than modifying the original in place.

---

# 34. Important: Not Every Method Mutates the Object

Some methods modify the existing bytearray:

```text
append()
extend()
insert()
remove()
pop()
clear()
```

Some methods return a new bytearray:

```text
replace()
upper()
lower()
```

Always check what the method does.

Example:

```python
data = bytearray(b"python")

result = data.upper()

print(data)
print(result)
```

Output:

```text
bytearray(b'python')
bytearray(b'PYTHON')
```

The original was not changed by `upper()`.

---

# 35. `upper()`

```python
data = bytearray(b"python")

print(data.upper())
```

Output:

```text
bytearray(b'PYTHON')
```

---

# 36. `lower()`

```python
data = bytearray(b"PYTHON")

print(data.lower())
```

Output:

```text
bytearray(b'python')
```

These operations are mainly relevant to ASCII-compatible byte values.

---

# 37. `count()`

Use `count()` to count occurrences.

```python
data = bytearray(b"banana")

print(data.count(b"a"))
```

Output:

```text
3
```

You can also count a byte value:

```python
data = bytearray(b"ABCABC")

print(data.count(65))
```

Output:

```text
2
```

Because:

```text
65 → A
```

---

# 38. `find()`

```python
data = bytearray(b"Python")

print(data.find(b"th"))
```

Output:

```text
2
```

If the sequence is not found:

```python
print(data.find(b"Java"))
```

Output:

```text
-1
```

---

# 39. `index()`

```python
data = bytearray(b"Python")

print(data.index(b"th"))
```

Output:

```text
2
```

If the value is not found, `index()` raises:

```text
ValueError
```

So:

```text
find()
   ↓
not found → -1

index()
   ↓
not found → ValueError
```

---

# 40. `startswith()`

```python
data = bytearray(b"Python")

print(data.startswith(b"Py"))
print(data.startswith(b"Java"))
```

Output:

```text
True
False
```

---

# 41. `endswith()`

```python
data = bytearray(b"Python")

print(data.endswith(b"on"))
print(data.endswith(b"py"))
```

Output:

```text
True
False
```

---

# 42. Iterating Over Bytearray

When you iterate over a bytearray, you receive integers.

```python
data = bytearray(b"ABC")

for value in data:
    print(value)
```

Output:

```text
65
66
67
```

Important:

```text
str       → characters
bytes     → integers
bytearray → integers
```

---

# 43. Convert Bytearray to List

```python
data = bytearray(b"ABC")

numbers = list(data)

print(numbers)
```

Output:

```text
[65, 66, 67]
```

---

# 44. Convert List to Bytearray

```python
numbers = [65, 66, 67]

data = bytearray(numbers)

print(data)
```

Output:

```text
bytearray(b'ABC')
```

---

# 45. Convert String to Bytearray

You can specify the encoding.

```python
text = "Python"

data = bytearray(text, "utf-8")

print(data)
```

Output:

```text
bytearray(b'Python')
```

You can also use:

```python
data = bytearray(text.encode("utf-8"))
```

Both approaches create a bytearray containing the UTF-8 encoded data.

---

# 46. Convert Bytearray to String

Use `decode()`.

```python
data = bytearray(b"Python")

text = data.decode("utf-8")

print(text)
```

Output:

```text
Python
```

The flow is:

```text
bytearray
    ↓
decode()
    ↓
str
```

---

# 47. Encoding and Bytearray

Encoding converts text into bytes.

Example:

```python
text = "Hello"

data = text.encode("utf-8")

print(data)
```

Output:

```text
b'Hello'
```

To make it mutable:

```python
data = bytearray(text.encode("utf-8"))

print(data)
```

Output:

```text
bytearray(b'Hello')
```

Flow:

```text
String
  ↓
encode()
  ↓
bytes
  ↓
bytearray()
  ↓
mutable binary data
```

---

# 48. UTF-8 and Bytearray

Bytearray can contain UTF-8 encoded data.

Example:

```python
text = "é"

data = bytearray(text, "utf-8")

print(data)
print(len(data))
```

Output:

```text
bytearray(b'\xc3\xa9')
2
```

The character:

```text
é
```

takes two bytes in UTF-8.

This is why:

```text
number of characters
```

and:

```text
number of bytes
```

can be different.

---

# 49. Bytearray and Hexadecimal

You can use `hex()`:

```python
data = bytearray(b"ABC")

print(data.hex())
```

Output:

```text
414243
```

Because:

```text
A → 41
B → 42
C → 43
```

---

# 50. Create Bytearray from Hexadecimal

Use:

```python
bytearray.fromhex()
```

Example:

```python
data = bytearray.fromhex("41 42 43")

print(data)
```

Output:

```text
bytearray(b'ABC')
```

Another example:

```python
data = bytearray.fromhex("48656c6c6f")

print(data)
print(data.decode())
```

Output:

```text
bytearray(b'Hello')
Hello
```

---

# 51. Bytearray and Membership

You can use `in`.

```python
data = bytearray(b"Python")

print(80 in data)
print(100 in data)
```

Output:

```text
True
False
```

Because:

```text
P → 80
```

You can also search for a sequence:

```python
print(b"Py" in data)
```

Output:

```text
True
```

---

# 52. Concatenation

Bytearrays can be concatenated.

```python
a = bytearray(b"Hello ")

b = bytearray(b"Python")

result = a + b

print(result)
```

Output:

```text
bytearray(b'Hello Python')
```

The result is a new bytearray.

---

# 53. Bytearray Repetition

Bytearrays support repetition.

```python
data = bytearray(b"Hi")

print(data * 3)
```

Output:

```text
bytearray(b'HiHiHi')
```

---

# 54. Bytearray and String Cannot Be Directly Combined

This is invalid:

```python
data = bytearray(b"Python")

print(data + "Hello")
```

It raises:

```text
TypeError
```

Because:

```text
bytearray != str
```

Convert the string first:

```python
data = bytearray(b"Python")

result = data + bytearray("Hello", "utf-8")

print(result)
```

Output:

```text
bytearray(b'PythonHello')
```

---

# 55. Bytearray and Bytes

A bytes object can be converted to bytearray:

```python
data = b"Python"

mutable_data = bytearray(data)

print(mutable_data)
```

Output:

```text
bytearray(b'Python')
```

And a bytearray can be converted back to bytes:

```python
data = bytearray(b"Python")

immutable_data = bytes(data)

print(immutable_data)
print(type(immutable_data))
```

Output:

```text
b'Python'
<class 'bytes'>
```

This is useful when you need to:

```text
bytes → modify → bytearray → convert back → bytes
```

---

# 56. Important Conversion Flow

```text
             bytes
               ↓
        bytearray(bytes)
               ↓
          bytearray
               ↓
            modify
               ↓
        bytes(bytearray)
               ↓
             bytes
```

Example:

```python
data = b"ABC"

mutable_data = bytearray(data)

mutable_data[0] = 90

data = bytes(mutable_data)

print(data)
```

Output:

```text
b'ZBC'
```

---

# 57. Bytearray is Not Hashable

Unlike `bytes`, a `bytearray` is **mutable**.

Mutable objects are not hashable.

Therefore this is invalid:

```python
data = bytearray(b"Python")

print(hash(data))
```

It raises:

```text
TypeError
```

Similarly, you cannot use a bytearray as:

- Dictionary key
- Set element

---

# 58. Bytes vs Bytearray: Hashability

```text
bytes
 ↓
Immutable
 ↓
Hashable
```

```text
bytearray
 ↓
Mutable
 ↓
Not hashable
```

This is an important connection between **mutability and hashability**.

---

# 59. Bytearray as a Dictionary Key

This is invalid:

```python
data = bytearray(b"Python")

my_dict = {
    data: "value"
}
```

It raises:

```text
TypeError: unhashable type: 'bytearray'
```

If you need to use the binary data as a dictionary key, convert it to `bytes`:

```python
data = bytearray(b"Python")

my_dict = {
    bytes(data): "value"
}

print(my_dict)
```

---

# 60. Bytearray as a Set Element

This is also invalid:

```python
data = bytearray(b"Python")

my_set = {data}
```

because bytearray is unhashable.

But:

```python
data = bytes(b"Python")

my_set = {data}

print(my_set)
```

works because `bytes` is hashable.

---

# 61. Reading Binary Files into Bytearray

Binary files are commonly read as bytes.

Example:

```python
with open("example.bin", "rb") as file:
    data = bytearray(file.read())

print(type(data))
```

Output:

```text
<class 'bytearray'>
```

Now the binary data can be modified.

---

# 62. Writing Bytearray to a Binary File

A bytearray can be written in binary mode.

```python
data = bytearray(b"Hello Python")

with open("example.bin", "wb") as file:
    file.write(data)
```

The file receives the binary data.

---

# 63. Modifying Binary Data

This is where bytearray becomes useful.

Suppose binary data is loaded:

```python
data = bytearray(b"ABC")
```

You can modify it:

```python
data[0] = 90
```

Now:

```text
ABC
 ↓
ZBC
```

This kind of direct modification is not possible with immutable `bytes`.

---

# 64. Bytearray and Networking

Network programs often receive data as bytes.

Sometimes the program needs to modify that data.

A bytearray provides a mutable buffer.

Conceptually:

```text
Network
   ↓
Bytes
   ↓
bytearray
   ↓
Modify / process
   ↓
Send / store
```

This is useful in:

- Socket programming
- Network protocols
- Packet processing
- Communication systems

---

# 65. Bytearray and Cryptography

Cryptographic programs often work with binary data.

A simplified flow can look like:

```text
Text
 ↓
Encoding
 ↓
Bytes
 ↓
Bytearray if modification is needed
 ↓
Processing
 ↓
Encrypted/processed data
```

However, actual cryptographic libraries may require specifically `bytes`, `bytearray`, or another buffer-compatible type depending on the API.

---

# 66. Bytearray and `memoryview`

`bytearray` is also commonly used with `memoryview`.

The basic idea is:

```text
bytearray
    ↓
memoryview
    ↓
access/modify underlying data
```

A `memoryview` allows access to the underlying buffer without necessarily creating another copy.

This becomes especially useful when working with large binary data.

---

# 67. Bytearray vs List

Both are mutable.

But they have different purposes.

### List

```python
data = [65, 66, 67]
```

A list can contain almost any Python object:

```python
data = [65, "Python", 3.14, True]
```

### Bytearray

```python
data = bytearray([65, 66, 67])
```

A bytearray can contain only byte values:

```text
0 to 255
```

Therefore:

```text
list
 ↓
general-purpose collection

bytearray
 ↓
mutable binary data
```

---

# 68. Bytearray vs Bytes vs String

| Feature | `str` | `bytes` | `bytearray` |
|---|---|---|---|
| Stores | Text | Binary data | Binary data |
| Mutable | No | No | Yes |
| Indexed result | String | Integer | Integer |
| Values | Unicode characters | 0–255 | 0–255 |
| Hashable | Yes | Yes | No |
| Encoding | Used to create bytes | Binary representation | Binary representation |
| Decoding | Not applicable | Yes | Yes |
| Main use | Text | Immutable binary data | Mutable binary data |

---

# 69. Important Methods

### Methods that modify the bytearray

| Method | Purpose |
|---|---|
| `append()` | Add one byte |
| `extend()` | Add multiple bytes |
| `insert()` | Insert one byte |
| `remove()` | Remove a byte |
| `pop()` | Remove and return a byte |
| `clear()` | Remove all bytes |
| `reverse()` | Reverse the bytearray in place |

### Methods that return a result

| Method | Purpose |
|---|---|
| `decode()` | Convert to string |
| `replace()` | Replace byte sequences |
| `upper()` | Convert ASCII letters to uppercase |
| `lower()` | Convert ASCII letters to lowercase |
| `find()` | Find a sequence |
| `count()` | Count occurrences |
| `startswith()` | Check prefix |
| `endswith()` | Check suffix |
| `hex()` | Convert to hexadecimal |

---

# 70. Important Functions

| Function | Purpose |
|---|---|
| `bytearray()` | Create bytearray |
| `bytes()` | Convert bytearray to bytes |
| `len()` | Get number of bytes |
| `type()` | Check type |
| `isinstance()` | Check type |
| `list()` | Convert to list |
| `bool()` | Check truthiness |

Important class method:

```python
bytearray.fromhex()
```

creates a bytearray from hexadecimal text.

---

# 71. Practical Example: Modify Text as Bytes

```python
data = bytearray(b"Python")

print(data)

data[0] = ord("J")

print(data)

print(data.decode())
```

Output:

```text
bytearray(b'Python')
bytearray(b'Jython')
Jython
```

Here:

```python
ord("J")
```

returns:

```text
74
```

So the first byte is changed from:

```text
P → 80
```

to:

```text
J → 74
```

---

# 72. Practical Example: Modify Multiple Bytes

```python
data = bytearray(b"ABC")

data[0] = ord("X")
data[1] = ord("Y")
data[2] = ord("Z")

print(data)
```

Output:

```text
bytearray(b'XYZ')
```

---

# 73. Practical Example: Add Data

```python
data = bytearray(b"Hello")

data.extend(b" Python")

print(data)
```

Output:

```text
bytearray(b'Hello Python')
```

---

# 74. Practical Example: Remove Data

```python
data = bytearray(b"ABCDE")

data.remove(ord("C"))

print(data)
```

Output:

```text
bytearray(b'ABDE')
```

---

# 75. Practical Example: Reverse

```python
data = bytearray(b"Python")

data.reverse()

print(data)
```

Output:

```text
bytearray(b'nohtyP')
```

Notice that `reverse()` modifies the existing bytearray.

This is different from:

```python
data[::-1]
```

which creates a new bytearray.

---

# 76. Practical Example: Binary Data

```python
data = bytearray([10, 20, 30, 40, 50])

print(data)

data[2] = 100

print(data)
```

Output:

```text
bytearray(b'\n\x14\x1e(2')
bytearray(b'\n\x14d(2')
```

The representation may contain escape sequences because the values are not necessarily printable characters.

The important part is that the values are:

```text
10, 20, 100, 40, 50
```

---

# 77. Practical Example: Convert to Bytes

```python
data = bytearray(b"Python")

data[0] = ord("J")

result = bytes(data)

print(result)
```

Output:

```text
b'Jython'
```

This is useful when an API expects immutable `bytes`.

---

# 78. Common Mistakes

### Mistake 1: Thinking bytearray is immutable

Wrong assumption:

```python
data = bytearray(b"ABC")
data[0] = 90
```

Some beginners expect an error.

But this is valid because bytearray is mutable.

---

### Mistake 2: Using values greater than 255

Wrong:

```python
data[0] = 300
```

Correct:

```text
0 <= value <= 255
```

---

### Mistake 3: Mixing string and bytearray

Wrong:

```python
data = bytearray(b"ABC")

data + "DEF"
```

Use:

```python
data + bytearray(b"DEF")
```

instead.

---

### Mistake 4: Thinking bytearray indexing returns characters

```python
data = bytearray(b"ABC")

print(data[0])
```

returns:

```text
65
```

not:

```text
A
```

---

### Mistake 5: Trying to hash bytearray

```python
hash(bytearray(b"ABC"))
```

raises:

```text
TypeError
```

because bytearray is mutable.

---

### Mistake 6: Confusing `bytes()` and `bytearray()`

```python
bytes(...)
```

creates immutable binary data.

```python
bytearray(...)
```

creates mutable binary data.

---

# 79. Time Complexity

For a bytearray containing `n` bytes:

| Operation | Typical Complexity |
|---|---:|
| Indexing | O(1) |
| `len()` | O(1) |
| Membership | O(n) |
| Slicing | O(k) |
| `append()` | Amortized O(1) |
| `insert()` | O(n) |
| `remove()` | O(n) |
| `pop()` at end | O(1) |
| `pop()` at beginning | O(n) |
| `clear()` | O(n) |
| `find()` | Depends on search |
| `count()` | O(n) |

The important point is that bytearray is designed for efficient mutable binary data operations.

---

# 80. Important Characteristics of Bytearray

A `bytearray` is:

- Mutable
- Ordered
- Indexed
- Sliceable
- Iterable
- Not hashable
- A sequence type
- Used for binary data
- Stores values from `0` to `255`
- Supports direct modification
- Supports encoding/decoding
- Useful for binary files
- Useful for network data
- Useful for buffers
- Different from `bytes`
- Different from `str`

---

# 81. Complete Mental Model

Think about `bytearray` like this:

```text
                bytearray
                    |
             Mutable binary data
                    |
        ┌───────────┼───────────┐
        ↓           ↓           ↓
     Index       Modify       Slice
        ↓           ↓           ↓
    integer      0–255      bytearray
```

Example:

```python
data = bytearray(b"ABC")
```

Internally:

```text
A → 65
B → 66
C → 67
```

You can change:

```python
data[0] = 90
```

Now:

```text
A → Z
65 → 90
```

Result:

```text
bytearray(b"ZBC")
```

---

# 82. Complete Bytes → Bytearray → Bytes Flow

This is one of the most useful things to remember:

```text
        b"ABC"
          |
          | bytearray()
          ↓
   bytearray(b"ABC")
          |
       modify
          ↓
   bytearray(b"ZBC")
          |
          | bytes()
          ↓
       b"ZBC"
```

Example:

```python
data = b"ABC"

mutable_data = bytearray(data)

mutable_data[0] = ord("Z")

result = bytes(mutable_data)

print(result)
```

Output:

```text
b'ZBC'
```

---

# 83. Quick Revision

### Definition

```text
bytearray = mutable sequence of bytes
```

### Valid values

```text
0 to 255
```

### Creation

```python
bytearray()
bytearray(b"Python")
bytearray([65, 66, 67])
```

### Main property

```text
bytes     → immutable
bytearray → mutable
```

### Indexing

```python
data = bytearray(b"ABC")

print(data[0])
```

Output:

```text
65
```

### Modification

```python
data[0] = 90
```

Result:

```text
bytearray(b'ZBC')
```

### Add

```python
data.append(65)
data.extend([66, 67])
```

### Remove

```python
data.remove(65)
data.pop()
data.clear()
```

### Convert

```python
bytes(data)
data.decode()
bytearray(b"ABC")
```

### Hashability

```text
bytes     → hashable
bytearray → not hashable
```

---

# 84. Bytes vs Bytearray — Final Comparison

| Feature | `bytes` | `bytearray` |
|---|---|---|
| Type | `bytes` | `bytearray` |
| Binary data | Yes | Yes |
| Mutable | No | Yes |
| Immutable | Yes | No |
| Indexed | Yes | Yes |
| Slicing | Yes | Yes |
| Iterable | Yes | Yes |
| Index returns | Integer | Integer |
| Values | `0–255` | `0–255` |
| Hashable | Yes | No |
| Dictionary key | Yes | No |
| Set element | Yes | No |
| `append()` | No | Yes |
| `extend()` | No | Yes |
| `insert()` | No | Yes |
| `remove()` | No | Yes |
| `pop()` | No | Yes |
| `clear()` | No | Yes |
| `decode()` | Yes | Yes |
| Main use | Immutable binary data | Mutable binary data |

---

# 85. One-Line Definition

> **Bytearray is a mutable sequence of bytes in Python, where each element contains a value from 0 to 255, and it is mainly used when binary data needs to be modified after creation.**

---

# 86. Final Example

```python
# Create bytearray
data = bytearray(b"Python")

print(data)

# Access a byte
print(data[0])

# Modify a byte
data[0] = ord("J")

print(data)

# Add a byte
data.append(ord("!"))

print(data)

# Convert bytearray to string
text = data.decode("utf-8")

print(text)
```

**Output:**

```text
bytearray(b'Python')
80
bytearray(b'Jython')
bytearray(b'Jython!')
Jython!
```

Complete flow:

```text
"Python"
   ↓
bytearray()
   ↓
bytearray(b"Python")
   ↓
modify P → J
   ↓
bytearray(b"Jython")
   ↓
append !
   ↓
bytearray(b"Jython!")
   ↓
decode()
   ↓
"Jython!"
```

The most important thing to remember is:

```text
bytes
  → immutable binary data

bytearray
  → mutable binary data
```