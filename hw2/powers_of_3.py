"""
Given a set of weights {1,3,9,27}, write a function to construct any number between 1 and 40.
In other words, using the set above and the addition and subtraction operations, construct any integer between 1
 and 40 without re-using elements.
For example, 4 = 1+1+1+1 is not acceptable.

For example,

8 = 9 - 1

10 = 1 + 9

Hint: see the itertools module.
Your function should return a 4-element list of the decomposition.
For example, your return value given input 10 should be [1,0,1,0] because 1*1 + 0*3 + 9*1 + 27*0=10.
Name your function get_power_of3.
"""


def dot(arr1, arr2):
    """
    Computes the dot product of two lists
    :param arr1:
    :type arr1:
    :param arr2:
    :type arr2:
    :return:
    :rtype:
    """
    assert len(arr1) == len(arr2)

VALUES = {1,3,9,27}


def get_power_of_3(target: int):
    """
    Finds a transform B such that dot(A, Btranspose)  == target, where elements of B are within integer set {0,1}
    :param target:
    :type target:
    :return:
    :rtype:
    """

    assert isinstance(target, int)
    assert 1 <= target <= 40

    ternary = as_ternary(target+1)
    trits = list(map(lambda x: int(x) - 1, ternary))
    print(trits)


def as_ternary(num: int) -> str:
    """
    Creates a ternary representation of a number by recursion, in string format
    :param num:
    :type num:
    :return:
    :rtype:
    """
    quotient, remainder = divmod(num, 3)
    if quotient == 0:
        return str(remainder)

    return as_ternary(quotient) + str(remainder)


if __name__ == '__main__':
    for i in range(1, 40):
        print(i)
        get_power_of_3(i)