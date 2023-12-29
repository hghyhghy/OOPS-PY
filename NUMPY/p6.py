
import numpy as np 

# creating an array 

a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

print("The newly created array is ")

print(a)

#printing the max element 

print(f"The maimum element from the array {a} is")

print(a.max())

print("Row wise maximum elements are ")

print(a.max(axis=1))

print("Column wise minimum elements are ")

print(a.min(axis=0))

# sum of all elements from that array

print(f"The sum of all elements from {a} is ")

print(a.sum)

# cumulative sum of all elements 

print(f"The ciumulative sum of all elements from {a} is ")

print(a.cumsum(axis=1))

# creating another array 

a1=np.array([[2,3,1],
             [4,5,2],
             [6,7,5]])

print("The elementary multiplication of two array ")

print(a*a1)

#matrix multiplication 

print("Maltrix multiplication of two elements are ")

print(a.dot(a1))