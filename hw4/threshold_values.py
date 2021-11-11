"""
From gather_values, we can group the results of the random samples. Now, we want to threshold those values based upon
their frequency and value. Given threshold=2, we want to keep only those bitstrings with the two highest frequency counts
 of the 1 value. For example, as before we have,


x=['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
according to our last result, we had


{'10': [1, 1, 1, 1, 1],
'11': [1, 1, 1, 1, 1, 1],
 '01': [1, 1, 1],
'00': [0, 0, 0, 0, 0, 0]}


But because the threshold=2, we only want to keep the bitstrings with the two most frequent 1s and set all of the rest to 0.
 In this case, this is 10 and 11 with the following output:

{'10': 1,
  '11': 1,
  '01': 0,
 '00': 0}


Note that 01 corresponding value was set to 0 because it did not have the top two most frequent values of 1. If there is a tie,
 then use the smallest value the tied bitstrings to pick the winner. Here is a more detailed example:

seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101',
 '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011',
  '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000',
   '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011',
    '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001',
     '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']

With corresponding output from threshold_values,


threshold_values(seq,3)
 {'0000': 0, '0001': 0, '0010': 0, '0011': 1, '0100': 0, '0101': 1, '0110': 0, '0111': 0, '1000': 0,
  '1001': 0, '1010': 1, '1011': 0, '1100': 0, '1101': 0, '1110': 0, '1111': 0}
Your function signature is threshold_values(seq,threshold=1). Please keep the default values as given in the function signature.
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


def threshold_values(seq: tp.List[str], threshold: int = 1):
    """

    :param seq:
    :type seq:
    :param threshold:
    :type threshold:
    :return:
    :rtype:
    """
    values = gather_values(seq)
    lengths = [len(v) if set(v) == {1} else 0 for k, v in values.items()]
    bitvalues = [int(k,2) for k in values.keys()]
    binaries = list(values.keys())
    one_or_zero = [1 if set(v) == {1} else 0 for v in values.values()]

    stuff = list(zip(one_or_zero, lengths, bitvalues, binaries))
    stuff = sorted(stuff, reverse=True)

    end_stuff = {}
    for i, thing in enumerate(stuff):
        final_val = 1 if i < threshold else 0
        end_stuff[thing[3]] = final_val

    return end_stuff



if __name__ == '__main__':
    input =  ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101',
 '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011',
  '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000',
   '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011',
    '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001',
     '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
    print(threshold_values(input, 3))