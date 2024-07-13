Notes
Continue keyword skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

Syntax:
while condition:
    if some_condition:
        continue
Example:
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)