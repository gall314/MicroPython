# Introduction to Python

**Usefull Links**:
- [Python.org - Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python.org - Documentation](https://docs.python.org/3/)
  - [Python.org - Library Reference](https://docs.python.org/3/library/index.html)
  - [Python.org - Language Reference](https://docs.python.org/3/reference/index.html)
- [MicroPython Library Documentation](https://docs.micropython.org/en/latest/library/index.html)
  - [MicroPython - Machine](https://docs.micropython.org/en/latest/library/machine.html) 

The basic syntax and data types in MicroPython are similar to those in standard Python. Here are some examples to illustrate the basics:

Variables: Variables in MicroPython are used to store values. A variable is created by assigning a value to a name. For example:
```python
x = 5
y = "Hello World!"
```

Data Types: MicroPython supports several data types, including numbers (integers and floating-point), strings, lists, and dictionaries. Here are some examples:

# Numbers
```python
a = 5
b = 3.14

# Strings
c = "Hello World!"

# Lists
d = [1, 2, 3, 4, 5]

# Dictionaries
e = {"name": "John", "age": 30}
```

Operators: MicroPython supports the standard mathematical and comparison operators, such as `+, -, *, /, %, and ==, !=, >, <, >=, <=`. Here are some examples:

```python
x = 5
y = 3

# Addition
result = x + y

# Subtraction
result = x - y

# Multiplication
result = x * y

# Division
result = x / y

# Modulus
result = x % y
```

Control Flow: MicroPython supports the standard control flow statements such as if-else, for and while loops.

```python
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is negative")

# For loop
for i in range(5):
    print(i)

# While loop
x = 0
while x < 5:
    print(x)
    x += 1
```

Functions: MicroPython supports the creation of functions using the def keyword. A function is a block of code that can be called multiple times to perform a specific task.

```python
def add(x, y):
    return x + y

result = add(5, 3)
print(result)
```

Useful functions

```python
import utime

utime.sleep(5) # sleep (wait) 5 seconds before doing next instruction
```
