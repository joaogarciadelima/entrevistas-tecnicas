from random import shuffle


def retorna_max_min(lst):
    """
    param:lst =   lista
    return tuple(min_value, max_value
    Test ordered lists
    Test random lists
    >>> retorna_max_min([1])
    (1, 1)
    >>> retorna_max_min([1,2])
    (2, 1)
    >>> retorna_max_min(list(range(100)))
    (99, 0)
    >>> lista = list(range(100))
    >>> shuffle(lista)
    >>> retorna_max_min(lista)
    (99, 0)
    """
    if len(lst)==0:
        raise ValueError('Empty list')
    max_value = min_value = lst[0]
    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return max_value, min_value

print(retorna_max_min([1]))
print(retorna_max_min([1,2]))
random_list = list(range(100))
shuffle(random_list)
print(retorna_max_min(random_list))
