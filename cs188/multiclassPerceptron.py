import numpy as np

A = np.array([[1.44, 0.4],[-0.68, -1.09], [0.72, -1.95]])
x = np.array([-0.8, 1.07])
for i in range(3):
    print (A[i][0]*x[0] + A[i][1]*x[1])
    
print ('\n')
    
    
B = np.array([[1.44, 0.4],[0.12,-2.16],[-0.08,-0.88]])
x = np.array([-0.25, 0.86])
for i in range(3):
    print (B[i][0]*x[0] + B[i][1]*x[1])
print ('\n')

C = np.array([[6.99, 0.56],[6.9,-3.24],[-12.41, 0.04]])
x = np.array([-1.97, -0.7])
for i in range(3):
    print (C[i][0]*x[0] + C[i][1]*x[1])
print ('\n')