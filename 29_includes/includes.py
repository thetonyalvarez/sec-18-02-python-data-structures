def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    # for val in collection:
    if isinstance(collection, set):
        # print(type(collection))
        for val in collection:
            if val == sought:
                return True
    elif isinstance(collection, dict):
        if sought in collection.values():
            return True
    else:
        if start == None:
            for val in collection:
                if val == sought:
                    return True
        elif start:
            if sought in collection[start:]:
                return True
            else:
                return False


# Is sought in collection, starting at index start?

#     Return True/False if sought is in the given collection:
#     - lists/strings/sets/tuples: returns True/False if sought present
#     - dictionaries: return True/False if *value* of sought in dictionary

#     If string/list/tuple and `start` is provided, starts searching only at that
#     index. This `start` is ignored for sets/dictionaries, since they aren't
#     ordered.

print(includes([1, 2, 3], 1))
# True

print(includes([1, 2, 3], 1, 2))
# False

print(includes("hello", "o"))
# True

print(includes(('Elmo', 5, 'red'), 'red', 1))
# True

print(includes({1, 2, 3}, 1))
# True

print(includes({1, 2, 3}, 1, 3))
# "start" ignored for sets!
# True

print(includes({"apple": "red", "berry": "blue"}, "blue"))
# True