"""
Write a function to return samples from the Multinomial distribution using pure Python (i.e., no third-party modules like Numpy, Scipy).
Here is some sample output.

# >>> multinomial_sample(10,[1/3,1/3,1/3],k=10)
 [[3, 3, 4],
  [4, 4, 2],
  [3, 4, 3],
  [5, 2, 3],
  [3, 3, 4],
  [3, 4, 3],
  [6, 2, 2],
  [2, 6, 2],
  [5, 4, 1],
  [4, 4, 2]]


Here is your function signature
def multinomial_sample(n,p,k=1):
         '''
         Return samples from a multinomial distribution.

         n:= number of trials
         p:= list of probabilities
         k:= number of desired samples
         '''


Please keep the default values as given in the function signature.
"""
import random


def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''

    assert isinstance(n, int)
    assert n > 0
    assert isinstance(k, int)
    assert k >= 0
    assert isinstance(p, list)
    assert sum(p) == 1


    samples = []
    for _ in range(k):  # samples
        sample = [0 for _ in range(len(p))]
        indices = list(range(len(p)))
        for _ in range(n): # trials
            index = random.choices(indices, p)[0]
            sample[index] += 1
        samples.append(sample)
    return samples


if __name__ == '__main__':
    stuff = multinomial_sample(10, [0,0,1], k=1)
    for thing in stuff:
        print(thing)