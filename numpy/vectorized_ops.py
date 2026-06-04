import numpy as np
print(np.__version__)
#numpy array
array=np.array([1,2,3,4,5])
print(array)
print(type(array))
array=array*2
print(array) # Output: [ 2  4  6  8 10] if normal python this gives the list with the same elements twice

#dimentional array
array0=np.array(42)
print(array0.ndim)#0d

array1=np.array([1,2,3,4,5])
print(array1.ndim)#1d

array2=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]]) #refered to as a matrix
print(array2.ndim)#2d

array3=np.array([[[1,2,3],[4,5,6],[7,8,9]],
                [[1,2,3],[4,5,6],[7,8,9]],
                [[1,2,3],[4,5,6],[7,8,9]]]) #refered to as a tensor
print(array3.ndim)#3d 
#here if one of the elements was less 2 instead of 3 it would given an error 
print(array3.shape) #(3 layers, 3 rows, 3 columns) this is the shape of the array it gives the number of elements in each dimension
 #comcatination of arrays
word= array3[0,0,0]+array3[1,1,2]+array3[2,2,1]
print(word) #1+6+8=15

#slicing of arrays
arrayx= np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20]])
# print(arrayx[1:2])
#coloumn selection
print(arrayx[:,1:])
#row and col selection
print(arrayx[2:,0:2])#(row,col)