"""
The Frobenius equation is the Diophantine equation,

a_1 x_1 +... + a_n x_n = b

where a_i> 0 are positive integers, b> 0 is a positive integer, and the solution x_i consists
of non-negative integers. Here is a sample run,

->>> solvefrob([1,2,3,5],10)
 [(0, 0, 0, 2),
  (0, 1, 1, 1),
  (0, 2, 2, 0),
  (0, 5, 0, 0),
  (1, 0, 3, 0),
  (1, 2, 0, 1),
  (1, 3, 1, 0),
  (2, 0, 1, 1),
  (2, 1, 2, 0),
  (2, 4, 0, 0),
  (3, 1, 0, 1),
  (3, 2, 1, 0),
  (4, 0, 2, 0),
  (4, 3, 0, 0),
  (5, 0, 0, 1),
  (5, 1, 1, 0),
  (6, 2, 0, 0),
  (7, 0, 1, 0),
  (8, 1, 0, 0),
  (10, 0, 0, 0)]

Hint: Use Numpy broadcasting effectively. There is a timeout in the test-case,
so if it takes too long to compute (e.g, you used too many for loops), it will be marked wrong.
The function signature is solvefrob(coefs,b) where coefs is the list of a_i coefficients.
You can only use Numpy for this problem. No other third party packages.
"""
import numpy as np
import time


def solvefrob(coefs, b):
    """
    Solves frobenius equation

    Bounding the domain space makes enormous difference in performance
    :param coefs:
    :param b:
    :return:
    """

    for elem in coefs:
        assert isinstance(elem, int)
        assert elem > 0

    assert isinstance(b, int)
    assert b > 0
    arr = None
    for i, coef in enumerate(coefs[::-1]):
        max = b // coef
        r = np.arange(max+1)[:, None]
        if arr is None:
            arr = r
        else:
            new_r = np.repeat(r, len(arr))[:, None]
            new_arr = np.concatenate([arr for _ in range(len(r))])
            arr = np.concatenate([new_r, new_arr], axis=1)

    out = np.matmul(arr, coefs)
    results = arr[out == b].tolist()
    results = [tuple(thing) for thing in results]

    return results



if __name__ == '__main__':

    for f in [solvefrob]:
        coefs = [1,2,3,5,6,4,6,4]
        b = 15
        s = time.time()
        results = f(coefs, b)
        e = time.time()
        print(f"{f.__name__}, time: {e-s} seconds")

        for result in results:
            print(result, coefs, np.dot(result, coefs))
