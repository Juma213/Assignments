def main():
    """
    This is a calculator method
    """
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform arithmetic operations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    
    # Check if num2 is not zero to avoid division by zero
    if num2 != 0:
        division_result = num1 / num2
    else:
        division_result = "Undefined (division by zero)"
    
    # Display the results
    print(f"\n{num1} + {num2} = {sum_result}")
    print(f"{num1} - {num2} = {difference_result}")
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {division_result}")

if __name__ == "__main__":
    main()
