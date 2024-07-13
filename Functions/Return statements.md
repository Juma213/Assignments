Notes
The `return` statement is used to exit a function and return a value to the caller. If no `return` statement is used, or if the `return` statement does not include an expression, the function returns `None` by default.

Syntax:

def function_name(parameters):

    # Function body

    return [expression]
Examples:
1. Returning a Single Value:

    def square(x):

       return x * x

   result = square(4)

   print(result)  # Output: 16
2. Returning Multiple Values:

   Python functions can return multiple values as a tuple.

   Example:
   def arithmetic_operations(a, b):

       return a + b, a - b, a * b, a / b

   add, subtract, multiply, divide = arithmetic_operations(10, 2)

   print(add, subtract, multiply, divide)  # Output: 12 8 20 5.0
 3. Returning None:

   If a function does not explicitly return a value, it returns `None` by default.

   Example:
 

   def greet(name):

       print(f"Hello, {name}!")

   result = greet("Alice")

   print(result)  # Output: Hello, Alice!

                  # None