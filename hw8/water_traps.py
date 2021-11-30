"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where
each element is unit-width wall and the integer value is the height. Suppose rain fills all available
gaps between two bordering walls.

Compute how many units of water remain trapped between the walls in the map.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle. Here's another example
for the sequence [3, 0, 1, 3, 0, 5] where the answer is 8,
Example

Here is the function signature get_trapped_water(seq) where seq is an input list, as in the examples.
"""
from dataclasses import dataclass


def get_trapped_water(seq):
    """
    Calculates the amount of water trapped between walls, depicted by a 1D sequence of numeric values
    which denote the heights of the walls. Looks for pockets of convexity, then groups pockets surrounded
    by large walls together, then calculates the amount of water that can be trapped
    :param seq:
    :return:
    """

    assert len(seq) > 0
    for elem in seq:
        assert isinstance(elem, int)
        assert elem >= 0

    nbds = convex_neighborhoods(seq)
    reduced_nbds = reduce_neighborhoods(nbds)

    total = sum([compute_neighborhood_value(nbd) for nbd in reduced_nbds])
    return total


@dataclass
class NBD:
    parent: list
    inds: list

    @property
    def start(self):
        return min(self.inds)

    @property
    def start_val(self):
        return self.parent[self.start]

    @property
    def end(self):
        return max(self.inds)

    @property
    def end_val(self):
        return self.parent[self.end]

    @property
    def elements(self):
        return [self.parent[i] for i in self.inds]

    def union(self, other):
        """
        if self.end == other.start

            AND

        if self.start_val > self.end_val and other.end_val > self.end_val
        :param other:
        :return:
        """
        return NBD(self.parent, sorted(set(self.inds).union(set(other.inds))))


def convex_neighborhoods(seq):
    """
    Finds convex pockets within the sequence and yields them as Neighborhood objects
    :param seq:
    :return:
    """

    def nbd(nbd_inds):
        return NBD(seq, nbd_inds)

    inds = list()
    i = 0

    DESCENDING = True

    while True:
        try:
            cur_val = seq[i]
        except IndexError:
            yield nbd(inds)
            break

        if i > 0:
            prev_val = seq[i-1]

            if DESCENDING and cur_val > prev_val:  # turning back up
                DESCENDING = False

            elif not DESCENDING and cur_val <= prev_val:  # turning back down
                yield nbd(inds)

                # reset with that element
                DESCENDING = True
                inds = [i-1]

        inds.append(i)
        i += 1


def reduce_neighborhoods(nbds):
    """
    Reduces the nbds by combining all where water can get trapped together,
    i.e. the start point of the lefthand nbd and the end point of the righthand nbd are the
    two highest values
    :param nbds:
    :return:
    """

    prev_nbd = None
    while True:

        try:
            cur_nbd = next(nbds)
        except StopIteration:
            if prev_nbd is not None:
                yield prev_nbd
            break

        if prev_nbd is None:  # first iteration
            prev_nbd = cur_nbd
            continue

        else:
            # if they have the same endpoint
            if all((prev_nbd.end == cur_nbd.start,
                   prev_nbd.start_val >= prev_nbd.end_val,
                   cur_nbd.end_val >= prev_nbd.end_val)):

                prev_nbd = prev_nbd.union(cur_nbd)

            else:
                yield prev_nbd
                prev_nbd = cur_nbd


def compute_neighborhood_value(nbd):
    """
    Computes the value of water trapped in a neighborhood.
    A neighborhood is defined as a sequence having the first and second largest
    elements being the first and last in the sequence.

    The value of the neighborhood is defined as the sum([min(first, last) - elem for elem in inner_elems])

    where the inner_elems are nbd[1:-1
    :param nbd:
    :return:
    """
    inner_elems = nbd.elements[1:-1]
    min_val = min(nbd.start_val, nbd.end_val)
    return sum([min_val - elem for elem in inner_elems])


if __name__ == '__main__':

    SEQ = [3, 0, 1, 3, 0, 5]

    nbds = list(convex_neighborhoods(SEQ))
    print("convex neighborhoods:")
    for nbd in nbds:
        print(nbd.elements)

    nbds = convex_neighborhoods(SEQ)
    reduced = list(reduce_neighborhoods(nbds))
    print("condensed neighborhoods")
    for nbd in reduced:
        print(nbd.elements)

    print("Total units of water trapped:", get_trapped_water(SEQ))