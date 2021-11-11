"""
Write a function map_bitstring that takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0
if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1.
 The output of your function is a dictionary of the so-described key-value pairs.


Here is an example:


x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
map_bitstring(x)
 {'100': 0, '110': 1, '010': 0, '111': 1, '000': 0, '011': 1}
"""
import typing as tp
from collections import Counter


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


if __name__ == '__main__':
    print(map_bitstring(["101", "111", "000", "001"]))