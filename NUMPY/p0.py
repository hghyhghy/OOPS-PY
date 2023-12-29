
# creating numpy array 

import numpy as np 

a=np.arange(1,20,2) 

# where 1 is the start 20 is the end and 2 is the gap between them 

# printing the  value of a 

print("The created  array is ", a)

print("The type of this array is",type(a))

# making it to float 

f=np.arange(1,20,2, dtype=float)

# printing the float values

print(f)

# creating 2D array with numpy
myl=[[1,2,3],[3,4,5],[5,6,7]]

print("The newly crated list is ", myl)

print("The 2D version of the list is ")

a1=np.array(myl)

print(a1)

# creating an empty 2D array with 0 values and 3 roes and 2 colms

a2=np.empty([3,2])

print("The empty array is ")

print(a2)