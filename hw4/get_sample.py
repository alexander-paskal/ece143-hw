"""
Given a number of bits, write the get_sample function to return a list n of random samples from a finite probability mass function
defined by a dictionary with keys defined by a specified number of bits.
For example, given 3 bits, we have the following dictionary that defines the probability of each of the keys.
The values of the dictionary correspond of the probability of drawing any one of these.
For example, if all of these were equally likely, then here is the corresponding dictionary p,

 p={'000': 0.125, 
 '001': 0.125, 
 '010': 0.125, 
 '011': 0.125, 
 '100': 0.125, 
 '101': 0.125, 
 '110': 0.125, 
 '111': 0.125} 
 
Your get_sample function should return something like the following,

get_sample(nbits=3,prob=p,n=4)
['101', '000', '001', '100'] 
Hint: Validate your inputs thoroughly.

Function signature: get_sample(nbits=3,prob=None,n=1). Keep the default values as given in the function signature.
"""
import random
import typing as tp


def get_sample(nbits=3,prob=None,n=1) -> tp.List[str]:
    """
    Gets a sample bit based on a number of bits. Can optionally provide a probability density, and
    can provide a variable length of outputs
    :param nbits: 
    :type nbits: 
    :param prob: 
    :type prob: 
    :param n: 
    :type n: 
    :return: 
    :rtype: 
    """
    assert isinstance(nbits, int) and nbits >= 1
    assert isinstance(n, int) and n >= 1
    if prob is not None:
        assert isinstance(prob, dict)
        for k, v in prob.items():
            assert isinstance(k, str)
            assert len(k) == nbits

            assert set(k).issubset({"1", "0"})
            assert isinstance(v, (float, int)) and 0 <= v <= 1
        assert sum(list(prob.values())) == 1
    else:
        prob = {(nbits-len(bin(i)[2:])) * "0" + bin(i)[2:]: 1/2**nbits for i in range(2**nbits)}


    population, density = [], []
    for k, v in prob.items():
        population.append(k)
        density.append(v)

    outputs = [random.choices(population, density)[0] for i in range(n)]
    return outputs


if __name__ == '__main__':
    print(get_sample(3))
    print(get_sample(nbits=2, prob={"10": 0.99, "11": 0.01}, n=2))
