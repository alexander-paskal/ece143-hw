"""
We will implement a very simple encryption scheme that closely resembles the one-time-pad. You have probably seen this
method used in movies like Unknown. The idea is that you and your counterparty share a book whose words you will use as
the raw material for a codebook. In this case, you need Metamorphosis, by Franz Kafka.

Your job is to create a codebook of 2-tuples that map to specific words in the given text based on the line and position the
words appears in the text. The text is very long so there will be duplicated words. Strip out all of the punctuation and make
 everything lowercase.

For example, the word let appears on line 1683 in the text as the fifth word (reading from left-to-right). Similarly, the word
us appears in the text on line 1761 as the fifth word.

Thus, if the message you want to send is the following:

let us not say we met late at the night about the secret
Then, one possible valid sequence for that message is the following:

 [(1394, 2), (1773, 11), (894, 10), (840, 1), (541, 2), (1192, 5), (1984, 7), (2112, 6), (1557, 2), (959, 8), (53, 10), (2232, 8), (552, 5)]
Your counterparty receives the above sequence of tuples, and, because she has the same text, she is able to look up the line and word numbers
of each of the tuples to retrieve the encoded message. Notice that the word the appears twice in the above message but is encoded differently
each time. This is because re-using codewords (i.e., 2-tuples) destroys the encryption strength. In case of repeated words, you should have a
randomized scheme to ensure that no message contains the same 2-tuple, even if the same word appears multiple times in the message. If there
is only one occurrence of a word in the text and the message uses that word repeatedly so that each occurrence of the word cannot have a unique
 2-tuple, then the message should be rejected (i.e., assert against this).

Your assignment is to create an encryption function and the corresponding decryption function to implement this scheme. Note that your
downloaded text should have 2362 lines and 25186 words in it.

Here are the function signatures:
  1 def encrypt_message(message,fname):
  2     '''
  3     Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
  4     name of a text file source for the codebook, generate a sequence of 2-tuples that
  5     represents the `(line number, word number)` of each word in the message. The output is a list
  6     of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.
  7
  8     :param message: message to encrypt
  9     :type message: str
 10     :param fname: filename for source text
 11     :type fname: str
 12     :returns: list of 2-tuples
 13     '''
 33 def decrypt_message(inlist,fname):
 34     '''
 35     Given `inlist`, which is a list of 2-tuples`fname` which is the
 36     name of a text file source for the codebook, return the encrypted message.
 37
 38     :param message: inlist to decrypt
 39     :type message: list
 40     :param fname: filename for source text
 41     :type fname: str
 42     :returns: string decrypted message
"""
import os
import string
import random
from collections import defaultdict


def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.

    To this end, I am going to create a dictionary of lists, such that each word has appended all corresponding
    codewords. When selecting a codeword for a word, i will randomly select from the list of codewords, and then remove that index
    from the list. This ensures randomization and repeatability


    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str)
    for char in message:
        if char == " ":
            continue
        assert 97 <= ord(char) <= 122
    assert isinstance(fname, str)
    assert os.path.exists(fname)
    assert fname.lower().endswith(".txt")

    encrypt = _encrypt_lookup(fname)

    words = message.split()
    output = []
    for word in words:
        codewords = encrypt[word]
        ix = random.randint(0, len(codewords) - 1)
        codeword = codewords.pop(ix)  # will throw an index error if out of codewords
        output.append(codeword)
    return output


def decrypt_message(inlist, fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message.
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist, list)
    for value in inlist:
        assert isinstance(value, tuple)
        for ix in value:
            assert isinstance(ix, int)
            assert ix >= 0
    assert isinstance(fname, str)
    assert os.path.exists(fname)
    assert fname.lower().endswith(".txt")

    lookup = _decrypt_lookup(fname)
    output = list()
    for i, j in inlist:
        word = lookup[i][j]
        output.append(word)

    return " ".join(output)


def _read_text(fname):
    with open(fname, "r") as f:
        text = f.read()

    text = text.lower()
    char_list = [
        char for char in text if char == " " or char == "\n" or char in string.ascii_lowercase
    ]

    return "".join(char_list)


def _decrypt_lookup(fname):
    text = _read_text(fname)

    lookup = dict()
    for i, line in enumerate(text.splitlines()):
        lookup[i] = dict(list(enumerate(line.split())))
    return lookup


def _encrypt_lookup(fname):
    text = _read_text(fname)

    lookup = defaultdict(list)
    for i, line in enumerate(text.splitlines()):
        for j, word in enumerate(line.split()):
            lookup[word].append((i,j))

    return lookup


if __name__ == '__main__':
    file = "metamorphosis_kafka.txt"
    message = "let us not say we met late at the night about the secret"
    encrypted = encrypt_message(message, file)
    decrypted = decrypt_message(encrypted, file)

    print(encrypted)
    print(decrypted)

    dlookup = _decrypt_lookup(file)
    elookup = _encrypt_lookup(file)

    print(len(dlookup))
    total = 0
    for words in dlookup.values():
        total += len(words)
    print(total)