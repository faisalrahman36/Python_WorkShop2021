import numpy as np
import statsmodels.api as sm

#import statsmodels.formula.api as smf   #version dependent
#import statsmodels.api as smf

#Multiple Ordinary least square regression using statsmodels
#This will also give f-stats , r^2,AIC,BIC etc.

data=np.genfromtxt('E:\Python_Programming_Course\Python2021\SciPy_Curve_fit_StatsModel_Sci-kit_multiple_Reg\hba1c_fake.csv',delimiter=',',skip_header=1)
y=data[:,0]
x1=data[:,1]
x2=data[:,2]
x3=data[:,3]
x4=data[:,4]
x5=data[:,5]
x6=data[:,6]
x7=data[:,7]
print(y)
print(x1)

x=np.column_stack((x1,x2,x3,x4,x5,x6,x7))
#x = sm.add_constant(x, prepend=True)
x = sm.add_constant(x, prepend=False)

results = sm.OLS(y,x).fit()

print(results.summary())