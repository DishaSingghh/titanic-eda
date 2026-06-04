import numpy as np

# np.array()
a = np.array([1, 2, 3, 4, 5])

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)

# np.zeros()
b = np.zeros((3, 4))

print(b)
print(b.shape)
print(b.ndim)
print(b.dtype)

# np.ones()
c = np.ones((2, 3))

print(c)
print(c.shape)
print(c.ndim)
print(c.dtype)

# np.arange() - stop excluded
d = np.arange(0, 20, 2)

print(d)
print(d.shape)
print(d.ndim)
print(d.dtype)

# np.linspace() - fixed number of values
e = np.linspace(0, 1, 10)

print(e)
print(e.shape)
print(e.ndim)
print(e.dtype)

# Mixed int and float
f = np.array([1, 2, 3.5, 4])

print(f)
print(f.dtype)

# 1D array
g = np.array([10, 20, 30, 40, 50])

print(g)
print(g.shape)
print(g.ndim)

# 2D array
h = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(h)
print(h.shape)
print(h.ndim)

# 3D array
i = np.zeros((2, 3, 4))

print(i)
print(i.shape)
print(i.ndim)
print(i.dtype)