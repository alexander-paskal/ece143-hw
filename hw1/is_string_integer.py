"""
Homework instructions:

Write a function that takes a single string character (i.e., 'a','b','c') as input and returns True or False
if that character represents a valid integer in base 10. The function should be named is_string_integer.
Please put your Python code in a Python script file and upload it. Please retain your submitted source files!

Remember to use all the best practices we discussed in class.

You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to
those explicitly mentioned in the problem description.
"""


def is_string_integer(string: str):
    """
    This function takes in a character value and checks if it is a valid integer.

    All entries must be strings of length 1

    :param string: the string to be analyzed
    :type string: str
    :return: true or false, depending on if the character is a valid integer
    :rtype: bool
    """
    assert isinstance(string, str)
    assert len(string) == 1
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True


if __name__ == '__main__':
    string = input("Please enter your string: ")
    print(is_string_integer(string))