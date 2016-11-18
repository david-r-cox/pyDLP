# pyDLP
Python implementation of the index calculus method for solving discrete logarithms.

## About
[Index calculus](https://en.wikipedia.org/wiki/Index_calculus_algorithm) is a probabilistic method for solving [discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm) problems. As of this writing, there do not appear to be many implementations of index calculus. Hopefully this can serve as a useful reference.

## Setup
This script requires that [SageMath](https://www.sagemath.org/) be installed to solve the system of linear equations. The `primefac` module is also required and can be installed with `pip install -r ./requirements.txt`

## Usage

```
$ python2.7 ./pyDLP.py
p: 18443, g: 37, h: 211, B: 5
searching for congruences.
congruences: 6
bases: 3
converting to matrix format.
solving linear system with sage:
sage done.
checking congruences: Passed!

checking dlog exponents:
37^5733 = 2 (mod 18443)
37^15750 = 3 (mod 18443)
37^6277 = 5 (mod 18443)
Passed!

searching for k such that h*g^-k is B-smooth.
found k = 13999
Solving the main dlog problem:

37^8500 = 211 (mod 18443) holds!
DLP solution: 8500
```
