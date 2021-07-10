from numba import jit
import random
import time
#import numba as nb

#@nb.jit
@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


def monte_carlo_pi2(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
    
n_samples=12000000          
start = time.time()

print(monte_carlo_pi(n_samples))
end = time.time()

difference=end-start
print('time taken using numba',difference)

    
start2 = time.time()

print(monte_carlo_pi2(n_samples))
end2 = time.time()

difference2=end2-start2
print('time taken without numba',difference2)
