def mode(values : list[float]) -> tuple[float] | float:
    """
    Calculate the mode of the given list of values.

    parameters:
    values (list[float]): A list of numerical values.

    Returns:
    tuple[float] | float: The mode of the values. If there are multiple modes, returns a tuple with all the modes sorted in ascending order.
    """

    if not values:
        raise ValueError("The list must contain at least one value to calculate the mode.")

    frequency = {}
    max_freq = 0

    for i in range(len(values)):
        if values[i] in frequency:
            frequency[values[i]] += 1
        else:
            frequency[values[i]] = 1

        if frequency[values[i]] > max_freq:
            max_freq = frequency[values[i]]
    
    modes = [key for key, value in frequency.items() if value == max_freq]

    if len(modes) == 1:
        return modes[0]
    else:
        return tuple(sorted(modes))
    

def weighted_mode(values : list[float], weights : list[float]) -> tuple[float] | float:
    """
    Calculate the weighted mode of the given list of values.

    parameters:
    values (list[float]): A list of numerical values.
    weights (list[float]): A list of weights corresponding to the values.

    Returns:
    tuple[float] | float: The weighted mode of the values. If there are multiple modes, returns a tuple with all the modes sorted in ascending order.
    """

    if not values: 
        raise ValueError("The list of values cannot be empty.")
    
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")
    
    frequency = {}
    max_freq = 0

    for i in range(len(values)):
        if values[i] in frequency:
            frequency[values[i]] += weights[i]
        else:
            frequency[values[i]] = weights[i]
        
        if frequency[values[i]] > max_freq:
            max_freq = frequency[values[i]]

    modes = [key for key, value in frequency.items() if value == max_freq]
    if len(modes) == 1:
        return modes[0]
    else:
        return tuple(sorted(modes))
    
def number_occurrences_mode(values : list[float]) -> int:
    """
    Calculate the number of occurrences of the mode in the given list of values.

    parameters:
    values (list[float]): A list of numerical values.

    Returns:
    int: The number of occurrences of the mode in the values.
    """

    if not values:
        raise ValueError("The list must contain at least one value to calculate the mode.")

    occurences = 0
    mode_value = mode(values)

    if type(mode_value) == tuple:
        mode_value = mode_value[0]

    for value in values:
        if value == mode_value:
            occurences += 1
    
    return occurences

def number_occurrences_weighted_mode(values : list[float], weights : list[float]) -> int:
    """
    Calculate the number of occurrences of the weighted mode in the given list of values.

    parameters:
    values (list[float]): A list of numerical values.
    weights (list[float]): A list of weights corresponding to the values.

    Returns:
    int: The number of occurrences of the weighted mode in the values.
    """

    if not values:
        raise ValueError("The list of values cannot be empty.")
    
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")

    occurences = 0
    mode_value = weighted_mode(values, weights)

    if type(mode_value) == tuple:
        mode_value = mode_value[0]

    for i in range(len(values)):
        if values[i] == mode_value:
            occurences += weights[i]
    
    return occurences