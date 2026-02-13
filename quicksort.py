def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  # Choosing last element as pivot
        left = []
        right = []

        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        return quick_sort(left) + [pivot] + quick_sort(right)


# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("unsorted array:",arr)
print("Sorted array:", sorted_arr)
