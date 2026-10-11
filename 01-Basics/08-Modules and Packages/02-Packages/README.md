# Python Packages — Complete Notes

## 1. What Is a Package?

A **package is a way to organize related Python modules into a hierarchical structure.**

A module is commonly a `.py` file. A package organizes modules and can also contain subpackages.

Consider this project:

```text
college_app/
├── main.py
├── students/
│   ├── __init__.py
│   ├── details.py
│   └── marks.py
└── fees/
    ├── __init__.py
    ├── payments.py
    └── reports.py
```

Here:

- `students` is a package.
- `fees` is a package.
- `details.py` and `marks.py` are modules inside `students`.
- `payments.py` and `reports.py` are modules inside `fees`.
- `main.py` is the program's entry-point module.

The packages group related modules according to their responsibilities.

## 2. Why Do We Need Packages?

Imagine creating a large application with 50 Python files.

Keeping every file in one directory makes the project difficult to navigate.

Packages let us group related modules together.

For example:

```text
ecommerce/
├── main.py
├── users/
│   ├── __init__.py
│   ├── registration.py
│   └── authentication.py
├── products/
│   ├── __init__.py
│   ├── catalog.py
│   └── search.py
└── orders/
    ├── __init__.py
    ├── checkout.py
    └── payments.py
```

The `users` package contains user-related code, `products` contains product-related code, and `orders` contains order-related code.

Packages help us:

1. Organize large applications.
2. Group related modules.
3. Create a clear project hierarchy.
4. Reduce confusion when navigating files.
5. Separate responsibilities.
6. Maintain and test individual components.
7. Reuse code across different parts of a project.

## 3. Package, Module, and Directory

These three terms are related, but they do not mean the same thing.

| Term | Meaning | Example |
|---|---|---|
| Module | A unit of Python code with a namespace | `details.py` |
| Package | An importable structure that groups modules and possibly subpackages | `students/` |
| Directory | A filesystem folder | `project/` |

A directory is not automatically a regular Python package. Traditionally, a regular package contains an `__init__.py` file. Python also supports namespace packages that do not require that file.

## 4. Types of Packages

Two important package forms are regular packages and namespace packages.

### 4.1 Regular packages

A regular package commonly contains an `__init__.py` file.

Example:

```text
calculations/
├── __init__.py
├── addition.py
└── subtraction.py
```

The `calculations` directory is a regular package.

### 4.2 Namespace packages

A namespace package can span multiple directories and does not require an `__init__.py` file in the namespace-package directory.

For example, two separate locations could contribute to the same namespace:

```text
location_one/
└── company/
    └── sales/
        └── reports.py
```

```text
location_two/
└── company/
    └── finance/
        └── accounts.py
```

If the locations are configured appropriately on the import path and `company` is treated as a namespace package, its subpackages can be discovered from both locations.

Namespace packages are useful for certain large systems and separately distributed components.

For ordinary beginner projects, regular packages are usually easier to understand.

## 5. Creating Your First Package

Let's create a package named `calculations`.

### Step 1: Create the structure

```text
project/
├── main.py
└── calculations/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py
```

### Step 2: Write `addition.py`

```python
def add(a, b):
    return a + b
```

### Step 3: Write `subtraction.py`

```python
def subtract(a, b):
    return a - b
```

### Step 4: Create `__init__.py`

```python
# Package initialization file
```

For now, this file can remain empty.

### Step 5: Import functions in `main.py`

```python
from calculations.addition import add
from calculations.subtraction import subtract

print(add(20, 10))
print(subtract(20, 10))
```

Output:

```text
30
10
```

### Understand the import path

Consider:

```python
from calculations.addition import add
```

Each part has a meaning:

```text
calculations.addition.add
     │          │      │
  package     module  function
```

Python uses the import path to locate the module and obtain the requested name.

## 6. What Is `__init__.py`?

`__init__.py` is a special file used to initialize a regular package.

Example:

```text
calculations/
├── __init__.py
├── addition.py
└── subtraction.py
```

When Python imports the package for the first time in a normal import sequence, its initialization code is executed.

The file can contain:

- Initialization statements.
- Imports that expose selected package names.
- Package-level constants.
- Package documentation.
- Other package setup code.

It can also be empty.

### Example 1: Empty `__init__.py`

```python
# __init__.py
```

An empty file is enough to establish a regular package.

### Example 2: Package initialization

`calculations/__init__.py`:

```python
print("Calculations package initialized")
```

`main.py`:

```python
import calculations
```

Output:

```text
Calculations package initialized
```

The initialization code runs when the package is first imported in that interpreter process.

### Important points

- `__init__.py` is not the same as `__main__.py`.
- `__init__.py` initializes a regular package.
- `__main__.py` provides code that can be executed when a package is run with `python -m package_name`.
- Modern namespace packages do not require `__init__.py`.
- Avoid putting unnecessary work or unwanted side effects in package initialization.

## 7. How Package Initialization Works

Consider:

```text
project/
├── main.py
└── calculations/
    ├── __init__.py
    └── addition.py
```

`calculations/__init__.py`:

```python
print("Package initialized")
```

`calculations/addition.py`:

```python
print("Addition module loaded")

def add(a, b):
    return a + b
```

`main.py`:

```python
import calculations.addition

print(calculations.addition.add(5, 3))
```

Typical output:

```text
Package initialized
Addition module loaded
8
```

### Execution process

1. Python encounters `import calculations.addition`.
2. Python locates the `calculations` package.
3. Python initializes the regular package if it has not already been initialized.
4. The package's `__init__.py` executes.
5. Python locates and loads the `addition` submodule.
6. The module's top-level code executes.
7. The import finishes.
8. The program calls `add(5, 3)`.

This explains why a package's initialization code can run before the submodule's top-level code.

## 8. Importing from a Package

There are several ways to import a module or function from a package.

Suppose:

```text
calculations/
├── __init__.py
├── addition.py
└── subtraction.py
```

`addition.py`:

```python
def add(a, b):
    return a + b
```

### Method 1: Import the full submodule path

```python
import calculations.addition

print(calculations.addition.add(5, 4))
```

Output:

```text
9
```

### Method 2: Import a submodule from the package

```python
from calculations import addition

print(addition.add(5, 4))
```

Output:

```text
9
```

### Method 3: Import a function from a submodule

```python
from calculations.addition import add

print(add(5, 4))
```

Output:

```text
9
```

### Method 4: Import using an alias

```python
from calculations.addition import add as calculate_sum

print(calculate_sum(5, 4))
```

Output:

```text
9
```

All four approaches can access the same function, but they create different names in the importing namespace.

## 9. Exposing Names Through `__init__.py`

A package can provide a convenient public interface by importing selected names into its package namespace.

Structure:

```text
calculations/
├── __init__.py
└── addition.py
```

`calculations/addition.py`:

```python
def add(a, b):
    return a + b
```

`calculations/__init__.py`:

```python
from .addition import add
```

Now `main.py` can use:

```python
from calculations import add

print(add(10, 20))
```

Output:

```text
30
```

Without the re-export in `__init__.py`, the usual import would be:

```python
from calculations.addition import add
```

### Why does this work?

When the package initializes, its `__init__.py` imports `add` from the `addition` module. The imported name becomes available as `calculations.add`.

This does not move the function into another file. It makes the same function accessible through the package namespace.

### When should we do this?

Use package-level re-exports when you want a simpler public API.

For a small package, direct imports from the actual module are also perfectly acceptable.

## 10. The `__all__` Variable in a Package

A package can define `__all__` to control which names are requested by:

```python
from package_name import *
```

Example:

`calculations/__init__.py`:

```python
from .addition import add
from .subtraction import subtract

__all__ = ["add", "subtract"]
```

Suppose the corresponding modules define those functions.

Then:

```python
from calculations import *

print(add(10, 5))
print(subtract(10, 5))
```

Output:

```text
15
5
```

### Important distinction

`__all__` does not automatically import every submodule in the package. The names must be available in the package namespace or otherwise provided by the package.

It also does not make unlisted names private or inaccessible. It primarily controls star-import behavior.

In regular application code, explicit imports are often clearer.

## 11. What Is a Subpackage?

A subpackage is a package inside another package.

Example:

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

Here, `students` and `finance` are subpackages of `college_app` when the structure is imported that way.

The `details.py` and `marks.py` files are modules inside `students`.

The `fees.py` and `payments.py` files are modules inside `finance`.

### Importing from a subpackage

Suppose `students/details.py` contains:

```python
def get_student_name():
    return "Ravi"
```

From a context in which `college_app` is importable:

```python
from college_app.students.details import get_student_name

print(get_student_name())
```

Output:

```text
Ravi
```

The import path follows the directory hierarchy.

## 12. Nested Packages

Packages can contain subpackages, which can contain further subpackages.

Example:

```text
company/
├── __init__.py
└── departments/
    ├── __init__.py
    └── engineering/
        ├── __init__.py
        ├── developers.py
        └── testers.py
```

The `company` package contains `departments`, and `departments` contains `engineering`.

Import a function from `developers.py`:

```python
from company.departments.engineering.developers import get_developers
```

Assuming the function exists, this import refers to the `get_developers` name in the `developers` module.

Nested packages are useful when an application has several levels of related components.

However, do not create deep directory structures without a clear organizational need.

## 13. Absolute Imports

An absolute import uses a full path from an importable top-level module or package.

Example:

```python
from calculations.addition import add
```

For a nested package:

```python
from company.departments.engineering.developers import get_developers
```

### Advantages

- The import path makes the origin of a name clear.
- It is often easy to read.
- It works well when a project has a stable package structure.

An absolute import still depends on the relevant top-level package being available on Python's import path.

## 14. Relative Imports

Relative imports refer to modules using dots.

They are designed for modules that belong to a package.

Example:

```text
college_app/
├── __init__.py
└── students/
    ├── __init__.py
    ├── details.py
    └── marks.py
```

`students/details.py`:

```python
def get_name():
    return "Ravi"
```

`students/marks.py`:

```python
from .details import get_name

def display():
    print(get_name())
```

The single dot means the current package, `students`.

To use it from an entry-point file in a suitable environment:

```python
from college_app.students.marks import display

display()
```

Output:

```text
Ravi
```

### Meaning of relative-import dots

- `.` refers to the current package.
- `..` refers to the parent package.
- `...` refers to the package two levels above the current package.

Example:

```python
from ..shared import helper
```

This attempts to import `helper` from a `shared` module in the parent package.

### Important rule

Relative imports require package context. Running a file directly by its filename can cause an error such as:

```text
ImportError: attempted relative import with no known parent package
```

A suitable package entry point or `python -m` execution is generally preferable.

## 15. Absolute vs Relative Imports

| Feature | Absolute import | Relative import |
|---|---|---|
| Example | `from app.users import details` | `from . import details` |
| Reference point | Importable top-level name | Current or parent package |
| Readability | Explicit full path | Compact within a package |
| Common use | Application entry points and cross-package imports | Imports between modules inside a package |
| Package context required | Requires the top-level name to be importable | Requires a valid package context |

Neither form is always better. Choose the form that makes the project's structure and dependencies easiest to understand.

## 16. What Is `__path__`?

Packages have a `__path__` attribute that identifies the locations used to search for their submodules.

For a regular package, it commonly contains the package directory.

Example:

```python
import calculations

print(calculations.__path__)
```

The result depends on where the package is installed or located.

`__path__` is particularly relevant to namespace packages, which can have portions in multiple locations.

Ordinary modules that are not packages do not normally have a package `__path__`.

## 17. The Difference Between `__init__.py` and `__main__.py`

These files have different purposes.

### `__init__.py`

Initializes a regular package and can expose names.

Example:

```text
calculations/
├── __init__.py
└── addition.py
```

### `__main__.py`

Provides the code to execute when a package is run using:

```bash
python -m package_name
```

Example:

```text
calculator_app/
├── __init__.py
├── __main__.py
└── operations.py
```

`calculator_app/operations.py`:

```python
def add(a, b):
    return a + b
```

`calculator_app/__main__.py`:

```python
from .operations import add

print(add(10, 20))
```

From the directory containing `calculator_app`, run:

```bash
python -m calculator_app
```

Output:

```text
30
```

Python executes the package's `__main__.py`.

**Remember:** `__init__.py` is for package initialization; `__main__.py` is the package's executable entry point.

## 18. Running a Module Inside a Package

Consider:

```text
project/
└── mypackage/
    ├── __init__.py
    ├── helper.py
    └── runner.py
```

Suppose `runner.py` contains:

```python
from .helper import greet

greet()
```

When it is executed directly using:

```bash
python mypackage/runner.py
```

the relative import may fail because the file is being treated as a standalone script.

Instead, from the directory containing `mypackage`, run:

```bash
python -m mypackage.runner
```

The `-m` option locates and executes the module using its import name, providing the appropriate package context.

## 19. How Python Finds Packages

Python's import system uses the module cache, registered finders, and search locations to locate packages and modules.

The search path can be inspected using:

```python
import sys

print(sys.path)
```

For submodules, Python also uses a package's search locations, available through `__path__`.

### Example

Structure:

```text
project/
├── main.py
└── tools/
    ├── __init__.py
    └── helper.py
```

In `main.py`:

```python
from tools.helper import greet

greet()
```

This works when the project is launched in an appropriate context and the `project` directory is on the import path.

A common mistake is assuming Python automatically searches every folder on the computer.

It does not. The import path and package structure must allow Python to find the requested name.

## 20. Import Caching in Packages

Python normally caches successfully imported modules in `sys.modules`.

For example:

```python
import calculations.addition
import calculations.addition
```

The second import normally reuses the cached module.

The package's initialization code is also normally executed once during its first import in that interpreter process.

Deleting entries from `sys.modules` or using `importlib.reload()` can change this behavior, but doing so casually may leave old references or partially inconsistent states.

## 21. Circular Imports Between Packages

A circular import occurs when packages or modules depend on one another during initialization.

Example:

```text
package_a imports package_b
package_b imports package_a
```

The same issue can occur between modules within one package.

Because Python registers modules in `sys.modules` before their initialization has finished, one module may encounter another module before all its names have been defined.

### How to prevent circular imports

1. Reduce dependencies between packages.
2. Move shared functionality into a separate module.
3. Keep each package focused on a clear responsibility.
4. Avoid unnecessary initialization work in `__init__.py`.
5. Use delayed imports only when they are appropriate to the design.

Packages should organize dependencies clearly, not simply place every file into a directory.

## 22. Importing Data Files from a Package

Packages can contain non-Python files, such as templates, configuration files, or text resources.

Example:

```text
myapp/
├── __init__.py
├── main.py
└── data/
    ├── __init__.py
    └── message.txt
```

For installed applications, `importlib.resources` provides a more reliable way to access package resources than assuming a particular filesystem path.

Example:

```python
from importlib.resources import files

message = (
    files("myapp.data")
    .joinpath("message.txt")
    .read_text(encoding="utf-8")
)

print(message)
```

This example assumes the package and resource file are available in the installed or importable application.

The resource API can support resources that are not represented as ordinary filesystem files, depending on the package loader.

## 23. What Is a Distribution Package?

A distribution package is the installable software unit that you obtain from a package index or another source.

It is different from an import package.

For example, you might install a distribution using:

```bash
python -m pip install requests
```

Then import it:

```python
import requests
```

The name used for installation does not always match the name used in an `import` statement.

This distinction is important when working with third-party libraries.

- **Distribution package:** The software unit installed by a packaging tool.
- **Import package:** The package or module made available to Python's import system.

A distribution may provide several import packages, and an import package may be provided by a distribution whose name is different.

## 24. Namespace Packages in More Detail

A namespace package allows multiple locations to contribute portions of one package namespace.

Unlike a regular package, a namespace package does not require `__init__.py` in its namespace directory.

Suppose two separate locations are configured on the import path:

```text
location_one/
└── company/
    └── sales/
        └── reports.py
```

```text
location_two/
└── company/
    └── finance/
        └── accounts.py
```

If Python discovers `company` as a namespace package across both locations, the two subpackages can coexist under the same top-level namespace.

This is useful when different distributions contribute different parts of a larger system.

For everyday beginner projects, a regular package with `__init__.py` is often simpler.

## 25. Common Package Errors

### 25.1 `ModuleNotFoundError`

Python cannot locate a requested package or module.

Possible causes:

- Incorrect import path.
- Missing package.
- Wrong active Python environment.
- Incorrect project working directory.
- The package is not installed or otherwise available on the import path.

### 25.2 `ImportError`

The module or package was found, but the requested name could not be imported.

Possible causes include a misspelled function name, an unavailable name, or a circular import.

### 25.3 Relative import has no known parent package

This often occurs when a package module is executed directly as a script.

Use an appropriate package execution context, such as:

```bash
python -m mypackage.runner
```

### 25.4 Incorrect capitalization

Python import names are case-sensitive on many platforms.

For example, a file named `details.py` should normally be imported as:

```python
import details
```

not:

```python
import Details
```

### 25.5 Naming a package after a standard-library module

Avoid package names such as `email`, `json`, `random`, or `statistics` for unrelated projects because they may shadow standard-library modules or interfere with imports.

Choose distinct, meaningful names.

## 26. Complete Practical Example: Student Management Package

Let's build a small student application using multiple modules.

### Folder structure

```text
student_app/
├── __init__.py
├── __main__.py
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
from .details import get_details
from .results import calculate_average, get_result
```

This makes the selected functions available through the `student` package.

### File 4: `student_app/__init__.py`

```python
# Student application package
```

### File 5: `student_app/__main__.py`

```python
from .student import get_details, calculate_average, get_result

details = get_details()
marks = [80, 75, 90]

print("Name:", details["name"])
print("Roll Number:", details["roll_number"])
print("Average:", calculate_average(marks))
print("Result:", get_result(marks))
```

### Run the application

From the directory containing `student_app`, run:

```bash
python -m student_app
```

Output:

```text
Name: Ravi
Roll Number: 101
Average: 81.66666666666667
Result: Pass
```

### Understand the design

- `student_app` is the outer package.
- `student` is a subpackage.
- `details.py` handles student information.
- `results.py` handles marks and results.
- The `student/__init__.py` file exposes selected functions.
- The `student_app/__main__.py` file provides the package's executable entry point.

This example combines package structure, imports, initialization, re-exports, and module execution.

## 27. Best Practices for Packages

1. Use meaningful package names.
2. Group modules according to responsibility.
3. Keep package initialization simple.
4. Use `__init__.py` for regular packages when appropriate.
5. Do not assume `__init__.py` is required for namespace packages.
6. Prefer explicit imports.
7. Use relative imports for clear relationships within a package.
8. Use absolute imports when full import paths improve clarity.
9. Avoid circular dependencies.
10. Avoid deeply nested packages unless they provide useful organization.
11. Avoid names that shadow standard-library modules.
12. Use `python -m package_name` when executing a package through `__main__.py`.
13. Use `importlib.resources` for package data when appropriate.
14. Test imports from the same execution context in which the application will run.

## 28. Quick Revision

| Concept | Meaning |
|---|---|
| Package | Organizes related modules and subpackages |
| Regular package | A package that commonly contains `__init__.py` |
| Namespace package | A package that can span locations without requiring `__init__.py` |
| Subpackage | A package inside another package |
| `__init__.py` | Initializes a regular package and can expose names |
| `__main__.py` | Provides the executable entry point for `python -m package_name` |
| `__path__` | Package search locations |
| Absolute import | Uses an import path from a top-level name |
| Relative import | Uses dots to refer to the current or parent package |
| `__all__` | Controls names requested by a star import when defined |
| `sys.path` | Import search-path entries |
| `sys.modules` | Cache of loaded modules |
| Distribution package | Installable software unit |
| Import package | Package exposed through Python's import system |
| Circular import | Modules or packages depend on each other during initialization |

## 29. Practice Questions

1. What is a package, and why is it useful?
2. What is the difference between a module, package, and directory?
3. What is the difference between a regular package and a namespace package?
4. What is the purpose of `__init__.py`?
5. Is `__init__.py` always required?
6. What happens when a package is imported for the first time?
7. How do you import a function from a module inside a package?
8. How can `__init__.py` expose selected functions?
9. What is the purpose of `__all__`?
10. What is a subpackage?
11. Explain absolute and relative imports with examples.
12. What does `__path__` represent?
13. What is the difference between `__init__.py` and `__main__.py`?
14. Why can a relative import fail when a file is executed directly?
15. What does `python -m package_name` do?
16. What is a namespace package?
17. What is the difference between a distribution package and an import package?
18. What causes circular imports?
19. How can package resources be accessed safely?
20. Create a student-management package with separate modules for details and marks.

## Final Understanding

A package organizes related modules into a hierarchy. A regular package commonly contains `__init__.py`, while namespace packages can exist without it. Packages may contain subpackages, expose selected names, use absolute or relative imports, and provide an executable entry point through `__main__.py`.

Understanding packages is essential for building maintainable Python projects that contain multiple files and clearly separated responsibilities.
