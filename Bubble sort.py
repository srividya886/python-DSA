arr = [5, 2, 4, 1, 3]
n = len(arr)
for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array:", arr)
print("Smallest:", arr[0])
print("Largest:", arr[-1])
print("Length:", len(arr))
print("Ascending order")
print("Sorting completed")