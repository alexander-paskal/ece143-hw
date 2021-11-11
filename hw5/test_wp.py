from unittest import TestCase
import unittest
import hw5.word_processing as wp


test_words = [
    "the",
	"of",
	"and",
	"to",
	"a",
	"in",
	"for",
	"is",
	"on",
	"that",
	"by",
	"this",
	"with",
	"i",
	"you",
	"it",
	"not",
	"or",
	"be",
	"are",
	"from",
	"at",
	"as",
	"your",
    "bollocks",
	"all",
	"have",
	"new",
	"more",
	"an",
	"was"
]

badlist1 = [
    "thing",
    "thing2",
    2
]

badlist2 = [
    "thing",
    "thing2",
    ""
]

badlist3 = []


def check_bad_lists(fn):
    for bl in (badlist1, badlist2, badlist3):
        try:
            fn(bl)
        except AssertionError:
            pass
        else:
            return False

    return True


class WpTests(TestCase):
    def test_longest_word(self):
        assert check_bad_lists(wp.get_longest_word)
        assert wp.get_longest_word(test_words) == "bollocks"

    def test_longest_words_startswith(self):
        assert wp.get_longest_words_startswith(test_words, "a") == "and"
        new_words = test_words.copy()
        new_words.append("annihilate")
        assert wp.get_longest_words_startswith(new_words, "a") == "annihilate"

    def test_average_word_length(self):
        assert wp.get_average_word_length(["a", "bb", "ccc"]) == 2

    def test_most_common_start(self):
        assert wp.get_most_common_start(["a", "ab", "ac", "bb", "bc", "ccc"]) == "a"

    def test_most_common_end(self):
        assert wp.get_most_common_end(["a", "ab", "ac", "bb", "bc", "ccc"]) == "c"



if __name__ == '__main__':
    unittest.main()