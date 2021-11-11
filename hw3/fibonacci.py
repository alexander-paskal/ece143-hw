"""
The Fibonacci numbers are defined by the following recursion: F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1.
Write a generator to compute the first n Fibonacci numbers.
For example, for n=10, the output for list(fibonacci(n)) should be [1,1,2,3,5,8,13,21,34,55].
"""
import typing as tp


def fibonacci(n: int) -> tp.List[int]:
    """
    Creates a sequence of fibonacci numbers
    :param n: the length of the sequence to be computed
    :type n:
    :return:
    :rtype:
    """

    assert isinstance(n, int) and n > 0

    a, b = 1, 1
    yield a
    yield b

    for i in range(n-2):
        a, b = b, b+a
        yield b




if __name__ == '__main__':
    print(list(fibonacci(10)))