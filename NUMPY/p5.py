
import numpy as np 

# creating an array 

a=np.array([[1,2,3],
            
            [4,5,6]])

print("The newly created array is ")

print(a)

print("The type of the array  is ")

print(type(a))

# printing the dimesions of the array

print(f"The dimension of the array {a} ")

print(a.ndim)

# printing the shape of the array 

print(f"The shape of the array {a } is ")

print(a.shape)

# printing the shape of the array 

print(f"The size of the array {a } is ")

print(a.size)

print(f"The shape of the array {a } is ")

print(a.dtype)

# multiplying eac element of the array by 10

print(f"Mutiplying each vaue of {a} by 10 it becomes ")

print(a*10)

# squaring each element without using square

print(f"The square version of all elements of {a} is ")

print(a**2)