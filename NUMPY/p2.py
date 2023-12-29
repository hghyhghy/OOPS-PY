

import numpy as np 

a=np.arange(1,21,2)

print("The newly created array is")

print(a)

#  reshaping the array 

RA=a.reshape(5,2)

print("After reshaping the array becomes")

print(RA)

print("The array with rank 1 is ")

a1=np.array([1,2,3])

print(a1)

print("The array with rank 2 is ")

a2=np.array([[1,2,3],
            [2,3,4]])

print(a2)

# creating array from tuple 

a3=np.array((1,2,3))

print("The created from tuple is ")

print(a3)