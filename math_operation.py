def math_operations(a, b):
    
    """
    This shall take two inputs as numbers and returns their sum and product.

    This function uses lambda functions to find:
    - The sum of the two numbers entered by user
    - The product of the two numbers entered by user

    Arguments:
    a (int or float): The first number is entered
    b (int or float): The second number is entered

    Returns:
    tuple: Sum and product of two numbers in a tuple.
    """
    sum_func = lambda x, y: x + y
    product_func = lambda x, y: x * y

    sum_result = sum_func(a, b)
    product_result = product_func(a, b)
    
    return sum_result, product_result

def main():
    # Sample input numbers
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    # Invoking the math_operations function
    sum_result, product_result = math_operations(a, b)
    
    # Printing the results
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

# Running the main function
if __name__ == "__main__":
    main()
