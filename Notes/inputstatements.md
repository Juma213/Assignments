Notes
Discover how to capture user input using Python's input() function. Learn how to handle user responses and incorporate them into your programs

Reading Input from the User:
Use `input()` function to prompt the user for input.

     name = input("Enter your name: ")
​​​​​
Handling User Input:
Input is typically stored as a string, so convert it to the desired type (int, float, etc.) using type casting.

     age = int(input("Enter your age: "))
Multiple Inputs:
Use `split()` method to separate inputs entered in a single line.

 numbers = input("Enter numbers separated by space: ").split()