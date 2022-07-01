import numpy as np

num_trail = 10
r=5
N = 1000000
p=0.5

dis = np.random.randint(0,2,size = (N,num_trail))

val = np.count_nonzero(dis == 1,axis =1)

num = np.count_nonzero(val == r)
prob = num/N

prob_rel = prob/p
print(prob_rel)

