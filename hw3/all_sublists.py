"""
Generate all sublists of a list. Note there will be 2**len(x)-1 subsets of the list x, excluding the empty list.
For example, the list [0,1,2] has seven sublists: [[0],[1],[2],[0,1],[1,2],[0,2],[0,1,2]].
Note that you don't have to mind the ordering of each sublist.
The function should assert against an input empty list ([]).
The input to the function should be a list of unique items to be processed.

Hint: use recursion.
Hint: You probably want to use list instead of set.
Here is the output of all_sublists(list(range(4))):

  [[0],    [1],    [2],    [3],    [2, 3],    [1, 2],    [1, 3],    [1, 2, 3],    [0, 1],
   [0, 2],    [0, 3],    [0, 2, 3],    [0, 1, 2],    [0, 1, 3],    [0, 1, 2, 3]]

"""
import typing as tp
from itertools import combinations


def all_sublists(iterable):
    """
    Returns all the sublists of a list
    :param iterable:
    :type iterable:
    :param subsets:
    :type subsets:
    :param mask:
    :type mask:
    :return:
    :rtype:
    """
    assert isinstance(iterable, list) and len(iterable) > 0
    assert len(set(iterable)) == len(iterable)

    return list(inner(iterable))


def inner(iterable: tp.List, *, subsets: tp.Optional[tp.List[tp.List]] = None, mask: int = None) -> tp.List[tp.List]:
    """
    Returns all the sublists of a list
    :param iterable:
    :type iterable:
    :param subsets:
    :type subsets:
    :param mask:
    :type mask:
    :return:
    :rtype:
    """

    if mask is None:
        mask = len(iterable)

    if subsets is None:
        subsets = []

    if mask > 0:
        yield from inner(iterable, subsets=subsets, mask=mask - 1)
        for combination in combinations(iterable, r=mask):
            yield list(combination)


if __name__ == '__main__':
    things = list(range(4))
    print(type(things), len(things))
    for thing in all_sublists(things):
        print(thing)
