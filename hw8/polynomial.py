"""
Create a Python class that can implement a univariate polynomial (Polynomial) over the field of integers (only!) 
with the following operations and interfaces.

->>> p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
->>> q=Polynomial({0:8,1:2,2:8,4:4})
->>> repr(p)
 8 + 2 x + 4 x^(3)
->>> p*3 # integer multiply
 24 + 6 x + 12 x^(3)
->>> 3*p # multiplication is commutative!
 24 + 6 x + 12 x^(3)
->>> p+q # add two polynomials
16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)
->>> p*4 + 5 - 3*p - 1 # compose operations and add/subtract constants
 12 + 2 x + 4 x^(3)
->>> type(p-p) # zero requires special handling but is still a Polynomial
 Polynomial
->>> p*q # polynomial by polynomial multiplication works as usual
 64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)
->>> p.subs(10) # substitute in integers and evaluate
 4028
->>> (p-p) == 0
 True
->>> p == q
 False
->>> p=Polynomial({0:8,1:0,3:4}) # keys are powers, values are coefficients
->>> repr(p)
'8 + 4 x^(3)'
->>> p = Polynomial({2:1,0:-1})
->>> q = Polynomial({1:1,0:-1})
->>> p/q
 1 + x
->>> p  / Polynomial({1:1,0:-3}) # raises NotImplementedError
"""
from collections import defaultdict
import math
import functools


class Polynomial:
    def __init__(self, coeffs):
        for k, v in coeffs.items():
            try:
                assert isinstance(k, int)
                # assert k >= 0
                assert isinstance(v, int)
            except AssertionError:
                # raise NotImplementedError("decimal numbers not supported.")
                raise AssertionError("decimal numbers not supported.")
        self._coeffs = coeffs
        # self.simplify()

    def __repr__(self):
        symbols = []
        highest = self.degree

        for i, tup in enumerate(self._cordered):
            k, v = tup

            if v == 0:
                continue
            elif k == 0:
                symbols.append(str(v))
            elif k == 1:
                symbols.append(f"{abs(v)}x")

            else:
                symbols.append(f"{abs(v)}x^({k})")

            if k < highest:
                if self._cordered[i+1][1] > 0:
                    symbols.append("+")
                else:
                    symbols.append("-")

        return " ".join(symbols)

    @property
    def _cordered(self):
        """
        ordered form of coefficients
        :return:
        """
        if len(self._coeffs) > 0:
            coeffs = {k: v for k, v in self._coeffs.items() if v != 0}
            return sorted(coeffs.items())
        return []

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            new_coeffs = defaultdict(int)
            for k1, v1 in self._coeffs.items():
                for k2, v2 in other._coeffs.items():
                    k = k2+k1
                    v = v1*v2
                    new_coeffs[k] += v

            return Polynomial(new_coeffs)

        elif isinstance(other, int):
            new_coeffs = dict()
            for k, v in self._coeffs.items():
                new_coeffs[k] = v * other
            return Polynomial(new_coeffs)
        else:
            raise NotImplementedError("Can't handle this type yet")

    def __rmul__(self, other):
        if isinstance(other, (int, Polynomial)):
            return self.__mul__(other)
        else:
            raise NotImplementedError("Can't handle this type yet")
        
    def __add__(self, other):
        if isinstance(other, Polynomial):

            new_coeffs = dict()

            keys = set(self._coeffs).union(set(other._coeffs))
            for k in keys:
                v1 = self._coeffs.get(k)
                v2 = other._coeffs.get(k)

                v1 = 0 if v1 is None else v1
                v2 = 0 if v2 is None else v2

                if v1 + v2 != 0:
                    new_coeffs[k] = v1 + v2

            return Polynomial(new_coeffs)

        elif isinstance(other, int):
            new_coeffs = self._coeffs
            if 0 in self._coeffs:
                new_coeffs[0] = self._coeffs[0] + other
            else:
                new_coeffs[0] = other
            return Polynomial(new_coeffs)

        else:
            raise NotImplementedError("Can't handle this type yet")
    
    def __radd__(self, other):
        if isinstance(other, (Polynomial, int)):
            return self.__add__(other)
        else:
            raise NotImplementedError("Can't handle this type yet")
    
    def __sub__(self, other):
        if isinstance(other, (int, Polynomial)):
            return self + -1*other
        else:
            raise NotImplementedError("Can't handle this type yet")
    
    def __rsub__(self, other):
        if isinstance(other, (int, Polynomial)):
            return -1*self + other
        else:
            raise NotImplementedError("Can't handle this type yet")
        
    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            return self._long_div(self, other)

        elif isinstance(other, int):
            new_coeffs = {}
            for k, v in self._coeffs.items():
                new_coeffs[k] = v / other

            return Polynomial(new_coeffs)
        else:
            raise NotImplementedError("Can't handle this type yet")
    
    def __rtruediv__(self, other):
        if isinstance(other, Polynomial):
            return self._long_div(other, self)
            
        elif isinstance(other, (int, float)):
            raise NotImplementedError("Can't handle rational polynomials yet")
        else:
            raise NotImplementedError("Can't handle this type yet")

    @staticmethod
    def _long_div(p1, p2):

        # stop condition
        # p2.degree > p1
        #   raise NotImplementedError

        answer = Polynomial({})
        minuend = p1

        while True:
            if minuend == 0:
                return answer
            elif minuend.degree < p2.degree:
                raise NotImplementedError("Rational and floating point polynomials not supported")

            else:
                multiplier_degree = minuend.degree - p2.degree
                multiplier_coeff = minuend.leading[1] / p2.leading[1]
                if int(multiplier_coeff) != multiplier_coeff:
                    raise NotImplementedError("Cannot handle decimal coefficients")

                multiplier = Polynomial({multiplier_degree: int(multiplier_coeff)})
                subtrahend = p2*multiplier
                minuend -= subtrahend
                answer += multiplier


    @property
    def degree(self):
        return self.leading[0]

    @property
    def leading(self):
        if len(self._cordered) > 0:
            return self._cordered[-1]
        return (0, 0)


    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self._cordered == other._cordered:
                return True
            return False
        elif isinstance(other, int):
            if other != 0:
                if len(self._cordered) == 1 and self._cordered[0][0] == 0:
                    return True
            elif other == 0:
                if len(self._cordered) == 0:
                    return True
            return False
        else:
            raise NotImplementedError("Can't handle this type yet")

    def subs(self, x):
        value = 0
        for k, v in self._coeffs.items():
            value += v*x**k

        return value

    def simplify(self):
        non_zero_values = set(self._coeffs.values())
        if 0 in non_zero_values:
            non_zero_values.remove(0)

        non_zero_values = map(lambda x: int(x), non_zero_values)

        gcd = functools.reduce(math.gcd, non_zero_values)
        self._coeffs = {k // gcd: v for k, v in self._coeffs.items()}


if __name__ == '__main__':
    p = Polynomial({0: 8, 1: 2, 3: 4})  # keys are powers, values are coefficients
    q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})

    print("Exact repr output not important, the values are the point of the exercise\n")

    print("Expected | Actual ")
    print("---------------------------")
    print(repr(p), "| 8 + 2x + 4x^(3)")
    print(p * 3, "| 24 + 6x + 12x^(3)")
    print(3 * p, "| 24 + 6x + 12x^(3)") # multiplication is commutative!
    print(p + q, "| 16 + 4x + 8x^(2) + 4x ^ (3) + 4x ^ (4)")  # add two polynomials
    print(p * 4 + 5 - 3 * p - 1, "| 12 + 2x + 4x ^ (3)")  # compose operations and add/subtract constants
    print(type(p - p), "| Polynomial")  # zero requires special handling but is still a Polynomial
    print(p * q, "| 64 + 32x + 68x ^ (2) + 48x ^ (3) + 40x ^ (4) + 40x ^ (5) + 16x ^ (7)")  # polynomial by polynomial multiplication works as usual
    print(p.subs(10), "| 4028")  # substitute in integers and evaluate
    print((p - p) == 0, "| True")
    print(p == q, "| False")
    p = Polynomial({0: 8, 1: 0, 3: 4})  # keys are powers, values are coefficients
    print(repr(p), '| 8 + 4 x^(3)')

    # Division

    print(Polynomial({2: 1, 0: -1}) / Polynomial({1: 1, 0: -1}), "| 1 + x")
    print(Polynomial({2:1, 0:-4}) / Polynomial({1:1, 0:-2}), "| 2 + x")
    print(Polynomial({2:1, 0:-9})/ Polynomial({1:1, 0:3}))

    # long division tests, cause this part was tricky
    a = Polynomial({0:1, 1:4, 2:1})
    b = Polynomial({1:2})
    c = Polynomial({0:5, 2:3})

    product = a*b*c

    assert product/c == a*b
    assert product/b == a*c
    assert product/a == b*c
    assert product/(a*b) == c
    assert product/(b*c) == a

    try:
        print(p / Polynomial({1: 1, 0: -3}))  # raises NotImplementedError"""
        raise AssertionError("failed to raise proper error")
    except NotImplementedError:
        pass

    print("\nLong division tests passed")
