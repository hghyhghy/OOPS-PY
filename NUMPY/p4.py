
# datatypes in numpy 

import  numpy as n 

# creating an array

a=n.array([[1,2],
           [3,4]])

print("The newly created array is ")

print(a)

print(f"The datatype  of the  elements {a} is  ")

print(a.dtype)

a1=n.array([[1.0,2.0],
            
            [2.0,3.0]])

print(f"The daatype of the elements {a1} is ")

print(a1.dtype)

# creating two arrays 

ar=n.array([[1,2],
            [3,4]], dtype=n.float32)

ar1=n.array([[7,8],
             [9,10]], dtype=n.float32)

# adding of two array elements 


add=n.add(ar,ar1)

print("The result of add of two elements are ")

print(add)

# printing the sum of all elements from ar1 

print(f"The sum of all  elements from {ar} is ")

s=n.sum(ar)

print(s)

# the square root of all elements from first array is 

print(f"The squareroot  of all  elements from {ar} is ")

s1=n.sqrt(ar)

print(s1)

# transposing of the array 

trans=ar.T

print("The transposed version of the array is ")

print(trans)

