

import numpy as np 

# creating an array 

a=np.array([0, np.pi/2, np.pi])

print(f"The sine values of the array {a} is ")

print(np.sin(a))

a1=np.array([0,1,2,3])

print(f"The exponential of the array elements of {a1} is ")

print(np.exp(a1))

# multiplication of two lists using numpy 

l=[2,3,4]

l1=[20,3,4]

# converting the two lists into numpy array 

q=np.array(l)

q1=np.array(l1)

print("Multplication of two array ")

print(q*q1)

# indexing of the array 

q2=np.arange(10,1,-2)

print("The new array is ")

print(q2)

# indexing 

new_ar=q2[np.array([3,1,2])]

print("The indexed elements are ", new_ar)

# another  example of array indexing 

s=np.array([1,2,4,8,6,9,20])

arr=s[np.array([1,3,-3])]

print("Indexed elements are ", arr)

s1=np.arange(20)

print(s1)

# indexing element from 10 

print(s1[10:])