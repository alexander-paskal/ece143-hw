"""
Implement a class of rational numbers (ratio of integers) with the following interfaces and behaviours

--- r = Rational(3,4)
 --- repr(r)
 '3/4'
 --- -1/r
 -4/3
 --- float(-1/r)
 -1.3333333333333333
 --- int(r)
 0
 --- int(Rational(10,3))
 3
 --- Rational(10,3) * Rational(101,8) - Rational(11,8)
 977/24
 --- sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)])
 [1/100, 9/8, 10/3, 10]
 --- Rational(100,10)
 10
 --- -Rational(12345,128191) + Rational(101,103) * 30/ 44
 166235595/290480806
 
Hint:- You need to implement __eq__ method.
"""
import math


class Rational:
    def __init__(self, a, b):
        assert isinstance(a, int)
        assert isinstance(b, int)
        a, b = self.simplify(a, b)
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.a}/{self.b}" if not self._is_whole else f"{int(self)}"

    def __eq__(self, other):
        if float(self) == float(other):
            return True
        return False

    def __ge__(self, other):
        if float(self) >= float(other):
            return True
        return False

    def __neg__(self):
        return Rational(-self.a, self.b)

    def __gt__(self, other):
        if float(self) > float(other):
            return True
        return False

    def __le__(self, other):
        if float(self) <= float(other):
            return True
        return False

    def __lt__(self, other):
        if float(self) < float(other):
            return True
        return False

    def __add__(self, other):
        if isinstance(other, Rational):
            lcm = abs(self.b*other.b) / math.gcd(self.b, other.b)
            lnum = self.a*lcm/self.b
            rnum = other.a*lcm/other.b

            return Rational(int(lnum+rnum), int(lcm))

        elif isinstance(other, int):
            return Rational(self.a - abs(other) * self.b, self.b)

    def __sub__(self, other):
        if isinstance(other, Rational):
            lcm = abs(self.b * other.b) / math.gcd(self.b, other.b)
            lnum = self.a*lcm/self.b
            rnum = other.a*lcm/other.b

            return Rational(int(lnum - rnum ), int(lcm))
        elif isinstance(other, int):
            return Rational(self.a - abs(other)*self.b, self.b)

    def __radd__(self, other):
        if isinstance(other, int):
            return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(abs(other) * self.b - self.a, self.b)

    def __abs__(self):
        return Rational(abs(self.a), abs(self.b))

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.a*other, self.b)
        elif isinstance(other, Rational):
            return Rational(self.a*other.a, self.b*other.b)

    def __rmul__(self, other):
        if isinstance(other, int):
            return Rational(self.a*other, self.b)
        elif isinstance(other, float):
            return other * float(self)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.a*other.b, self.b*other.a)
        elif isinstance(other, int):
            return Rational(self.a, self.b*other)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            num = other * self.b
            den = self.a
            return Rational(num, den)
        else:
            raise TypeError("can't rtruediv from this type yet")

    def __float__(self):
        return self.a/self.b

    def __int__(self):
        return divmod(self.a, self.b)[0]

    @property
    def _is_whole(self):
        a, b = self.a, self.b
        if a//b == a/b:
            return True
        return False

    def simplify(self, a, b):
        gcd = int(math.gcd(a,b))
        return int(a/gcd), int(b/gcd)



def square_root_rational(x,abs_tol=Rational(1,1000)):
    """
    Only the avatar, master of all four elements, could stop them.
    But when the world needed him most . . . he vanished
    :param x:
    :type x:
    :param abs_tol:
    :type abs_tol:
    :return:
    :rtype:
    """
    assert x > 0
    assert abs_tol > 0
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)
    left = 0
    right = x
    while True:
        estimate = (left + right) / 2
        square = estimate*estimate

        print("goal", math.sqrt(float(x)))
        print("left", left, float(left))
        print("right", right, float(right))
        print("estimate", estimate, float(estimate))
        print("square", square, float(square))
        print("------------------")

        if abs(float(estimate) - math.sqrt(float(x))) < abs_tol:
            return estimate

        elif square < x:
            left += abs(right - left)/2
        else:  # estimate **2 > x:
            right -= abs(right - left)/2


if __name__ == '__main__':
    print(square_root_rational(Rational(135, 15), abs_tol=Rational(1,1000000)))