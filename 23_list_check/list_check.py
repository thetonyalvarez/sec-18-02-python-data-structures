def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    
    # print(all(isinstance(item, list) for item in lst))
    return all([isinstance(item, list) for item in lst])


# Are all items in lst a list?

print(list_check([[1], [2, 3]]))
# True

print(list_check([[1], "nope"]))
# False