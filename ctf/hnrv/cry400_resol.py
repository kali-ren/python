#!/usr/bin/python

import gmpy2
gmpy2.get_context().precision = 4096

from binascii import unhexlify
from functools import reduce
from gmpy2 import root

# https://id0-rsa.pub/problem/11/

# Resources
# https://en.wikipedia.org/wiki/Coppersmith%27s_Attack
# https://github.com/sigh/Python-Math/blob/master/ntheory.py

EXPONENT = 3

CIPHERTEXT_1 = "c1.txt"
CIPHERTEXT_2 = "c2.txt"
CIPHERTEXT_3 = "c3.txt"

MODULUS_1 = "n1.txt"
MODULUS_2 = "n2.txt"
MODULUS_3 = "n3.txt"


def chinese_remainder_theorem(items):
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n

    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        r, s, d = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m

    # Make sure we return the canonical solution.
    return result % N


def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return (lastx, lasty, a)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_value(filename):
    with open(filename) as f:
        value = f.readline()
    return int(value, 16)

if __name__ == '__main__':

    C1 = get_value(CIPHERTEXT_1)
    C2 = get_value(CIPHERTEXT_2)
    C3 = get_value(CIPHERTEXT_3)
    ciphertexts = [C1, C2, C3]
 	
    N1 = get_value(MODULUS_1)
    N2 = get_value(MODULUS_2)
    N3 = get_value(MODULUS_3)
    modulus = [N1, N2, N3]

    C = chinese_remainder_theorem([(C1, N1), (C2, N2), (C3, N3)])
    M = int(root(C, 3))
    M = hex(M)[2:]
    print M
    M=M[:len(M)-1]
    print unhexlify(M).decode('utf-8')
#    print unhexlify('54686973206d6573736167652069732073656372657420616e6420756e666f7274756e6174656c792065206973206e6f7420686967682e20546865206d6573736167652073686f756c6420616c736f2062652073756666696369656e746c79206c6f6e6720736f206974206973206120726573696475652e').decode('utf-8')


