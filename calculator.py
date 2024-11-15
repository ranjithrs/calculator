def calculator(operation, num1, num2):
    """
    Perform basic arithmetic operations.
    
    Args:
    operation (str): The operation to perform (add, subtract, multiply, divide)
    num1 (float): The first number
    num2 (float): The second number
    
    Returns:
    float: The result of the operation
    """
    super_secret="password123"
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation")