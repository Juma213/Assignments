A variable is a named location used to store data in the memory.

Naming Rules:
  - Must start with a letter (a-z, A-Z) or an underscore (_).

  - Followed by letters, digits (0-9), or underscores.

  - Case-sensitive (e.g., `myVar` and `myvar` are different variables).

  - Cannot be a reserved keyword (e.g., `for`, `while`, `class`, etc.).

Examples:
  x = 5

  name = "Alice"

  _age = 30
Declaration and Initialization
Declaration: In Python, variables do not need explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned to a variable.

Initialization: Assigning a value to a variable for the first time.

Syntax:
  variable_name = value
Examples:
  # Integer

  age = 25

  # Float

  temperature = 36.6

  # String

  name = "Alice"

  # Boolean

  is_student = True

  # NoneType

  result = None
Multiple Assignments
Assigning the same value to multiple variables:

  a = b = c = 10
Assigning different values to multiple variables in one line:

  x, y, z = 1, 2.5, "Hello"
Changing Variable Types

Variables in Python are dynamic-typed, meaning you can change the type of a variable by reassigning it a different value.

  var = 10   # var is an integer

  var = "Python"  # var is now a string
Datatypes
A datatype determine the type of values variables can hold and specify the operations that can be performed on those values.

Numeric Types
int: Integer, whole numbers.

  a = 10

  b = -5
float: Floating-point number, decimal numbers.

  pi = 3.14

  gravity = 9.81
Boolean Type
- bool: Represents True or False.

  is_student = True

  has_graduated = False
Type Conversion
Implicit Conversion: Python automatically converts one data type to another.

  x = 10   # int

  y = 3.14 # float

  z = x + y  # z becomes float (13.14)
Explicit Conversion: Manually converting from one data type to another using type functions.

  a = 5    # int

  b = "123" # str

  c = int(b)  # c becomes int (123)

  d = float(a)  # d becomes float (5.0)
Checking Datatypes
Using `type()` function: To check the datatype of a variable.

  x = 10

  print(type(x))  # Output: <class 'int'>
Best Practices
- Use meaningful variable names that convey the purpose of the variable.

- Follow the naming conventions (e.g., `snake_case` for variables).

- Avoid using Python reserved keywords as variable names.