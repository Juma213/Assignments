Notes
Explore loops and repetitive execution with for and while loops.

while Loop
Repeats a block of code as long as a condition is true.

Syntax:
  while condition:

      # code block
Example:
  count = 0

  while count < 5:

      print(count)

      count += 1
for Loop
- Iterates over a sequence (such as a list, tuple, string) and executes a block of code for each item in the sequence.

Syntax:
  for item in sequence:

      # code block
Example:
  fruits = ["apple", "banana", "cherry"]

  for fruit in fruits:

      print(fruit)
Nested Loops
Loops inside another loop.

Example:
  for i in range(3):

      for j in range(2):

          print(f"i: {i}, j: {j}")