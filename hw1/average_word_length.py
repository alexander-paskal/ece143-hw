"""
Here is some example input text:


'''Mary had a little lamb
its fleece was white as snow
and everywhere that Mary went
the lamb was sure to go'''


Write a compute_average_word_length(instring,unique=False) function to compute the average length of the words in the input string (instring).
If the unique option is True, then exclude duplicated words.
For example, in the example input text above, the word the should be counted exactly once for the average word length if unique=True.
Note that the words are case sensitive.
Remember to carefully validate your inputs using assert statements.

Please put your Python code in a Python script file and upload it.
Please retain your submitted source files! Remember to use all the best practices we discussed in class.
You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to
those explicitly mentioned in the problem description.
"""
from collections import Counter


def compute_average_word_length(instring: str, unique: bool = False) -> float:
    """
    Computes the average word length for a string. If the unique flag is active,
    only looks at repeat words once.
    :param instring: The string to be analyzed
    :type instring: string
    :param unique: if true, ignores duplicate words
    :type unique:
    :return:
    :rtype:
    """

    # argument validation
    assert isinstance(instring, str)
    assert isinstance(unique, bool)
    ######

    # get unique word counts
    words = instring.lower().split(' ')

    if unique:
        words = set(words)  # will cause each word to have a count of just 1

    counter = Counter(words)

    # compute
    character_count: int = 0
    word_count: int = 0
    for word, count in counter.items():
        character_count += len(word) * count
        word_count += count

    return character_count / word_count



if __name__ == '__main__':
    instring = input("Enter your string. ")
    is_unique = lambda x: True if x == 'y' else False
    unique = is_unique(input("Analyze only unique words? y = yes, n = no: "))
    print(compute_average_word_length(instring, unique))

