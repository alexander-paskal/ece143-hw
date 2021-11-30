"""
Given a permutation of any length, generate the next permutation in lexicographic order.
 For example, this are the permutations for [1,2,3] in lexicographic order.

# >>> list(it.permutations([1,2,3]))
 [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
Then, your function next_permutation(t:tuple)->tuple should do the following

# >>> next_permutation((2,3,1))
 (3,1,2)
Because (3,1,2) is the next permutation in lexicographic order. Here is another example:

# >>> next_permutation((0, 5, 2, 1, 4, 7, 3, 6))
 (0, 5, 2, 1, 4, 7, 6, 3)
Your function should work for very long input tuples so the autograder will time-out if you
 try to brute force your solution. The last permutation should wrap aruond to the first.

# >>> next_permutation((3,2,1,0))
 (0, 1, 2, 3)
"""


def next_permutation(t: tuple) -> tuple:
    """
    Prints the permutation of the input element t immediately following t in lexicographic order
    :param t:
    :return:
    """

    assert isinstance(t, tuple)
    for elem in t:
        assert isinstance(elem, int)
    assert len(t) == len(set(t))

    RIGHT = -1
    LEFT = RIGHT - 1

    left = t[LEFT]
    right = t[RIGHT]

    while True:

        if left < right:
            if RIGHT == -1: # if first two:
                l = list()
                l.extend(t[:LEFT])
                l.append(t[RIGHT])
                l.append(t[LEFT])
                return tuple(l)
            else:
                #   pick the second highest, that's left
                #   add the rest of the elements in sorted order
                l = list()
                l.extend(t[:LEFT])
                
                remaining = sorted(t[LEFT:])
                second_highest = remaining.pop(remaining.index(left) + 1)
                l.append(second_highest)
                l.extend(sorted(remaining))
                return tuple(l)
                
        else:  # left > right
            try:
                RIGHT -= 1
                LEFT = RIGHT - 1

                left = t[LEFT]
                right = t[RIGHT]
            except IndexError:  # fully reversed list, return start condition
                return tuple(sorted(t))
        

if __name__ == '__main__':

    from itertools import permutations


    ##### Arguments
    p = (1,2,3,4,5)
    ##### End Arguments

    ps = permutations(p)

    print("Start permutation:", p)
    print("\nExpected | Actual | Matching")
    print("-"*20)

    for i in range(10):
        p_n = next(ps)
        print(p, p_n, p==p_n)
        p = next_permutation(p)

