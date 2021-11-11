"""
Download this corpus of 10,000 common English words and write the following functions given a list of words:

Compute the average length of the words (get_average_word_length(words))
What is the longest word (get_longest_word(words))?
What is the longest word that starts with a single letter (get_longest_words_startswith(words,start))
What is the most common starting letter (get_most_common_start(words))?
What is the most common ending letter (get_most_common_end(words))?
For testing you can use this bit of code to download the words from the corpus:

from urllib.request import urlopen
u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
response = urlopen(u)
words = [i.strip().decode('utf8') for i in response.readlines()]
Please put your Python code in a Python script file and upload it.
Please retain your submitted source files! Remember to use all the best practices we discussed in class.
You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to
those explicitly mentioned in the problem description.
"""
from collections import Counter



def validate_words(fn):
    def inner(words, *args, **kwargs):
        """
        Do i need a docstring?
        :param words:
        :type words:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        assert isinstance(words, list)
        assert len(words) > 0
        for word in words:
            assert isinstance(word, str)
            assert len(word) > 0
        result = fn(words, *args, **kwargs)
        return result
    return inner


@validate_words
def get_average_word_length(words):
    """
    Finds the average word length
    :param words:
    :type words:
    :return:
    :rtype:
    """
    return sum([len(word) for word in words]) / len(words)


@validate_words
def get_longest_word(words):
    """
    Finds the longest word in words. If multiple words share the length,
    will return the first word encountered
    :param words: 
    :type words: 
    :return: 
    :rtype: 
    """
    longest_len, longest_word = 0, ""
    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
            longest_word = word
            
    return longest_word


@validate_words
def get_longest_words_startswith(words,start):
    """
    Gets the longest word that starts with a certain letter.
    :param words: 
    :type words: 
    :param start: 
    :type start: 
    :return: 
    :rtype: 
    """
    assert isinstance(start, str)
    assert len(start) == 1

    candidates = list(filter(lambda x: x.lower().startswith(start), words))
    # maybe assert len(candidates) > 0?
    return get_longest_word(candidates)



@validate_words
def get_most_common_start(words):
    """
    Finds the most common starting letter for the words given.
    returns a single character
    Pushes all words to lower case
    :param words:
    :type words:
    :return:
    :rtype:
    """
    start_letters = map(lambda x: x.lower()[0], words)
    counts = Counter(start_letters)
    return counts.most_common()[0][0]



@validate_words
def get_most_common_end(words):
    """
    Finds the most common ending letter for the words given.
    returns a single character
    Pushes all words to lower case
    :param words:
    :type words:
    :return:
    :rtype:
    """
    end_letters = map(lambda x: x.lower()[-1], words)
    counts = Counter(end_letters)
    return counts.most_common()[0][0]
