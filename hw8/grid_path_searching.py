"""
A two dimensional grid has M horizontal rows and N vertical columns. Let (i,j) denote the square at the 
(i+1)th row from the top and the (j+1)th column from the left i.e., they are 0-indexed.Within the grid, 
for each i and j (0≤i≤M−1, 0≤j≤N−1), there can only be two symbols # and . where # denotes a blockage 
and . denotes a passable opening. Starting at the upper left and only moving downwards and rightwards, 
find the number of connected paths between the top-left square and the bottom right square by traversing 
only the intermediate squares with the . symbol. The start and end positions are never be marked with #.

Example:

M=3 and N=4
.

...#
.#..
....

calling count_paths(3,4,[(0,3),(1,1)]) returns the answer is 3. Here is the function signature:
count_paths(m,n,blocks) where m is the number of rows and n is the number of columns.
The blocks variable is a list of tuples indicating the blocked # entries in the grid.
"""
from copy import deepcopy


def count_paths(m,n,blocks):
    """
    Counts the number of viable paths from the top left to the bottom right square of a specified grid
    :param m:
    :param n:
    :param blocks:
    :return:
    """
    assert isinstance(m, int)
    assert m > 0
    assert isinstance(n, int)
    assert n > 0

    for block in blocks:
        assert isinstance(block, tuple)
        assert isinstance(block[0], int)
        assert 0 <= block[0] < m
        assert isinstance(block[1], int)
        assert 0 <= block[1] < n

    tree = build_tree((0,0), m, n, blocks)
    paths = dfs_search(tree, target=(m-1, n-1))
    return len(paths)


def build_tree(point, m, n, blocks):
    """
    recursively builds a tree starting from the top left corner of
    all viable points
    :param blocks:
    :return:
    """

    tree = dict()

    tree[point] = list()
    for neighbor in neighbors(point, m, n, blocks):
        tree[point].append(build_tree(neighbor, m, n, blocks))

    return tree


def neighbors(point, m, n, blocks):
    """
    yields neighbors of a point
    :param point:
    :return:
    """
    candidates = (point[0]+1, point[1]), (point[0], point[1]+1)

    for candidate in candidates:
        if candidate[0] <= m and candidate[1] <= n and candidate not in blocks:
            yield candidate


def dfs_search(tree, target, *, path=None, paths=None):
    """
    Searches the tree for a given target point using dfs.
    Since exhaustive search, dfs vs bfs don't matter
    :param tree:
    :param target:
    :param paths:
    :return:
    """
    if paths is None:
        paths = list()

    if path is None:
        path = list()

    for point, subtrees in tree.items():

        path.append(point)
        if point == target:
            paths.append(path)

        else:
            for subtree in subtrees:
                dfs_search(subtree, target, paths=paths, path=deepcopy(path))

    return paths


def print_grid(m, n, blocks):
    grid = [["." for j in range(n)] for i in range(m)]

    for i, j in blocks:
        grid[i][j] = "#"

    for row in grid:
        print(" ".join(row))


def print_path_on_grid(m, n, blocks, path):
    grid = [["." for j in range(n)] for i in range(m)]

    for i, j in blocks:
        grid[i][j] = "#"

    for i, j in path:
        grid[i][j] = "+"

    for row in grid:
        print(" ".join(row))


if __name__ == '__main__':


    M = 9
    N = 10
    BLOCKS = [(0, 3), (1, 1), (1,3), (3,3), (4,3), (6,3), (7,3), (8,3),(2,6), (3,6), (4,6), (5,6), (6,6)]
    START = (0,0)
    TARGET = (M-1, N-1)


    tree = build_tree(START,M, N, BLOCKS)
    print_grid(M, N, BLOCKS)
    print("--------------------------")
    print("number of paths:", count_paths(M, N, BLOCKS), "\n\n")
    paths = dfs_search(tree, target=TARGET)
    for path in paths:
        print_path_on_grid(M, N, BLOCKS, path)
        print("--------------------------")