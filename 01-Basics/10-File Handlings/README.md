
# Python File Handling — Complete Notes

## 1. Introduction to File Handling

### What is File Handling?

File handling in Python means creating, reading, writing, appending, and managing files using Python programs.

A file allows us to store data permanently on a computer. Unlike a variable, whose value is not automatically saved for use in another program run, file data can remain available after the program finishes.

Example:

```python
name = "Teja"
print(name)
```

The variable stores the value while the program runs. To save the value in a file:

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write(name)
```

The file `student.txt` now contains:

```text
Teja
```

### Why do we need File Handling?

File handling is useful for:

- Saving student details.
- Storing marks and results.
- Saving application settings.
- Reading data from text files.
- Writing logs and reports.
- Processing CSV and JSON data.
- Saving information for future program runs.

---

## 2. The `open()` Function

The `open()` function opens a file and returns a file object.

### Syntax

```python
open(file, mode="r", encoding=None)
```

Parameters:

- `file`: The filename or path.
- `mode`: Specifies how the file should be opened.
- `encoding`: Specifies how text is decoded or encoded.

Example:

```python
file = open("student.txt", "r", encoding="utf-8")
print(file.read())
file.close()
```

Here:

1. `open()` opens the file.
2. `"r"` specifies read mode.
3. `file.read()` reads the content.
4. `file.close()` closes the file.

For normal file operations, prefer `with open()` because it closes the file automatically.

---

## 3. File Modes

A file mode tells Python what operation to perform.

| Mode | Meaning |
|---|---|
| `"r"` | Read an existing file |
| `"w"` | Write; creates or overwrites a file |
| `"a"` | Append content at the end |
| `"x"` | Create a new file exclusively |
| `"r+"` | Read and write without initially truncating |
| `"w+"` | Read and write; truncates existing content |
| `"a+"` | Read and append |
| `"rb"` | Read binary data |
| `"wb"` | Write binary data |
| `"ab"` | Append binary data |

### Important differences

**Read mode (`"r"`)**

- Opens an existing file for reading.
- Raises `FileNotFoundError` if the file cannot be found.

**Write mode (`"w"`)**

- Creates a file if it does not exist.
- Truncates existing content when the file is opened.

**Append mode (`"a"`)**

- Creates a file if it does not exist.
- Preserves existing content.
- Writes new content at the end.

**Exclusive creation mode (`"x"`)**

- Creates a new file.
- Raises `FileExistsError` if the path already exists.

Be careful with `"w"` because it can erase existing content.

---

## 4. Writing to a File Using `write()`

The `write()` method writes a string to a file.

### Example

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Hello Teja")
```

File content:

```text
Hello Teja
```

### Does `write()` add a newline automatically?

No.

Example:

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Python")
    file.write("Java")
```

File content:

```text
PythonJava
```

To write on separate lines, use `\n`.

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("SQL")
```

File content:

```text
Python
Java
SQL
```

### Return value of `write()`

`write()` returns the number of characters written.

```python
with open("student.txt", "w", encoding="utf-8") as file:
    result = file.write("Python")
    print(result)
```

Output:

```text
6
```

---

## 5. Writing Multiple Lines Using `writelines()`

The `writelines()` method writes multiple strings from an iterable.

Example:

```python
lines = ["Python\n", "Java\n", "SQL\n"]

with open("student.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

File content:

```text
Python
Java
SQL
```

### Important point

`writelines()` does not automatically add newline characters.

Example:

```python
with open("student.txt", "w", encoding="utf-8") as file:
    file.writelines(["Python", "Java", "SQL"])
```

File content:

```text
PythonJavaSQL
```

If you want separate lines, include `\n` in the strings.

---

## 6. Reading a File Using `read()`

The `read()` method returns the remaining file content as a string.

Suppose `student.txt` contains:

```text
Python
Java
SQL
```

Program:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

Output:

```text
Python
Java
SQL
```

### Reading a specified number of characters

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read(3))
```

Output:

```text
Pyt
```

`read(3)` reads up to three characters from the current position.

If fewer than three characters remain, it returns whatever remains.

---

## 7. Reading One Line Using `readline()`

The `readline()` method reads one line at a time.

Suppose the file contains:

```text
Python
Java
SQL
```

Program:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")
```

Output:

```text
Python
Java
```

### Internal execution

1. The first `readline()` reads `Python`.
2. The file position moves to the next line.
3. The second `readline()` reads `Java`.
4. The remaining line, `SQL`, is not read.

The newline character may be included in the string returned by `readline()`.

At the end of the file, `readline()` returns an empty string.

---

## 8. Reading All Lines Using `readlines()`

The `readlines()` method returns the remaining lines as a list of strings.

Example:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
```

Possible output:

```python
['Python\n', 'Java\n', 'SQL\n']
```

Each string can contain its newline character.

Access individual lines using indexing:

```python
print(lines[0])
print(lines[1])
print(lines[2])
```

Remember that list indexing starts at zero.

### Difference between reading methods

| Method | Returns |
|---|---|
| `read()` | One string containing all remaining content |
| `readline()` | One line as a string |
| `readlines()` | A list of remaining lines |
| `for line in file` | Iterates through lines one by one |

For very large files, iterating over the file is usually more memory-efficient than using `readlines()`.

---

## 9. Reading a File Using a `for` Loop

A file object can be used directly in a loop.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

Output:

```text
Python
Java
SQL
```

### Internal execution

Suppose the file contains three lines.

| Iteration | Value of `line` |
|---|---|
| 1 | `"Python\n"` |
| 2 | `"Java\n"` |
| 3 | `"SQL\n"` |

After the last line, there is no more content, so the loop stops.

This technique is especially useful when reading large files.

---

## 10. Appending Content Using `"a"`

Append mode adds content at the end without replacing existing content.

Suppose `student.txt` contains:

```text
Python
Java
```

Program:

```python
with open("student.txt", "a", encoding="utf-8") as file:
    file.write("SQL\n")
```

New content:

```text
Python
Java
SQL
```

This example assumes the existing file already ends with a newline.

If it does not, the appended text may join the final existing line. Add a newline when needed.

```python
with open("student.txt", "a", encoding="utf-8") as file:
    file.write("\nSQL")
```

This inserts a line break before `SQL`, although it can create a blank line if the file already ends with a newline.

### Difference between `"w"` and `"a"`

| `"w"` | `"a"` |
|---|---|
| Creates or overwrites content | Creates or preserves existing content |
| Existing content is truncated | Existing content is retained |
| Used to replace content | Used to add content |

---

## 11. Exclusive Creation Using `"x"`

The `"x"` mode creates a file only if the specified path does not already exist.

Example:

```python
with open("new_student.txt", "x", encoding="utf-8") as file:
    file.write("Teja")
```

If the file does not exist, it is created.

If it already exists, Python raises:

```text
FileExistsError
```

Example with exception handling:

```python
try:
    with open("new_student.txt", "x", encoding="utf-8") as file:
        file.write("Teja")
    print("File created successfully")

except FileExistsError:
    print("File already exists")
```

This is useful when you do not want to overwrite an existing file.

---

## 12. The `with open()` Statement

The `with` statement is the recommended way to work with files.

Example:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

### Why use `with`?

- It automatically closes the file when the block finishes.
- It closes the file even when an exception occurs inside the block.
- It reduces the chance of leaving files open accidentally.

The variable `file` refers to the file object.

The block of code belonging to `with` must be indented.

---

## 13. File Pointer: `tell()` and `seek()`

The file pointer represents the current stream position used for reading or writing.

Suppose `student.txt` contains:

```text
PYTHON
```

### `tell()`

The `tell()` method returns the current stream position.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.tell())
    print(file.read(3))
    print(file.tell())
```

For this simple ASCII text, the output is commonly:

```text
0
PYT
3
```

### `seek()`

The `seek()` method changes the file position.

```python
with open("student.txt", "r", encoding="utf-8") as file:
    file.seek(1)
    print(file.read(2))
```

Output:

```text
YT
```

### Difference

| Method | Purpose |
|---|---|
| `tell()` | Returns the current stream position |
| `seek()` | Changes the stream position |

In text mode, position values are not always simple character or byte counts, especially with multibyte encodings. Use binary mode when you need to work directly with byte offsets.

---

## 14. File Paths

A file path tells Python where a file is located.

### Relative path

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

A relative path is resolved from the current working directory.

### Absolute path

Example for Windows:

```python
with open(r"C:\Users\Teja\PythonProject\student.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

An absolute path specifies the complete location.

### Find the current working directory

```python
import os

print(os.getcwd())
```

`os.getcwd()` returns the current working directory.

It is not necessarily the directory where the Python source file is stored.

---

## 15. Exception Handling in File Operations

File operations can fail because a file is missing, permissions are insufficient, or another filesystem problem occurs.

### 15.1 `FileNotFoundError`

Occurs when a requested file cannot be found.

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
```

### 15.2 `PermissionError`

Can occur when the requested operation is not permitted.

```python
try:
    with open("protected.txt", "w", encoding="utf-8") as file:
        file.write("Hello")

except PermissionError:
    print("Permission denied")
```

### 15.3 `FileExistsError`

Occurs when `"x"` mode tries to create a path that already exists.

```python
try:
    with open("student.txt", "x", encoding="utf-8") as file:
        file.write("Hello")

except FileExistsError:
    print("File already exists")
```

### 15.4 `try`, `except`, `else`, and `finally`

- `try`: contains code that might raise an exception.
- `except`: handles a matching exception.
- `else`: runs if the `try` block completes without an exception.
- `finally`: runs during normal exception handling whether an exception occurred or not.

Example:

```python
try:
    with open("student.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found")

else:
    print(content)

finally:
    print("Operation finished")
```

The `with` statement already handles closing the file.

---

## 16. Checking Whether a File Exists

Using `os`:

```python
import os

print(os.path.exists("student.txt"))
```

This returns `True` if the path exists and `False` otherwise.

Check whether it is a regular file:

```python
import os

print(os.path.isfile("student.txt"))
```

Check whether it is a directory:

```python
import os

print(os.path.isdir("PythonProject"))
```

The result depends on the actual filesystem.

---

## 17. Creating, Renaming, and Deleting Files

### Rename a file

```python
import os

os.rename("old.txt", "new.txt")
```

The operation may fail if the source is missing or the filesystem does not permit the change.

### Delete a file

```python
import os

os.remove("unwanted.txt")
```

Be careful: deletion removes the file from the filesystem and should not be performed on important data accidentally.

### Create a directory

```python
import os

os.mkdir("reports")
```

This creates one directory. It raises an error if the directory already exists.

---

## 18. Using `pathlib`

The `pathlib` module provides an object-oriented way to work with filesystem paths.

```python
from pathlib import Path

path = Path("student.txt")

print(path.exists())
print(path.is_file())
print(path.name)
print(path.suffix)
```

Useful methods and properties:

| Method/property | Purpose |
|---|---|
| `Path.cwd()` | Current working directory |
| `Path.exists()` | Check whether a path exists |
| `Path.is_file()` | Check whether it is a file |
| `Path.is_dir()` | Check whether it is a directory |
| `Path.name` | Final path component |
| `Path.suffix` | File extension |
| `Path.parent` | Parent directory |
| `Path.mkdir()` | Create a directory |
| `Path.unlink()` | Delete a file |
| `Path.read_text()` | Read text |
| `Path.write_text()` | Write text |

Example:

```python
from pathlib import Path

path = Path("notes.txt")
path.write_text("Learn Python\n", encoding="utf-8")

content = path.read_text(encoding="utf-8")
print(content)
```

`write_text()` replaces existing content, so use it carefully.

---

## 19. Binary File Handling

Binary files store data as bytes rather than decoded text.

Examples include images, audio, PDFs, and other non-text formats.

### Read binary data

```python
with open("image.png", "rb") as file:
    data = file.read()

print(type(data))
```

Output:

```text
<class 'bytes'>
```

### Write binary data

```python
with open("copy.bin", "wb") as file:
    file.write(b"Hello")
```

The prefix `b` creates a bytes literal.

### Copy a large binary file in chunks

```python
with open("source.bin", "rb") as source:
    with open("destination.bin", "wb") as destination:
        while True:
            chunk = source.read(4096)

            if not chunk:
                break

            destination.write(chunk)
```

Reading in chunks avoids loading the entire file into memory.

---

## 20. CSV File Handling

CSV stands for Comma-Separated Values. It is commonly used to store tabular data.

Example `students.csv`:

```csv
name,marks
Teja,90
Ravi,85
```

### Read CSV

```python
import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

### Read CSV using `DictReader`

```python
import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["marks"])
```

### Write CSV

```python
import csv

rows = [
    ["name", "marks"],
    ["Teja", 90],
    ["Ravi", 85]
]

with open("students_out.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

Using the `csv` module is safer than manually splitting strings on commas because CSV supports quoted fields.

---

## 21. JSON File Handling

JSON stands for JavaScript Object Notation. It is commonly used for structured data exchange.

Example JSON data:

```json
{
    "name": "Teja",
    "skills": ["Python", "SQL"],
    "active": true
}
```

### Write JSON

```python
import json

student = {
    "name": "Teja",
    "skills": ["Python", "SQL"],
    "active": True
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)
```

### Read JSON

```python
import json

with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student["name"])
print(student["skills"])
```

`json.dump()` writes a Python object to a JSON file.

`json.load()` reads JSON data from a file and converts it into Python values.

---

## 22. Common Mistakes

### Mistake 1: Using read mode for a missing file

```python
open("missing.txt", "r")
```

This normally raises `FileNotFoundError`.

### Mistake 2: Accidentally overwriting content

```python
open("important.txt", "w")
```

Opening in `"w"` mode truncates an existing file.

### Mistake 3: Expecting automatic newlines

```python
file.write("Python")
file.write("Java")
```

Result:

```text
PythonJava
```

### Mistake 4: Confusing `seek(1)` with moving backward by one character

`seek(1)` moves to the position represented by `1`; it does not mean move backward by one character.

### Mistake 5: Forgetting to close files

Prefer:

```python
with open("student.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

### Mistake 6: Ignoring file paths

Use `os.getcwd()` to find the current working directory when a relative file path is not behaving as expected.

---

## 23. Practice Programs

### Program 1: Write text to a file

```python
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to Python\n")
```

### Program 2: Read a file

```python
with open("message.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

### Program 3: Append content

```python
with open("message.txt", "a", encoding="utf-8") as file:
    file.write("I am learning file handling.\n")
```

### Program 4: Count lines

```python
count = 0

with open("message.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print("Number of lines:", count)
```

### Program 5: Count words

```python
word_count = 0

with open("message.txt", "r", encoding="utf-8") as file:
    for line in file:
        word_count += len(line.split())

print("Word count:", word_count)
```

This counts whitespace-separated tokens as words.

### Program 6: Count characters

```python
character_count = 0

with open("message.txt", "r", encoding="utf-8") as file:
    for line in file:
        character_count += len(line)

print("Character count:", character_count)
```

This includes newline characters in the count.

### Program 7: Copy a text file

```python
with open("source.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("destination.txt", "w", encoding="utf-8") as destination:
    destination.write(content)
```

This simple version reads the entire source file into memory. For large files, use chunks.

### Program 8: Find lines containing a word

```python
target = "Python"

with open("message.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if target.lower() in line.lower():
            print(line_number, line.rstrip("\n"))
```

### Program 9: Save a dictionary to JSON

```python
import json

student = {"name": "Teja", "marks": 90}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)
```

### Program 10: Load a dictionary from JSON

```python
import json

with open("student.json", "r", encoding="utf-8") as file:
    student = json.load(file)

print(student)
```

---

## 24. Interview Questions

1. What is file handling in Python?
2. What does the `open()` function return?
3. What is the difference between `"r"`, `"w"`, `"a"`, and `"x"`?
4. Why can `"w"` mode be dangerous?
5. What is the difference between `write()` and `writelines()`?
6. Does `writelines()` automatically add newlines?
7. What is the difference between `read()`, `readline()`, and `readlines()`?
8. Why is `with open()` recommended?
9. What does `tell()` do?
10. What does `seek()` do?
11. What is the difference between relative and absolute paths?
12. What does `os.getcwd()` return?
13. What is `FileNotFoundError`?
14. What is `FileExistsError`?
15. What is the difference between text mode and binary mode?
16. Why is UTF-8 commonly used for text files?
17. How can you check whether a file exists?
18. What is the purpose of `pathlib`?
19. How do you read and write CSV files?
20. How do you read and write JSON files?
21. How can you process a large file efficiently?
22. How do you copy a binary file?

---

## 25. Quick Revision

| Concept | Meaning |
|---|---|
| `open()` | Opens a file |
| `"r"` | Read |
| `"w"` | Write or overwrite |
| `"a"` | Append |
| `"x"` | Create exclusively |
| `read()` | Read remaining content |
| `readline()` | Read one line |
| `readlines()` | Read lines into a list |
| `write()` | Write a string |
| `writelines()` | Write multiple strings |
| `with open()` | Automatically closes the file |
| `tell()` | Get the current stream position |
| `seek()` | Change the stream position |
| `os.getcwd()` | Get the current working directory |
| `pathlib` | Work with filesystem paths |
| `csv` | Handle CSV data |
| `json` | Handle JSON data |

---

## Recommended Learning Order

1. Learn `open()`, `read()`, `write()`, and file modes.
2. Practise `readline()`, `readlines()`, and loops.
3. Understand append mode and exclusive creation.
4. Learn `with open()`.
5. Practise `tell()` and `seek()`.
6. Understand relative and absolute paths.
7. Practise exception handling.
8. Learn file and directory operations.
9. Study binary files, CSV, and JSON.

**Important:** Before running any example using `"w"` mode, check whether the target file contains data you want to preserve.
