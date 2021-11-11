import unittest as ut
from hw5.interval_objects import Interval

# a = Interval(1,3)
#  >>> b = Interval(2,4)
#  >>> c = Interval(5,10)


class IntervalTests(ut.TestCase):
    def test_1(self):
        a = Interval(1,3)
        b = Interval(2,4)
        assert a + b == Interval(1,4)
        assert b + a == Interval(1,4)

    def test_2(self):
        a = Interval(1,3)
        b = Interval(4, 6)
        assert a + b == [Interval(1,3), Interval(4,6)]

    def test_3(self):
        a = Interval(1,9)
        b = Interval(4, 6)
        assert a + b == Interval(1, 9)

    def test_4(self):
        assert Interval(2, 3) + Interval(1, 2) == [Interval(1, 2), Interval(2, 3)]

    def test_5(self):
        print(Interval(2,3))

if __name__ == '__main__':
    ut.main()