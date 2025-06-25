def variance(values: list[float]) -> float:
    """
    Calculate the population variance of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The variance of the values.
    """
    
    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    from pymathstools.statistic.mean import arithmetic_mean
    avg = arithmetic_mean(values)
    return sum((x - avg) ** 2 for x in values) / len(values)


def sample_variance(values: list[float]) -> float:
    """
    Calculate the sample variance of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The sample variance of the values.
    """
    
    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    from pymathstools.statistic.mean import arithmetic_mean
    avg = arithmetic_mean(values)
    return sum((x - avg) ** 2 for x in values) / (len(values) - 1)

def standard_deviation(values: list[float]) -> float:
    """
    Calculate the standard deviation of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The standard deviation of the values.
    """
    
    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    return variance(values) ** 0.5

def sample_standard_deviation(values: list[float]) -> float:
    """
    Calculate the sample standard deviation of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The sample standard deviation of the values.
    """
    
    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    return sample_variance(values) ** 0.5

