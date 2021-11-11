"""
Using Python object oriented programming, write a class called Interval that represents a one-dimensional open interval on the real line.
 This main purpose of this class is to simplify overlapping continuous intervals.
 The code below should get you started but there are a lot of missing pieces that you will have to figure out.


The API should take a pair of integers as input and respond to the + operator such that

 
 # >>> a = Interval(1,3)
 # >>> b = Interval(2,4)
 # >>> c = Interval(5,10)
 # >>> a + b
 Interval(1,4) 
 # >>> b+c
 [ Interval(2,4), Interval(5,10)]
Note that in the case of non-overlapping intervals, the output should be a list of constituent Intervals.
 Keep in mind that these are open intervals.
 Specifically,


# >>> Interval(2,3)+Interval(1,2)
 [Interval(2,3), Interval(1,2)]

Note that these do not produce a single interval because each interval is open (not closed).
 The interval endpoints can be negative also (e.
g.
, Interval(-10,-3) is valid).
 The output does not have to be sorted.


It's up to you to write the dunder functions for your object.
 If you do this right, you will have a very general solution to this problem.


This is where good object-oriented design pays off.


Note: Make sure to implement __eq__ method below, to pass all the test cases in the grader.


Starter Code:
     # fill out the necessary methods shown below and add others if need be.



Please put your Python code in a Python script file and upload it.
 Please retain your submitted source files! Remember to use all the best practices we discussed in class.
 You can use any module in the Python standard library, but third-party modules (e.
g.
, Numpy, Pandas) are restricted to those explicitly mentioned in the problem description.

"""


class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self):
        return f"Interval({self._a},{self._b})"

    def __eq__(self, other):
        return True if (self._a, self._b) == (other._a, other._b) else False

    def __lt__(self, other):
        return True if self._b <= other._a else False

    def __le__(self, other):
        # (4,7), (5,9)
        return True if self._a <= other._a and other._a < self._b <= other._b else False

    def __gt__(self, other):
        return True if self._a >= other._b else False

    def __ge__(self, other):
        # (5,9) , (4, 7)
        return True if self._a > other._a and self._a < other._b <= self._b else False

    def __contains__(self, other):
        return True if self._a <= other._a < other._b <= self._b else False

    def __add__(self, other):
        """
        overlapping intervals are combined, nonoverlapping intervals returned in list
        As a bonus, they will be in sorted order
        :param other:
        :type other:
        :return:
        :rtype:
        """
        a = self
        b = other

        if a < b:
            return [a, b]
        elif a <= b:
            return self.__class__(a._a, b._b)
        elif a in b:
            return b
        elif a == b:
            return a
        elif b in a:
            return a
        elif a >= b:
            return self.__class__(b._a, a._b)
        elif a > b:
            return [b, a]


if __name__ == '__main__':
    print(Interval(2,3))




