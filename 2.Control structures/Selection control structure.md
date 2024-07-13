Notes
Selection control structures, also known as conditional statements, allow you to execute different blocks of code based on certain conditions. In Python, the main selection control structures are if, elif, and else.

if Statement
Executes a block of code if a condition is true.

Syntax:
  if condition:

      # code block
Example:
  age = 18

  if age >= 18:

      print("You are an adult.")
 if-else Statement
- Executes one block of code if a condition is true, and another block of code if the condition is false.

Syntax:
  if condition:

      # code block

  else:

      # code block
Example:
  age = 16

  if age >= 18:

      print("You are an adult.")

  else:

      print("You are a minor.")
 if-elif-else Statement
- Executes different blocks of code depending on multiple conditions.

Syntax:
  if condition1:

      # code block

  elif condition2:

      # code block

  else:

      # code block
Example:
  score = 85

  if score >= 90:

      print("Grade: A")

  elif score >= 80:

      print("Grade: B")

  elif score >= 70:

      print("Grade: C")

  else:

      print("Grade: F")