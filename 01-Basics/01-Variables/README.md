# Python Variables

## 1. What is a Variable?

- A variable is a name used to refer to an object in Python.
- Python variables do not need to be declared before assigning a value.
- A variable is better understood as a name/reference that is bound to an object.
- The assignment operator `=` is used to assign or bind a name to an object.

### Example

```python
name = "Teja"
age = 21
cgpa = 8.43
Here:

name is the variable name.
"Teja" is a string object.
age is the variable name.
21 is an integer object.
cgpa is the variable name.
8.43 is a floating-point object.

Conceptually:

name  ─────► "Teja"
age   ─────► 21
cgpa  ─────► 8.43
2. Variable Assignment
Assignment is the process of binding a name to an object.
Python uses the = operator for assignment.
The left side contains the variable name.
The right side contains the value or expression.
Example
age = 21

Conceptually:

age ─────► 21
3. Variable Assignment Syntax

The general syntax is:

variable_name = value
Example
name = "Teja"
age = 21
salary = 50000
4. Assignment = vs Equality ==
= — Assignment
= assigns or rebinds a name.
age = 21
== — Equality Comparison
== checks whether two values are equal.
age = 21

print(age == 21)

Output:

True
Remember
=   → Assignment
==  → Equality comparison
5. Variable Declaration in Python
Python does not require explicit variable declaration.
A variable is created when a name is assigned to an object.
We do not need to specify the data type while assigning the variable.
Example
age = 21
name = "Teja"
cgpa = 8.43

Python determines the type of each object.

6. Python is Dynamically Typed
Python is a dynamically typed language.
We do not specify the type of a variable when assigning it.
A name can later be rebound to an object of another type.
The object has a type; the name is bound to that object.
Example
x = 10
print(type(x))

x = "Python"
print(type(x))

x = 10.5
print(type(x))

Output:

<class 'int'>
<class 'str'>
<class 'float'>

Conceptually:

x ───► 10

x ───► "Python"

x ───► 10.5
7. Variables Can Refer to Different Data Types

A variable can refer to objects of different types.

Example
name = "Teja"
age = 21
percentage = 92.9
is_student = True

Here:

name → str
age → int
percentage → float
is_student → bool

We can check the types:

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))
Variable Naming Rules
8. A Variable Name Can Contain Letters
Uppercase and lowercase letters are allowed.
Letters can appear anywhere in the identifier.
Example
name = "Teja"
student = "Python"
studentName = "Teja"

All of these are syntactically valid.

9. A Variable Name Can Contain Digits
Digits are allowed in variable names.
However, a variable name cannot start with a digit.
Valid
student1 = "Teja"
marks2 = 90
subject3 = "Python"
Invalid
1student = "Teja"
2marks = 90

Remember:

student1  → Valid
1student  → Invalid
10. Underscore _ is Allowed
The underscore character can be used in variable names.
It is commonly used to separate words.
Example
student_name = "Teja"
total_marks = 450
average_marks = 90
11. Spaces are Not Allowed
Spaces cannot be used inside variable names.
Invalid
student name = "Teja"
Correct
student_name = "Teja"

Use _ instead of a space.

12. Special Characters are Not Allowed

Normal variable names cannot contain special characters such as:

@  $  %  -  !  #
Invalid
student-name = "Teja"
student@name = "Teja"
student$name = "Teja"
Correct
student_name = "Teja"
13. Python Keywords Cannot Be Used
Python has reserved keywords.
Keywords have special meanings in Python.
They cannot be used as normal variable names.
Invalid
class = 10
if = 20
for = 30
Correct
class_number = 10
if_value = 20
for_count = 30

You can view Python keywords using:

import keyword

print(keyword.kwlist)
14. Variable Names are Case-Sensitive
Python is case-sensitive.
Uppercase and lowercase names are treated as different names.
Example
age = 21
Age = 30
AGE = 40

print(age)
print(Age)
print(AGE)

Output:

21
30
40

Therefore:

age ≠ Age ≠ AGE
15. Use Meaningful Variable Names
Variable names should describe the data they represent.
Meaningful names make programs easier to read and understand.
Poor example
x = 50000

It is not clear what 50000 represents.

Better example
salary = 50000

Another example:

Poor
a = 450
Better
total_marks = 450
16. Use snake_case
Python commonly uses snake_case for variable names.
Words are written in lowercase.
Multiple words are separated using _.
Example
student_name = "Teja"
total_marks = 450
average_marks = 90
employee_salary = 50000
number_of_students = 50
17. Multiple Assignment
Python allows multiple variables to be assigned in one statement.
The number of variables must match the number of values.
Example
a, b, c = 10, 20, 30

This is equivalent to:

a = 10
b = 20
c = 30
18. Assigning the Same Value to Multiple Variables
Multiple names can be assigned to the same object.
Example
x = y = z = 100

Conceptually:

x ──┐
y ──┼────► 100
z ──┘
19. Variable Reassignment
A variable can be assigned a new object.
This is called reassignment or rebinding.
Example
x = 10

print(x)

x = 20

print(x)

Output:

10
20

Initially:

x ───► 10

After x = 20:

x ───► 20
20. type() Function
type() is a built-in function.
It tells us the type of the object referred to by a variable.
Example
x = 100

print(type(x))

Output:

<class 'int'>

Another example:

name = "Teja"

print(type(name))

Output:

<class 'str'>
21. id() Function
id() returns an identity associated with an object.
The exact number can vary between program executions.
Example
x = 100

print(id(x))
22. Variable References
Multiple names can refer to the same object.
Example
x = 10
y = x

print(x)
print(y)

Conceptually:

x ──┐
    ├────► 10
y ──┘

We can check object identity using is:

print(x is y)

Output:

True
23. is vs ==
==
Checks whether two objects compare equal in value.
x = 10
y = 10

print(x == y)
is
Checks whether two names refer to the same object.
x = 10
y = x

print(x is y)

Remember:

==  → Equality
is  → Object identity
24. Swapping Variables
Python allows variables to be swapped without using a temporary variable.
Example
a = 10
b = 20

a, b = b, a

print(a)
print(b)

Output:

20
10
25. Constants
Python does not have a special keyword that strictly creates constants.
Uppercase names are used as a convention for values that should normally not be changed.
Example
PI = 3.14159
MAX_USERS = 100
DAYS_IN_WEEK = 7

Python technically allows reassignment:

PI = 3.14

Therefore, uppercase naming is a convention rather than strict enforcement.

26. del Statement
The del statement removes a name binding.
After deleting the name, trying to access it causes a NameError.
Example
x = 100

print(x)

del x

After:

del x

this would cause an error:

print(x)

Quick Revision
Concept	Meaning
Variable	Name referring to an object
=	Assignment
==	Equality comparison
is	Object identity comparison
type()	Gets object's type
id()	Gets object's identity
Dynamic typing	Names can be rebound to objects of different types
del	Removes a name binding
snake_case	Common Python naming convention
Variable Naming Checklist

A valid variable name:

Can contain letters.
Can contain digits.
Cannot start with a digit.
Can contain _.
Cannot contain spaces.
Cannot contain normal special characters.
Cannot be a Python keyword.
Is case-sensitive.
Should preferably be meaningful.
Should normally follow snake_case.