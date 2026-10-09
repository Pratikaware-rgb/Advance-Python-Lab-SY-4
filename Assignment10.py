
import numpy as np

# 1. Create a one-dimensional array
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Slicing operations
print("First five elements:", arr[:5])
print("Last five elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])

# 3. Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting
print("Add 5 to each element:", arr + 5)
print("Multiply each element by 2:", arr * 2)
print("Subtract 1 from each element:", arr - 1)
