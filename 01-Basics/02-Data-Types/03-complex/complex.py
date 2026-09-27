# Python Complex Number Examples


# 1. Creating complex numbers

a = 3 + 4j
b = 5 - 2j
c = 4j

print(a)
print(b)
print(c)

# Output:
# (3+4j)
# (5-2j)
# 4j


# 2. Checking the type

z = 3 + 4j

print(type(z))

# Output:
# <class 'complex'>


# 3. Getting real and imaginary parts

z = 3 + 4j

print(z.real)
print(z.imag)

# Output:
# 3.0
# 4.0


# 4. Creating a complex number using complex()

z = complex(3, 4)

print(z)

# Output:
# (3+4j)


# 5. Creating complex number with only real part

z = complex(10)

print(z)

# Output:
# (10+0j)


# 6. Addition

a = 2 + 3j
b = 4 + 5j

print(a + b)

# Output:
# (6+8j)


# 7. Subtraction

a = 5 + 6j
b = 2 + 3j

print(a - b)

# Output:
# (3+3j)


# 8. Multiplication

a = 2 + 3j
b = 4 + 5j

print(a * b)

# Output:
# (-7+22j)


# 9. Division

a = 2 + 3j
b = 1 + 2j

print(a / b)

# Output:
# (1.6-0.2j)


# 10. Conjugate

z = 3 + 4j

print(z.conjugate())

# Output:
# (3-4j)


# 11. Magnitude using abs()

z = 3 + 4j

print(abs(z))

# Output:
# 5.0


# 12. Checking whether a value is complex

z = 3 + 4j

print(isinstance(z, complex))

# Output:
# True


# 13. Complex number with negative real part

z = -3 + 4j

print(z)
print(z.real)
print(z.imag)

# Output:
# (-3+4j)
# -3.0
# 4.0


# 14. Complex numbers are immutable

z = 3 + 4j

z = z + 2

print(z)

# Output:
# (5+4j)