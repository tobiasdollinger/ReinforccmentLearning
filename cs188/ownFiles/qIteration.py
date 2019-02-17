'''
Exact Q-Iteration with two transitions
'''
import numpy as np
# gamma = 0.5
# 
# T0 = 1.0
# R0 = 10.0
# Q0 = 3.32
# T1 = 0.0
# R1 = 2.0
# Q1 = 3.32
# 
# print T0*(R0+gamma*Q0)+T1*(R1+gamma*Q1)

'''
Running average Q-iteration
'''

# Q0 = np.array([[3.238, 0.352, 1.345],
#       [4.131, 5.125, 1.525]])
# Q1 = np.empty_like(Q0)
# for i in range(Q0.shape[0]):
#     for j in range(Q0.shape[1]):
#         Q1[i][j] = (1-alpha)*Q0[i][j]+ alpha*()
alpha = 0.5
gamma = 0.5
r = 0.0
maxQ = 4.875
Q0 = -5.439
Q1 = (1.0-alpha)*Q0+ alpha*(r+ gamma*maxQ)

print Q1

