def check_separators_symmetry(input_string: str) -> str:
    """
    Checks if the separators in the input string are symmetric.
    The function checks for matching pairs of parentheses '()', brackets '[]', and braces '{}'.
    Args:
        input_string (str): The string to check.
    Returns:
        str: A message indicating whether the separators are symmetric or not.
    """

    separator_pairs = {')': '(', ']': '[', '}': '{'}
    opening_separators = set(separator_pairs.values())
    closing_separators = set(separator_pairs.keys())
    stack = []

    for char in input_string:
        if char in opening_separators:
            stack.append(char)
        elif char in closing_separators:
            # Check if there is a corresponding opening separator
            if not stack:
                return f"{input_string}: Asymmetrical"

            last_open = stack.pop()
            # Check for mismatched pair
            if separator_pairs[char] != last_open:
                return f"{input_string}: Asymmetrical"

        # Ignore all other characters

    # Final check: are there any unclosed separators?
    if not stack:
        return f"{input_string}: Symmetrical"
    else:
        return f"{input_string}: Asymmetrical"
