from math import sqrt
from joblib import Parallel, delayed
import time
import numpy as np

rangemax=100000
njobs=3
start1 = time.time()
sqrtout=Parallel(n_jobs=njobs)(delayed(sqrt)(i) for i in range(rangemax))
end1 = time.time()
difference1=end1-start1
print('time taken for square root using Parallel joblibs and math.sqrt',difference1)

start1 = time.time()
sqrtout=Parallel(n_jobs=1)(delayed(sqrt)(i) for i in range(rangemax))
end1 = time.time()
difference1=end1-start1


#print('square root using Parallel joblibs and math.sqrt',sqrtout)
print('time taken for square root using Parallel joblibs and math.sqrt',difference1)
def square_root(n):
    sqrt=n**0.5
    
        
    return sqrt
        

start2 = time.time()
sqrtout=Parallel(n_jobs=njobs)(delayed(square_root)(i) for i in range(rangemax))
end2 = time.time()
difference2=end2-start2

#print('square root using Parallel joblibs and our own square_root function',sqrtout)
print('time taken for square root using Parallel joblibs and our own square_root function',difference2)

sqrtout=np.linspace(0,1,num=rangemax)

start3 = time.time()
for x in range(0,rangemax):
    sqrtout[x]=x**0.5
    
end3 = time.time()
difference3=end3-start3

#print('square root using normal foor loop and our own square_root function',sqrtout)
print('time taken for square root using normal for loop and our own square_root function',difference3)
    
