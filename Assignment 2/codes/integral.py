

from cmath import pi
import numpy as np
from scipy import integrate

 

def integ(x):
    return x*np.tan(x)/(1/np.cos(x)+np.tan(x))

I = integrate.quad(integ, 0, pi)

print("Integral value computed by python is",I[0])
print("Integral value manually calculated was",pi*(pi-2)/2)
