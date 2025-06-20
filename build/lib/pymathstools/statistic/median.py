def median(values : list[float]) -> float:
    """
    Calculate the median of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The median of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    sorted_values = sorted(values)
    
    if len(values) % 2 == 1:
        return sorted_values[len(sorted_values) // 2]
    else:
        mid_index = len(sorted_values) // 2
        return (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2
    
def median_absolute_deviation(values : list[float]) -> float:
    """
    Calculate the median absolute deviation (MAD) of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The median absolute deviation of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    med = median(values)
    deviations = [abs(x - med) for x in values]
    
    return median(deviations)

def weighted_median(values : list[float], weights : list[float]) -> float | tuple[float]:
    """
    Calculate the weighted median of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    weights (list[float]): A list of weights corresponding to the values.

    Returns:
    float : The weighted median of the values. Returns the mean of the upper and lower median.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    
    if not 0.999 < sum(weights) < 1.001:
        raise ValueError("Weights must sum to 1.")
    
    return (upper_weighted_median(values, weights) + lower_weighted_median(values, weights)) / 2



def upper_weighted_median(values : list[float], weights : list[float]) -> float:
    """
    Calculate the upper weighted median of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    weights (list[float]): A list of weights corresponding to the values.
    Returns:

    float: The upper weighted median of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    
    if not 0.999 < sum(weights) < 1.001:
        raise ValueError("Weights must sum to 1.")
    
    sorted_pairs = sorted(zip(values, weights), key=lambda x: x[0])
    cumulative_weight = 0.0

    for index in range(len(sorted_pairs)-1, -1, -1):
        weight = sorted_pairs[index][1]
        cumulative_weight += weight
        
        if cumulative_weight >= 0.5:
            return sorted_pairs[index][0]
        

def lower_weighted_median(values : list[float], weights : list[float]) -> float:
    """
    Calculate the lower weighted median of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    weights (list[float]): A list of weights corresponding to the values.

    Returns:
    float: The lower weighted median of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if not weights:
        raise ValueError("The list of weights cannot be empty.")
    
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    
    if not 0.999 < sum(weights) < 1.001:
        raise ValueError("Weights must sum to 1.")
    
    sorted_pairs = sorted(zip(values, weights), key=lambda x: x[0])
    cumulative_weight = 0.0

    for value, weight in sorted_pairs:
        cumulative_weight += weight
        
        if cumulative_weight >= 0.5:
            return value



def percentile(values : list[float], p : float) -> float:
    """
    Calculate the p-th percentile of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.
    p (float): The desired percentile, between 0 and 100.

    Returns:
    float: The p-th percentile of the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100.")
    
    sorted_values = sorted(values)
    n = (p/100)*(len(sorted_values)-1)

    if n == int(n):
        return sorted_values[int(n)]
    else:
        return sorted_values[int(n)] + (n-int(n))*(sorted_values[int(n)+1] - sorted_values[int(n)])
    

def interquartile_range(values : list[float]) -> float:
    """
    Calculate the interquartile range (IQR) of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The interquartile range of the values.
    """

    if len(values) < 4:
        raise ValueError("The list must contain at least 4 values to calculate the interquartile range.")
    
    return percentile(values, 75) - percentile(values, 25)


def midhinge(values : list[float]) -> float:
    """
    Calculate the midhinge of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The midhinge of the values.
    """

    if len(values) < 4:
        raise ValueError("The list must contain at least 4 values to calculate the midhinge.")
    
    return (percentile(values, 25) + percentile(values, 75)) / 2

def first_quartile(values : list[float]) -> float:
    """
    Calculate the first quartile (Q1) of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The first quartile of the values.
    """
    
    if len(values) < 4:
        raise ValueError("The list must contain at least 4 values to calculate the first quartile.")
    
    return percentile(values, 25)

def third_quartile(values : list[float]) -> float:
    """
    Calculate the third quartile (Q3) of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The third quartile of the values.
    """
    
    if len(values) < 4:
        raise ValueError("The list must contain at least 4 values to calculate the third quartile.")
    
    return percentile(values, 75)

def quartile_deviation(values : list[float]) -> float:
    """
    Calculate the quartile deviation of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The quartile deviation of the values.
    """
    
    if len(values) < 4:
        raise ValueError("The list must contain at least 4 values to calculate the quartile deviation.")
    return interquartile_range(values) / 2

def coefficient_quartile_deviation(values : list[float]) -> float:
    """
    Calculate the coefficient of quartile deviation of the given list of numbers.

    Parameters:
    values (list[float]): A list of numerical values.

    Returns:
    float: The coefficient of quartile deviation of the values.
    """
    
    if len(values) < 4:
        raise ValueError("The list must contain at least 4 values to calculate the coefficient of quartile deviation.")
    
    q1 = first_quartile(values)
    q3 = third_quartile(values)

    return (q3-q1)/(q3+q1) if (q3+q1) != 0 else None

