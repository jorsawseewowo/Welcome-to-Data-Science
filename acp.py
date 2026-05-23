import numpy as np

arr = np.linspace(0, 9, 10, dtype=int)
print("=== Original Array ===")
print(arr)

arr_modified = np.where(arr % 2 != 0, -1, arr)
print("\n=== Array with odd numbers replaced by -1 ===")
print(arr_modified)

arr_2d = arr.reshape(2, -1)
print("\n=== 2D Array (two rows) ===")
print(arr_2d)

even_sum = sum(x for x in arr if x % 2 == 0)
print("\n=== Sum of all even numbers ===")
print(even_sum)