def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "we can't divide by zero"
    return result