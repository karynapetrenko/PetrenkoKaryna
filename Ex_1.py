# TASK 1
def filter_list(list):
    return [i for i in list if isinstance(i, int)]


def filter_list(list):
    b = []
    for i in list:
        a = isinstance(i, int)
        if a:
            b.append(i)
    return b


# Test cases
print(filter_list([1, 2, 'a', 'b']))  # Output: [1, 2]
print(filter_list([1, 'a', 'b', 0, 15]))  # Output: [1, 0, 15]
print(filter_list([1, 2, 'aasf', '1', '123', 123]))  # Output: [1, 2, 123]
