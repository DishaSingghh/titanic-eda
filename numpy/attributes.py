import numpy as np
# 1. Creating array using np.array()
a = np.array([1, 2, 3, 4, 5])

print("Array a:")
print(a)
print()


# 2. Creating array of zeros
b = np.zeros((3, 4))

print("Array b:")
print(b)
print()


# 3. Creating array of ones
c = np.ones((2, 3))

print("Array c:")
print(c)
print()


# 4. Creating array using arange()
d = np.arange(0, 20, 2)

print("Array d:")
print(d)
print()


# 5. Creating array using linspace()
e = np.linspace(0, 1, 5)

print("Array e:")
print(e)
print()


 

# .shape  tells dimensions
print("a.shape =", a.shape)
print("b.shape =", b.shape)
print("c.shape =", c.shape)
print()


# .ndim number of dimensions
print("a.ndim =", a.ndim)
print("b.ndim =", b.ndim)
print("c.ndim =", c.ndim)
print()


# .dtype datatype of elements
print("a.dtype =", a.dtype)
print("b.dtype =", b.dtype)
print("e.dtype =", e.dtype)
print()

# mix data tupes in an array
f = np.array([1, 2, 3.5, 4])

print("Mixed int + float array:")
print(f)

print("Datatype of f:")
print(f.dtype)
print()


# 1D array
g = np.array([10, 20, 30])

print("1D array:")
print(g)

print("Shape:", g.shape)
print("Dimensions:", g.ndim)
print()


# 2D array
h = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("2D array:")
print(h)

print("Shape:", h.shape)
print("Dimensions:", h.ndim)
print()


# 3D ARRAY

i = np.zeros((2, 3, 4))

print("3D array:")
print(i)

print("Shape:", i.shape)
print("Dimensions:", i.ndim)
print()
