from collections import deque
import re


def is_palindrome(input_string: str) -> bool:
    """
    Checks if a given string is a palindrome using a deque.

    The check is case-insensitive and ignores spaces and punctuation.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # The regex pattern '[^a-z0-9]' matches anything that is NOT
    # a lowercase letter or a digit.
    cleaned_string = re.sub(r'[^a-z0-9]', '', input_string.lower())

    char_deque = deque(cleaned_string)

    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()

        if first != last:
            return False

    return True
