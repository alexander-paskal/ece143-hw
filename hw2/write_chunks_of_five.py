"""
Using corpus of 10,000 common English words, create a new file that consists of each consecutive non-overlapping
sequence of five lines merged into one line.
Here are the first 10 lines of ouptut corresponding to the above sample corpus:

the of and to a
in for is on that
by this with i you
it not or be are
from at as your all
have new more an was
we will home can us
about if page my has
search free but our one
other do no information time

.
If the last group has less than five at the end, just write out the last group.
Here is your function signature: write_chunks_of_five(words,fname).
The words is a list of words from the above corpus and fname is the output filename string.

Please put your Python code in a Python script file and upload it.
Please retain your submitted source files! Remember to use all the best practices we discussed in class.
You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are
restricted to those explicitly mentioned in the problem description.
"""
import typing


def write_chunks_of_five(words: typing.List, fname: str):
    """
    Takes a list of words and creates a file of lines where each line contains the next 5 words in the input
    sequence, joined on a space. Lines are non-overlapping

    i.e. [a,b,c,d,e,f,g,h,i,j]  ->  ["a b c d e", "f g h i j"]  -> file.writelines()


    :param words: list of words
    :type words: List[str]
    :param fname: filename, must end with .txt
    :type fname: str
    :return:
    :rtype:
    """
    for word in words:
        assert isinstance(word, str)
    assert isinstance(fname, str) and fname.endswith(".txt")


    lines = []
    line = []
    for i, word in enumerate(words):
        if i % 5 == 0:
            lines.append(" ".join(line))
            line = []

        line.append(word)

    lines.append(" ".join(line))  # will get the last line that never got added

    lines = lines[1:]
    with open(fname, "w") as f:
        for line in lines:
            f.write(line+"\n")



if __name__ == '__main__':
    with open("corpus.txt", "r") as f:
        words = f.read()

    words = words.splitlines()
    fname = "chunks_five_out.txt"
    write_chunks_of_five(words, fname)

