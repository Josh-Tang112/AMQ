The code I wrote depend on external packages bloom-filter2, pympler, and bbhash.
bloom-filter2 source: https://pypi.org/project/bloom-filter2/
pympler source: https://pypi.org/project/Pympler/
bbhash source: https://pypi.org/project/bbhash/

Run:
pip install bloom-filter2
pip install cython          # needed for bbhash
pip install bbhash
pip install pympler
to get the dependent packages. 
Then, run 
python3 bloom.py            # to execute bloom filter
python3 mphf.py             # to execute minimal perfect hash function
python3 mphf_fp.py          # to execute minimal perfect hash function with fingerprint

