num1 = int(input("Enter first number : "))
operator = input("Enter your operator : ")
num2 = int(input("Enter second number : "))

# For adding two numbers
if operator == "+":
    print(num1 + num2)
    
# For subtracting two numbers
elif operator == "-":
    print(num1-num2)

# For multiplying two numbers
elif operator == "*":
    print(num1*num2)

# For dividing two numbers
elif operator == "/":
    print(num1/num2)

else:
    print("Please enter a valid operator........")