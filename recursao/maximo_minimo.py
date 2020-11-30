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
    n = len(lst)
    if n == 0:
        raise ValueError('Empty list')
    max_value = min_value = lst[-1]

    def max_min_rec(cursor):
        """
        t(n) = 1 + t(n-1)
        t(n) = 1 + 1 + t(n-2)
        t(n) = 1 + 1 + 1 + t(n-3)
        t(n) = 1 + 1 + 1 +...t(n-1)
        t(n) n + 1 => 0(n)


        """
        nonlocal max_value, min_value
        if cursor < 0:
            return max_value, min_value
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        return max_min_rec(cursor-1)
    return max_min_rec(n-1)



print(retorna_max_min([1]))
print(retorna_max_min([1,2]))
random_list = list(range(100))
shuffle(random_list)
print(retorna_max_min(random_list))
