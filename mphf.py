import math
import numpy as np
from pympler import asizeof # https://pypi.org/project/Pympler/
import time
import bbhash # https://pypi.org/project/bbhash/
from bbhash_table import BBHashTable

def get_mphf(keys):
    mphf = BBHashTable()
    mphf.initialize(keys)
    for k in keys:
        mphf[k] = 1
    return mphf

def test_mphf(k,kp):
    mphf = get_mphf(k)
    size_str = "Minimal Perfect Hash Function with {} keys has size {} bytes."
    print(size_str.format(len(k),asizeof.asizeof(mphf)))

    c = 0
    for i in k:
        c += mphf[i]
    assert(c == len(k))

    c = 0
    a = time.time()
    for i in kp:
        c += 0 if mphf[i] is None else 1
    b = time.time()

    res_str = "Minimal Perfect Hash Function takes {} sec to query {} entries and has false positive rate of {}."
    print(res_str.format(b-a,len(kp),(c - len(k))/len(kp)))

k_1 = [1]
k_1p = [1,2,3,4,5]
k_30p = np.random.randint(100, size=(50)).tolist()
k_30 = k_30p[:30]
k_300p = np.random.randint(1000, size=(500)).tolist()
k_300 = k_300p[:300]
k_1000p = np.random.randint(5000, size=(2000)).tolist()
k_1000 = k_1000p[:1000]

test_mphf(k_1,k_1p)
test_mphf(k_30,k_30p)
test_mphf(k_300,k_300p)
test_mphf(k_1000,k_1000p)