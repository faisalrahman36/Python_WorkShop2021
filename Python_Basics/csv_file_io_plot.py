# CSV File I/O

import numpy as np
import pylab as pl


def power(x,n):
   
        y=np.linspace(0.,1.,num=len(x))
        for i in range(0,len(x)):
            y[i]=x[i]**n
            
        return y
            
a=np.linspace(-1,1,num=100)
#a=np.arange(0,11)
b=power(a,3)

datain=np.empty((len(a),2))
datain[:,0]=a
datain[:,1]=b

#print type(datain)
#print datain[0][0]
#print datain[:,1]
#File write
np.savetxt('C:\Lab_10\example.csv',datain,delimiter=',')

#File read
data=np.genfromtxt('C:\Lab_10\example.csv',delimiter=',')

#print data
#print data[:,0]
#print data[0][0]

x=data[:,0]
y=data[:,1]


#pl.plot(x,y,'r.')
pl.plot(x,y)
#pl.yscale('log')
pl.show()