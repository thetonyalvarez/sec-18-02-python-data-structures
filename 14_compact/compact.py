def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [t for t in lst if t]


# Return a copy of lst with non-true elements removed.

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
# [1, 2, 'All done']