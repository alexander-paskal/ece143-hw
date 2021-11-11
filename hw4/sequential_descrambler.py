"""
You are given a sequence of n lower-case letters and a k-tuple of integers that indicate partition-lengths of the sequence.
Also, you have a dictionary of commonly used words. The n letters represent a phrase of k words where the length of the
jth word is the jth element of the tuple.

Here is an example: w = 'trleeohelh' , k=(5,5). Your generator descrambler(w,k) should iteratively yield the output
['hello three','three hello','hello there','there hello']. Note that because both words have 5 characters,
it is not possible to definitively know the order of the phrase.

Here are more interesting examples:

list(descrambler('choeounokeoitg',(3,5,6)))

 ['one tough cookie',
  'one ought cookie',
  'neo tough cookie',
  'neo ought cookie']

 list(descrambler('qeodwnsciseuesincereins',(4,7,12)))

 ['wise insider consequences']

Hints

Use a hash-map to process the input file of valid words
The order of the strings in the output sequence is irrelevent.
Within each output string, the order of words should follow the sequence of word-lengths in k.
Use itertools.
The autograder may time out if your solution is too slow.
The word list above is in a file /tmp/google-10000-english-no-swears.txt on the autograder.
"""
from itertools import combinations
from collections import Counter, defaultdict
import copy




def descrambler(w, k):
    """
    Descrabmles some words

    Approach:

    map the dictionary to a list of sets
    filter to small_list where only subsets of set(w) remain

    for each subset in small_lists, recursively find the k-1 complementary sets

    Once you have your sequences of sets, you can go through and convert
    each set in the sequence into a subsequence of words that match that set
    For each sequence of subsequences, you can then compute the cartesian product to get all
    of the combinations of words

    :param w: sequence of lower case letters
    :type w:
    :param k: number of words
    :type k:
    :return:
    :rtype:
    """
    assert isinstance(w, str)
    assert isinstance(k, tuple)
    for elem in k:
        assert isinstance(elem, int)

    FILENAME = "/tmp/google-10000-english-no-swears.txt"

    with open(FILENAME, "r") as f:
        text = f.read()
        words = text.splitlines()

    dictionary = create_dictionary(words)
    dictionary = filter_dictionary(dictionary, w)
    k = list(sorted(k, reverse=True))
    yield from _recursive_search(w, dictionary, k)


def create_dictionary(words):
    d = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        d[key].append(word)

    return d


def filter_dictionary(dictionary, word):
    d = defaultdict(list)
    for k, v in dictionary.items():
        foreign = False
        for char in k:
            if char not in word:
                foreign = True
                break
        if not foreign:
            d[k] = v
    return d


def word_count(word):
    return tuple(Counter(word).most_common())

def word_from_count(word_count):
    return "".join([v[1]*v[0] for v in word_count])


def count_difference(count1, count2):
    d1 = dict(count1)
    d2 = dict(count2)

    d3 = copy.deepcopy(d1)
    for k, v in d2.items():
        diff = d1[k] - d2[k]
        if diff > 0:
            d3[k] = diff
        else:
            d3.pop(k)

    return tuple(Counter(d3).most_common())


def _recursive_search(w, dictionary, k, existing=None):
    """
    finds the substrings
    :param w:
    :type w:
    :param counts:
    :type counts:
    :param k:
    :type k:
    :param existing:
    :type existing:
    :return:
    :rtype:
    """


    if existing is None:
        existing = list()

    if len(k) == 0:
        yield " ".join(existing)
    else:
        substrs = list(combinations(w, r=k[0]))
        substrs = {"".join(sorted(substr)) for substr in substrs}

        for substr in substrs:
            for word in dictionary[substr]:
                n_existing = copy.deepcopy(existing)
                n_existing.append(word)
                n_w = word_from_count(count_difference(word_count(w), word_count(substr)))
                n_k = copy.deepcopy(k)
                n_k.pop(0)
                yield from _recursive_search(n_w, dictionary, n_k, existing=n_existing)


if __name__ == '__main__':
    print(list(descrambler("choeounokeoitg", (3,5,6))))
    print(list(descrambler('qeodwnsciseuesincereins', (4, 7, 12))))
    print(list(descrambler(w = 'trleeohelh' , k=(5,5))))
    # print(list(descrambler("waswewillhomecanus", (3,2,4,4,3,2))))
