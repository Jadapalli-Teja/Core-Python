# Bytes (`bytes`) Data Type in Python

## 1. What is Bytes?

The **`bytes`** data type is used to store a sequence of **bytes**.

A byte is an integer value from:

```text
0 to 255
```

Bytes are mainly used when working with **binary data**, such as:

- Images
- Audio
- Video
- PDF files
- Network communication
- File handling
- Encoded text
- Cryptography
- Data transmission

Example:

```python
data = b"Python"

print(data)
```

**Output:**

```text
b'Python'
```

The `b` before the string indicates that it is a **bytes object**.

---

# 2. What is a Byte?

A byte consists of **8 bits**.

```text
1 byte = 8 bits
```

Each byte can represent a value from:

```text
00000000 → 0
11111111 → 255
```

Therefore:

```text
1 byte → 0 to 255
```

Example:

```python
data = bytes([65, 66, 67])

print(data)
```

**Output:**

```text
b'ABC'
```

Here:

```text
65 → A
66 → B
67 → C
```

---

# 3. Creating Bytes

There are several ways to create a bytes object.

### Using a bytes literal

```python
data = b"Python"

print(data)
```

Output:

```text
b'Python'
```

---

### Using `bytes()`

```python
data = bytes([65, 66, 67])

print(data)
```

Output:

```text
b'ABC'
```

---

### Using `bytes` with an integer

```python
data = bytes(5)

print(data)
```

Output:

```text
b'\x00\x00\x00\x00\x00'
```

This creates **5 zero bytes**.

---

# 4. Type of Bytes

Use `type()`:

```python
data = b"Python"

print(type(data))
```

Output:

```text
<class 'bytes'>
```

You can also use `isinstance()`:

```python
print(isinstance(data, bytes))
```

Output:

```text
True
```

---

# 5. Bytes Literal

A bytes literal is written using:

```python
b"..."
```

Example:

```python
name = b"Teja"

print(name)
```

Output:

```text
b'Teja'
```

Compare:

```python
text = "Teja"
data = b"Teja"

print(type(text))
print(type(data))
```

Output:

```text
<class 'str'>
<class 'bytes'>
```

So:

```text
"Teja"   → str
b"Teja"  → bytes
```

---

# 6. String vs Bytes

This is one of the most important concepts.

A string stores **text**.

```python
name = "Python"
```

A bytes object stores **raw byte data**.

```python
data = b"Python"
```

Their types are different:

```python
print(type(name))
print(type(data))
```

Output:

```text
<class 'str'>
<class 'bytes'>
```

Think of it as:

```text
str
 ↓
Human-readable text

bytes
 ↓
Raw binary data
```

---

# 7. Bytes Contain Integers

A bytes object behaves like a sequence of integers from `0` to `255`.

Example:

```python
data = b"ABC"

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

Why?

```text
A → 65
B → 66
C → 67
```

So:

```python
data[0]
```

returns:

```text
65
```

not:

```text
b"A"
```

---

# 8. Bytes and ASCII

For common English characters, the byte values correspond to **ASCII** values.

Example:

```python
data = b"ABC"

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

Some common ASCII values:

| Character | Byte value |
|---|---:|
| `A` | 65 |
| `B` | 66 |
| `C` | 67 |
| `a` | 97 |
| `b` | 98 |
| `c` | 99 |
| `0` | 48 |
| `1` | 49 |
| Space | 32 |

---

# 9. Creating Bytes from Integer Values

You can create bytes using integers from `0` to `255`.

```python
data = bytes([65, 66, 67])

print(data)
```

Output:

```text
b'ABC'
```

Each number represents one byte.

```text
65 → A
66 → B
67 → C
```

---

# 10. Valid Byte Values

Every integer used to create a bytes object must be between:

```text
0 and 255
```

Valid:

```python
data = bytes([0, 100, 200, 255])

print(data)
```

Invalid:

```python
data = bytes([256])
```

This raises:

```text
ValueError
```

because `256` cannot fit into one byte.

Similarly:

```python
data = bytes([-1])
```

also raises:

```text
ValueError
```

---

# 11. Bytes are Immutable

The `bytes` data type is **immutable**.

Once a bytes object is created, its individual values cannot be changed.

Example:

```python
data = b"Python"

data[0] = 80
```

This produces:

```text
TypeError
```

You cannot modify a bytes object directly.

---

# 12. Bytes vs Bytearray

This is an important difference.

### `bytes`

Immutable:

```python
data = b"Python"
```

Cannot be changed.

### `bytearray`

Mutable:

```python
data = bytearray(b"Python")
```

Can be changed.

Think:

```text
bytes
   ↓
Immutable

bytearray
   ↓
Mutable
```

---

# 13. Reassigning Bytes

Although bytes are immutable, the variable can be reassigned.

```python
data = b"Python"

data = b"Java"

print(data)
```

Output:

```text
b'Java'
```

The original bytes object was not modified.

Instead:

```text
data → b"Python"
```

then:

```text
data → b"Java"
```

This is **reassignment**, not modification.

---

# 14. Bytes Indexing

Bytes support indexing like strings and lists.

Example:

```python
data = b"Python"

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

Because:

```text
P → 80
y → 121
t → 116
```

---

# 15. Positive Indexing

For:

```python
data = b"Python"
```

the indexes are:

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

# 16. Negative Indexing

Bytes also support negative indexing.

```python
data = b"Python"

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

Indexing:

```text
 P    y    t    h    o    n
 0    1    2    3    4    5
-6   -5   -4   -3   -2   -1
```

---

# 17. Bytes Slicing

Bytes support slicing.

```python
data = b"Python"

print(data[0:3])
```

Output:

```text
b'Pyt'
```

Example:

```python
print(data[2:5])
```

Output:

```text
b'tho'
```

---

# 18. Bytes Slicing with Step

```python
data = b"Python"

print(data[::2])
```

Output:

```text
b'Pto'
```

Because indexes:

```text
0 → P
2 → t
4 → o
```

---

# 19. Reverse Bytes

Use a negative step:

```python
data = b"Python"

print(data[::-1])
```

Output:

```text
b'nohtyP'
```

---

# 20. Length of Bytes

Use `len()`:

```python
data = b"Python"

print(len(data))
```

Output:

```text
6
```

Each ASCII character occupies one byte in this example.

---

# 21. Important: Character Count vs Byte Count

For normal ASCII text:

```text
1 character = 1 byte
```

For many Unicode characters, this is not true.

Example:

```python
text = "é"

print(len(text))
print(len(text.encode("utf-8")))
```

Output:

```text
1
2
```

So:

```text
1 character
2 bytes in UTF-8
```

This is an important difference between strings and bytes.

---

# 22. Bytes and UTF-8

Text needs an encoding to be converted into bytes.

The most commonly used encoding is:

```text
UTF-8
```

Example:

```python
text = "Python"

data = text.encode("utf-8")

print(data)
```

Output:

```text
b'Python'
```

---

# 23. Encoding

**Encoding** means converting text (`str`) into bytes.

```text
str
 ↓
encode()
 ↓
bytes
```

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

---

# 24. Decoding

**Decoding** means converting bytes back into text.

```text
bytes
 ↓
decode()
 ↓
str
```

Example:

```python
data = b"Hello"

text = data.decode("utf-8")

print(text)
```

Output:

```text
Hello
```

---

# 25. Encoding and Decoding Together

```python
text = "Python"

data = text.encode("utf-8")

print(data)

original_text = data.decode("utf-8")

print(original_text)
```

Output:

```text
b'Python'
Python
```

The complete flow:

```text
"Python"
   ↓
 encode()
   ↓
b"Python"
   ↓
 decode()
   ↓
"Python"
```

---

# 26. Why Encoding is Needed

Computers ultimately store and transmit data as bytes.

Humans work with:

```text
Text
```

Computers often need:

```text
Bytes
```

Therefore:

```text
Human text
    ↓
Encoding
    ↓
Bytes
    ↓
Storage / Network / File
    ↓
Decoding
    ↓
Human text
```

---

# 27. UTF-8 Example with Non-English Text

```python
text = "హలో"

data = text.encode("utf-8")

print(data)
```

The output contains multiple bytes.

This happens because UTF-8 uses a variable number of bytes for different Unicode characters.

Therefore:

```text
ASCII character → usually 1 byte
Other Unicode characters → may require multiple bytes
```

---

# 28. Decode Using the Correct Encoding

Example:

```python
text = "hello"

data = text.encode("utf-8")

result = data.decode("utf-8")

print(result)
```

Output:

```text
hello
```

If bytes were created using one encoding but decoded using an incompatible encoding, the result may be incorrect or raise an error.

So the encoding used for decoding should match the encoding used to create the bytes.

---

# 29. Bytes Membership

You can use `in` with bytes.

```python
data = b"Python"

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

---

# 30. Bytes Membership with a Bytes Object

You can also search for a bytes sequence.

```python
data = b"Python"

print(b"Py" in data)
print(b"Java" in data)
```

Output:

```text
True
False
```

---

# 31. Bytes Concatenation

Bytes objects can be concatenated using `+`.

```python
a = b"Hello "
b = b"Python"

result = a + b

print(result)
```

Output:

```text
b'Hello Python'
```

Both operands must be bytes.

---

# 32. Cannot Directly Concatenate String and Bytes

This is invalid:

```python
text = "Hello"
data = b"Python"

print(text + data)
```

This raises:

```text
TypeError
```

Because:

```text
str != bytes
```

Convert them when necessary.

Example:

```python
text = "Hello"
data = b"Python"

result = text.encode() + data

print(result)
```

Output:

```text
b'HelloPython'
```

---

# 33. Bytes Repetition

Bytes support repetition using `*`.

```python
data = b"Hi"

print(data * 3)
```

Output:

```text
b'HiHiHi'
```

---

# 34. Bytes Comparison

Bytes objects can be compared.

```python
print(b"abc" == b"abc")
print(b"abc" == b"xyz")
```

Output:

```text
True
False
```

They can also be compared lexicographically.

```python
print(b"abc" < b"abd")
```

Output:

```text
True
```

---

# 35. Bytes Methods

Bytes provide several useful methods.

Some important ones are:

| Method | Purpose |
|---|---|
| `decode()` | Convert bytes to string |
| `count()` | Count occurrences |
| `find()` | Find position |
| `index()` | Find position, raises error if absent |
| `replace()` | Replace bytes |
| `startswith()` | Check beginning |
| `endswith()` | Check ending |
| `split()` | Split bytes |
| `join()` | Join bytes |
| `strip()` | Remove specified bytes from ends |
| `upper()` | Convert ASCII letters to uppercase |
| `lower()` | Convert ASCII letters to lowercase |

---

# 36. `bytes.decode()`

The most important bytes method is:

```python
decode()
```

Example:

```python
data = b"Python"

text = data.decode()

print(text)
print(type(text))
```

Output:

```text
Python
<class 'str'>
```

By default, Python normally uses UTF-8 for `decode()` when no encoding is specified.

It is often clearer to write:

```python
data.decode("utf-8")
```

---

# 37. `bytes.count()`

```python
data = b"banana"

print(data.count(b"a"))
```

Output:

```text
3
```

It counts how many times the specified bytes occur.

---

# 38. `bytes.find()`

```python
data = b"Python"

print(data.find(b"th"))
```

Output:

```text
2
```

If the value is not found:

```python
print(data.find(b"Java"))
```

Output:

```text
-1
```

---

# 39. `bytes.index()`

```python
data = b"Python"

print(data.index(b"th"))
```

Output:

```text
2
```

But unlike `find()`, `index()` raises an error if the value is not found.

```python
data.index(b"Java")
```

raises:

```text
ValueError
```

So:

```text
find()  → -1 if not found
index() → ValueError if not found
```

---

# 40. `bytes.startswith()`

```python
data = b"Python"

print(data.startswith(b"Py"))
print(data.startswith(b"Java"))
```

Output:

```text
True
False
```

---

# 41. `bytes.endswith()`

```python
data = b"Python"

print(data.endswith(b"on"))
print(data.endswith(b"py"))
```

Output:

```text
True
False
```

---

# 42. `bytes.replace()`

```python
data = b"Python Python"

result = data.replace(b"Python", b"Java")

print(result)
```

Output:

```text
b'Java Java'
```

Remember:

`bytes` is immutable, so `replace()` creates a **new bytes object**.

It does not modify the original object.

---

# 43. `bytes.upper()`

```python
data = b"python"

print(data.upper())
```

Output:

```text
b'PYTHON'
```

This operation is mainly relevant to ASCII characters.

---

# 44. `bytes.lower()`

```python
data = b"PYTHON"

print(data.lower())
```

Output:

```text
b'python'
```

Again, bytes represent raw values, and text-oriented operations on bytes are generally based on ASCII-compatible byte values.

---

# 45. Iterating Over Bytes

When you iterate over bytes, you get integers.

```python
data = b"ABC"

for value in data:
    print(value)
```

Output:

```text
65
66
67
```

This is different from iterating over a string.

```python
text = "ABC"

for value in text:
    print(value)
```

Output:

```text
A
B
C
```

Important:

```text
str iteration  → characters
bytes iteration → integers
```

---

# 46. Convert Bytes to List

Because bytes contain integer values:

```python
data = b"ABC"

print(list(data))
```

Output:

```text
[65, 66, 67]
```

---

# 47. Convert List to Bytes

A list containing values from `0` to `255` can be converted into bytes.

```python
numbers = [65, 66, 67]

data = bytes(numbers)

print(data)
```

Output:

```text
b'ABC'
```

---

# 48. Convert String to Bytes

Use `encode()`:

```python
text = "Python"

data = text.encode("utf-8")

print(data)
```

Output:

```text
b'Python'
```

Do not use:

```python
bytes("Python")
```

without specifying an encoding.

This raises:

```text
TypeError
```

Use:

```python
bytes("Python", "utf-8")
```

or preferably:

```python
"Python".encode("utf-8")
```

---

# 49. Convert Bytes to String

Use `decode()`:

```python
data = b"Python"

text = data.decode("utf-8")

print(text)
```

Output:

```text
Python
```

---

# 50. Bytes and Escape Sequences

Bytes literals support escape sequences.

Example:

```python
data = b"Hello\nWorld"

print(data)
```

Output representation:

```text
b'Hello\nWorld'
```

When decoded and printed as text:

```python
print(data.decode())
```

Output:

```text
Hello
World
```

---

# 51. Hexadecimal Representation

Bytes are often represented using hexadecimal notation.

Example:

```python
data = b"ABC"

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

in hexadecimal.

---

# 52. Convert Hexadecimal to Bytes

Use `bytes.fromhex()`.

```python
data = bytes.fromhex("41 42 43")

print(data)
```

Output:

```text
b'ABC'
```

This is useful when working with:

- Network data
- Cryptography
- File formats
- Binary protocols

---

# 53. Bytes from Hexadecimal String

Example:

```python
hex_value = "48656c6c6f"

data = bytes.fromhex(hex_value)

print(data)
print(data.decode())
```

Output:

```text
b'Hello'
Hello
```

Flow:

```text
Hexadecimal
     ↓
fromhex()
     ↓
Bytes
     ↓
decode()
     ↓
String
```

---

# 54. Bytes and Binary Data

Bytes are useful because computer files are fundamentally represented as binary data.

For example:

```text
Image
  ↓
Binary data
  ↓
Bytes
```

Similarly:

```text
PDF
  ↓
Binary data
  ↓
Bytes
```

Bytes allow Python programs to work with this raw data.

---

# 55. Reading Binary Files

When opening a file in binary mode, use:

```python
"rb"
```

Example:

```python
with open("image.jpg", "rb") as file:
    data = file.read()

print(type(data))
```

Output:

```text
<class 'bytes'>
```

The contents of the image are returned as bytes.

---

# 56. Writing Binary Files

Use:

```text
"wb"
```

Example:

```python
data = b"Hello"

with open("example.bin", "wb") as file:
    file.write(data)
```

Here:

```text
wb
 ↓
write binary
```

The file receives bytes rather than normal text.

---

# 57. Binary File Modes

Common binary modes:

| Mode | Meaning |
|---|---|
| `rb` | Read binary |
| `wb` | Write binary |
| `ab` | Append binary |
| `rb+` | Read and write binary |
| `wb+` | Write and read binary |

These modes are commonly used for binary files such as:

- Images
- Audio
- Video
- PDFs
- Executable files

---

# 58. Bytes and Networking

Network communication often works with bytes.

For example, when sending data through a socket:

```text
String
   ↓
encode()
   ↓
Bytes
   ↓
Network
```

When receiving:

```text
Network
   ↓
Bytes
   ↓
decode()
   ↓
String
```

This is why understanding `bytes` is important for:

- Networking
- APIs
- Web protocols
- Sockets
- HTTP
- Security

---

# 59. Bytes and Cryptography

Cryptographic operations commonly work with bytes.

For example:

```text
Plain text
    ↓
Encoding
    ↓
Bytes
    ↓
Encryption
    ↓
Encrypted bytes
```

Similarly, decryption produces bytes that can be decoded back into text.

This is one reason bytes are important in cybersecurity and cryptography.

---

# 60. Bytes are Hashable

`bytes` objects are immutable, so they are hashable.

Therefore they can be used as:

- Dictionary keys
- Set elements

Example:

```python
data = b"Python"

my_dict = {
    data: "Programming"
}

print(my_dict[data])
```

Output:

```text
Programming
```

---

# 61. Bytes as Set Elements

```python
data = {
    b"Python",
    b"Java",
    b"C"
}

print(data)
```

Each bytes object can be stored in a set because bytes are hashable.

---

# 62. Bytes and `==`

Bytes can be compared using `==`.

```python
a = b"Python"
b = b"Python"

print(a == b)
```

Output:

```text
True
```

It checks whether their contents are equal.

---

# 63. Bytes and `is`

Remember that:

```python
==
```

checks value equality.

Whereas:

```python
is
```

checks object identity.

Example:

```python
a = b"Python"
b = b"Python"

print(a == b)
```

The important rule is:

> Use `==` when comparing the contents of bytes.

Do not use `is` when you mean content equality.

---

# 64. Bytes Truthiness

Bytes follow the same general truthiness rule as other collections.

Empty bytes:

```python
data = b""

print(bool(data))
```

Output:

```text
False
```

Non-empty bytes:

```python
data = b"Python"

print(bool(data))
```

Output:

```text
True
```

Therefore:

```text
b""       → False
b"Python" → True
```

---

# 65. Empty Bytes

You can create an empty bytes object:

```python
data = b""

print(data)
print(len(data))
```

Output:

```text
b''
0
```

You can also use:

```python
data = bytes()
```

Both represent empty bytes.

---

# 66. `bytes()` with an Integer

This is an important point.

```python
data = bytes(3)

print(data)
```

Output:

```text
b'\x00\x00\x00'
```

It does **not** mean the bytes contain the number `3`.

Instead, it creates **three zero bytes**.

So:

```python
bytes(3)
```

means:

```text
3 zero bytes
```

---

# 67. `bytes()` with an Iterable

You can provide an iterable containing integers from `0` to `255`.

Example:

```python
numbers = [65, 66, 67]

data = bytes(numbers)

print(data)
```

Output:

```text
b'ABC'
```

Another example:

```python
numbers = range(5)

data = bytes(numbers)

print(data)
```

Output:

```text
b'\x00\x01\x02\x03\x04'
```

---

# 68. Bytes are a Sequence

Bytes are a **sequence type**.

Therefore they support:

- Indexing
- Negative indexing
- Slicing
- Iteration
- Length
- Membership
- Concatenation
- Repetition

Example:

```python
data = b"Python"

print(data[0])
print(data[1:4])
print(len(data))
print(b"Py" in data)
```

Output:

```text
80
b'yth'
6
True
```

---

# 69. Bytes vs List

Both can contain integer values, but they are different.

### List

```python
data = [65, 66, 67]
```

### Bytes

```python
data = b"ABC"
```

Differences:

| Feature | List | Bytes |
|---|---|---|
| Mutable | Yes | No |
| Elements | Any Python object | Integers `0–255` |
| Binary data | Not specialized | Yes |
| Hashable | No | Yes |
| Index result | Element itself | Integer |

---

# 70. Bytes vs Bytearray

| Feature | `bytes` | `bytearray` |
|---|---|---|
| Mutable | No | Yes |
| Indexing result | Integer | Integer |
| Supports binary data | Yes | Yes |
| Hashable | Yes | No |
| Can modify elements | No | Yes |

Example:

```python
data = bytearray(b"ABC")

data[0] = 90

print(data)
```

Output:

```text
bytearray(b'ZBC')
```

This cannot be done with `bytes`.

---

# 71. Bytes vs String

| Feature | `str` | `bytes` |
|---|---|---|
| Stores | Text | Binary data |
| Element on indexing | String of length 1 | Integer |
| Mutable | No | No |
| Encoding | Not needed for text itself | Used to create from text |
| Decoding | Not applicable | Converts to `str` |
| Hashable | Yes | Yes |
| Example | `"Python"` | `b"Python"` |

---

# 72. Common Mistake: Forgetting `b`

```python
data = "ABC"
```

This is:

```text
str
```

Whereas:

```python
data = b"ABC"
```

is:

```text
bytes
```

The `b` matters.

---

# 73. Common Mistake: Mixing String and Bytes

Wrong:

```python
name = "Python"
data = b"Programming"

result = name + data
```

This raises:

```text
TypeError
```

Correct:

```python
name = "Python"
data = b"Programming"

result = name.encode() + data

print(result)
```

Output:

```text
b'PythonProgramming'
```

Or convert the bytes back to string:

```python
result = name + data.decode()

print(result)
```

Output:

```text
PythonProgramming
```

---

# 74. Common Mistake: Thinking Bytes Store Characters

Consider:

```python
data = b"ABC"

print(data[0])
```

Output:

```text
65
```

Bytes do not return `"A"` when indexed.

They return the integer byte value.

```text
b"ABC"
   ↓
[65, 66, 67]
```

---

# 75. Common Mistake: Invalid Byte Range

This is invalid:

```python
bytes([300])
```

because:

```text
300 > 255
```

Valid range:

```text
0 <= value <= 255
```

---

# 76. Common Mistake: `bytes(5)`

Do not confuse:

```python
bytes(5)
```

with:

```python
bytes([5])
```

They are different.

### `bytes(5)`

Creates five zero bytes:

```text
b'\x00\x00\x00\x00\x00'
```

### `bytes([5])`

Creates one byte containing the value `5`:

```text
b'\x05'
```

This distinction is very important.

---

# 77. Practical Example: Convert Text to Bytes

```python
message = "Hello Python"

data = message.encode("utf-8")

print(data)
print(type(data))
```

Output:

```text
b'Hello Python'
<class 'bytes'>
```

---

# 78. Practical Example: Convert Bytes to Text

```python
data = b"Hello Python"

message = data.decode("utf-8")

print(message)
print(type(message))
```

Output:

```text
Hello Python
<class 'str'>
```

---

# 79. Practical Example: Display Byte Values

```python
data = b"ABC"

for value in data:
    print(value)
```

Output:

```text
65
66
67
```

---

# 80. Practical Example: Convert Bytes to List

```python
data = b"ABC"

numbers = list(data)

print(numbers)
```

Output:

```text
[65, 66, 67]
```

---

# 81. Practical Example: Convert List to Bytes

```python
numbers = [65, 66, 67]

data = bytes(numbers)

print(data)
```

Output:

```text
b'ABC'
```

---

# 82. Practical Example: Hexadecimal

```python
data = b"Hello"

print(data.hex())
```

Output:

```text
48656c6c6f
```

---

# 83. Practical Example: Hex to Bytes

```python
hex_data = "48656c6c6f"

data = bytes.fromhex(hex_data)

print(data)
print(data.decode())
```

Output:

```text
b'Hello'
Hello
```

---

# 84. Practical Example: Binary File

```python
with open("example.bin", "wb") as file:
    file.write(b"Hello Python")
```

To read it:

```python
with open("example.bin", "rb") as file:
    data = file.read()

print(data)
```

Output:

```text
b'Hello Python'
```

---

# 85. Important Methods

| Method | Purpose |
|---|---|
| `decode()` | Convert bytes to string |
| `count()` | Count occurrences |
| `find()` | Search and return index |
| `index()` | Search and raise error if missing |
| `replace()` | Replace byte sequences |
| `startswith()` | Check prefix |
| `endswith()` | Check suffix |
| `split()` | Split bytes |
| `join()` | Join byte sequences |
| `strip()` | Remove bytes from ends |
| `upper()` | Uppercase ASCII bytes |
| `lower()` | Lowercase ASCII bytes |
| `hex()` | Convert bytes to hexadecimal string |

---

# 86. Important Functions

| Function | Purpose |
|---|---|
| `bytes()` | Create bytes |
| `len()` | Find number of bytes |
| `type()` | Check type |
| `isinstance()` | Check type relationship |
| `list()` | Convert bytes to integer list |
| `bytearray()` | Convert/create mutable byte sequence |

Useful class methods:

| Method | Purpose |
|---|---|
| `bytes.fromhex()` | Create bytes from hexadecimal |
| `bytes.fromhex("41 42")` | Produces `b"AB"` |

---

# 87. Time Complexity

For a bytes object of length `n`:

| Operation | Typical Complexity |
|---|---:|
| Indexing | O(1) |
| Length | O(1) |
| Membership | O(n) |
| Slicing | O(k) |
| Concatenation | O(n) |
| `find()` | depends on search |
| `count()` | O(n) |

Bytes are efficient for storing and processing raw binary data.

---

# 88. Important Characteristics

The `bytes` data type is:

- Immutable
- Ordered
- Indexed
- Sliceable
- Iterable
- Hashable
- A sequence type
- Used for binary data
- Contains values from `0` to `255`
- Supports encoding/decoding workflows
- Useful for files and networks
- Useful in cryptography
- Different from `str`
- Different from `bytearray`

---

# 89. Complete Mental Model

Think of bytes like this:

```text
Text
 |
 | encode("utf-8")
 ↓
Bytes
 |
 ├── indexing → integer
 ├── slicing → bytes
 ├── iteration → integers
 ├── binary file handling
 ├── networking
 └── cryptography
 |
 | decode("utf-8")
 ↓
Text
```

Example:

```text
"Hello"
   ↓
encode()
   ↓
b"Hello"
   ↓
decode()
   ↓
"Hello"
```

---

# 90. Quick Revision

### Definition

```text
bytes = immutable sequence of integers from 0 to 255
```

### Creating bytes

```python
b"Python"
bytes([65, 66, 67])
bytes(5)
```

### Important properties

```text
Immutable
Ordered
Indexed
Sliceable
Iterable
Hashable
Binary data
```

### Indexing

```python
b"ABC"[0]
```

Output:

```text
65
```

### Encoding

```python
"Python".encode("utf-8")
```

Result:

```text
b"Python"
```

### Decoding

```python
b"Python".decode("utf-8")
```

Result:

```text
"Python"
```

### Valid byte range

```text
0 to 255
```

### Empty bytes

```python
b""
```

### Truthiness

```text
b""       → False
b"Python" → True
```

---

# 91. One-Line Definition

> **Bytes is an immutable sequence type in Python that stores binary data as integer values from 0 to 255 and is commonly used for files, networking, encoding, and other low-level data operations.**

---

# 92. Final Example

```python
text = "Hello Python"

# Convert string to bytes
data = text.encode("utf-8")

print(data)
print(type(data))

# Access individual byte
print(data[0])

# Convert bytes back to string
result = data.decode("utf-8")

print(result)
```

**Output:**

```text
b'Hello Python'
<class 'bytes'>
72
Hello Python
```

The complete flow is:

```text
"Hello Python"
       ↓
    encode()
       ↓
b"Hello Python"
       ↓
    bytes
       ↓
   decode()
       ↓
"Hello Python"
```

This is the most important concept to remember about the `bytes` datatype.