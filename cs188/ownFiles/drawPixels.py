import numpy as np
import scipy.misc as smp

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (28,28,3), dtype=np.uint8 )

data[26,0] = [254,0,0]       # Makes the middle pixel red
data[26,1] = [254,0,0]    
data[27,0] = [254,0,0]    
data[27,1] = [254,0,0]    


# data[512,513] = [0,0,255]       # Makes the next pixel blue

img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer