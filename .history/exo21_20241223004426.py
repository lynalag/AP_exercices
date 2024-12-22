def length(lst):
    """
    Returns the number of elements in the list.
    
    Parameters:
    lst (list): The input list whose length is to be calculated.
    
    Returns:
    int: The number of elements in the list.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return len(lst)

def mean(lst):
    """
    Calculates the arithmetic mean of the elements in the list.
    
    Parameters:
    lst (list): The input list of numbers.
    
    Returns:
    float: The arithmetic mean of the list elements. Returns None if the list is empty.
    
    Raises:
    ValueError: If the list contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if not lst:
        return None
    
    # Check if all elements are numeric
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List contains non-numeric values.")
    
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    
    Parameters:
    lst (list): The input list of numbers.
    
    Returns:
    float: The range of the list. Returns None if the list is empty.
    
    Raises:
    ValueError: If the list contains non-numeric values.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if not lst:
        return None
    
    # Check if all elements are numeric
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List contains non-numeric values.")
    
    return max(lst) - min(lst)


# Testing the functions
sample_list = [3, 7, 2, 5, 9]

print(f"Length of the list: {length(sample_list)}")
print(f"Mean of the list: {mean(sample_list)}")
print(f"Range of the list: {range_of_list(sample_list)}")

# Testing with an empty list
empty_list = []
print(f"Mean of the empty list: {mean(empty_list)}")
print(f"Range of the empty list: {range_of_list(empty_list)}")

# Testing with a list containing non-numeric values
mixed_list = [3, 'seven', 5]
try:
    print(f"Mean of the mixed list: {mean(mixed_list)}")
except ValueError as e:
    print(e)
