import numpy as np
import matplotlib.pyplot as plt
l=np.arange(0,101)

#print(np.sum(l))

n=[1,2,3,4,5,6,7,8,9,10]
#n=np.arange(1,11)
#print(n)

def square(n):
     sq=n**2
     return sq
  
sqv=np.vectorize(square)

#print(sqv(4))
#print(sqv(l))

#plt.plot(n,square(n))
plt.plot(n,sqv(n))

plt.show()