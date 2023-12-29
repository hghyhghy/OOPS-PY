
import numpy as n 


# creating an array 

a=n.array([[1,2,4,5],
           
           [5,6,7,8],
           
           [7,8,9,10],
           
           [11,12,13,14]])

print("The initial array is ")

print(a)

# slicing of the array 

sliced_array= a[:2,::2]

print("After slicing the array becomes ")

print(sliced_array)


# adding and substract operation in numpy array 

a1=n.array([[1,2],
            [3,4]])

print("The newly created array is ")

print(a1)

print(f"After adding 1 to each element to {a1} is ")

print(a1+1)

print(f"substracting value from elements from {a1} is ")

print(a1-1)

print("The sum of all elements from the array is ")

print(a1.sum())

#creating other array 

a2=n.array([[3,4],
            [5,6]])

print("The other array is ")

print(a2)

print("The sum of all elements are ")

print(a1+a2)