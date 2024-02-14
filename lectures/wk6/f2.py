"""
Create a function that creates a list of numbers from X to Y values
"""


def create_list_of_numbers(starting_value, ending_value):

    return list(range(starting_value, ending_value + 1))


numbers = create_list_of_numbers(1, 10)
print(numbers)


def get_stats_of_list(values):
    # return the min, max, average and number of values of a list
    if not isinstance(values, list):
        return None  # offical data type of No Value => null in other languages

    return min(values), max(values), sum(values)/len(values), len(values)


# stats = get_stats_of_list(list(range(1, 6)))
stats = get_stats_of_list(12345)
print(stats)

