import math
import numpy as np
from pympler import asizeof 
import time
import bbhash 
from bbhash_table import BBHashTable

def get_mphf_fp(keys,b):
    mphf = bbhash.PyMPHF(keys, len(keys), 1, 1.0)
    fp = [0 for i in range(len(keys))]
    for val in keys:
        fp[mphf.lookup(val)] = abs(hash(str(val))) % 2**b # last b bits of h(k)
    return mphf, fp

def exist(k,mphf,fp,b):
    if mphf.lookup(k) is not None and abs(hash(str(k))) % 2**b == fp[mphf.lookup(k)]:
        return True
    else:
        return False

def test_mphf_fp(k,kp,b):
    mphf,fp = get_mphf_fp(k,b)
    size_str = "Minimal Perfect Hash Function with fingerprint array and {} keys has size {} bytes."
    print(size_str.format(len(k),asizeof.asizeof(mphf) + (len(fp)*(b+1))/8))

    c = 0
    for i in k:
        c += 1 if exist(i,mphf,fp,b) else 0
    assert(c == len(k))

    c = 0
    a = time.time()
    for i in kp:
        c += 1 if exist(i,mphf,fp,b) else 0
    b = time.time()

    res_str = "Minimal Perfect Hash Function with fingerprint array takes {} sec to query {} entries and has false positive rate of {}."
    print(res_str.format(b-a,len(kp),(c - len(k))/len(kp)))

def test_3_mphf(k,kp):
    test_mphf_fp(k,kp,7)
    test_mphf_fp(k,kp,8)
    test_mphf_fp(k,kp,10)

k_1 = [1]
k_1p = [1,2,3,4,5]
k_30p = np.random.randint(100, size=(50)).tolist()
k_30 = k_30p[:30]
k_300p = np.random.randint(1000, size=(500)).tolist()
k_300 = k_300p[:300]
k_1000p = np.random.randint(5000, size=(2000)).tolist()
k_1000 = k_1000p[:1000]
test_3_mphf(k_1,k_1p)
test_3_mphf(k_30,k_30p)
test_3_mphf(k_300,k_300p)
test_3_mphf(k_1000,k_1000p)