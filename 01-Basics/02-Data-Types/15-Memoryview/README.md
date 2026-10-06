# Memoryview (`memoryview`) Data Type in Python

## 1. What is `memoryview`?

`memoryview` is a built-in Python type that allows us to **access the memory of another binary object without making a copy of its data**.

In simple words:

> **memoryview gives us a view of existing binary data instead of creating a new copy.**

It is mainly useful when working with large amounts of binary data.

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view)
print(type(view))
```

Output:

```text
<memory at 0x...>
<class 'memoryview'>
```

The important point is that `view` does not contain a separate copy of `"Hello"`.

It refers to the memory of `data`.

---

# 2. Why do we need `memoryview`?

Consider a large binary object:

```python
data = bytearray(b"Hello World")
```

If we create another object containing the same data:

```python
data2 = bytes(data)
```

Python may need to create another copy of the data.

With `memoryview`:

```python
view = memoryview(data)
```

we can work with the existing memory directly.

So:

```text
bytearray
   │
   │ existing memory
   ▼
memoryview
   │
   │ view
   ▼
same underlying data
```

This can be useful for **performance and memory efficiency**, especially with large binary data.

---

# 3. Creating a memoryview

The basic syntax is:

```python
memoryview(object)
```

Example:

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view)
```

Output:

```text
<memory at 0x...>
```

---

# 4. Type of memoryview

We can use `type()`:

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(type(view))
```

Output:

```text
<class 'memoryview'>
```

We can also use `isinstance()`:

```python
print(isinstance(view, memoryview))
```

Output:

```text
True
```

---

# 5. Memoryview works with binary objects

`memoryview` works with objects that support Python's **buffer protocol**.

Common examples include:

```text
bytes
bytearray
array.array
```

For example:

```python
data = bytearray(b"Python")

view = memoryview(data)

print(view)
```

---

# 6. Memoryview with bytes

We can create a memoryview from `bytes`:

```python
data = b"Hello"

view = memoryview(data)

print(view)
```

A `bytes` object is immutable.

Therefore, its memoryview is also **read-only**.

```python
data = b"Hello"

view = memoryview(data)

print(view.readonly)
```

Output:

```text
True
```

Trying to modify it:

```python
view[0] = 72
```

will raise:

```text
TypeError
```

because the original `bytes` object cannot be modified.

---

# 7. Memoryview with bytearray

This is one of the most important examples.

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.readonly)
```

Output:

```text
False
```

Because `bytearray` is mutable.

We can modify the data through the memoryview:

```python
data = bytearray(b"Hello")

view = memoryview(data)

view[0] = 72

print(data)
```

Output:

```text
bytearray(b'Hello')
```

`72` is the ASCII value of `H`, so the result looks unchanged.

Let's use another value:

```python
data = bytearray(b"Hello")

view = memoryview(data)

view[0] = 74

print(data)
```

Output:

```text
bytearray(b'Jello')
```

The important idea is:

```text
data
 │
 │ same underlying memory
 ▼
memoryview
```

Changing the memoryview changes the original `bytearray`.

---

# 8. Memoryview does not make a copy

This is the main concept.

```python
data = bytearray(b"Hello")

view = memoryview(data)
```

Think of it like this:

```text
Original data
┌─────────────────────┐
│ H │ e │ l │ l │ o │
└─────────────────────┘
          ▲
          │
      memoryview
```

The memoryview is simply looking at the existing memory.

It is **not another independent copy** of the data.

---

# 9. Indexing memoryview

A memoryview can be indexed.

```python
data = bytearray(b"Python")

view = memoryview(data)

print(view[0])
print(view[1])
print(view[2])
```

Output:

```text
80
121
116
```

Remember:

```text
P → 80
y → 121
t → 116
```

For a byte-oriented memoryview, indexing normally gives an integer representing the byte value.

---

# 10. Negative indexing

Negative indexing works like other sequence types.

```python
data = bytearray(b"Python")

view = memoryview(data)

print(view[-1])
print(view[-2])
```

Output:

```text
110
111
```

Because:

```text
Python
     ↑
     n
```

---

# 11. Length of memoryview

Use `len()`:

```python
data = bytearray(b"Python")

view = memoryview(data)

print(len(view))
```

Output:

```text
6
```

Because `"Python"` contains six bytes in ASCII/UTF-8.

---

# 12. Slicing memoryview

We can slice a memoryview.

```python
data = bytearray(b"Python")

view = memoryview(data)

part = view[0:3]

print(part)
```

The result is another memoryview:

```text
<memory at 0x...>
```

We can convert it to bytes:

```python
print(part.tobytes())
```

Output:

```text
b'Pyt'
```

Important:

> A memoryview slice is another view into the underlying buffer rather than an ordinary copied bytes object.

---

# 13. Changing data through a sliced memoryview

Example:

```python
data = bytearray(b"Python")

view = memoryview(data)

part = view[0:3]

part[0] = 74

print(data)
```

Output:

```text
bytearray(b'Jython')
```

Why?

Because:

```text
data
 │
 └── underlying memory
          ▲
          │
       view
          ▲
          │
       part
```

Both views refer to the same underlying data.

---

# 14. `readonly`

The `readonly` attribute tells us whether the memoryview can modify the underlying object.

Example with `bytes`:

```python
data = b"Hello"

view = memoryview(data)

print(view.readonly)
```

Output:

```text
True
```

Example with `bytearray`:

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.readonly)
```

Output:

```text
False
```

So:

```text
bytes      → read-only memoryview
bytearray  → writable memoryview
```

---

# 15. `tobytes()`

The `tobytes()` method creates a `bytes` object containing the data.

```python
data = bytearray(b"Hello")

view = memoryview(data)

result = view.tobytes()

print(result)
print(type(result))
```

Output:

```text
b'Hello'
<class 'bytes'>
```

Remember:

```text
memoryview → bytes
```

using:

```python
view.tobytes()
```

---

# 16. `tolist()`

`tolist()` converts the memoryview data into a list.

```python
data = bytearray(b"ABC")

view = memoryview(data)

print(view.tolist())
```

Output:

```text
[65, 66, 67]
```

Because:

```text
A → 65
B → 66
C → 67
```

---

# 17. `hex()`

We can represent the data in hexadecimal.

```python
data = bytearray(b"ABC")

view = memoryview(data)

print(view.hex())
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

# 18. `obj` attribute

The `obj` attribute tells us about the original object that the memoryview is viewing.

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.obj)
```

Output:

```text
bytearray(b'Hello')
```

So:

```python
view.obj
```

refers to the underlying object.

---

# 19. `format`

The `format` attribute tells us the format of the elements in the viewed buffer.

For a normal byte-oriented object:

```python
data = bytearray(b"ABC")

view = memoryview(data)

print(view.format)
```

Output:

```text
B
```

`B` represents an unsigned byte.

---

# 20. `itemsize`

`itemsize` tells us the size of one element in bytes.

```python
data = bytearray(b"ABC")

view = memoryview(data)

print(view.itemsize)
```

Output:

```text
1
```

Each byte occupies one byte.

---

# 21. `nbytes`

`nbytes` tells us the total number of bytes represented by the memoryview.

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.nbytes)
```

Output:

```text
5
```

Difference:

```text
len(view)
```

and

```text
view.nbytes
```

For a simple byte-oriented memoryview they are often the same.

For multidimensional or differently formatted views, they can differ.

---

# 22. `ndim`

`ndim` tells us the number of dimensions of the viewed data.

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.ndim)
```

Output:

```text
1
```

A normal bytearray gives us a one-dimensional view.

---

# 23. `shape`

`shape` describes the dimensions of the viewed data.

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.shape)
```

Output is typically:

```text
(5,)
```

This means:

```text
5 elements
1 dimension
```

---

# 24. `strides`

`strides` tells us the number of bytes that need to be moved to reach the next element along each dimension.

Example:

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.strides)
```

For a simple byte view, it is typically:

```text
(1,)
```

because each element is one byte apart.

---

# 25. Memoryview and string

We cannot directly create a memoryview from a normal Python string.

This will fail:

```python
name = "Hello"

view = memoryview(name)
```

because `str` does not provide the required buffer interface.

Instead, convert the string into bytes:

```python
name = "Hello"

data = name.encode()

view = memoryview(data)

print(view)
```

Now it works.

The process is:

```text
str
 ↓
encode()
 ↓
bytes
 ↓
memoryview
```

---

# 26. String → memoryview

Example:

```python
text = "Python"

data = text.encode("utf-8")

view = memoryview(data)

print(view.tolist())
```

Output:

```text
[80, 121, 116, 104, 111, 110]
```

To convert it back:

```python
result = view.tobytes().decode("utf-8")

print(result)
```

Output:

```text
Python
```

---

# 27. UTF-8 and memoryview

This is important when working with non-English characters.

For example:

```python
text = "A"
print(len(text.encode("utf-8")))
```

Output:

```text
1
```

But:

```python
text = "₹"

print(len(text))
print(len(text.encode("utf-8")))
```

The character count and byte count can be different.

This is important because `memoryview` works with the **underlying bytes**, not directly with characters.

---

# 28. Memoryview and bytearray modification

Example:

```python
data = bytearray(b"ABCDE")

view = memoryview(data)

view[1] = 90

print(data)
```

Output:

```text
bytearray(b'AZCDE')
```

Because:

```text
B → 66
Z → 90
```

The memoryview modified the original bytearray.

---

# 29. Memoryview vs bytes

### `bytes`

```python
data = b"Hello"
```

Properties:

```text
Immutable
Cannot modify
Binary data
Memoryview created from it is read-only
```

### `memoryview`

```python
view = memoryview(data)
```

Properties:

```text
Provides a view
Does not need to copy the data
Can access the underlying buffer
Can be read-only or writable depending on source
```

---

# 30. Memoryview vs bytearray

| Feature | bytearray | memoryview |
|---|---|---|
| Mutable | Yes | Depends on source |
| Stores its own data | Yes | No separate copy |
| Binary data | Yes | Views binary data |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Can modify source | Directly | If source is writable |
| Hashable | No | No |
| Main purpose | Store/change bytes | Efficiently access existing buffer |

Simple idea:

```text
bytearray = actual mutable data

memoryview = window/view over existing data
```

---

# 31. Memoryview vs bytes vs bytearray

```text
bytes
  ↓
Immutable binary data

bytearray
  ↓
Mutable binary data

memoryview
  ↓
View of existing binary data
```

This is one of the most important things to remember.

---

# 32. Memoryview is not a normal copy

Consider:

```python
data = bytearray(b"Hello")

view = memoryview(data)
```

We can modify the original:

```python
data[0] = 74

print(view[0])
```

Output:

```text
74
```

The view sees the change because it refers to the same underlying memory.

---

# 33. Changes through memoryview are visible in original object

```python
data = bytearray(b"Hello")

view = memoryview(data)

view[0] = 74

print(data)
```

Output:

```text
bytearray(b'Jello')
```

So:

```text
memoryview modification
        ↓
underlying memory changes
        ↓
original object changes
```

---

# 34. `release()`

A memoryview can be released when we no longer need it.

```python
data = bytearray(b"Hello")

view = memoryview(data)

view.release()
```

After releasing it, operations using the view can raise:

```text
ValueError
```

`release()` is useful when we want to explicitly release the view.

---

# 35. Why resizing can be a problem

Suppose:

```python
data = bytearray(b"Hello")

view = memoryview(data)
```

The memoryview is currently using the bytearray's buffer.

While the view is active, operations that resize the underlying bytearray may raise `BufferError`.

For example:

```python
data = bytearray(b"Hello")

view = memoryview(data)

data.append(33)
```

This can raise:

```text
BufferError
```

Why?

Because changing the size of the bytearray could invalidate the memory location being viewed.

After releasing the view:

```python
view.release()

data.append(33)

print(data)
```

Output:

```text
bytearray(b'Hello!')
```

Important:

> A memoryview can prevent resizing of its underlying buffer while the view is active.

---

# 36. Memoryview and membership

We can check whether a byte value exists.

```python
data = bytearray(b"Python")

view = memoryview(data)

print(80 in view)
```

Output:

```text
True
```

Because:

```text
P → 80
```

---

# 37. Iterating over memoryview

We can use a loop:

```python
data = bytearray(b"ABC")

view = memoryview(data)

for value in view:
    print(value)
```

Output:

```text
65
66
67
```

Again, iteration gives byte values.

---

# 38. Converting memoryview to list

```python
data = bytearray(b"ABC")

view = memoryview(data)

numbers = list(view)

print(numbers)
```

Output:

```text
[65, 66, 67]
```

---

# 39. Converting memoryview to bytes

```python
data = bytearray(b"Python")

view = memoryview(data)

result = bytes(view)

print(result)
```

Output:

```text
b'Python'
```

Another common way:

```python
result = view.tobytes()
```

---

# 40. Converting memoryview to bytearray

```python
data = b"Python"

view = memoryview(data)

result = bytearray(view)

print(result)
```

Output:

```text
bytearray(b'Python')
```

---

# 41. `cast()` method

`cast()` allows us to view the same underlying memory using a different format.

For example, a byte-oriented view can sometimes be interpreted as another format.

Basic idea:

```python
view.cast(format)
```

Example:

```python
data = bytearray([1, 0, 2, 0])

view = memoryview(data)

new_view = view.cast('H')

print(new_view.tolist())
```

The exact result depends on the machine's byte order.

The important concept is:

> `cast()` changes how the existing bytes are interpreted; it does not simply create a new copy of the data.

`cast()` is mainly useful for advanced binary-data processing.

---

# 42. Memoryview and binary files

Memoryview can be useful when dealing with binary files.

For example, binary data may be read into memory:

```python
data = bytearray(b"Binary Data")

view = memoryview(data)
```

We can inspect or modify portions of that buffer without creating separate copies for every operation.

This can be useful for:

- Binary file processing
- Image processing
- Audio processing
- Network packets
- Large data buffers
- Protocol handling

---

# 43. Memoryview and networking

Network applications often deal with binary data.

For example:

```text
Network
   ↓
Binary data
   ↓
bytearray / bytes
   ↓
memoryview
   ↓
Process selected part
```

Instead of repeatedly copying large buffers, a memoryview can provide access to the required section.

This can improve efficiency in suitable applications.

---

# 44. Memoryview and large data

Suppose we have a large bytearray:

```python
data = bytearray(10_000_000)
```

Creating multiple copies of portions of the data can consume additional memory.

A memoryview can allow us to work with sections of the existing buffer.

Conceptually:

```text
Large buffer
┌──────────────────────────────────────┐
│                                      │
│             Large Data               │
│                                      │
└──────────────────────────────────────┘
          ▲
          │
      memoryview
          │
          ▼
    selected section
```

This is one reason memoryview exists.

---

# 45. Memoryview is useful for performance

The main advantage is:

```text
Avoid unnecessary copying
        ↓
Less memory usage
        ↓
Potentially better performance
```

However, `memoryview` does not automatically make every program faster.

It is most useful when processing large binary buffers or when avoiding copies matters.

---

# 46. Common memoryview attributes

| Attribute | Meaning |
|---|---|
| `format` | Format of each element |
| `itemsize` | Size of each element in bytes |
| `ndim` | Number of dimensions |
| `shape` | Shape of the viewed data |
| `strides` | Byte steps between elements |
| `nbytes` | Total bytes represented |
| `readonly` | Whether the view is read-only |
| `obj` | Underlying object |
| `c_contiguous` | Whether data is C-contiguous |
| `f_contiguous` | Whether data is Fortran-contiguous |
| `contiguous` | Whether data is contiguous |

---

# 47. Important memoryview methods

| Method | Purpose |
|---|---|
| `tobytes()` | Convert view to bytes |
| `tolist()` | Convert view to list |
| `hex()` | Get hexadecimal representation |
| `release()` | Release the view |
| `cast()` | View data using another format |

---

# 48. `memoryview` is not hashable

A memoryview cannot generally be used like a normal hashable immutable object.

For example, do not think of it as something you can freely use as:

```python
my_set = {view}
```

Hashability depends on the memoryview's format and readonly/contiguous properties, and writable views are not hashable.

For normal learning purposes:

> **A writable memoryview is not hashable.**

---

# 49. Truthiness

A memoryview can be checked in an `if` statement.

```python
data = bytearray(b"Hello")

view = memoryview(data)

if view:
    print("Memoryview contains data")
```

Output:

```text
Memoryview contains data
```

An empty memoryview is false:

```python
data = bytearray()

view = memoryview(data)

print(bool(view))
```

Output:

```text
False
```

---

# 50. `memoryview` and `is`

Remember that `is` checks object identity.

```python
data = bytearray(b"Hello")

view1 = memoryview(data)
view2 = memoryview(data)

print(view1 is view2)
```

Output:

```text
False
```

They are two different memoryview objects.

But both can refer to the same underlying object:

```python
print(view1.obj is data)
print(view2.obj is data)
```

Output:

```text
True
True
```

---

# 51. Practical Example 1 — Modify one byte

```python
data = bytearray(b"Hello")

view = memoryview(data)

view[0] = ord("J")

print(data)
```

Output:

```text
bytearray(b'Jello')
```

---

# 52. Practical Example 2 — Read byte values

```python
data = bytearray(b"ABC")

view = memoryview(data)

for value in view:
    print(value)
```

Output:

```text
65
66
67
```

---

# 53. Practical Example 3 — Modify multiple bytes

```python
data = bytearray(b"Hello")

view = memoryview(data)

view[1:3] = b"EY"

print(data)
```

Output:

```text
bytearray(b"HEYlo")
```

The assigned data must be compatible with the selected view.

---

# 54. Practical Example 4 — Convert to bytes

```python
data = bytearray(b"Python")

view = memoryview(data)

result = view.tobytes()

print(result)
```

Output:

```text
b'Python'
```

---

# 55. Practical Example 5 — Convert to list

```python
data = bytearray(b"ABC")

view = memoryview(data)

print(view.tolist())
```

Output:

```text
[65, 66, 67]
```

---

# 56. Practical Example 6 — Check read-only status

```python
data = bytes(b"Hello")

view = memoryview(data)

print(view.readonly)
```

Output:

```text
True
```

For bytearray:

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.readonly)
```

Output:

```text
False
```

---

# 57. Practical Example 7 — String to memoryview

```python
text = "Python"

data = text.encode("utf-8")

view = memoryview(data)

print(view.tolist())
```

Output:

```text
[80, 121, 116, 104, 111, 110]
```

---

# 58. Practical Example 8 — Modify original data through view

```python
data = bytearray(b"ABCDE")

view = memoryview(data)

view[2] = ord("Z")

print(data)
```

Output:

```text
bytearray(b'ABZDE')
```

---

# 59. Practical Example 9 — View a portion of data

```python
data = bytearray(b"Python Programming")

view = memoryview(data)

part = view[0:6]

print(part.tobytes())
```

Output:

```text
b'Python'
```

---

# 60. Practical Example 10 — Release memoryview

```python
data = bytearray(b"Hello")

view = memoryview(data)

print(view.tobytes())

view.release()
```

Output:

```text
b'Hello'
```

After `release()`, the view should no longer be used.

---

# 61. Memoryview vs List

### List

```python
data = [65, 66, 67]
```

A list stores Python objects.

### Memoryview

```python
data = bytearray(b"ABC")

view = memoryview(data)
```

A memoryview accesses an existing buffer.

So they serve different purposes.

```text
list
 ↓
General-purpose collection

memoryview
 ↓
Efficient view of binary memory
```

---

# 62. Memoryview vs String

```python
text = "Python"
```

A string represents text/Unicode characters.

```python
view = memoryview(text)
```

This does not work because `str` does not expose the required buffer interface.

Instead:

```python
data = text.encode("utf-8")
view = memoryview(data)
```

So:

```text
str
 ↓ encode()
bytes
 ↓
memoryview
```

---

# 63. Memoryview vs bytes vs bytearray vs str

| Type | Main purpose | Mutable? |
|---|---|---|
| `str` | Text | No |
| `bytes` | Binary data | No |
| `bytearray` | Mutable binary data | Yes |
| `memoryview` | View existing binary memory | Depends on source |

Remember:

```text
str        → text

bytes      → immutable binary data

bytearray  → mutable binary data

memoryview → view of existing binary data
```

---

# 64. Important characteristics

`memoryview` is:

- A built-in Python type
- Used for binary data
- A view rather than a separate data copy
- Based on the buffer protocol
- Useful with `bytes`
- Useful with `bytearray`
- Can be read-only or writable
- Supports indexing
- Supports slicing
- Supports iteration
- Supports conversion to bytes/list
- Can expose format and memory-layout information
- Useful for efficient binary processing
- Useful for large buffers
- Useful in networking and file processing
- Useful in performance-sensitive applications

---

# 65. Common mistakes

### Mistake 1: Thinking memoryview stores a copy

```python
view = memoryview(data)
```

It is a view of existing buffer data.

---

### Mistake 2: Trying to create memoryview directly from string

```python
memoryview("Hello")
```

This does not work.

Use:

```python
memoryview("Hello".encode())
```

---

### Mistake 3: Trying to modify a bytes-based memoryview

```python
data = b"Hello"

view = memoryview(data)

view[0] = 72
```

This fails because `bytes` is immutable.

---

### Mistake 4: Forgetting that indexing gives byte values

```python
data = bytearray(b"ABC")

view = memoryview(data)

print(view[0])
```

Output:

```text
65
```

Not:

```text
A
```

---

### Mistake 5: Resizing the underlying bytearray while a view exists

```python
data = bytearray(b"Hello")

view = memoryview(data)

data.append(33)
```

This can raise `BufferError`.

Release the view first when appropriate:

```python
view.release()
data.append(33)
```

---

# 66. Important functions and methods

| Function / Method | Purpose |
|---|---|
| `memoryview()` | Create a memoryview |
| `type()` | Check type |
| `isinstance()` | Check whether object is memoryview |
| `len()` | Number of elements |
| `bool()` | Check whether view is non-empty |
| `bytes()` | Convert to bytes |
| `bytearray()` | Convert to bytearray |
| `list()` | Convert to list |
| `tobytes()` | Convert view to bytes |
| `tolist()` | Convert view to list |
| `hex()` | Convert/view data as hexadecimal |
| `release()` | Release the view |
| `cast()` | View the same memory using another format |

---

# 67. Time and memory idea

The major advantage of memoryview is avoiding unnecessary data copies.

For example:

```text
Without memoryview:

Large data
   ↓
copy
   ↓
new object
   ↓
more memory


With memoryview:

Large data
   ↓
memoryview
   ↓
same underlying memory
```

This can be especially useful for large binary buffers.

---

# 68. Simple mental model

Think of `memoryview` like a **window**.

```text
                Memoryview
                   ↓
          ┌─────────────────┐
          │     WINDOW      │
          └─────────────────┘
                   ↓
       ┌──────────────────────┐
       │ Existing binary data │
       │ A B C D E F G H ...  │
       └──────────────────────┘
```

The window does not create another house.

It simply lets you look at a particular part of the existing data.

Similarly:

> **memoryview does not need to copy the underlying buffer; it provides a view of it.**

---

# 69. Quick Revision

```text
memoryview
    ↓
View of existing binary memory
```

### Main points

```text
memoryview(data)
```

- Used for binary/buffer data
- Does not simply create a separate copy
- Works with buffer-supporting objects
- `bytes` → read-only view
- `bytearray` → writable view
- Indexing gives byte values
- Supports slicing
- `tobytes()` → bytes
- `tolist()` → list
- `hex()` → hexadecimal representation
- `readonly` → tells whether it can be modified
- `obj` → underlying object
- `format` → element format
- `itemsize` → size of each element
- `nbytes` → total bytes represented
- `ndim` → dimensions
- `shape` → dimensions/shape
- `strides` → memory steps
- `release()` → release view
- `cast()` → reinterpret existing buffer using another format
- Useful for large binary data and performance-sensitive processing

---

# 70. Final Comparison

```text
str
 ↓
Text / Unicode characters


bytes
 ↓
Immutable binary data


bytearray
 ↓
Mutable binary data


memoryview
 ↓
View/access existing binary memory
```

The most important distinction is:

```text
bytes      → immutable binary data

bytearray  → mutable binary data

memoryview → view of existing binary data
```

### One-line definition

> **`memoryview` is a built-in Python type that provides a view of an object's binary buffer without requiring a separate copy of the underlying data.**