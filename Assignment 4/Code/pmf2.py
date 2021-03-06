def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

#Function for batch usage of line_gen
def batch_plot(A, B):
    len = A.shape[0]
    for i in range(len):
        x_AB = line_gen(A[i, :], B[i, :])
        plt.plot(x_AB[0, :], x_AB[1, :], 'k-')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#Arrays for PMF
X = np.array([0, 1, 2, 3])
Y = np.array([1/52, 1/13, 1/2, 0])
Z = np.cumsum(Y)

#Extra points
X_pmf = np.array([0, 3])
Y_pmf = np.array([0, 0])




#Plotting the PMF
plt.subplot(1, 2, 1)
plt.xlabel('Value of X')
plt.ylabel('Probability Mass Function')

stem(X, Y, linefmt='k--', markerfmt='ko', basefmt='k-')
stem(X_pmf, Y_pmf, linefmt='k--', markerfmt='ko', basefmt='k-')


plt.savefig('C:/Users/prabh/AI1110 ASSIGNMENTS/Assignment 4/Code/pmf2.png')