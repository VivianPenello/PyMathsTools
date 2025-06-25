def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of n.
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    
    if type(n) != int:
        raise ValueError("n must be a natural number.")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result

def exponential(exponent: float, precision: float = 1e-15) -> float:
    """
    Calculate an approximation the exponential of the given number.

    Parameters:
    exponent (float): The exponent to calculate e^x.
    precision (float): The precision for the series expansion.

    Returns:
    float: The value of e raised to the power of exponent.
    """

    if precision <= 0:
        raise ValueError("Precision must be a positive number.")
    
    if exponent == 0:
        return 1.0
    
    n = 0
    result = 1.0
    term = 1.0

    while term > precision:
        n += 1
        term *= exponent/n
        result += term
    
    return result


def ln(value: float, precision: float = 1e-15) -> float :
    """
    
    Calculate an approximation of the natural logarithm (ln) of the given number.
    
    Parameters:
    value (float): The value to calculate ln(x).
    precision (float): The precision for the series expansion.
    
    Returns:
    float: The value of the natural logarithm of the given number.
    """

    if value < 0:
        raise ValueError("The value must be a positive number.")
    
    if value == 0:
        return float("-inf")
    
    
    x = (value - 1)/(value + 1)   
    x2 = x*x
    term = x
    n = 1
    result = term/n

    while term > precision:
        term *= x2
        n += 2
        result += term/n

    return 2 * result


def log(value: float, base: float, precision: float = 1e-15) -> float :
    """
    
    Calculate an approximation of the logarithm of the given number in the given base.
    
    Parameters:
    value (float): The value to calculate the log.
    base (float): The base to calculate the log.
    precision (float): The precision for the series expansion.
    
    Returns:
    float: The value of the logarithm of the given number in the given base.
    """

    if value < 0 or base <= 0:
        raise ValueError("The value and the base must be positives numbers.")
    
    if value == base:
        return 1
    
    if base == 1:
        raise ValueError("The base can't be equal to 1.")
    
    x = 1
    power = 0

    while x < value:
        x *= base
        power += 1

    if x == value:
        return power
    
    return ln(value, precision) / ln(base, precision)