#operations, aggregate functions and normalization functions for the data
import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([10,20,30])

# Element-wise operations
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Aggregations
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.std(a))

# Axis examples
print(a.mean(axis=0))
print(a.mean(axis=1))

# Normalization
data = np.random.randn(100,5)

normalized = (
    data - data.mean(axis=0)
) / data.std(axis=0)

print(normalized.mean(axis=0))
print(normalized.std(axis=0))