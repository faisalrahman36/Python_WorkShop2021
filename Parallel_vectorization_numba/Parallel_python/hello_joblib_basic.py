from math import sqrt
from joblib import Parallel, delayed
import time
import numpy as np
import multiprocessing 
rangemax=10

num_cores = multiprocessing.cpu_count()

print('number of cores :',num_cores)

njobs=3

def square_root(n):
    sqrt=n**0.5
    
    return sqrt
        

start = time.time()
sqrtout=Parallel(n_jobs=njobs)(delayed(square_root)(i) for i in range(rangemax))
end = time.time()
difference=end-start

#print('square root using Parallel joblibs and our own square_root function',sqrtout)
print('time taken for square root using Parallel joblibs and our own square_root function',difference)
print('square root values : ',sqrtout)