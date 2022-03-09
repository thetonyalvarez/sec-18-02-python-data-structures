import re


def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    count = 0

    for p in parens:
        if parens[0] == ")":
            return False
        elif p == "(":
            count = count + 1
        elif p == ")":
            count = count - 1
        
        elif count < 0:
            return False

    return count % 2 == 0



# Are the parentheses validly balanced?

print(valid_parentheses("()"))
# True

print(valid_parentheses("()()"))
# True

print(valid_parentheses("(()())"))
# True

print(valid_parentheses(")()"))
# False

print(valid_parentheses("())"))
# False

print(valid_parentheses("((())"))
# False

print(valid_parentheses(")()("))
# False