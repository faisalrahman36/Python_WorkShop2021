#Lab 5: Task 2: Basic Plot
import matplotlib.pyplot as plt
import numpy as np
def square(x):
    #y=x**2
    #return y
    return x**2
    
v=[1,2,3,4,5,6,7.5]
sq=np.linspace(0,1,num=len(v))
#sq=np.arange(0,len(v))
#sq=np.arange(0,len(v))*1.
for i in range(0,len(v)):
    sq[i]=square(v[i])
    
print(v)
print(sq)

plt.plot(v,sq,'r+')
plt.xlabel('values')
plt.ylabel('squares of values')
plt.title('plot of square of values')
plt.show()


