

import random

n = 5000
l = [random.randint(1, 10000) for _ in range(n)]

n_len = len(l)
for i in range(n_len):
    min_idx = i
    for j in range(i + 1, n_len):
        if l[j] < l[min_idx]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]

print("Sorted list:", l)
