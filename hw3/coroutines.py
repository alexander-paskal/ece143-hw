"""
The code below defines a generator that returns the duration of its lifetime when called.

 from time import sleep
 import random
 from datetime import datetime
 import itertools as it

 def producer():
     'produce timestamps'
     starttime = datetime.now()
     while True:
         sleep(random.uniform(0,0.2))
         yield datetime.now()-starttime

For example,

# >>> p = producer()
# >>> next(p)
datetime.timedelta(0, 0, 106641)

Note that the output of producer has a seconds attribute. Write a generator that tracks the output of this producer and ultimately returns the number of odd numbered seconds that have been iterated over. The usage pattern is the following,
#
# >>> t = tracker(p,limit=2)
# >>> next(t)
1
# >>> list( tracker(p,limit=2))
[1,2]
The limit keyword argument is the number of odd-numbered seconds to track until completion.

# >>> list( tracker(p,limit=5))
[0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
The last line is interesting because is shows that the producer's seconds value output was an even number for the first six iterations. Your tracker generator should also receive input that changes the existing limit,

# >>> t = tracker(p,limit=3)
# >>> next(t)
0
# >>> next(t)
0
# >>> t.send(5)
1
# >>> list(t)
[1, 1, 1, 1, 2, 3, 4, 5]
Please put your Python code in a Python script file and upload it. Please retain your submitted source files! Remember to use all the best practices we discussed in class. You can use any module in the Python standard library, but third-party modules (e.g., Numpy, Pandas) are restricted to those explicitly mentioned in the problem description.
"""

from time import sleep
import random
import math
from datetime import datetime
import itertools as it
import types
import typing as tp


def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2))
        yield datetime.now() - starttime




def tracker(p: types.GeneratorType, limit: int = 3):
    """
    Tracks output of another generator, counts number of times the returned timedelta is an
    has been an odd number of seconds
    :param p:
    :type p:
    :param limit:
    :type limit:
    :return:
    :rtype:
    """
    assert isinstance(limit, int) and limit > 0
    assert isinstance(p,types.GeneratorType)
    i = 0
    while True:
        seconds = next(p).total_seconds()
        if math.floor(seconds) % 2 != 0:
            i += 1
        if i > limit:
            break
        yielded = yield i
        if yielded is not None:
            assert isinstance(yielded, int) and yielded > 0
            limit = yielded


if __name__ == '__main__':
    p = producer()
    t = tracker(p, limit=5)
    print(next(t))
    t.send(3)
    print(list(t))
    t = tracker(p, limit=3)
    next(t)
    t.send('a')
