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
import typing


def get_power_of3(target: int, *, vector: typing.Optional[typing.List] = None, invert: bool = False):
    """
    Finds a transform B such that dot(A, Btranspose)  == target, where A is a sorted list of powers of three
    [1,3,9,27] and B is some list of equal length are within integer set {-1,0,1}

    :param target:
    :type target:
    :param vector:
    :type vector:
    :param invert:
    :type invert:
    :return:
    :rtype:
    """
    assert isinstance(target, int)

    if vector is None:
        assert 1 <= target <= 40
        vector = []


    if len(vector) == 4:
        return vector[::-1]

    multiplier = -1 if invert else 1
    power = 3-len(vector)
    divisor = 3**power


    if target >= divisor:
        vector.append(1*multiplier)
        return get_power_of3(target-divisor, vector=vector, invert=invert)

    if divisor // 2 < target < divisor:
        vector.append(1*multiplier)
        return get_power_of3(divisor-target, vector=vector, invert=not invert)

    vector.append(0)
    return get_power_of3(target, vector=vector, invert=invert)


if __name__ == '__main__':
    outputs = [(i, get_power_of3(i)) for i in range(1, 41)]

    print(get_power_of3(10))


