from bloom_filter2 import BloomFilter # https://pypi.org/project/bloom-filter2/
import math
import numpy as np
from pympler import asizeof # https://pypi.org/project/Pympler/
import time

def get_bloom(size):
    b_7 = BloomFilter(max_elements=size, error_rate=0.5**7)
    b_8 = BloomFilter(max_elements=size, error_rate=0.5**8)
    b_10 = BloomFilter(max_elements=size, error_rate=0.5**10)
    return b_7, b_8, b_10

def get_k_helper(alpha, strlen, k_length):
    if strlen == 1:
        return alpha
    else:
        val = get_k_helper(alpha,strlen-1,k_length)
        ret = []
        c = 0
        for i in val:
            for j in alpha:
                ret.append(i + j)
                c+=1
                if c == k_length:
                    return ret
        return ret

def get_k(alpha,k_length):
    strlen = math.ceil(math.log(k_length,(len(alpha)))) # len(alpha) ** strlen gives number of length strlen combinations of char in aplha
    return get_k_helper(alpha,strlen, k_length)

def test_bloom(bsize,k,kp):
    b_7, b_8, b_10 = get_bloom(bsize)
    size_str = "bloom filter with {} bits and error rate 0.5^{} has size {} bytes."
    print(size_str.format(bsize,7,asizeof.asizeof(b_7)))
    print(size_str.format(bsize,8,asizeof.asizeof(b_8)))
    print(size_str.format(bsize,10,asizeof.asizeof(b_10)))
    for i in k:
        b_7.add(i) 
        b_8.add(i) 
        b_10.add(i)
    c_7 = c_8 = c_10 = 0
    for i in k:
        if i in b_7:
            c_7 += 1
        if i in b_8:
            c_8 += 1
        if i in b_10:
            c_10 += 1
    assert(c_7 == len(k))
    assert(c_8 == len(k))
    assert(c_10 == len(k))
    c_7 = c_8 = c_10 = 0
    time_7 = time_8 = time_10 = 0
    for i in kp:
        a = time.time()
        if i in b_7:
            c_7 += 1
        b = time.time()
        time_7 += b - a

        a = time.time()
        if i in b_8:
            c_8 += 1
        b = time.time()
        time_8 += b - a

        a = time.time()
        if i in b_10:
            c_10 += 1
        b = time.time()
        time_10 += b - a
    res_str = "bloom filter with 0.5^{} error rate has false positive rate of {} and takes {} sec to query."
    print(res_str.format(7,(c_7 - len(k))/len(kp), time_7))
    print(res_str.format(8,(c_8 - len(k))/len(kp), time_8))
    print(res_str.format(10,(c_10 - len(k))/len(kp), time_10))

alphabet = ['a','b','c','d','e']

k_1 = ["aaa"]
k_1p = ["aaa","aab","aac","aad"]
k_30 = get_k(alphabet,30)
k_30p = get_k(alphabet,50)
assert(len(k_30[0]) == len(k_30p[0]))
k_300 = get_k(alphabet,300)
k_300p = get_k(alphabet,500)
assert(len(k_300[0]) == len(k_300p[0]))
k_1000 = get_k(alphabet,1000)
k_1000p = get_k(alphabet,2000)
assert(len(k_1000[0]) == len(k_1000p[0]))

test_bloom(10,k_1,k_1p)
test_bloom(100,k_30,k_30p)
test_bloom(1000,k_300,k_300p)
test_bloom(1000,k_1000,k_1000p)
test_bloom(2000,k_1000,k_1000p)