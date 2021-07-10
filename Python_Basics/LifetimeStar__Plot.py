#Lab 6: Task 2: Plot lifetime of a star using Mass in solar masses
import numpy as np
import matplotlib.pyplot as plt

def lifetime(M):
    '''
    Input:
        M: Mass of star in solar masses
    Output:
        lt: Lifetime of stars in years
    '''
    p=0.
    
    if(M>=30):
        p=3.
    elif(M<=10):
        p=4.
    else:
        p=3.5
    
    lt=(1./(M**(p-1)))*(10**10)
    return lt
    

#M=np.arange(0,101)
M=np.linspace(0,101,num=1000)
lifet=np.linspace(0,1,num=len(M))

for x in range(0,len(M)):
    lifet[x]=lifetime(M[x])
    print(M[x],lifet[x])
    
plt.plot(M,lifet,'bo')
plt.xlabel('Mass of stars in solar masses')
plt.ylabel('life time of stars in years')
plt.yscale('log')
plt.xscale('log')
plt.title('life time of stars')
plt.show()


    
    