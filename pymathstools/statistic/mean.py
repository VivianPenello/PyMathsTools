def arithmetic_mean(values : list[float]) -> float:
    """
    Calculate the mean (average) of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The mean of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    return sum(values) / len(values)

def weighted_mean(values : list[float], weights : list[float]) -> float:
    """
    Calculate the weighted mean of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    weights (list[float]): A list of weights corresponding to the values.

    Returns:
    float: The weighted mean of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    if len(values) != len(weights) or not values or not weights:
        raise ValueError("The lists of values and weights must have the same length and cannot be empty.")
    
    list_products = [v * w for v, w in zip(values, weights)]

    return sum(list_products) / sum(weights)

def geometric_mean(values : list[float]) -> float:
    """
    Calculate the geometric mean of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The geometric mean of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    product = 1.0
    for i in range(len(values)):
        if values[i] < 0:
            pass
        else:
            product *= values[i]
    
    return product ** (1 / len(values)) 

def harmonic_mean(values : list[float]) -> float:
    """
    Calculate the harmonic mean of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The harmonic mean of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    intermediate_list = []

    for i in range(len(values)):
        if values[i] <= 0:
            pass
        else:
            intermediate_list.append(1 / values[i])

    return len(intermediate_list) / sum(intermediate_list) 

def quadratic_mean(values : list[float]) -> float:
    """
    Calculate the quadratic mean of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The quadratic mean of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    return (sum(x ** 2 for x in values) / len(values)) ** 0.5


def midrange(values : list[float]) -> float:
    """
    Calculate the midrange of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The midrange of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    return (min(values) + max(values)) / 2

def trimmed_mean(values : list[float], lower_trim: float, upper_trim: float = None) -> float:
    """
    Calculate the trimmed mean of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    trimn (float): The fraction of values to trim from each end.

    Returns:
    float: The trimmed mean of the values.
    """

    if upper_trim is None:
        upper_trim = lower_trim

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if 0 > lower_trim or lower_trim > 0.5 or 0 > upper_trim or upper_trim > 0.5:
        raise ValueError("Trim trim must be between 0 and 0.5.")
    
    sorted_values = sorted(values)
    n= len(sorted_values)

    truncated_values = sorted_values[int(n * lower_trim):int(n * (1 - upper_trim))]

    return sum(truncated_values) / len(truncated_values)

def winsorized_mean(values : list[float], lower_percentile: float, upper_percentile: float = None) -> float:
    """
    Calculate the winsorized mean of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    lower_percentile (float): The lower percentile to winsorize.
    upper_percentile (float): The upper percentile to winsorize (optional; defaults to lower_percentile).

    Returns:
    float: The winsorized mean of the values.
    """

    if upper_percentile is None:
        upper_percentile = lower_percentile

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if 0 > lower_percentile or 0 > upper_percentile or lower_percentile+ upper_percentile > 1:
        raise ValueError("Percentiles must be between 0 and 1.")
    
    sorted_values = sorted(values)
    n = len(sorted_values)

    lower_index = int(n * lower_percentile)
    upper_index = int(n - (n * upper_percentile))

    truncated_values = [sorted_values[lower_index]] *lower_index + sorted_values[lower_index:upper_index] + [sorted_values[upper_index-1]]*(n - upper_index)

    return sum(truncated_values) / len(truncated_values)


def values_range(values : list[float]) -> float:
    """
    Calculate the range of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The range of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    return max(values) - min(values)



def coefficient_of_variation(values : list[float]) -> float:
    """
    Calculate the coefficient of variation of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The coefficient of variation of the values.
    """
    from .standard_deviation import standard_deviation

    if not values:
        raise ValueError("The list of values cannot be empty.")

    return standard_deviation(values) / arithmetic_mean(values) if arithmetic_mean(values) != 0 else None