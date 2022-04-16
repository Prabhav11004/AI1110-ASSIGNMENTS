
import numpy as np
import matplotlib.pyplot as plt


def parab_gen(x, a,b,c):
    y = a*(x**2) + b*x + c
    return y


def line_dir_pt(m, A, k1, k2):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam_1 = np.linspace(k1, k2, len)
    for i in range(len):
        temp1 = A + lam_1[i]*m
        x_AB[:, i] = temp1.T
    return x_AB


O = np.array([0,0])


plt.title("Varification of root obtained")
plt.grid()


m =  np.array([1,0])
xO = line_dir_pt(m,O,-7,40)
plt.plot(xO[0,:],xO[1,:],label="X-axis")


x_parabola = np.linspace(-5,35,100)
y_parabola = parab_gen(x_parabola, 3,-84,-180)
plt.plot(x_parabola,y_parabola,label= "$y = 3x^2 -84x -180$")


coeff = [3,-84,-180]
roots = np.roots(coeff)
for loc in roots:
    point = np.array([loc,0])
    plt.plot(loc,0,marker = "o", c = "green")
    plt.annotate((loc,0),point,xytext=(0,10),ha='center',textcoords="offset points")


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(left=-7,right=35)
plt.legend(loc='best')



plt.show()
