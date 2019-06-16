import numpy as np

x = np.array([1.0,0.0])
xnew = x.copy()
for i in range(100):
    xnew[0]= 0.75*x[0]+0.55*x[1]
    xnew[1]= 0.25*x[0]+0.45*x[1]
    x[0] = xnew[0]
    x[1] = xnew[1]

print(xnew)
print (11.0/16.0)