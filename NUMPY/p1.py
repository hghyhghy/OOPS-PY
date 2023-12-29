
# creating array using eye

import numpy as np

a=np.eye(3,3) # delivering the shape of the array 

print("The created array is ")

print(a)

# creating array using identity

a1=np.identity(3)

# creating (3x3) identity matrix

print("The newly created identity matrix is ")

print(a1)

# creating array using linespace

a2=np.linspace(0,20,11) # by default it is float type 

a3=np.linspace(0,20,11, dtype=int)

print("The float type array is ", a2)

print("The int type array is ", a3)

# creating array using logspace 

a4=np.logspace(0,4,5,dtype=int)

print("The created  array is ",a4 )

# creating array using ones 

b=np.ones((2,3),dtype=int)

print(b)

# creating array using zeroes 

b0=np.zeros((2,3),dtype=int)

print(b0)

