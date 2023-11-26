"""This module prints a full name."""

def say_my_name(first_name, last_name=""):
    """
    A function that takes two arguments to print the name.

    Args:
        first_name (str): The first name of the function argument.
        last_name (str): The second name of the function argument.

    Returns:
        str: Full name as a string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
