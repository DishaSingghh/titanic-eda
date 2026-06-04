import numpy as np

m = np.arange(1, 25).reshape(4, 6)

print("Matrix:")
print(m)
print()

# Indexing
print("m[1,3]:")
print(m[1,3])
print()

# Column slicing
print("m[:,2]:")
print(m[:,2])
print()

# Submatrix slicing
print("m[1:3,2:5]:")
print(m[1:3,2:5])
print()

# Boolean masking
print("m[m > 12]:")
print(m[m > 12])
print()

# Flatten
print("Flattened:")
print(m.flatten())
print()

# Reshape
a = np.arange(1,11)

print("Reshaped:")
print(a.reshape(2,5))



# Access single element
print("m[1,3]:")
print(m[1,3])      # row 1, column 3
print()

# First element
print("m[0,0]:")
print(m[0,0])
print()

# Last element
print("m[-1,-1]:")
print(m[-1,-1])
print()



a = np.array([10,20,30,40,50,60])

print("1D Array:")
print(a)
print()

# Elements from index 1 to 3
print("a[1:4]:")
print(a[1:4])
print()

# Every 2nd element
print("a[::2]:")
print(a[::2])
print()

# All rows, column 2
print("m[:,2]:")
print(m[:,2])
print()

# Rows 1 to 2, columns 2 to 4
print("m[1:3,2:5]:")
print(m[1:3,2:5])
print()

# Every 2nd row
print("m[::2]:")
print(m[::2])
print()

# Every 2nd column
print("m[:,::2]:")
print(m[:,::2])
print()

# Every 2nd row and column
print("m[::2,::2]:")
print(m[::2,::2])
print()



# Create boolean mask
print("m > 12:")
print(m > 12)
print()

# Get elements greater than 12
print("m[m > 12]:")
print(m[m > 12])
print()

# Even numbers
print("m[m % 2 == 0]:")
print(m[m % 2 == 0])
print()

# Odd numbers
print("m[m % 2 != 0]:")
print(m[m % 2 != 0])
print()


#reshape

b = np.arange(1,13)

print("Original 1D array:")
print(b)
print()

# Reshape into 3 rows and 4 columns
print("b.reshape(3,4):")
print(b.reshape(3,4))
print()

# Reshape into 2 blocks, 2 rows, 3 columns
print("b.reshape(2,2,3):")
print(b.reshape(2,2,3))
print()

# FLATTEN


c = np.arange(1,13).reshape(3,4)

print("2D array:")
print(c)
print()

# Convert to 1D array
print("c.flatten():")
print(c.flatten())
print()


# SHAPE, NDIM, DTYPE


print("Shape of m:")
print(m.shape)
print()

print("Dimensions of m:")
print(m.ndim)
print()

print("Datatype of m:")
print(m.dtype)
print()