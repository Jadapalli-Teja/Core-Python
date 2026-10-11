# Python Modules and Packages

## 1. Introduction

As Python programs become larger, writing all the code in a single file becomes difficult to manage.

Python provides two important ways to organize code:

1. **Modules** — organize code into separate Python files.
2. **Packages** — organize related modules into directories.

For example, consider a student management application. It might contain code for student details, marks, attendance, and fees.

Instead of putting everything into one file, we can organize it like this:

```text
student_app/
├── main.py
├── students.py
├── marks.py
├── attendance.py
└── fees.py
```

Here, each `.py` file is a module.

If the application grows further, we can group related modules into packages:

```text
student_app/
├── main.py
├── students/
│   ├── __init__.py
│   ├── details.py
│   └── attendance.py
└── finance/
    ├── __init__.py
    ├── fees.py
    └── payments.py
```

Here, `students` and `finance` are regular Python packages, and the files inside them are modules.

---

# PART 1: MODULES

## 2. What Is a Module?

A **module is a Python file containing code that can be reused or imported into another Python file.**

A module can contain:

- Variables
- Functions
- Classes
- Import statements
- Executable statements

Example:

```python
# calculator.py

number = 100

def add(a, b):
    return a + b

class Calculator:
    def multiply(self, a, b):
        return a * b
```

In this example, `calculator.py` is a module.

Its contents include a variable named `number`, a function named `add()`, and a class named `Calculator`.

## 3. Why Do We Use Modules?

Modules help us:

- Reuse code in multiple files.
- Separate different responsibilities.
- Avoid repeatedly writing the same functions.
- Maintain and test programs more easily.
- Organize large applications.

## 4. Types of Modules

### 4.1 Built-in and standard-library modules

Python provides modules for common tasks.

Examples include:

```python
import math
import random
import os
import sys
import datetime
import json
```

Example:

```python
import math

print(math.sqrt(25))
print(math.factorial(5))
```

Output:

```text
5.0
120
```

### 4.2 User-defined modules

These are modules created by us.

**greetings.py**

```python
def greet(name):
    return f"Hello, {name}!"
```

**main.py**

```python
import greetings

print(greetings.greet("Teja"))
```

Output:

```text
Hello, Teja!
```

### 4.3 Third-party modules

These are provided by external libraries and may require installation.

For example, install `requests` with:

```bash
python -m pip install requests
```

Then:

```python
import requests
```

---

## 5. Importing Modules

Suppose we have these files:

```text
project/
├── main.py
└── calculator.py
```

**calculator.py**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### 5.1 Using `import`

**main.py**

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

Output:

```text
15
5
```

When we use `import calculator`, we access its functions using the module name:

```python
calculator.add(10, 5)
```

### 5.2 Using `from ... import`

```python
from calculator import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

Output:

```text
15
5
```

We can call the imported functions directly.

### 5.3 Using aliases

```python
import calculator as calc

print(calc.add(20, 30))
```

Output:

```text
50
```

### 5.4 Importing everything

```python
from calculator import *
```

This requests the names exposed by the module for star imports. Avoid this style in normal projects because it can make names and their origins difficult to identify.

Prefer explicit imports.

---

## 6. How Does Python Execute a Module During Import?

Consider:

**message.py**

```python
print("Message module started")

def greet():
    print("Hello")

print("Message module finished")
```

**main.py**

```python
import message

print("Main program started")

message.greet()
```

Output:

```text
Message module started
Message module finished
Main program started
Hello
```

### Step-by-step execution

**Step 1:** Python reaches `import message`.

**Step 2:** Python searches for the module using its import system.

**Step 3:** When the module is found and has not already been loaded, Python creates its module object and executes its top-level code.

**Step 4:** The first `print()` executes.

```text
Message module started
```

**Step 5:** Python defines the `greet()` function. Its body does not execute yet.

**Step 6:** The final top-level `print()` executes.

```text
Message module finished
```

**Step 7:** The import completes. Python continues executing `main.py`.

**Step 8:** `message.greet()` calls the function, producing:

```text
Hello
```

**Important:** Importing a module executes its top-level statements, but it does not automatically call every function defined inside it.

---

## 7. The `__name__` Variable

Python provides a special variable named `__name__`.

When a file is executed directly, its `__name__` is normally `"__main__"`.

When imported as a module, its `__name__` is normally the module's import name.

**demo.py**

```python
print(__name__)
```

Run it directly:

```bash
python demo.py
```

Output:

```text
__main__
```

Import it from another file:

```python
import demo
```

Output:

```text
demo
```

### The `if __name__ == "__main__":` pattern

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

The `print()` runs when this file is executed directly, but not when it is imported under another module name.

This helps us keep reusable code separate from demonstration or entry-point code.

---

# PART 2: PACKAGES

## 8. What Is a Package?

A **package is a way to organize related Python modules into a hierarchical structure.**

A package usually consists of a directory containing Python modules and, for a regular package, an `__init__.py` file.

Consider this structure:

```text
project/
├── main.py
└── calculations/
    ├── __init__.py
    ├── addition.py
    ├── subtraction.py
    └── multiplication.py
```

Understand each item:

| Item | Meaning |
|---|---|
| `project/` | Project directory |
| `main.py` | Main Python module |
| `calculations/` | Package directory |
| `__init__.py` | Package initialization file |
| `addition.py` | Module inside the package |
| `subtraction.py` | Module inside the package |
| `multiplication.py` | Module inside the package |

The package groups related calculation modules together.

Without a package structure, a large project can end up with many unrelated Python files in one directory.

---

## 9. Why Do We Need Packages?

Imagine an application with 20 modules.

If every module is kept in the same directory, finding the correct file can become difficult.

Packages let us group related modules together.

For example:

```text
college_app/
├── main.py
├── students/
│   ├── __init__.py
│   ├── details.py
│   ├── marks.py
│   └── attendance.py
└── finance/
    ├── __init__.py
    ├── fees.py
    └── payments.py
```

The `students` package contains student-related modules.

The `finance` package contains finance-related modules.

Benefits:

- Better organization.
- Easier navigation.
- Clear separation of responsibilities.
- Fewer unrelated files in the same directory.
- A structure that can grow with the application.

---

## 10. Create Your First Package Step by Step

Let's build a package named `calculations`.

### Step 1: Create the directory structure

```text
project/
├── main.py
└── calculations/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py
```

Create the `calculations` directory and the three files inside it.

### Step 2: Write the addition module

**calculations/addition.py**

```python
def add(a, b):
    return a + b
```

### Step 3: Write the subtraction module

**calculations/subtraction.py**

```python
def subtract(a, b):
    return a - b
```

### Step 4: Create `__init__.py`

**calculations/__init__.py**

```python
# Package initialization file
```

For this example, the file can be empty.

### Step 5: Import the package modules

**main.py**

```python
from calculations.addition import add
from calculations.subtraction import subtract

print(add(10, 5))
print(subtract(10, 5))
```

Output:

```text
15
5
```

### What happened?

1. Python located the `calculations` package.
2. It located the `addition` module inside the package.
3. It imported the `add` function.
4. It located the `subtraction` module.
5. It imported the `subtract` function.
6. The main program called both functions.

The important syntax is:

```python
from package_name.module_name import function_name
```

For example:

```python
from calculations.addition import add
```

Here:

- `calculations` is the package.
- `addition` is the module.
- `add` is the function.

---

## 11. Different Ways to Import from a Package

Using the same package:

```text
calculations/
├── __init__.py
├── addition.py
└── subtraction.py
```

Assume `addition.py` contains `add()` and `subtraction.py` contains `subtract()`.

### Method 1: Import the module using its full package path

```python
import calculations.addition

print(calculations.addition.add(10, 5))
```

Output:

```text
15
```

### Method 2: Import a module from the package

```python
from calculations import addition

print(addition.add(10, 5))
```

Output:

```text
15
```

### Method 3: Import a function from a module

```python
from calculations.addition import add

print(add(10, 5))
```

Output:

```text
15
```

These approaches access the same function, but the names available in the current file differ.

---

## 12. What Is `__init__.py`?

`__init__.py` is a special Python file used to initialize a regular package.

It can be empty, or it can contain code that runs when the package is imported.

For example:

```text
calculations/
├── __init__.py
└── addition.py
```

**calculations/__init__.py**

```python
print("Calculations package initialized")
```

**calculations/addition.py**

```python
def add(a, b):
    return a + b
```

**main.py**

```python
import calculations.addition

print(calculations.addition.add(2, 3))
```

Typical output:

```text
Calculations package initialized
5
```

The package initialization code runs as part of importing the package, normally on its first import in that interpreter.

### Can `__init__.py` be empty?

Yes.

An empty file is often sufficient to mark a regular package.

### Is `__init__.py` always required?

No. Modern Python also supports **namespace packages**, which can exist without an `__init__.py` file.

For learning and for many ordinary project structures, including `__init__.py` makes the package organization explicit.

---

## 13. Exposing Functions Through `__init__.py`

Suppose the package looks like this:

```text
calculations/
├── __init__.py
└── addition.py
```

**calculations/addition.py**

```python
def add(a, b):
    return a + b
```

We can re-export the function through `__init__.py`.

**calculations/__init__.py**

```python
from .addition import add
```

Now, in `main.py`:

```python
from calculations import add

print(add(10, 20))
```

Output:

```text
30
```

Normally, without that re-export, the function would be imported using:

```python
from calculations.addition import add
```

### Why is this useful?

It can give a package a simpler public interface, so users do not need to know every internal module.

For small projects, importing directly from the module is also perfectly fine.

---

## 14. What Is a Subpackage?

A **subpackage is a package inside another package.**

Consider:

```text
college_app/
├── __init__.py
├── main.py
├── students/
│   ├── __init__.py
│   ├── details.py
│   └── marks.py
└── finance/
    ├── __init__.py
    ├── fees.py
    └── payments.py
```

Here:

- `college_app` is the outer package if imported as a package.
- `students` is a subpackage.
- `finance` is a subpackage.
- `details`, `marks`, `fees`, and `payments` are modules.

The package hierarchy helps organize large applications by feature.

### Import from a subpackage

Suppose `students/details.py` contains:

```python
def get_student_name():
    return "Ravi"
```

From a context where `college_app` is importable:

```python
from college_app.students.details import get_student_name

print(get_student_name())
```

Output:

```text
Ravi
```

The import path identifies each level:

```text
college_app → students → details → get_student_name
 package      subpackage  module    function
```

---

## 15. Absolute Imports in Packages

An absolute import uses the full import path from an importable top-level package or module.

Example:

```python
from calculations.addition import add
```

Here, `calculations` is the top-level package, `addition` is the module, and `add` is the function.

For an application package:

```python
from college_app.students.details import get_student_name
```

Absolute imports are often straightforward to read because the package path is explicit.

They still depend on the package being available on Python's import path and the program being launched in a suitable context.

---

## 16. Relative Imports in Packages

A relative import uses dots to refer to the current package or one of its parent packages.

Consider:

```text
college_app/
├── __init__.py
└── students/
    ├── __init__.py
    ├── details.py
    └── marks.py
```

**students/details.py**

```python
def get_name():
    return "Ravi"
```

**students/marks.py**

```python
from .details import get_name

def display():
    print(get_name())
```

Here:

```python
from .details import get_name
```

The single dot (`.`) means the current package, which is `students`.

To run it, use a suitable package context. For example, from the directory containing `college_app`, create an entry-point script:

```python
# main.py

from college_app.students.marks import display

display()
```

Output:

```text
Ravi
```

### Meaning of the dots

- `.` — current package.
- `..` — parent package.
- `...` — package two levels above, where that level exists.

For example:

```python
from ..shared import helper
```

This attempts to import `helper` from a `shared` module in the parent package.

**Important:** Relative imports are designed for package modules. Running a package file directly as a standalone script can fail because it may lack the necessary package context.

---

## 17. Module vs Package vs Subpackage

| Feature | Module | Package | Subpackage |
|---|---|---|---|
| Meaning | A Python file | A group of importable modules | A package nested inside another package |
| Typical form | `addition.py` | `calculations/` | `college_app/students/` |
| Can contain modules? | Its code can define names but is not a directory of files | Yes | Yes |
| Can contain packages? | No | Yes | Yes |
| Import example | `import addition` | `import calculations.addition` | `import college_app.students.details` |

A directory is a filesystem concept. A directory becomes an importable regular package when it has the appropriate package structure, traditionally including `__init__.py`. Namespace packages provide another valid arrangement without that file.

---

## 18. How Python Finds Modules and Packages

Python does not search every directory on your computer.

Its import system uses several mechanisms, including:

- `sys.modules`, which caches loaded modules.
- Built-in and other registered import finders.
- Locations on `sys.path`.
- Package-specific search locations when importing submodules.

Example:

```python
import sys

print(sys.path)
```

This displays the search-path entries for the current interpreter.

### Example of a common mistake

Structure:

```text
project/
├── main.py
└── tools/
    ├── __init__.py
    └── helper.py
```

If `helper.py` contains:

```python
def greet():
    print("Hello")
```

A suitable import from `main.py` is:

```python
from tools.helper import greet

greet()
```

Output:

```text
Hello
```

But this import:

```python
import helper
```

may fail because `helper` is inside `tools`, not necessarily at the top level of the import path.

Use an import path that matches the directory structure and run the program from the appropriate project context.

---

## 19. Import Caching

Python normally caches successfully loaded modules in `sys.modules`.

Example:

**demo.py**

```python
print("Demo module loaded")
```

**main.py**

```python
import demo
import demo

print("Main program")
```

Output:

```text
Demo module loaded
Main program
```

Why is the first message printed only once?

The first import loads and executes the module. The second import normally reuses the cached module.

This applies within the same interpreter process; running the script again starts a new process and creates a new import state.

---

## 20. Circular Imports

A circular import occurs when two modules depend on each other.

Example:

```text
module_a.py imports module_b.py
module_b.py imports module_a.py
```

Circular imports can work in some circumstances, but they may fail if a module accesses a name before the other module has finished initializing.

### How to reduce circular imports

- Keep each module focused on a clear responsibility.
- Move shared code into a third module.
- Reduce unnecessary dependencies between modules.
- Use delayed imports only when they genuinely improve the design.

Packages should make dependencies clearer, not merely divide files into folders.

---

## 21. Common Errors with Modules and Packages

### 21.1 `ModuleNotFoundError`

Python cannot find the requested module or package.

Possible causes:

- Incorrect module name.
- Incorrect package path.
- Missing third-party library.
- Wrong active interpreter or virtual environment.
- Program launched from an unsuitable project context.

### 21.2 `ImportError`

Python found the module but could not import the requested name.

Example:

```python
from math import unknown_function
```

### 21.3 Naming a file after a standard-library module

Avoid names such as:

```text
random.py
math.py
json.py
datetime.py
```

A file with one of these names can interfere with importing the corresponding standard-library module.

### 21.4 Running a package module directly

A file using relative imports may fail when executed directly because Python does not know its parent package.

For package-based applications, prefer an appropriate entry point or module execution, such as:

```bash
python -m college_app.students.marks
```

This example assumes `college_app` is importable from the current working directory or environment.

---

## 22. Complete Practical Example: Student Management Package

Let's combine modules and packages in a small application.

### Folder structure

```text
student_app/
├── main.py
└── student/
    ├── __init__.py
    ├── details.py
    └── results.py
```

### File 1: `student/details.py`

```python
def get_details():
    return {
        "name": "Ravi",
        "roll_number": 101
    }
```

### File 2: `student/results.py`

```python
def calculate_average(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)

def get_result(marks):
    if all(mark >= 35 for mark in marks):
        return "Pass"

    return "Fail"
```

### File 3: `student/__init__.py`

```python
# Package initialization file
```

### File 4: `main.py`

```python
from student.details import get_details
from student.results import calculate_average, get_result

details = get_details()
marks = [80, 75, 90]

print("Name:", details["name"])
print("Roll Number:", details["roll_number"])
print("Average:", calculate_average(marks))
print("Result:", get_result(marks))
```

Output:

```text
Name: Ravi
Roll Number: 101
Average: 81.66666666666667
Result: Pass
```

### Understand the design

- `details.py` handles student information.
- `results.py` handles marks and results.
- `student/` groups these related modules into a package.
- `main.py` imports and combines their functionality.

This is a simple example of how modules and packages work together in a real project.

---

## 23. Best Practices

1. Use modules to separate related functionality.
2. Use packages to group related modules.
3. Give files, modules, and packages meaningful lowercase names.
4. Keep `__init__.py` simple unless package initialization or re-exports are needed.
5. Prefer explicit imports over `from module import *`.
6. Avoid circular dependencies.
7. Use absolute imports when they make the project structure clearer.
8. Use relative imports when modules inside a package need to refer to one another.
9. Avoid filenames that shadow standard-library modules.
10. Run package applications from the correct project context.

---

## 24. Quick Revision

| Term | Meaning |
|---|---|
| Module | A Python file containing reusable code |
| Package | A way to organize related modules |
| Subpackage | A package inside another package |
| `import` | Imports a module or package |
| `from ... import` | Imports selected names |
| `__init__.py` | Initializes a regular package and can expose names |
| Absolute import | Uses a full import path from an importable top-level name |
| Relative import | Uses dots to refer to the current or parent package |
| `sys.path` | Search-path entries used by the import system |
| `sys.modules` | Cache of loaded modules |
| `__name__` | Name associated with the current module |
| `__main__` | Common name for the directly executed entry-point module |

## 25. Final Understanding

**Module:** A Python file that contains reusable code.

**Package:** A structure that groups related modules and can contain subpackages.

**Subpackage:** A package nested inside another package.

For example:

```text
college_app/                 # Package, when structured/imported as one
├── __init__.py
├── main.py                  # Module
└── students/                # Subpackage
    ├── __init__.py
    ├── details.py           # Module
    └── marks.py             # Module
```

Modules help divide code into files. Packages help organize those files into a hierarchy. Together, they make Python applications easier to understand, reuse, and maintain.
