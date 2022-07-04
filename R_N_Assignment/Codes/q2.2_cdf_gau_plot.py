#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy as scipy


#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(-4,4,50)#points on the x axis

simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list





plt.plot(x,err,'or')#plotting the empirical CDF

p1=np.ones(50)
def Q(x):
 return (0.5-0.5*mp.erf(x/mp.sqrt(2)))
 

vectorised_Q=scipy.vectorize(Q)

plt.plot(x,p1-vectorised_Q(x))#plotting the theorectical or analytical CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
plt.savefig('gau_cdf.png')
#plt.savefig('gau_cdf.eps')

#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot window