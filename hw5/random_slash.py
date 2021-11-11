"""
A 6x6 black-and-white image is represented as a Numpy array x as in the following,

# >>> import numpy as np
# >>> x = np.eye(6)
Note that this is not a grayscale or color image for which there would be three dimensions (e.g., 6 x 6 x 3).
This can easily be visualized using Matplotlib's imshow function, as in the following:
#
# >>> from matplotlib.pylab import subplots, cm >>> fig, ax = subplots()  >>> ax.imshow(x,cmap=cm.gray_r)
drawing

To debug an image processing algorithm, you have to generate a large number of exemplar training images that consist of such Numpy arrays.
Each image should represent a forward or backward leaning (shown above) slash symbol. Each symbol must consist of at least two non-zero
pixels and be contiguous (i.e., no gaps). For example, the longest possible slash symbol that is representable in a 6x6 image is the 6
nonzero pixel diagonal image show above (or its opposite leaning forwardslash variant).

The assignment is to write a function that can produce a uniformly random forward or backslashed image (i.e., Numpy array) of at least
two non-zero pixels. Here is some code that generates the following figure,

fig,axs=subplots(3,3,sharex=True,sharey=True)
 for ax in axs.flatten():
     ax.imshow(gen_rand_slash(),cmap=cm.gray_r)


drawing

Here is the function signature: gen_rand_slash(m=6,n=6,direction='back'). The direction keyword argument can be either back or forward.
The m is the number of rows in the image.

Note: Don't import matplotlib in your solutions. Only allowed external library is numpy.
"""
import numpy as np
import random
from itertools import product


def gen_rand_slash(m=6,n=6,direction='back'):
    """
    Cause i need a freaking docstring
    :param m:
    :type m:
    :param n:
    :type n:
    :param direction:
    :type direction:
    :return:
    :rtype:
    """
    s = SlashImage(m, n)
    s.random_slash(direction)
    return s.image


class SlashImage:
    def __init__(self, m=6, n=6):
        for dim in m, n:
            assert isinstance(dim, int)
            assert dim > 1

        self._m = m
        self._n = n
        self._base = np.zeros((m,n), dtype=int)
        self.image = self._base

    def preview(self):
        divider = "-" + "-" * 4*self._n
        strs = [divider]
        for i in range(self._m):
            str_row = "| "
            for j in range(self._n):
                str_row += str(self.image[i,j]) + " | "
            strs.append(str_row)
            strs.append(divider)

        return "\n".join(strs)

    def random_slash(self, direction):
        self.image = np.zeros((self._m,self._n), dtype=int)
        assert direction in ("back", "forward")

        rmult = 1
        cmult = 1


        row, col, length = random.choice(list(self._possible_combinations()))

        indices = [(row+rmult*i, col+cmult*i) for i in range(length+1)]

        for ix in indices:
            self.image[ix[0], ix[1]] = 1

        if direction == "forward":
            self.image = np.flip(self.image, axis=0)

        return indices



    def _possible_combinations(self):
        start_rows = start_columns = range(0, self._m - 1)
        lengths = range(1, min(self._m, self._n)+2)
        for combo in product(start_rows, start_columns, lengths):
            if self._valid_combination(*combo):
                yield combo

    def _valid_combination(self, row, column, length):
        if length >= 1 and row + length < self._m and column + length < self._n:
            return True
        return False

#
# if __name__ == '__main__':
#     import matplotlib.pyplot as plt
#
#     fig, axs = plt.subplots(10, 10, sharex=True, sharey=True)
#     for ax in axs.flatten():
#         image = gen_rand_slash()
#         ax.imshow(image, cmap=plt.cm.gray_r)
#     plt.show()