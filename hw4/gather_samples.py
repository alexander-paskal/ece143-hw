"""
Now that you have get_sample working, generate n samples and tally the number of times an existing key is repeated.
 Generate a new dictionary with bitstrings as keys and with values as lists that contain the corresponding mapped
 values from map_bitstring. Here is an example for n=20,

x=get_sample(nbits=2,prob={'00':1/4,'01':1/4,'10':1/4,'11':1/4},n=20)
print(x)
 ['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']

Write a function gather_values that can produce the following output from x:

{'10': [1, 1, 1, 1, 1],
  '11': [1, 1, 1, 1, 1, 1],
  '01': [1, 1, 1],
  '00': [0, 0, 0, 0, 0, 0]}
"""
from collections import Counter
import typing as tp


def map_bitstring(bitstrings: tp.List[str]) -> tp.Dict[str, int]:
    """
    Maps a list of bits to a numeric value, 0 or 1, depending on if
    the number of 0s strictly exceeds the number of 1s
    :param n:
    :type n:
    :return:
    :rtype:
    """

    assert isinstance(bitstrings, list)
    for bitstring in bitstrings:
        print(bitstring)
        assert set(bitstring).issubset({"1", "0"})
    assert max(bitstrings, key=lambda x: len(x)) == min(bitstrings, key=lambda x: len(x))

    unique_bitstrings = set(bitstrings)

    mapped_bitstrings = {}
    for string in unique_bitstrings:
        c = Counter(string)
        mapped_bitstrings[string] = 0 if c["0"] > c["1"] else 1

    return mapped_bitstrings


def gather_values(bitstrings: tp.List[str]) -> tp.Dict[str, tp.List[int]]:
    """
    Gathers the values my guy
    :param bitstrings:
    :type bitstrings:
    :return:
    :rtype:
    """

    maps = map_bitstring(bitstrings)

    c = Counter(bitstrings)

    gathered_values = {}
    for k, v in c.items():
        value = maps[k]
        gathered_values[k] = [maps[k] for i in range(v)]

    return gathered_values


if __name__ == '__main__':
    print(gather_values(['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']))